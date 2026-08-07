from __future__ import annotations

import ast
import base64
import builtins
import contextlib
import importlib
import io
import json
import math
import os
import random
import sys
import time as real_time
from typing import Any


# Este arquivo é executado com ``python -I``. Mantemos as constantes locais
# para que o worker não precise importar o pacote do aplicativo.
ALLOWED_IMPORT_ROOTS = {"math", "random", "time", "matplotlib"}
BLOCKED_CALL_NAMES = {
    "open",
    "eval",
    "exec",
    "compile",
    "breakpoint",
    "globals",
    "locals",
    "vars",
    "getattr",
    "setattr",
    "delattr",
    "help",
    "dir",
    "exit",
    "quit",
}
ALLOWED_ATTRIBUTE_NAMES = {
    "append", "extend", "insert", "pop", "remove", "clear", "sort", "reverse", "copy",
    "get", "keys", "values", "items", "update", "setdefault", "upper", "lower", "title",
    "capitalize", "strip", "lstrip", "rstrip", "split", "join", "replace", "startswith",
    "endswith", "count", "index", "choice", "choices", "randint", "randrange", "shuffle",
    "sample", "random", "uniform", "sleep", "time", "monotonic", "sqrt", "floor", "ceil",
    "factorial", "sin", "cos", "tan", "radians", "degrees", "log", "log10", "pi", "e",
    "plot", "bar", "scatter", "pie", "hist", "xlabel", "ylabel", "grid", "legend", "show",
    "xlim", "ylim", "xticks", "yticks", "figure", "subplots", "tight_layout", "pyplot",
}
SAFE_PLOT_ATTRIBUTES = {
    "plot", "bar", "scatter", "pie", "hist", "title", "xlabel", "ylabel", "grid", "legend",
    "show", "xlim", "ylim", "xticks", "yticks", "figure", "subplots", "tight_layout",
}
MAX_CODE_CHARS = 12_000
MAX_OUTPUT_CHARS = 20_000
MAX_INPUT_LINES = 50
MAX_PLOT_IMAGES = 4


class CodePolicyError(ValueError):
    pass


class OutputLimitError(RuntimeError):
    pass


class CappedWriter(io.StringIO):
    def write(self, value: str) -> int:
        text = str(value)
        remaining = MAX_OUTPUT_CHARS - self.tell()
        if remaining <= 0:
            raise OutputLimitError(
                f"A saída ultrapassou {MAX_OUTPUT_CHARS:,} caracteres e foi interrompida."
            )
        if len(text) > remaining:
            super().write(text[:remaining])
            raise OutputLimitError(
                f"A saída ultrapassou {MAX_OUTPUT_CHARS:,} caracteres e foi interrompida."
            )
        return super().write(text)


class SafeTime:
    @staticmethod
    def sleep(seconds: object) -> None:
        # Aulas continuam demonstrando espera sem bloquear o servidor por muito tempo.
        delay = max(0.0, min(float(seconds), 0.25))
        real_time.sleep(delay)

    @staticmethod
    def time() -> float:
        return real_time.time()

    @staticmethod
    def monotonic() -> float:
        return real_time.monotonic()


class SafePyplot:
    def __init__(self, pyplot: Any) -> None:
        self._pyplot = pyplot

    def __getattr__(self, name: str) -> Any:
        if name not in SAFE_PLOT_ATTRIBUTES:
            raise AttributeError(f"Recurso gráfico não permitido: plt.{name}")
        return getattr(self._pyplot, name)


class SafeMatplotlib:
    def __init__(self, pyplot: SafePyplot) -> None:
        self.pyplot = pyplot


def configure_resource_limits() -> None:
    if os.name == "nt":
        return
    try:
        import resource

        memory_bytes = 512 * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_DATA, (memory_bytes, memory_bytes))
        resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    except Exception:
        pass


configure_resource_limits()

_real_pyplot = None
_safe_pyplot = None
_safe_matplotlib = None


def get_safe_pyplot() -> SafePyplot:
    global _real_pyplot, _safe_pyplot, _safe_matplotlib
    if _safe_pyplot is None:
        matplotlib = importlib.import_module("matplotlib")
        matplotlib.use("Agg")
        _real_pyplot = importlib.import_module("matplotlib.pyplot")
        _safe_pyplot = SafePyplot(_real_pyplot)
        _safe_matplotlib = SafeMatplotlib(_safe_pyplot)
    return _safe_pyplot


def safe_import(name, globals_=None, locals_=None, fromlist=(), level=0):
    del globals_, locals_
    if level:
        raise ImportError("Import relativo não permitido.")
    root = str(name).split(".")[0]
    if root not in ALLOWED_IMPORT_ROOTS:
        allowed = ", ".join(sorted(ALLOWED_IMPORT_ROOTS))
        raise ImportError(f"Import de '{name}' não permitido. Permitidos: {allowed}")
    if root == "math":
        return math
    if root == "random":
        return random
    if root == "time":
        return SafeTime()
    if root == "matplotlib":
        pyplot = get_safe_pyplot()
        module_name = str(name)
        if module_name == "matplotlib.pyplot" and fromlist:
            return pyplot
        return _safe_matplotlib
    raise ImportError(f"Import de '{name}' não permitido.")


def safe_builtins() -> dict[str, Any]:
    allowed_names = (
        "abs", "all", "any", "bool", "chr", "dict", "divmod", "enumerate", "filter", "float",
        "int", "len", "list", "map", "max", "min", "ord", "pow", "print", "range", "repr",
        "round", "set", "sorted", "str", "sum", "tuple", "zip", "Exception", "ValueError",
        "TypeError", "RuntimeError", "ArithmeticError", "ZeroDivisionError", "IndexError", "KeyError",
    )
    result = {name: getattr(builtins, name) for name in allowed_names}
    result["__import__"] = safe_import
    return result


def make_input_function(raw_inputs: str):
    provided_inputs = str(raw_inputs).splitlines()
    if len(provided_inputs) > MAX_INPUT_LINES:
        raise CodePolicyError(f"Use no máximo {MAX_INPUT_LINES} linhas de entrada.")
    cursor = 0

    def runtime_input(prompt: str = "") -> str:
        nonlocal cursor
        if cursor >= len(provided_inputs):
            raise EOFError(
                "Faltaram respostas para input(). Adicione mais linhas em "
                "'Entradas do usuário' e execute novamente."
            )
        value = provided_inputs[cursor]
        cursor += 1
        print(f"{prompt}{value}")
        return value

    return runtime_input


def validate_and_compile(code: str):
    if len(code) > MAX_CODE_CHARS:
        raise CodePolicyError(f"O código deve ter no máximo {MAX_CODE_CHARS:,} caracteres.")
    try:
        tree = ast.parse(code, filename="<feitiço>", mode="exec")
    except SyntaxError as exc:
        raise CodePolicyError(f"Erro de sintaxe na linha {exc.lineno}: {exc.msg}") from exc

    blocked_nodes = (ast.ClassDef, ast.AsyncFunctionDef, ast.Await, ast.AsyncFor, ast.AsyncWith, ast.Global,
                     ast.Nonlocal, ast.With, ast.Delete)
    for node in ast.walk(tree):
        if isinstance(node, blocked_nodes):
            raise CodePolicyError(f"Construção não permitida neste ambiente: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id.startswith("__"):
            raise CodePolicyError("Nomes especiais do Python não estão disponíveis neste ambiente.")
        if isinstance(node, ast.Attribute):
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                raise CodePolicyError("Alteração direta de atributos não é permitida.")
            if node.attr.startswith("_") or node.attr not in ALLOWED_ATTRIBUTE_NAMES:
                raise CodePolicyError(f"Atributo não permitido: .{node.attr}")
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    raise CodePolicyError(f"Import não permitido: {alias.name}")
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                raise CodePolicyError(f"Import não permitido: {module or '<vazio>'}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in BLOCKED_CALL_NAMES:
                raise CodePolicyError(f"Uso não permitido: {node.func.id}()")

    warnings: list[str] = []
    has_infinite_while = any(
        isinstance(node, ast.While) and isinstance(node.test, ast.Constant) and node.test.value is True
        for node in ast.walk(tree)
    )
    if has_infinite_while:
        warnings.append("O código contém while True; a execução será interrompida se exceder o tempo limite.")
    return compile(tree, "<feitiço>", "exec"), warnings


def fresh_globals() -> dict[str, Any]:
    return {
        "__builtins__": safe_builtins(),
        "__name__": "__main__",
        "math": math,
        "random": random,
        "time": SafeTime(),
    }


def execute_code(code: str, raw_inputs: str, exec_globals: dict[str, Any]) -> dict[str, Any]:
    output = CappedWriter()
    error = ""
    warnings: list[str] = []
    plots: list[str] = []
    old_figures: set[int] = set()

    try:
        compiled, warnings = validate_and_compile(code)
        exec_globals["input"] = make_input_function(raw_inputs)
        needs_plotting = "plt" in code or "matplotlib" in code
        try:
            pyplot = None
            if needs_plotting or _real_pyplot is not None:
                pyplot = get_safe_pyplot()
                exec_globals["plt"] = pyplot
                old_figures = set(_real_pyplot.get_fignums())
        except Exception:
            pyplot = None

        with contextlib.redirect_stdout(output):
            exec(compiled, exec_globals)
    except CodePolicyError as exc:
        error = str(exc)
    except EOFError as exc:
        error = str(exc)
    except OutputLimitError as exc:
        error = str(exc)
    except MemoryError:
        error = "A execução usou memória demais e foi interrompida."
    except BaseException as exc:
        line = ""
        traceback_obj = exc.__traceback__
        while traceback_obj is not None:
            if traceback_obj.tb_frame.f_code.co_filename == "<feitiço>":
                line = f" na linha {traceback_obj.tb_lineno}"
            traceback_obj = traceback_obj.tb_next
        error = f"{type(exc).__name__}{line}: {exc}"

    if _real_pyplot is not None:
        new_figures = [num for num in _real_pyplot.get_fignums() if num not in old_figures]
        for number in new_figures[:MAX_PLOT_IMAGES]:
            figure = _real_pyplot.figure(number)
            image = io.BytesIO()
            figure.savefig(image, format="png", bbox_inches="tight", dpi=120)
            plots.append(base64.b64encode(image.getvalue()).decode("ascii"))
            _real_pyplot.close(figure)
        if len(new_figures) > MAX_PLOT_IMAGES:
            warnings.append(f"Foram exibidos somente os primeiros {MAX_PLOT_IMAGES} gráficos.")

    return {"stdout": output.getvalue(), "error": error, "plots": plots, "warnings": warnings}


def main() -> None:
    exec_globals = fresh_globals()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            command = request.get("command")
            if command == "execute":
                response = execute_code(
                    str(request.get("code", "")),
                    str(request.get("raw_inputs", "")),
                    exec_globals,
                )
            elif command == "reset":
                exec_globals = fresh_globals()
                response = {"status": "ok"}
            else:
                response = {"error": "Comando desconhecido.", "stdout": "", "plots": [], "warnings": []}
        except BaseException as exc:
            response = {
                "stdout": "",
                "error": f"Falha interna do caldeirão seguro: {type(exc).__name__}",
                "plots": [],
                "warnings": [],
            }
        sys.stdout.write(json.dumps(response, ensure_ascii=True, separators=(",", ":")) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
