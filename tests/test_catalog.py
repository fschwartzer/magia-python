from __future__ import annotations

import unittest

from motor_magia.catalog import adapt_markdown_for_streamlit
from motor_magia.licoes_extraidas import LESSONS_DATA


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


if __name__ == "__main__":
    unittest.main()
