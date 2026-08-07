from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path
from typing import Any

from .config import EXECUTION_TIMEOUT_SECONDS, MAX_HISTORY_ITEMS
from .models import ExecutionResult, HistoryEntry


class SandboxUnavailableError(RuntimeError):
    """Raised when the isolated Python worker cannot be started or contacted."""


class SandboxTimeoutError(TimeoutError):
    """Raised when student code exceeds the per-execution time limit."""


class _SandboxClient:
    """Persistent isolated interpreter used by one student session."""

    def __init__(self, timeout_seconds: float = EXECUTION_TIMEOUT_SECONDS) -> None:
        self.timeout_seconds = float(timeout_seconds)
        self._process: subprocess.Popen[str] | None = None
        self._lock = threading.RLock()

    @property
    def worker_path(self) -> Path:
        return Path(__file__).with_name("sandbox_worker.py")

    def _start(self) -> None:
        if self._process is not None and self._process.poll() is None:
            return

        creationflags = 0
        if os.name == "nt" and hasattr(subprocess, "CREATE_NO_WINDOW"):
            creationflags = subprocess.CREATE_NO_WINDOW

        env = {
            **os.environ,
            "MPLBACKEND": "Agg",
            "PYTHONUNBUFFERED": "1",
            "PYTHONIOENCODING": "utf-8",
        }
        self._process = subprocess.Popen(
            [sys.executable, "-I", "-u", str(self.worker_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            bufsize=1,
            env=env,
            creationflags=creationflags,
        )

    def _stop(self) -> None:
        process = self._process
        self._process = None
        if process is None:
            return
        if process.poll() is None:
            process.kill()
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass
        for stream in (process.stdin, process.stdout, process.stderr):
            if stream is not None:
                try:
                    stream.close()
                except OSError:
                    pass

    def request(self, payload: dict[str, Any]) -> dict[str, Any]:
        with self._lock:
            self._start()
            process = self._process
            if process is None or process.stdin is None or process.stdout is None:
                raise SandboxUnavailableError("O caldeirão seguro não pôde ser iniciado.")

            try:
                # O worker roda com ``-I`` e ignora PYTHONIOENCODING. JSON ASCII
                # evita divergência entre cp1252 no Windows e UTF-8 no Linux.
                process.stdin.write(json.dumps(payload, ensure_ascii=True) + "\n")
                process.stdin.flush()
            except (BrokenPipeError, OSError) as exc:
                self._stop()
                raise SandboxUnavailableError("O caldeirão seguro foi reiniciado.") from exc

            timed_out = threading.Event()

            def interrupt_worker() -> None:
                timed_out.set()
                self._stop()

            timer = threading.Timer(self.timeout_seconds, interrupt_worker)
            timer.daemon = True
            timer.start()
            try:
                line = process.stdout.readline()
            except (OSError, ValueError):
                line = ""
            finally:
                timer.cancel()

            if timed_out.is_set():
                raise SandboxTimeoutError(
                    f"A execução ultrapassou {self.timeout_seconds:.0f} segundos. "
                    "O ambiente foi reiniciado para manter o aplicativo responsivo."
                )

            if not line:
                details = ""
                try:
                    process.wait(timeout=0.2)
                except subprocess.TimeoutExpired:
                    pass
                if process.stderr is not None and process.poll() is not None:
                    try:
                        details = process.stderr.read().strip()[-500:]
                    except OSError:
                        details = ""
                self._stop()
                suffix = f" Detalhe técnico: {details}" if details else ""
                raise SandboxUnavailableError(
                    f"O caldeirão seguro encerrou inesperadamente.{suffix}"
                )
            try:
                response = json.loads(line)
            except json.JSONDecodeError as exc:
                self._stop()
                raise SandboxUnavailableError("Resposta inválida do caldeirão seguro.") from exc
            if not isinstance(response, dict):
                raise SandboxUnavailableError("Resposta inesperada do caldeirão seguro.")
            return response

    def reset(self) -> None:
        # Encerrar o subprocesso garante que nenhuma variável ou módulo da
        # execução anterior permaneça na nova sessão.
        with self._lock:
            self._stop()

    def close(self) -> None:
        self.reset()

    def __del__(self) -> None:  # pragma: no cover - limpeza defensiva
        try:
            self.close()
        except Exception:
            pass


class RuntimeSession:
    def __init__(
        self,
        max_history_items: int = MAX_HISTORY_ITEMS,
        timeout_seconds: float = EXECUTION_TIMEOUT_SECONDS,
    ) -> None:
        self.cell_outputs: dict[str, dict[str, Any]] = {}
        self.lesson_history: list[dict[str, Any]] = []
        self.max_history_items = int(max_history_items)
        self._sandbox = _SandboxClient(timeout_seconds=timeout_seconds)

    def execute(
        self,
        *,
        code: str,
        lesson_id: str,
        lesson_title: str,
        cell_id: str,
        raw_inputs: str = "",
    ) -> dict[str, Any]:
        try:
            payload = self._sandbox.request(
                {"command": "execute", "code": str(code), "raw_inputs": str(raw_inputs)}
            )
        except (SandboxTimeoutError, SandboxUnavailableError) as exc:
            payload = {
                "stdout": "",
                "error": str(exc),
                "plots": [],
                "warnings": ["As variáveis desta sessão foram apagadas por segurança."],
            }

        text_output = str(payload.get("stdout", ""))
        error_message = str(payload.get("error", ""))
        plot_payloads = [str(item) for item in payload.get("plots", [])]
        warnings = [str(item) for item in payload.get("warnings", [])]
        summary = text_output.strip() if text_output.strip() else "Executado com sucesso."
        status = "success"
        if error_message:
            summary = f"Erro: {error_message.splitlines()[-1]}"
            status = "error"

        executed_at = datetime.now().isoformat(sep=" ", timespec="seconds")
        history_entry = HistoryEntry(
            timestamp=executed_at,
            lesson_id=str(lesson_id),
            lesson_title=str(lesson_title),
            cell_id=str(cell_id),
            code=str(code),
            result=summary,
            status=status,
        )
        self.lesson_history.append(history_entry.to_dict())
        self.lesson_history = self.lesson_history[-self.max_history_items :]

        result = ExecutionResult(
            stdout=text_output,
            error=error_message,
            plots=plot_payloads,
            executed_at=executed_at,
            summary=summary,
            warnings=warnings,
        ).to_dict()
        self.cell_outputs[str(cell_id)] = result
        return result

    def clear_cell_output(self, cell_id: str) -> None:
        self.cell_outputs.pop(str(cell_id), None)

    def clear_history(self) -> None:
        self.lesson_history = []

    def reset_exec_globals(self) -> None:
        self._sandbox.reset()

    def close(self) -> None:
        self._sandbox.close()
