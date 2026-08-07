from __future__ import annotations

import base64
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import streamlit as st

from motor_magia.catalog import deserialize_lessons, extract_lessons_from_notebooks, serialize_lessons
from motor_magia.config import MAX_HISTORY_ITEMS, MAX_VISIBLE_HISTORY
from motor_magia.models import Lesson, ProgressState
from motor_magia.runtime import RuntimeSession


BASE_DIR = Path(__file__).resolve().parent
APP_VERSION = 1


def setup_page() -> None:
    st.set_page_config(
        page_title="Magia Python",
        page_icon="🪄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

        :root {
            --ink: #383832;
            --navy: #232044;
            --purple: #7e33ae;
            --purple-soft: #ead7f8;
            --gold: #ffd709;
            --orange: #d95204;
            --sky: #4cb9ff;
            --paper: #fffdf3;
            --paper-low: #f8f2e7;
            --well: #ebe8dd;
            --white: #ffffff;
            --error-soft: #ffe2e8;
            --success-soft: #e4f5e9;
        }

        .stApp {
            background:
                radial-gradient(circle at 8% 2%, rgba(255, 215, 9, .16), transparent 30%),
                radial-gradient(circle at 95% 18%, rgba(126, 51, 174, .12), transparent 28%),
                var(--paper);
            color: var(--ink);
        }

        html, body, [class*="css"], p, li, label, [data-testid="stMarkdownContainer"] {
            font-family: 'Be Vietnam Pro', system-ui, sans-serif;
        }

        h1, h2, h3, h4 {
            font-family: 'Plus Jakarta Sans', system-ui, sans-serif !important;
            color: var(--navy) !important;
            letter-spacing: -.02em;
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at 15% 5%, rgba(255, 215, 9, .18), transparent 26%),
                linear-gradient(180deg, #292452 0%, #49306d 100%);
        }

        [data-testid="stSidebar"] * { color: #fffdf3 !important; }
        [data-testid="stSidebar"] [data-baseweb="select"] > div,
        [data-testid="stSidebar"] textarea,
        [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
            background: rgba(255, 255, 255, .11) !important;
            border: 0 !important;
            border-radius: 18px !important;
        }

        [data-testid="stSidebar"] [data-testid="stProgressBar"] > div > div {
            background: linear-gradient(90deg, var(--gold), #ff9d3d) !important;
            box-shadow: 0 0 12px rgba(255, 215, 9, .55);
        }

        .magic-brand {
            text-align: center;
            padding: .65rem .5rem 1rem;
        }
        .magic-brand .orb {
            width: 76px;
            height: 76px;
            margin: 0 auto .55rem;
            display: grid;
            place-items: center;
            border-radius: 28px 42px 30px 46px;
            background: linear-gradient(145deg, var(--gold), #ff9d3d);
            box-shadow: 0 14px 34px rgba(0, 0, 0, .2), inset 0 2px 0 rgba(255,255,255,.65);
            font-size: 2.35rem;
            transform: rotate(-3deg);
        }
        .magic-brand strong { font: 800 1.2rem 'Plus Jakarta Sans', sans-serif; }
        .magic-brand small { opacity: .82; }

        .magic-hero {
            position: relative;
            overflow: hidden;
            border-radius: 34px 52px 36px 46px;
            padding: clamp(1.35rem, 3vw, 2.35rem);
            margin: .25rem 0 1.25rem;
            background:
                radial-gradient(circle at 90% 10%, rgba(255,255,255,.42), transparent 22%),
                linear-gradient(135deg, #ffd709 0%, #ffac45 55%, #f17b35 100%);
            box-shadow: 0 20px 50px rgba(65, 36, 15, .12);
        }
        .magic-hero::after {
            content: "✦  ·  ✧  ·  ✦";
            position: absolute;
            right: 2rem;
            top: 1.2rem;
            color: rgba(35,32,68,.38);
            font-size: 1.6rem;
            letter-spacing: .45rem;
        }
        .magic-hero h1 { margin: 0 0 .35rem; font-size: clamp(2rem, 4vw, 3.35rem); }
        .magic-hero p { margin: 0; max-width: 760px; font-size: 1.05rem; color: #342b35; }

        .lesson-chip, .safe-chip {
            display: inline-block;
            padding: .28rem .75rem;
            border-radius: 999px;
            font-weight: 800;
            font-size: .8rem;
            margin: 0 .35rem .5rem 0;
        }
        .lesson-chip { background: var(--purple-soft); color: #4d176b; }
        .safe-chip { background: var(--success-soft); color: #225c33; }

        [data-testid="stMetric"] {
            background: rgba(255,255,255,.78);
            border-radius: 24px 30px 22px 28px;
            padding: .8rem 1rem;
            box-shadow: 0 12px 32px rgba(58,0,91,.06);
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(255,255,255,.82);
            border: 0 !important;
            border-radius: 30px 38px 28px 34px !important;
            box-shadow: 0 16px 42px rgba(58,0,91,.07);
        }

        .spell-label {
            display: flex;
            align-items: center;
            gap: .55rem;
            margin-bottom: .35rem;
            font-weight: 800;
            color: var(--navy);
        }
        .spell-number {
            display: inline-grid;
            place-items: center;
            width: 2.05rem;
            height: 2.05rem;
            border-radius: 50% 44% 52% 40%;
            background: var(--gold);
            color: #5b4000;
        }

        .stTextArea textarea {
            font-family: 'JetBrains Mono', Consolas, monospace !important;
            background: var(--well) !important;
            color: #282633 !important;
            border: 0 !important;
            border-radius: 20px !important;
        }
        .stTextArea textarea:focus { box-shadow: 0 0 0 3px rgba(126,51,174,.22) !important; }

        .stButton > button, .stDownloadButton > button {
            border: 0 !important;
            border-radius: 999px !important;
            font-weight: 800 !important;
            min-height: 2.7rem;
            transition: transform .15s ease, filter .15s ease;
        }
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #51216f, var(--purple)) !important;
            color: white !important;
            box-shadow: 0 10px 22px rgba(126,51,174,.22);
        }
        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-1px);
            filter: brightness(.98);
        }

        [data-testid="stAlert"] { border: 0 !important; border-radius: 22px !important; }
        .stCodeBlock { border-radius: 20px; overflow: hidden; }

        .lesson-path {
            display: flex;
            gap: .45rem;
            flex-wrap: wrap;
            margin: .4rem 0 1.35rem;
        }
        .lesson-dot {
            padding: .42rem .7rem;
            border-radius: 999px;
            background: var(--well);
            color: #625f58;
            font-size: .78rem;
            font-weight: 700;
        }
        .lesson-dot.done { background: var(--success-soft); color: #225c33; }
        .lesson-dot.current { background: var(--purple-soft); color: #4d176b; }

        @media (max-width: 760px) {
            .magic-hero::after { display: none; }
            .magic-hero { border-radius: 26px 34px 28px 32px; }
            [data-testid="stMetric"] { padding: .55rem .7rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(show_spinner=False)
def load_lesson_payload() -> list[dict[str, Any]]:
    try:
        from motor_magia.licoes_extraidas import LESSONS_DATA

        if isinstance(LESSONS_DATA, list) and LESSONS_DATA:
            return LESSONS_DATA
    except Exception:
        pass
    return serialize_lessons(extract_lessons_from_notebooks(BASE_DIR))


def load_lessons() -> list[Lesson]:
    return deserialize_lessons(load_lesson_payload())


def bootstrap_session_state(lessons: list[Lesson]) -> None:
    first_lesson_id = lessons[0].lesson_id
    defaults: dict[str, Any] = {
        "runtime": RuntimeSession,
        "notes": dict,
        "lesson_status": dict,
        "selected_lesson_id": lambda: first_lesson_id,
        "import_digest": lambda: "",
        "flash_message": lambda: "",
        "celebrate": lambda: False,
    }
    for key, factory in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = factory()

    pending = st.session_state.pop("pending_lesson_id", None)
    valid_ids = {lesson.lesson_id for lesson in lessons}
    if pending in valid_ids:
        st.session_state["selected_lesson_id"] = pending
    if st.session_state["selected_lesson_id"] not in valid_ids:
        st.session_state["selected_lesson_id"] = first_lesson_id


def progress_document() -> dict[str, Any]:
    runtime: RuntimeSession = st.session_state["runtime"]
    return {
        "app": "magia-python",
        "version": APP_VERSION,
        "exported_at": datetime.now().isoformat(sep=" ", timespec="seconds"),
        "notes": dict(st.session_state["notes"]),
        "lesson_status": dict(st.session_state["lesson_status"]),
        "lesson_history": list(runtime.lesson_history[-MAX_HISTORY_ITEMS:]),
    }


def import_progress(raw: bytes, valid_lesson_ids: set[str]) -> None:
    if len(raw) > 1_000_000:
        raise ValueError("O arquivo de progresso deve ter no máximo 1 MB.")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("O arquivo não é um JSON de progresso válido.") from exc
    if not isinstance(data, dict):
        raise ValueError("O arquivo de progresso precisa conter um objeto JSON.")

    progress = ProgressState.from_dict(data)
    st.session_state["notes"] = {
        lesson_id: note[:10_000]
        for lesson_id, note in progress.notes.items()
        if lesson_id in valid_lesson_ids
    }
    st.session_state["lesson_status"] = {
        lesson_id: completed
        for lesson_id, completed in progress.lesson_status.items()
        if lesson_id in valid_lesson_ids
    }
    runtime: RuntimeSession = st.session_state["runtime"]
    runtime.lesson_history = progress.lesson_history[-MAX_HISTORY_ITEMS:]
    for key in list(st.session_state):
        if str(key).startswith("notes_widget::"):
            del st.session_state[key]


def toggle_lesson(lesson_id: str, total_lessons: int) -> None:
    current = bool(st.session_state["lesson_status"].get(lesson_id, False))
    st.session_state["lesson_status"][lesson_id] = not current
    completed = sum(bool(value) for value in st.session_state["lesson_status"].values())
    if not current and completed >= total_lessons:
        st.session_state["celebrate"] = True


def select_lesson(lesson_id: str) -> None:
    st.session_state["pending_lesson_id"] = lesson_id


def reset_code_widget(widget_key: str, default_code: str) -> None:
    st.session_state[widget_key] = default_code


def render_output(runtime: RuntimeSession, cell_id: str) -> None:
    output = runtime.cell_outputs.get(cell_id)
    if not output:
        return
    with st.expander("🔮 Resultado do caldeirão", expanded=True):
        for warning in output.get("warnings", []):
            st.warning(str(warning))
        stdout = str(output.get("stdout", ""))
        error = str(output.get("error", ""))
        if stdout.strip():
            st.code(stdout, language="text")
        elif not error:
            st.success("Feitiço executado com sucesso!")
        if error:
            st.error("O feitiço precisa de um pequeno ajuste. Leia a pista abaixo e tente novamente.")
            st.code(error, language="text")
        for encoded in output.get("plots", []):
            try:
                st.image(base64.b64decode(encoded), use_container_width=True)
            except Exception:
                st.warning("Um gráfico foi gerado, mas não pôde ser exibido.")
        st.caption(f"Executado em {output.get('executed_at', '')}")


def render_code_cell(lesson: Lesson, cell: Any) -> None:
    runtime: RuntimeSession = st.session_state["runtime"]
    code_key = f"code::{cell.cell_id}"
    input_key = f"inputs::{cell.cell_id}"
    if code_key not in st.session_state:
        st.session_state[code_key] = cell.default_code or cell.source
    if input_key not in st.session_state:
        st.session_state[input_key] = ""

    with st.container(border=True):
        st.markdown(
            f'<div class="spell-label"><span class="spell-number">{cell.index}</span>'
            "Laboratório de código</div>",
            unsafe_allow_html=True,
        )
        code = st.text_area(
            "Edite seu feitiço em Python",
            key=code_key,
            height=min(max(len(st.session_state[code_key].splitlines()) * 23 + 78, 170), 390),
            label_visibility="collapsed",
        )

        if cell.requires_input or "input(" in code:
            st.caption("Cada linha abaixo responde a uma chamada de `input()`, na ordem das perguntas.")
            raw_inputs = st.text_area(
                "Entradas do usuário",
                key=input_key,
                height=95,
                placeholder="Uma resposta por linha\nExemplo: Luna\ndragão\n3",
            )
        else:
            raw_inputs = st.session_state[input_key]

        run_col, restore_col, clear_col = st.columns([1.45, 1, 1])
        run_clicked = run_col.button(
            "▶ Executar magia",
            key=f"run::{cell.cell_id}",
            type="primary",
            use_container_width=True,
        )
        restore_col.button(
            "↺ Restaurar",
            key=f"restore::{cell.cell_id}",
            on_click=reset_code_widget,
            args=(code_key, cell.default_code or cell.source),
            use_container_width=True,
        )
        if clear_col.button("🧽 Limpar", key=f"clear::{cell.cell_id}", use_container_width=True):
            runtime.clear_cell_output(cell.cell_id)

        if run_clicked:
            with st.spinner("Misturando o feitiço no caldeirão seguro..."):
                runtime.execute(
                    code=code,
                    lesson_id=lesson.lesson_id,
                    lesson_title=lesson.title,
                    cell_id=cell.cell_id,
                    raw_inputs=raw_inputs,
                )
        render_output(runtime, cell.cell_id)


def render_lesson(lesson: Lesson) -> None:
    for cell in lesson.cells:
        if cell.cell_type == "markdown":
            st.markdown(cell.source)
        elif cell.cell_type == "code":
            render_code_cell(lesson, cell)


def render_sidebar(lessons: list[Lesson]) -> Lesson:
    lesson_by_id = {lesson.lesson_id: lesson for lesson in lessons}
    valid_ids = set(lesson_by_id)

    st.sidebar.markdown(
        """
        <div class="magic-brand">
          <div class="orb">🪄</div>
          <strong>Magia Python</strong><br>
          <small>Seu grimório de programação</small>
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected_id = st.sidebar.selectbox(
        "Escolha sua lição",
        options=[lesson.lesson_id for lesson in lessons],
        format_func=lambda lesson_id: lesson_by_id[lesson_id].title,
        key="selected_lesson_id",
    )
    lesson = lesson_by_id[selected_id]

    completed = sum(bool(st.session_state["lesson_status"].get(item.lesson_id, False)) for item in lessons)
    progress_ratio = completed / len(lessons)
    st.sidebar.markdown(f"### 🏅 Progresso: {completed}/{len(lessons)}")
    st.sidebar.progress(progress_ratio)

    is_completed = bool(st.session_state["lesson_status"].get(selected_id, False))
    st.sidebar.button(
        "↩ Desmarcar conclusão" if is_completed else "✓ Concluir esta aula",
        key=f"toggle::{selected_id}",
        on_click=toggle_lesson,
        args=(selected_id, len(lessons)),
        type="primary" if not is_completed else "secondary",
        use_container_width=True,
    )

    notes_key = f"notes_widget::{selected_id}"
    if notes_key not in st.session_state:
        st.session_state[notes_key] = st.session_state["notes"].get(selected_id, "")
    note = st.sidebar.text_area("📝 Anotações desta aula", key=notes_key, height=150)
    st.session_state["notes"][selected_id] = note

    st.sidebar.markdown("### 💾 Levar meu progresso")
    st.sidebar.caption(
        "No Community Cloud, o progresso fica nesta sessão. Baixe o arquivo para continuar em outro dia."
    )
    progress_json = json.dumps(progress_document(), ensure_ascii=False, indent=2)
    st.sidebar.download_button(
        "⬇ Baixar progresso",
        data=progress_json,
        file_name="magia_python_progresso.json",
        mime="application/json",
        use_container_width=True,
    )
    uploaded = st.sidebar.file_uploader(
        "Restaurar progresso",
        type=["json"],
        help="Selecione um arquivo baixado anteriormente pelo Magia Python.",
    )
    if uploaded is not None:
        raw = uploaded.getvalue()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != st.session_state["import_digest"]:
            try:
                import_progress(raw, valid_ids)
                st.session_state["import_digest"] = digest
                st.session_state["flash_message"] = "Progresso restaurado com sucesso."
                st.rerun()
            except ValueError as exc:
                st.sidebar.error(str(exc))

    runtime: RuntimeSession = st.session_state["runtime"]
    action_col, history_col = st.sidebar.columns(2)
    if action_col.button("🧹 Resetar", help="Apaga as variáveis criadas pelos códigos."):
        runtime.reset_exec_globals()
        st.sidebar.success("Caldeirão reiniciado.")
    if history_col.button("🗑 Histórico"):
        runtime.clear_history()
        st.sidebar.success("Histórico apagado.")

    with st.sidebar.expander("📜 Últimas execuções", expanded=False):
        if not runtime.lesson_history:
            st.caption("Nenhum feitiço executado ainda.")
        for entry in reversed(runtime.lesson_history[-MAX_VISIBLE_HISTORY:]):
            icon = "✅" if entry.get("status") == "success" else "🧩"
            st.markdown(f"{icon} **{entry.get('timestamp', '')}**")
            st.caption(f"{entry.get('lesson_title', '')} · {entry.get('cell_id', '')}")
            st.code(str(entry.get("result", ""))[:1200], language="text")

    st.sidebar.caption("🔒 Código executado com política restrita, limite de saída e timeout.")
    return lesson


def render_main(lessons: list[Lesson], selected_lesson: Lesson) -> None:
    completed = sum(
        bool(st.session_state["lesson_status"].get(lesson.lesson_id, False)) for lesson in lessons
    )
    progress_ratio = completed / len(lessons)
    selected_position = next(i for i, lesson in enumerate(lessons) if lesson.lesson_id == selected_lesson.lesson_id)

    st.markdown(
        """
        <section class="magic-hero">
          <h1>Escola de Magia do Python</h1>
          <p>Aprenda a conversar com o computador, resolver desafios e criar suas próprias magias — um feitiço de cada vez.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<span class="lesson-chip">Lição {selected_position + 1} de {len(lessons)}</span>'
        '<span class="safe-chip">🛡 Laboratório seguro</span>',
        unsafe_allow_html=True,
    )

    metric_a, metric_b, metric_c = st.columns(3)
    metric_a.metric("Aulas concluídas", f"{completed}/{len(lessons)}")
    metric_b.metric("Jornada completa", f"{progress_ratio:.0%}")
    metric_c.metric(
        "Feitiços nesta aula",
        sum(cell.cell_type == "code" for cell in selected_lesson.cells),
    )

    path_items = []
    for lesson in lessons:
        classes = ["lesson-dot"]
        if st.session_state["lesson_status"].get(lesson.lesson_id, False):
            classes.append("done")
        if lesson.lesson_id == selected_lesson.lesson_id:
            classes.append("current")
        path_items.append(
            f'<span class="{" ".join(classes)}">{lesson.order}. '
            f'{"✓" if "done" in classes else "○"}</span>'
        )
    st.markdown(f'<div class="lesson-path">{"".join(path_items)}</div>', unsafe_allow_html=True)

    if st.session_state.pop("flash_message", ""):
        st.success("Progresso restaurado com sucesso.")
    if st.session_state.pop("celebrate", False):
        st.balloons()
        st.success("🏆 Jornada completa! Você dominou as oito aulas do grimório.")

    if st.session_state["lesson_status"].get(selected_lesson.lesson_id, False):
        st.success("Aula concluída. Você pode revisar os feitiços ou avançar para a próxima missão.")
    else:
        st.info("Explore os exemplos, mude o código e marque a aula como concluída quando se sentir pronta ou pronto.")

    render_lesson(selected_lesson)

    st.markdown("### Continue sua jornada")
    previous_col, spacer, next_col = st.columns([1, 1.2, 1])
    if selected_position > 0:
        previous_col.button(
            "← Aula anterior",
            on_click=select_lesson,
            args=(lessons[selected_position - 1].lesson_id,),
            use_container_width=True,
        )
    if selected_position < len(lessons) - 1:
        next_col.button(
            "Próxima aula →",
            on_click=select_lesson,
            args=(lessons[selected_position + 1].lesson_id,),
            type="primary",
            use_container_width=True,
        )
    spacer.caption("Seu progresso pode ser exportado pelo menu lateral.")


def main() -> None:
    setup_page()
    lessons = load_lessons()
    if not lessons:
        st.error("Nenhuma aula foi encontrada no grimório.")
        st.stop()
    bootstrap_session_state(lessons)
    selected_lesson = render_sidebar(lessons)
    render_main(lessons, selected_lesson)


if __name__ == "__main__":
    main()
