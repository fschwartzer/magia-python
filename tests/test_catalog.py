from __future__ import annotations

import unittest

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


if __name__ == "__main__":
    unittest.main()
