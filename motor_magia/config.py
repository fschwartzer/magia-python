from __future__ import annotations

from typing import Final

MAX_HISTORY_ITEMS: Final[int] = 120
MAX_VISIBLE_HISTORY: Final[int] = 20
DEFAULT_PROGRESS_DIRNAME: Final[str] = "progress_data"
EXECUTION_TIMEOUT_SECONDS: Final[float] = 8.0
MAX_CODE_CHARS: Final[int] = 12_000
MAX_OUTPUT_CHARS: Final[int] = 20_000
MAX_INPUT_LINES: Final[int] = 50
MAX_PLOT_IMAGES: Final[int] = 4

# lesson_id, lesson_title, notebook_file
LESSON_FILES: Final[tuple[tuple[str, str, str], ...]] = (
    ("aula-1", "\U0001f31f Aula 1: Primeiros Passos", "minha_primeira_aula.ipynb"),
    ("aula-2", "\U0001f575\ufe0f Aula 2: O Computador Detetive", "minha_segunda_aula.ipynb"),
    ("aula-3", "\U0001f501 Aula 3: Repetições Mágicas", "minha_terceira_aula.ipynb"),
    ("aula-4", "\U0001f4e6 Aula 4: Listas Encantadas", "minha_quarta_aula.ipynb"),
    ("aula-5", "\U0001f9ea Aula 5: Funções e Poções", "minha_quinta_aula.ipynb"),
    ("aula-6", "\U0001f6e0\ufe0f Aula 6: Mini Projetos", "minha_sexta_aula.ipynb"),
    ("aula-7", "\U0001f3c6 Aula 7: Desafios Finais", "minha_setima_aula.ipynb"),
    ("aula-8", "\U0001f4ca Aula 8: A Grande Mestra", "minha_oitava_aula.ipynb"),
)

ALLOWED_IMPORT_ROOTS: Final[frozenset[str]] = frozenset(
    {
        "math",
        "random",
        "time",
        "matplotlib",
    }
)

BLOCKED_CALL_NAMES: Final[frozenset[str]] = frozenset(
    {
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
)

# Métodos suficientes para as aulas e exercícios introdutórios. A lista é
# intencionalmente explícita para impedir navegação pelo grafo de objetos do
# interpretador (por exemplo, via atributos especiais).
ALLOWED_ATTRIBUTE_NAMES: Final[frozenset[str]] = frozenset(
    {
        # Coleções e texto
        "append",
        "extend",
        "insert",
        "pop",
        "remove",
        "clear",
        "sort",
        "reverse",
        "copy",
        "get",
        "keys",
        "values",
        "items",
        "update",
        "setdefault",
        "upper",
        "lower",
        "title",
        "capitalize",
        "strip",
        "lstrip",
        "rstrip",
        "split",
        "join",
        "replace",
        "startswith",
        "endswith",
        "count",
        "index",
        # random, time e math
        "choice",
        "choices",
        "randint",
        "randrange",
        "shuffle",
        "sample",
        "random",
        "uniform",
        "sleep",
        "time",
        "monotonic",
        "sqrt",
        "floor",
        "ceil",
        "factorial",
        "sin",
        "cos",
        "tan",
        "radians",
        "degrees",
        "log",
        "log10",
        "pi",
        "e",
        # Matplotlib usado na Aula 8
        "plot",
        "bar",
        "scatter",
        "pie",
        "hist",
        "xlabel",
        "ylabel",
        "grid",
        "legend",
        "show",
        "xlim",
        "ylim",
        "xticks",
        "yticks",
        "figure",
        "subplots",
        "tight_layout",
        "pyplot",
    }
)
