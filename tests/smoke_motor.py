from __future__ import annotations

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from motor_magia.engine import MotorMagia  # noqa: E402


def main() -> None:
    engine = MotorMagia(base_dir=BASE_DIR)

    lessons = engine.list_lessons()
    assert len(lessons) == 8, f"Esperado 8 licoes, veio {len(lessons)}"

    lesson = engine.get_lesson("aula-1")
    code_cells = [cell for cell in lesson["cells"] if cell["cell_type"] == "code"]
    assert code_cells, "Aula 1 precisa ter celulas de codigo"

    first_cell = code_cells[0]
    result = engine.execute_cell(
        session_id="sessao-smoke",
        lesson_id="aula-1",
        cell_id=first_cell["cell_id"],
        code='print("teste motor")',
        raw_inputs="",
    )
    assert "teste motor" in result["stdout"], "stdout nao contem texto esperado"
    assert not result["error"], f"Nao era esperado erro: {result['error']}"

    dashboard = engine.get_dashboard("usuario-smoke")
    assert dashboard["total_lessons"] == 8
    assert "lessons" in dashboard and len(dashboard["lessons"]) == 8

    print("SMOKE_OK")


if __name__ == "__main__":
    main()

