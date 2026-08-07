from __future__ import annotations

from pathlib import Path
from threading import RLock
from typing import Any

from .catalog import deserialize_lessons, extract_lessons_from_notebooks
from .config import DEFAULT_PROGRESS_DIRNAME, LESSON_FILES, MAX_HISTORY_ITEMS, MAX_VISIBLE_HISTORY
from .models import Lesson
from .progress import FileProgressStore
from .runtime import RuntimeSession


class MotorMagia:
    """
    Motor desacoplado de UI para:
    - catalogo de licoes
    - execucao de celulas por sessao
    - progresso/notas por usuario
    """

    def __init__(
        self,
        *,
        base_dir: Path | str,
        progress_dir: Path | str | None = None,
    ) -> None:
        self.base_dir = Path(base_dir)
        self._lock = RLock()
        self._sessions: dict[str, RuntimeSession] = {}

        if progress_dir is None:
            progress_dir = self.base_dir / DEFAULT_PROGRESS_DIRNAME
        self.progress_store = FileProgressStore(progress_dir)

        self.lessons = self._load_lessons()
        self.lesson_by_id: dict[str, Lesson] = {lesson.lesson_id: lesson for lesson in self.lessons}

    def _load_lessons(self) -> list[Lesson]:
        # Primeiro tenta usar modulo Python pre-extraido (bom para deploy cloud).
        try:
            from .licoes_extraidas import LESSONS_DATA  # type: ignore

            if isinstance(LESSONS_DATA, list) and LESSONS_DATA:
                return deserialize_lessons(LESSONS_DATA)
        except Exception:
            pass

        # Fallback: le diretamente os notebooks.
        return extract_lessons_from_notebooks(self.base_dir, lesson_specs=LESSON_FILES)

    def _get_session(self, session_id: str) -> RuntimeSession:
        sid = str(session_id or "sessao-publica")
        with self._lock:
            session = self._sessions.get(sid)
            if session is None:
                session = RuntimeSession()
                self._sessions[sid] = session
            return session

    def list_lessons(self) -> list[dict[str, Any]]:
        return [
            {
                "lesson_id": lesson.lesson_id,
                "order": lesson.order,
                "title": lesson.title,
                "notebook_file": lesson.notebook_file,
                "total_cells": len(lesson.cells),
                "code_cells": sum(1 for c in lesson.cells if c.cell_type == "code"),
                "markdown_cells": sum(1 for c in lesson.cells if c.cell_type == "markdown"),
            }
            for lesson in self.lessons
        ]

    def get_lesson(self, lesson_id: str) -> dict[str, Any]:
        lesson = self.lesson_by_id.get(str(lesson_id))
        if lesson is None:
            raise KeyError(f"Licao nao encontrada: {lesson_id}")
        return lesson.to_dict()

    def _get_code_cell(self, lesson_id: str, cell_id: str):
        lesson = self.lesson_by_id.get(lesson_id)
        if lesson is None:
            raise KeyError(f"Licao nao encontrada: {lesson_id}")
        for cell in lesson.cells:
            if cell.cell_id == cell_id:
                if cell.cell_type != "code":
                    raise ValueError("A celula solicitada nao e do tipo code.")
                return lesson, cell
        raise KeyError(f"Celula nao encontrada: {cell_id}")

    def execute_cell(
        self,
        *,
        session_id: str,
        lesson_id: str,
        cell_id: str,
        code: str | None = None,
        raw_inputs: str = "",
    ) -> dict[str, Any]:
        lesson, cell = self._get_code_cell(str(lesson_id), str(cell_id))
        final_code = cell.default_code if code is None else str(code)
        session = self._get_session(session_id)
        return session.execute(
            code=final_code or "",
            lesson_id=lesson.lesson_id,
            lesson_title=lesson.title,
            cell_id=cell.cell_id,
            raw_inputs=raw_inputs,
        )

    def get_cell_output(self, session_id: str, cell_id: str) -> dict[str, Any] | None:
        session = self._get_session(session_id)
        return session.cell_outputs.get(cell_id)

    def clear_cell_output(self, *, session_id: str, cell_id: str) -> None:
        session = self._get_session(session_id)
        session.clear_cell_output(cell_id)

    def get_session_history(self, session_id: str, limit: int = MAX_VISIBLE_HISTORY) -> list[dict[str, Any]]:
        session = self._get_session(session_id)
        capped = max(1, min(int(limit), MAX_HISTORY_ITEMS))
        return list(reversed(session.lesson_history[-capped:]))

    def clear_session_history(self, session_id: str) -> None:
        session = self._get_session(session_id)
        session.clear_history()

    def reset_session_runtime(self, session_id: str) -> None:
        session = self._get_session(session_id)
        session.reset_exec_globals()

    def get_progress(self, user_id: str) -> dict[str, Any]:
        progress = self.progress_store.load(user_id)
        return progress.to_dict()

    def set_lesson_status(self, *, user_id: str, lesson_id: str, completed: bool) -> dict[str, Any]:
        if lesson_id not in self.lesson_by_id:
            raise KeyError(f"Licao nao encontrada: {lesson_id}")
        progress = self.progress_store.set_lesson_status(user_id, lesson_id, completed)
        return progress.to_dict()

    def save_note(self, *, user_id: str, lesson_id: str, note: str) -> dict[str, Any]:
        if lesson_id not in self.lesson_by_id:
            raise KeyError(f"Licao nao encontrada: {lesson_id}")
        progress = self.progress_store.set_note(user_id, lesson_id, note)
        return progress.to_dict()

    def clear_persisted_history(self, user_id: str) -> dict[str, Any]:
        progress = self.progress_store.clear_history(user_id)
        return progress.to_dict()

    def persist_session_history(self, *, user_id: str, session_id: str) -> dict[str, Any]:
        session = self._get_session(session_id)
        progress = self.progress_store.merge_history(user_id, session.lesson_history)
        return progress.to_dict()

    def get_dashboard(self, user_id: str) -> dict[str, Any]:
        progress = self.progress_store.load(user_id)
        total = len(self.lessons)
        completed_count = 0
        next_lesson_id = None
        lesson_cards: list[dict[str, Any]] = []

        unlocked = True
        for lesson in self.lessons:
            completed = bool(progress.lesson_status.get(lesson.lesson_id, False))
            if completed:
                completed_count += 1
            if not completed and next_lesson_id is None:
                next_lesson_id = lesson.lesson_id

            lesson_cards.append(
                {
                    "lesson_id": lesson.lesson_id,
                    "title": lesson.title,
                    "order": lesson.order,
                    "completed": completed,
                    "locked": not unlocked,
                }
            )

            # A proxima licao so desbloqueia quando a atual e concluida.
            if not completed:
                unlocked = False

        progress_ratio = (completed_count / total) if total else 0.0
        return {
            "user_id": user_id,
            "total_lessons": total,
            "completed_lessons": completed_count,
            "progress_ratio": progress_ratio,
            "next_lesson_id": next_lesson_id,
            "lessons": lesson_cards,
        }

