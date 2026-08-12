from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path

from motor_magia.licoes_extraidas import LESSONS_DATA


@unittest.skipUnless(importlib.util.find_spec("streamlit"), "streamlit não instalado")
class StreamlitAppTests(unittest.TestCase):
    def make_app(self):
        from streamlit.testing.v1 import AppTest

        app_path = Path(__file__).resolve().parents[1] / "app.py"
        return AppTest.from_file(str(app_path), default_timeout=30).run()

    def execute_cell(self, app, cell_index: int, answers: list[str] | None = None) -> None:
        cell_id = f"aula-1::cell-{cell_index}"
        run_button = next(button for button in app.button if button.key == f"run::{cell_id}")
        run_button.click().run()

        if answers is None:
            return

        modal_fields = [
            field for field in app.text_input if str(field.key).startswith(f"input::{cell_id}::")
        ]
        self.assertEqual(len(modal_fields), len(answers))
        for field, answer in zip(modal_fields, answers, strict=True):
            field.set_value(answer)
        submit_button = next(
            button for button in app.button if button.key == f"submit::{cell_id}"
        )
        submit_button.click().run()
        # O AppTest preserva a árvore do fragmento por um ciclo após st.rerun().
        # Reponha os valores removidos com o modal e faça um ciclo de estabilização.
        for field, answer in zip(modal_fields, answers, strict=True):
            app.session_state[str(field.key)] = answer
        app.run()

    def submit_interactive_turn(self, app, key_prefix: str, answers: list[str]) -> None:
        fields = [
            field for field in app.text_input if str(field.key).startswith(key_prefix)
        ]
        self.assertEqual(len(fields), len(answers))
        submitted_values: list[tuple[str, str]] = []
        for field, answer in zip(fields, answers, strict=True):
            field.set_value(answer)
            submitted_values.append((str(field.key), answer))
        submit_button = next(
            button
            for button in app.button
            if str(button.key).startswith(key_prefix.replace("input::", "submit::"))
        )
        submit_button.click().run()
        # Fragmentos removem as chaves do modal anterior antes de o AppTest
        # estabilizar sua árvore. Reponha somente o estado transitório antigo.
        for key, answer in submitted_values:
            app.session_state[key] = answer
        app.run()

    def test_app_starts_without_exception(self) -> None:
        app = self.make_app()
        self.assertFalse(list(app.exception))
        self.assertEqual(len(app.selectbox), 1)
        self.assertEqual(len(app.text_area) > 0, True)
        self.assertEqual(list(app.text_input), [])

    def test_input_fields_appear_only_after_opening_modal(self) -> None:
        app = self.make_app()

        self.execute_cell(app, 10, ["Luna"])

        self.assertFalse(list(app.exception))
        self.assertNotIn("input_dialog_request", app.session_state.filtered_state)
        output = app.session_state["runtime"].cell_outputs["aula-1::cell-10"]
        self.assertIn("Prazer em te conhecer, Luna", output["stdout"])
        self.assertTrue(app.session_state["completed_cells"]["aula-1::cell-10"])

    def test_progress_updates_after_successful_laboratories(self) -> None:
        app = self.make_app()
        executions = (
            (3, None),
            (5, None),
            (7, None),
            (10, ["Luna"]),
            (12, ["dragão", "azul", "pizza", "castelo"]),
        )
        for cell_index, answers in executions:
            self.execute_cell(app, cell_index, answers)
            self.assertFalse(list(app.exception))

        self.assertEqual(app.metric[0].value, "1/8")
        self.assertTrue(app.session_state["lesson_status"]["aula-1"])
        self.assertEqual(
            sum(app.session_state["completed_cells"].values()),
            5,
        )

    def test_laboratory_numbers_are_sequential_in_every_lesson(self) -> None:
        app = self.make_app()
        for lesson in LESSONS_DATA:
            app.selectbox[0].set_value(lesson["lesson_id"]).run()
            labels = [
                markdown.value
                for markdown in app.markdown
                if markdown.value.startswith('<div class="spell-label">')
            ]
            numbers = [
                int(re.search(r'spell-number">(\d+)', label).group(1))
                for label in labels
            ]
            self.assertEqual(numbers, list(range(1, lesson["code_cells"] + 1)))

    def test_guessing_game_keeps_one_secret_until_the_correct_guess(self) -> None:
        app = self.make_app()
        app.selectbox[0].set_value("aula-3").run()
        next(
            button for button in app.button if button.key == "run::aula-3::cell-8"
        ).click().run()

        for guess in range(1, 11):
            self.submit_interactive_turn(
                app,
                "input::aula-3::cell-8::guess::",
                [str(guess)],
            )
            if "input_dialog_request" not in app.session_state.filtered_state:
                break

        self.assertNotIn("input_dialog_request", app.session_state.filtered_state)
        self.assertTrue(app.session_state["completed_cells"]["aula-3::cell-8"])
        output = app.session_state["runtime"].cell_outputs["aula-3::cell-8"]["stdout"]
        self.assertEqual(output.count("Estou pensando em um número"), 1)
        self.assertIn("PARABÉNS", output)
        self.assertIn("Fim de jogo!", output)

    def test_tamagotchi_asks_name_once_and_preserves_status(self) -> None:
        app = self.make_app()
        app.selectbox[0].set_value("aula-7").run()
        next(
            button for button in app.button if button.key == "run::aula-7::cell-7"
        ).click().run()

        first_fields = [
            field
            for field in app.text_input
            if str(field.key).startswith("input::aula-7::cell-7::tamagotchi::")
        ]
        self.assertEqual(
            [field.label for field in first_fields],
            [
                "1. Que nome você quer dar ao seu bichinho?",
                "2. O que você quer fazer? (1-Comer, 2-Brincar, 3-Sair)",
            ],
        )
        self.submit_interactive_turn(
            app,
            "input::aula-7::cell-7::tamagotchi::",
            ["Luna", "1"],
        )

        later_fields = [
            field
            for field in app.text_input
            if str(field.key).startswith("input::aula-7::cell-7::tamagotchi::")
        ]
        self.assertEqual(
            [field.label for field in later_fields],
            ["O que você quer fazer? (1-Comer, 2-Brincar, 3-Sair)"],
        )
        self.submit_interactive_turn(
            app,
            "input::aula-7::cell-7::tamagotchi::",
            ["2"],
        )
        self.submit_interactive_turn(
            app,
            "input::aula-7::cell-7::tamagotchi::",
            ["3"],
        )

        self.assertNotIn("input_dialog_request", app.session_state.filtered_state)
        self.assertTrue(app.session_state["completed_cells"]["aula-7::cell-7"])
        output = app.session_state["runtime"].cell_outputs["aula-7::cell-7"]["stdout"]
        self.assertEqual(output.count("Que nome você quer dar"), 1)
        self.assertIn("🍖 Fome: 3", output)
        self.assertIn("😊 Alegria: 9", output)
        self.assertIn("Tchau! O Luna vai dormir.", output)


if __name__ == "__main__":
    unittest.main()
