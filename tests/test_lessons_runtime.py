from __future__ import annotations

import unittest

from motor_magia.licoes_extraidas import LESSONS_DATA
from motor_magia.models import Lesson
from motor_magia.runtime import RuntimeSession


class LessonRuntimeTests(unittest.TestCase):
    def test_all_default_code_cells_run_in_the_sandbox(self) -> None:
        lessons = [Lesson.from_dict(item) for item in LESSONS_DATA]
        generic_inputs = "\n".join(
            ["Luna", "chocolate", "gato", "azul", "pizza", "castelo"]
            + [str(number) for number in range(1, 11)]
        )

        for lesson in lessons:
            runtime = RuntimeSession(timeout_seconds=8)
            try:
                for cell in lesson.cells:
                    if cell.cell_type != "code":
                        continue
                    code = cell.default_code or cell.source
                    if "numero_secreto" in code and "Qual é o seu chute?" in code:
                        raw_inputs = "\n".join(str(number) for number in range(1, 11))
                    elif "Que nome você quer dar ao seu bichinho?" in code:
                        raw_inputs = "Luna\n3"
                    else:
                        raw_inputs = generic_inputs
                    result = runtime.execute(
                        code=code,
                        lesson_id=lesson.lesson_id,
                        lesson_title=lesson.title,
                        cell_id=cell.cell_id,
                        raw_inputs=raw_inputs,
                    )
                    self.assertFalse(
                        result["error"],
                        f"{lesson.lesson_id} / {cell.cell_id}: {result['error']}",
                    )
            finally:
                runtime.close()


if __name__ == "__main__":
    unittest.main()
