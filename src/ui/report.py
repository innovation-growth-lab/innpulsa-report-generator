"""UI components for report generation and display."""

from typing import Any, Dict
import streamlit as st
from src.utils.document import create_word_doc
from src.utils.constants import MIME_TYPES, HELP_TEXTS
from src.utils.errors import safe_operation


def render_download_buttons(session_state: Dict[str, Any]) -> None:
    """
    Render the download buttons for the report.

    Args:
        session_state: Streamlit session state containing report data
    """
    st.sidebar.markdown("### 💾 Descargar Reporte")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        unedited_docx = safe_operation(
            create_word_doc, "file_error", session_state, edited=False
        )
        if unedited_docx:
            st.download_button(
                label="📊 Sin Editar - Word",
                data=unedited_docx,
                file_name="reporte_zasca_sin_editar.docx",
                mime=MIME_TYPES["docx"],
                help=HELP_TEXTS["unedited_download"],
            )

    with col2:
        edited_docx = safe_operation(
            create_word_doc, "file_error", session_state, edited=True
        )
        if edited_docx:
            st.download_button(
                label="📝 Editado - Word",
                data=edited_docx,
                file_name="reporte_zasca_editado.docx",
                mime=MIME_TYPES["docx"],
                help=HELP_TEXTS["edited_download"],
            )

def render_report_section(section: Any) -> None:
    """
    Render a single report section.

    Args:
        section: Report section object containing content and variables
    """
    with st.expander(f"📑 {section.title}"):
        st.markdown("#### Contenido generado")
        st.markdown(section.content)
        st.markdown("#### Variables procesadas")
        for _, var_data in section.variables.items():
            st.markdown(f"**{var_data.description}**: {var_data.interpretation}")
            st.markdown("---")


def render_report_results(session_state: Dict[str, Any]) -> None:
    """
    Render the report results tabs.

    Args:
        session_state: Streamlit session state containing report data
    """
    result_tab1, result_tab2 = st.tabs(
        ["📝 Reporte Final Editado", "🔄 Secciones Sin Editar"]
    )

    with result_tab1:
        st.markdown("### Reporte Final")
        st.markdown("#### Resumen Ejecutivo")
        st.markdown(session_state.resumen_ejecutivo)
        st.markdown(session_state.edited_output)

    with result_tab2:
        st.markdown("### Contenido Sin Editar por Sección")
        for section in session_state.report_sections:
            render_report_section(section)
