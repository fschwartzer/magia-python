from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class LessonCell:
    cell_id: str
    index: int
    cell_type: str
    source: str
    requires_input: bool = False
    default_code: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "cell_id": self.cell_id,
            "index": self.index,
            "cell_type": self.cell_type,
            "source": self.source,
            "requires_input": self.requires_input,
            "default_code": self.default_code,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LessonCell":
        return cls(
            cell_id=str(data["cell_id"]),
            index=int(data["index"]),
            cell_type=str(data["cell_type"]),
            source=str(data.get("source", "")),
            requires_input=bool(data.get("requires_input", False)),
            default_code=data.get("default_code"),
        )


@dataclass(slots=True)
class Lesson:
    lesson_id: str
    order: int
    title: str
    notebook_file: str
    cells: list[LessonCell] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        code_cells = sum(1 for c in self.cells if c.cell_type == "code")
        markdown_cells = sum(1 for c in self.cells if c.cell_type == "markdown")
        return {
            "lesson_id": self.lesson_id,
            "order": self.order,
            "title": self.title,
            "notebook_file": self.notebook_file,
            "total_cells": len(self.cells),
            "code_cells": code_cells,
            "markdown_cells": markdown_cells,
            "cells": [cell.to_dict() for cell in self.cells],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Lesson":
        return cls(
            lesson_id=str(data["lesson_id"]),
            order=int(data["order"]),
            title=str(data["title"]),
            notebook_file=str(data.get("notebook_file", "")),
            cells=[LessonCell.from_dict(item) for item in data.get("cells", [])],
        )


@dataclass(slots=True)
class ExecutionResult:
    stdout: str
    error: str
    plots: list[str]
    executed_at: str
    summary: str
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "stdout": self.stdout,
            "error": self.error,
            "plots": list(self.plots),
            "executed_at": self.executed_at,
            "summary": self.summary,
            "warnings": list(self.warnings),
        }


@dataclass(slots=True)
class HistoryEntry:
    timestamp: str
    lesson_id: str
    lesson_title: str
    cell_id: str
    code: str
    result: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "lesson_id": self.lesson_id,
            "lesson_title": self.lesson_title,
            "cell_id": self.cell_id,
            "code": self.code,
            "result": self.result,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "HistoryEntry":
        return cls(
            timestamp=str(data.get("timestamp", "")),
            lesson_id=str(data.get("lesson_id", "")),
            lesson_title=str(data.get("lesson_title", "")),
            cell_id=str(data.get("cell_id", "")),
            code=str(data.get("code", "")),
            result=str(data.get("result", "")),
            status=str(data.get("status", "success")),
        )


@dataclass(slots=True)
class ProgressState:
    notes: dict[str, str] = field(default_factory=dict)
    lesson_status: dict[str, bool] = field(default_factory=dict)
    lesson_history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "notes": dict(self.notes),
            "lesson_status": dict(self.lesson_status),
            "lesson_history": list(self.lesson_history),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressState":
        notes = data.get("notes", {})
        lesson_status = data.get("lesson_status", {})
        lesson_history = data.get("lesson_history", [])

        if not isinstance(notes, dict):
            notes = {}
        if not isinstance(lesson_status, dict):
            lesson_status = {}
        if not isinstance(lesson_history, list):
            lesson_history = []

        return cls(
            notes={str(k): str(v) for k, v in notes.items()},
            lesson_status={str(k): bool(v) for k, v in lesson_status.items()},
            lesson_history=[item for item in lesson_history if isinstance(item, dict)],
        )

