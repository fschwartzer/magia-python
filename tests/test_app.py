from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


@unittest.skipUnless(importlib.util.find_spec("streamlit"), "streamlit não instalado")
class StreamlitAppTests(unittest.TestCase):
    def make_app(self):
        from streamlit.testing.v1 import AppTest

        app_path = Path(__file__).resolve().parents[1] / "app.py"
        return AppTest.from_file(str(app_path), default_timeout=30).run()

    def test_app_starts_without_exception(self) -> None:
        app = self.make_app()
        self.assertFalse(list(app.exception))
        self.assertEqual(len(app.selectbox), 1)
        self.assertEqual(len(app.text_area) > 0, True)
        self.assertEqual(
            [field.label for field in app.text_input],
            [
                "Qual é o seu nome?",
                "1. Digite o nome de um animal (ex: gato, dragão)",
                "2. Digite uma cor bem diferente",
                "3. Digite uma comida estranha",
                "4. Digite um lugar (ex: castelo, escola, lua)",
            ],
        )

    def test_progress_updates_after_successful_laboratories(self) -> None:
        app = self.make_app()
        answers = ["Luna", "dragão", "azul", "pizza", "castelo"]
        for field, answer in zip(app.text_input, answers, strict=True):
            field.set_value(answer)
        app.run()

        for cell_index in (3, 5, 7, 10, 12):
            run_button = next(
                button
                for button in app.button
                if button.key == f"run::aula-1::cell-{cell_index}"
            )
            run_button.click().run()
            self.assertFalse(list(app.exception))

        self.assertEqual(app.metric[0].value, "1/8")
        self.assertTrue(app.session_state["lesson_status"]["aula-1"])
        self.assertEqual(
            sum(app.session_state["completed_cells"].values()),
            5,
        )


if __name__ == "__main__":
    unittest.main()
