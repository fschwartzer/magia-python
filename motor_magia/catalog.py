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


# Ajustes editoriais próprios do aplicativo. Os notebooks continuam sendo a
# fonte pedagógica original, enquanto o catálogo publicado ganha exemplos e
# exercícios adequados à experiência interativa do Streamlit.
_SKIPPED_APP_CELLS: frozenset[tuple[str, int]] = frozenset(
    {
        ("aula-4", 6),  # Desafio Relâmpago da Regra do Zero
        ("aula-6", 7),  # Exemplo intermediário dar_oi_especial2
        ("aula-6", 8),  # Chamada isolada do exemplo intermediário
    }
)

_APP_MARKDOWN_OVERRIDES: dict[tuple[str, int], str] = {
    ("aula-8", 8): (
        "### 🏆 Desafio da Cientista\n\n"
        "Crie um gráfico sobre a sua família ou amigos!\n\n"
        "Ideias:\n"
        "1. **Idade das pessoas:** Crie uma lista com nomes e outra com idades.\n"
        "2. **Pontuação de Videogame:** Quem fez mais pontos?\n\n"
        "Use o **Laboratório de código abaixo**. Os comentários mostram onde trocar "
        "os nomes, os números, as cores e o título. Depois, clique em "
        "**Executar magia** para ver o resultado!"
    )
}

_APP_CODE_OVERRIDES: dict[tuple[str, int], str] = {
    ("aula-1", 5): 'print("escreva aqui seu nome")',
    ("aula-1", 7): (
        "# Criando a caixinha\n"
        'comida_favorita = "escreva aqui sua comida favorita"\n\n'
        "# Mandando o computador mostrar o que tem dentro da caixinha\n"
        "print(comida_favorita)"
    ),
    ("aula-4", 12): (
        "import random\n\n"
        'pessoas = ["Maria", "José", "João"]\n'
        "escolha = random.choice(pessoas)\n"
        'print("O computador está sorteando...")\n'
        'print("O escolhido é: " + escolha)'
    ),
    ("aula-5", 6): (
        'print("Vou imprimir 5 Geraldos para você:")\n\n'
        "# Repita 5 vezes\n"
        "for numero in range(5):\n"
        '    print("🦸‍♀️ Geraldo!")'
    ),
    ("aula-5", 11): (
        "numero_tabuada = 2\n\n"
        'print("Tabuada do " + str(numero_tabuada))\n\n'
        "# Vai contar do 1 até o 10 (o range para um número antes do final, por isso 11)\n"
        "for contador in range(1, 11):\n"
        "    resultado = numero_tabuada * contador\n"
        '    print(str(numero_tabuada) + " vezes " + str(contador) + " é igual a: " '
        "+ str(resultado))"
    ),
    ("aula-6", 11): (
        "# Criando a função (A Receita)\n"
        "def enfeitar(frase):\n"
        '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n'
        '    print("★ " + frase + " ★")\n'
        '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n\n'
        "# Usando a função (Cozinhando)\n"
        'enfeitar("EU AMO PYTHON")\n\n'
        'enfeitar("MINHA FAMÍLIA É LEGAL")\n\n'
        "# Podemos até usar input junto!\n"
        "sua_frase = input()\n"
        "enfeitar(sua_frase)"
    ),
    ("aula-8", 5): (
        "import matplotlib.pyplot as plt\n\n"
        'dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]\n'
        "temperatura = [25, 28, 22, 30, 31]\n\n"
        '# Tente mudar "orange" para "pink" ou "green"\n'
        'plt.plot(dias, temperatura, color="orange", marker="o")\n\n'
        'plt.title("Temperatura da Semana ☀️")\n'
        "plt.show()"
    ),
    ("aula-8", 7): (
        "import matplotlib.pyplot as plt\n\n"
        "# Nomes das frutas\n"
        'frutas = ["Maçã 🍎", "Banana 🍌", "Uva 🍇", "Laranja 🍊"]\n\n'
        "# Quantos votos cada uma teve\n"
        "votos = [5, 10, 3, 8]\n\n"
        "# Criando o gráfico de barras\n"
        "# Podemos escolher uma cor para cada barra!\n"
        'cores = ["red", "yellow", "purple", "orange"]\n\n'
        "plt.bar(frutas, votos, color=cores)\n\n"
        'plt.title("Campeonato das Frutas 🏆")\n'
        "plt.show()"
    ),
}

_EXTRA_APP_CODE_CELLS: dict[tuple[str, int], tuple[int, str]] = {
    ("aula-6", 12): (
        13,
        "def idade_canina(numero):\n"
        "    # Um ano humano vale sete anos de cachorro.\n"
        "    print(numero * 7)\n\n"
        "idade_canina(2)",
    ),
    ("aula-8", 8): (
        9,
        "import matplotlib.pyplot as plt\n\n"
        "# 1. Troque os nomes entre aspas pelos nomes da sua família ou dos seus amigos.\n"
        'nomes = ["Maria", "José", "João"]\n\n'
        "# 2. Troque os números pelas idades ou pontuações de cada pessoa.\n"
        "numeros = [10, 35, 62]\n\n"
        "# 3. Você também pode trocar as cores das barras.\n"
        'cores = ["purple", "orange", "green"]\n\n'
        "# 4. Troque o título para explicar o que o seu gráfico mostra.\n"
        'titulo = "Idade da minha família"\n\n'
        "# O computador usa suas listas para desenhar o gráfico.\n"
        "plt.bar(nomes, numeros, color=cores)\n"
        "plt.title(titulo)\n"
        'plt.xlabel("Pessoas")\n'
        'plt.ylabel("Idade ou pontuação")\n'
        "plt.show()",
    ),
}


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


def adapt_lesson_cell_for_app(
    lesson_id: str,
    index: int,
    cell_type: str,
    source: str,
) -> str | None:
    """Apply reproducible app-only edits to one notebook cell."""

    if (lesson_id, index) in _SKIPPED_APP_CELLS:
        return None
    if cell_type == "markdown":
        adapted = adapt_markdown_for_streamlit(source)
        return _APP_MARKDOWN_OVERRIDES.get((lesson_id, index), adapted)
    return _APP_CODE_OVERRIDES.get((lesson_id, index), source)


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
            source = adapt_lesson_cell_for_app(lesson_id, index, cell_type, source)
            if source is None:
                continue
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

            extra_cell = _EXTRA_APP_CODE_CELLS.get((lesson_id, index))
            if extra_cell is not None:
                extra_index, extra_source = extra_cell
                cells.append(
                    LessonCell(
                        cell_id=f"{lesson_id}::cell-{extra_index}",
                        index=extra_index,
                        cell_type="code",
                        source=extra_source,
                        requires_input=_cell_requires_input(extra_source),
                        default_code=extra_source,
                    )
                )

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
