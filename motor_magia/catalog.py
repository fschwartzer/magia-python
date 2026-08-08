from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .config import LESSON_FILES
from .models import Lesson, LessonCell


_STREAMLIT_EXECUTION_COPY: tuple[tuple[str, str], ...] = (
    (
        'Para fazer a mágica acontecer, clique no botão de "Play" ▶️ ao lado de cada código!',
        "Para fazer a mágica acontecer, clique em **Executar magia**, abaixo da caixa de código.",
    ),
    (
        "**Missão:** Clique no código abaixo e aperte o Play ▶️ para ver o que acontece.",
        "**Missão:** Observe o código abaixo e clique em **Executar magia** para ver o que acontece.",
    ),
    ("Depois aperte o Play!", "Depois, clique em **Executar magia**."),
    (
        "Usamos o comando `input`. Quando você rodar esse código, uma caixinha vai aparecer "
        "para você digitar sua resposta!",
        "Usamos o comando `input`. Clique em **Executar magia**, preencha a resposta no pop-up "
        "e confirme a execução!",
    ),
    (
        "**Instruções:**\n1. Rode o código abaixo.\n"
        "2. Responda as perguntas que o computador fizer.\n"
        "3. Veja a história mágica que aparece no final!",
        "**Instruções:**\n1. Clique em **Executar magia** abaixo do código.\n"
        "2. Preencha as caixas de resposta no pop-up.\n"
        "3. Clique em **Executar magia** no pop-up e veja a história mágica no final!",
    ),
    (
        "Tente rodar o gerador de histórias de novo e inventar coisas ainda mais malucas.",
        "Clique em **Executar magia**, preencha o pop-up com novas respostas e confirme para "
        "inventar coisas ainda mais malucas.",
    ),
    (
        "Tente adivinhar o que vai acontecer abaixo e aperte o Play ▶️.",
        "Tente adivinhar o que vai acontecer abaixo e clique em **Executar magia**.",
    ),
    (
        "**Desafio:** Rode o código acima duas vezes.\n"
        "1. Na primeira vez, digite `chocolate` (tudo minúsculo).\n"
        "2. Na segunda vez, digite `abacaxi` e veja o que acontece.",
        "**Desafio:** Execute o código duas vezes usando o botão **Executar magia**.\n"
        "1. Na primeira execução, preencha o pop-up com `chocolate` (tudo minúsculo) e confirme.\n"
        "2. Na segunda, preencha o pop-up com `abacaxi` e confirme novamente.",
    ),
    (
        "Rode o código abaixo **várias vezes** e veja o número mudar!",
        "Clique em **Executar magia** várias vezes e veja o número mudar!",
    ),
    (
        "Preparada? Aperte o play!",
        "Preparada? Clique em **Executar magia**, preencha a resposta no pop-up e confirme!",
    ),
    (
        "Veja a lista de compras abaixo e aperte o Play ▶️.",
        "Veja a lista de compras abaixo e clique em **Executar magia**.",
    ),
    (
        "3. Rode o código para ver o que o destino escolheu.",
        "3. Clique em **Executar magia** para ver o que o destino escolheu.",
    ),
    ("3. Aperte o Play!", "3. Clique em **Executar magia**!"),
    (
        "Rode o código e cuide do seu bichinho!",
        "Clique em **Executar magia**, preencha as respostas no pop-up e cuide do seu bichinho!",
    ),
)


def normalize_source(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(chunk) for chunk in source)
    return str(source)


def adapt_markdown_for_streamlit(source: str) -> str:
    """Troca instruções próprias de notebooks pelos controles do aplicativo."""
    adapted = source
    for notebook_copy, streamlit_copy in _STREAMLIT_EXECUTION_COPY:
        adapted = adapted.replace(notebook_copy, streamlit_copy)
    return adapted


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
                source = adapt_markdown_for_streamlit(source)
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
