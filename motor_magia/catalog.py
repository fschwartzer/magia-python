from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .config import LESSON_FILES
from .models import Lesson, LessonCell


def normalize_source(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(chunk) for chunk in source)
    return str(source)


def _cell_requires_input(source: str) -> bool:
    return "input(" in source


def extract_lessons_from_notebooks(
    base_dir: Path | str,
    lesson_specs: Iterable[tuple[str, str, str]] = LESSON_FILES,
) -> list[Lesson]:
    root = Path(base_dir)
    lessons: list[Lesson] = []

    for order, (lesson_id, title, notebook_file) in enumerate(lesson_specs, start=1):
        notebook_path = root / notebook_file
        if not notebook_path.exists():
            raise FileNotFoundError(f"Notebook nao encontrado: {notebook_path}")

        notebook_data = json.loads(notebook_path.read_text(encoding="utf-8"))
        cells_raw = notebook_data.get("cells", [])
        cells: list[LessonCell] = []

        for index, raw_cell in enumerate(cells_raw, start=1):
            cell_type = str(raw_cell.get("cell_type", "")).strip().lower()
            if cell_type not in {"markdown", "code"}:
                continue

            source = normalize_source(raw_cell.get("source", ""))
            cell_id = f"{lesson_id}::cell-{index}"

            if cell_type == "markdown":
                cell = LessonCell(
                    cell_id=cell_id,
                    index=index,
                    cell_type="markdown",
                    source=source,
                    requires_input=False,
                    default_code=None,
                )
            else:
                cell = LessonCell(
                    cell_id=cell_id,
                    index=index,
                    cell_type="code",
                    source=source,
                    requires_input=_cell_requires_input(source),
                    default_code=source,
                )

            cells.append(cell)

        lesson = Lesson(
            lesson_id=lesson_id,
            order=order,
            title=title,
            notebook_file=notebook_file,
            cells=cells,
        )
        lessons.append(lesson)

    return lessons


def serialize_lessons(lessons: list[Lesson]) -> list[dict]:
    return [lesson.to_dict() for lesson in lessons]


def deserialize_lessons(payload: list[dict]) -> list[Lesson]:
    return [Lesson.from_dict(item) for item in payload]

