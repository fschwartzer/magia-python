from __future__ import annotations

import pprint
from datetime import datetime
from pathlib import Path
from typing import Iterable

from .catalog import extract_lessons_from_notebooks, serialize_lessons
from .config import LESSON_FILES


def export_lessons_module(
    *,
    base_dir: Path | str,
    output_file: Path | str,
    lesson_specs: Iterable[tuple[str, str, str]] = LESSON_FILES,
) -> int:
    base_path = Path(base_dir)
    output_path = Path(output_file)

    lessons = extract_lessons_from_notebooks(base_path, lesson_specs=lesson_specs)
    payload = serialize_lessons(lessons)
    # ``json.dumps`` produz ``true``/``false``/``null``, que não são literais
    # Python válidos. ``pformat`` mantém o módulo importável no deploy.
    payload_literal = pprint.pformat(payload, width=100, sort_dicts=False)

    rendered = (
        '"""Licoes extraidas automaticamente dos notebooks.\n'
        "Nao editar manualmente. Rode scripts/extrair_licoes.py.\n"
        f'Gerado em: {datetime.now().isoformat(sep=" ", timespec="seconds")}\n'
        '"""\n\n'
        "LESSONS_DATA = "
        f"{payload_literal}\n"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    return len(lessons)
