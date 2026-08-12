from __future__ import annotations

import importlib.util
import unittest

from motor_magia.runtime import RuntimeSession, worker_environment


class RuntimeSessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.runtime = RuntimeSession(timeout_seconds=1.5)

    def tearDown(self) -> None:
        self.runtime.close()

    def execute(self, code: str, raw_inputs: str = "") -> dict:
        return self.runtime.execute(
            code=code,
            lesson_id="teste",
            lesson_title="Aula de teste",
            cell_id=f"cell-{len(self.runtime.lesson_history) + 1}",
            raw_inputs=raw_inputs,
        )

    def test_executes_and_preserves_variables(self) -> None:
        first = self.execute("pontos = 40")
        second = self.execute("pontos += 2\nprint(pontos)")
        self.assertFalse(first["error"])
        self.assertEqual(second["stdout"].strip(), "42")

    def test_simulates_input(self) -> None:
        result = self.execute('nome = input("Nome: ")\nprint("Olá, " + nome)', "Luna")
        self.assertFalse(result["error"])
        self.assertIn("Nome: Luna", result["stdout"])
        self.assertIn("Olá, Luna", result["stdout"])

    def test_blocks_files_imports_and_dunder_access(self) -> None:
        cases = (
            ("open('segredo.txt')", "Uso não permitido"),
            ("import os", "Import não permitido"),
            ("print((1).__class__)", "Atributo não permitido"),
        )
        for code, expected in cases:
            with self.subTest(code=code):
                result = self.execute(code)
                self.assertIn(expected, result["error"])

    def test_limits_output(self) -> None:
        result = self.execute("print('x' * 25000)")
        self.assertIn("saída ultrapassou", result["error"])
        self.assertLessEqual(len(result["stdout"]), 20_000)

    def test_timeout_restarts_runtime(self) -> None:
        timed_out = self.execute("while True:\n    pass")
        self.assertIn("ultrapassou", timed_out["error"])
        recovered = self.execute("print('ambiente novo')")
        self.assertFalse(recovered["error"])
        self.assertIn("ambiente novo", recovered["stdout"])

    def test_plot_worker_limits_native_math_threads(self) -> None:
        environment = worker_environment()
        for variable in (
            "OPENBLAS_NUM_THREADS",
            "OMP_NUM_THREADS",
            "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS",
            "BLIS_NUM_THREADS",
        ):
            self.assertEqual(environment[variable], "1")

    @unittest.skipUnless(importlib.util.find_spec("matplotlib"), "matplotlib não instalado")
    def test_captures_plot(self) -> None:
        self.runtime.close()
        self.runtime = RuntimeSession(timeout_seconds=8)
        result = self.execute(
            "import matplotlib.pyplot as plt\n"
            "plt.plot([1, 2, 3], [1, 4, 9])\n"
            "plt.title('Teste')\n"
            "plt.show()"
        )
        self.assertFalse(result["error"])
        self.assertEqual(len(result["plots"]), 1)


if __name__ == "__main__":
    unittest.main()
