from __future__ import annotations

import unittest

from motor_magia.catalog import adapt_markdown_for_streamlit
from motor_magia.licoes_extraidas import LESSONS_DATA
from motor_magia.models import Lesson


class CatalogTests(unittest.TestCase):
    def test_preextracted_catalog_is_valid(self) -> None:
        self.assertEqual(len(LESSONS_DATA), 8)
        self.assertEqual([item["order"] for item in LESSONS_DATA], list(range(1, 9)))
        self.assertTrue(all(item["cells"] for item in LESSONS_DATA))
        self.assertIn("Repetições Mágicas", LESSONS_DATA[2]["title"])
        self.assertIn("Funções e Poções", LESSONS_DATA[4]["title"])

    def test_every_lesson_has_markdown_and_code(self) -> None:
        for lesson in LESSONS_DATA:
            cell_types = {cell["cell_type"] for cell in lesson["cells"]}
            self.assertIn("markdown", cell_types, lesson["lesson_id"])
            self.assertIn("code", cell_types, lesson["lesson_id"])

    def test_execution_instructions_use_streamlit_button(self) -> None:
        markdown = "\n".join(
            cell["source"]
            for lesson in LESSONS_DATA
            for cell in lesson["cells"]
            if cell["cell_type"] == "markdown"
        )

        self.assertNotRegex(markdown, r"(?i)\bplay\b")
        self.assertNotIn("Rode o código", markdown)
        self.assertNotIn("rodar esse código", markdown)
        self.assertNotIn("rodar o gerador", markdown)
        self.assertNotIn("abaixo do código e clique", markdown)
        self.assertNotIn("caixas de resposta abaixo do código", markdown)
        self.assertGreaterEqual(markdown.count("**Executar magia**"), 14)
        self.assertGreaterEqual(markdown.count("pop-up"), 5)

    def test_notebook_copy_is_adapted_without_changing_other_text(self) -> None:
        source = (
            "Leia com atenção.\n"
            "Rode o código abaixo **várias vezes** e veja o número mudar!"
        )

        adapted = adapt_markdown_for_streamlit(source)

        self.assertIn("Leia com atenção.", adapted)
        self.assertIn("Clique em **Executar magia** várias vezes", adapted)
        self.assertNotIn("Rode o código", adapted)

    def test_app_specific_lesson_edits_are_published(self) -> None:
        lessons = {
            lesson.lesson_id: lesson
            for lesson in (Lesson.from_dict(item) for item in LESSONS_DATA)
        }
        code = {
            cell.cell_id: cell.source
            for lesson in lessons.values()
            for cell in lesson.cells
            if cell.cell_type == "code"
        }

        self.assertEqual(code["aula-1::cell-5"], 'print("escreva aqui seu nome")')
        self.assertIn(
            'comida_favorita = "escreva aqui sua comida favorita"',
            code["aula-1::cell-7"],
        )
        self.assertNotIn(
            "Desafio Relâmpago",
            "\n".join(cell.source for cell in lessons["aula-4"].cells),
        )
        self.assertIn(
            'pessoas = ["Maria", "José", "João"]',
            code["aula-4::cell-12"],
        )
        self.assertIn("range(5)", code["aula-5::cell-6"])
        self.assertIn("5 Geraldos", code["aula-5::cell-6"])
        self.assertIn("numero_tabuada = 2", code["aula-5::cell-11"])
        self.assertNotIn("aula-6::cell-7", code)
        self.assertNotIn("aula-6::cell-8", code)
        self.assertIn("sua_frase = input()", code["aula-6::cell-11"])
        self.assertIn("def idade_canina(numero):", code["aula-6::cell-13"])
        for cell_id in ("aula-8::cell-3", "aula-8::cell-5", "aula-8::cell-7"):
            self.assertIn("import matplotlib.pyplot as plt", code[cell_id])
        code_cell_count = sum(
            lesson.to_dict()["code_cells"] for lesson in lessons.values()
        )
        self.assertEqual(code_cell_count, 30)


if __name__ == "__main__":
    unittest.main()
