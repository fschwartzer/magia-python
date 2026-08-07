from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .config import MAX_HISTORY_ITEMS
from .models import ProgressState


def _sanitize_user_id(user_id: str) -> str:
    value = str(user_id or "anonimo").strip()
    if not value:
        value = "anonimo"
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value)


class FileProgressStore:
    def __init__(self, base_dir: Path | str) -> None:
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _file_path(self, user_id: str) -> Path:
        safe_id = _sanitize_user_id(user_id)
        return self.base_dir / f"{safe_id}.json"

    def load(self, user_id: str) -> ProgressState:
        path = self._file_path(user_id)
        if not path.exists():
            return ProgressState()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return ProgressState()
        return ProgressState.from_dict(data)

    def save(self, user_id: str, progress: ProgressState) -> None:
        path = self._file_path(user_id)
        path.write_text(
            json.dumps(progress.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def set_lesson_status(self, user_id: str, lesson_id: str, completed: bool) -> ProgressState:
        progress = self.load(user_id)
        progress.lesson_status[str(lesson_id)] = bool(completed)
        self.save(user_id, progress)
        return progress

    def set_note(self, user_id: str, lesson_id: str, note: str) -> ProgressState:
        progress = self.load(user_id)
        progress.notes[str(lesson_id)] = str(note)
        self.save(user_id, progress)
        return progress

    def clear_history(self, user_id: str) -> ProgressState:
        progress = self.load(user_id)
        progress.lesson_history = []
        self.save(user_id, progress)
        return progress

    def merge_history(
        self,
        user_id: str,
        session_history: Iterable[dict],
        max_history_items: int = MAX_HISTORY_ITEMS,
    ) -> ProgressState:
        progress = self.load(user_id)
        merged = [*progress.lesson_history, *list(session_history)]
        progress.lesson_history = merged[-max_history_items:]
        self.save(user_id, progress)
        return progress

