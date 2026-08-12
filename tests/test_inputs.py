from __future__ import annotations

import unittest

from app import input_labels_for_cell, input_prompts
from motor_magia.licoes_extraidas import LESSONS_DATA
from motor_magia.models import Lesson
from motor_magia.models import ProgressState


class InputPromptTests(unittest.TestCase):
    def test_extracts_each_prompt_in_source_order(self) -> None:
        prompts, repeats = input_prompts(
            'nome = input("Seu nome: ")\ncor = input("Sua cor favorita: ")'
        )
        self.assertEqual(prompts, ["Seu nome", "Sua cor favorita"])
        self.assertFalse(repeats)

    def test_detects_input_that_can_repeat(self) -> None:
        prompts, repeats = input_prompts(
            'while True:\n    resposta = input("Sua tentativa: ")\n    break'
        )
        self.assertEqual(prompts, ["Sua tentativa"])
        self.assertTrue(repeats)

    def test_decorator_uses_a_descriptive_modal_label(self) -> None:
        prompts, repeats = input_prompts("sua_frase = input()")
        self.assertEqual(
            input_labels_for_cell("aula-6::cell-11", prompts),
            ["Escreva algo para enfeitar"],
        )
        self.assertFalse(repeats)

    def test_all_notebook_inputs_receive_identified_fields(self) -> None:
        observed: dict[tuple[int, int], int] = {}
        for lesson_data in LESSONS_DATA:
            lesson = Lesson.from_dict(lesson_data)
            for cell in lesson.cells:
                if cell.cell_type == "code" and "input(" in cell.source:
                    prompts, _ = input_prompts(cell.source)
                    self.assertTrue(prompts, f"Sem campo para {cell.cell_id}")
                    observed[(lesson.order, cell.index)] = len(prompts)

        self.assertEqual(
            observed,
            {
                (1, 10): 1,
                (1, 12): 4,
                (2, 6): 1,
                (2, 9): 4,
                (3, 8): 1,
                (6, 11): 1,
                (7, 7): 2,
            },
        )

    def test_progress_state_remains_compatible_with_old_exports(self) -> None:
        progress = ProgressState.from_dict(
            {"lesson_status": {"aula-1": True}, "lesson_history": []}
        )
        self.assertEqual(progress.completed_cells, {})
        self.assertTrue(progress.lesson_status["aula-1"])


if __name__ == "__main__":
    unittest.main()
