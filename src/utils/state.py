"""Session state management utilities."""

from typing import Dict, Any
import streamlit as st


def init_session_state() -> Dict[str, Any]:
    """
    Initialize the session state variables.

    Returns:
        Dictionary containing the initialized session state
    """
    if "report_generated" not in st.session_state:
        st.session_state.report_generated = False
        st.session_state.report_finalised = False
        st.session_state.json_str = None
        st.session_state.markdown_content = None
        st.session_state.resumen_ejecutivo = None
        st.session_state.edited_output = None
        st.session_state.report_sections = None
        st.session_state.success_message = None
        st.session_state.loaded_data = None
        st.session_state.filtered_sections_config = {}
        st.session_state.variable_selections = {}
        st.session_state.missing_variables = {}

    return st.session_state


def update_report_state(
    json_str: str,
    resumen_ejecutivo: str,
    edited_output: str,
    report_sections: list,
) -> None:
    """
    Update the session state with report generation results.

    Args:
        json_str: JSON string representation of the report
        resumen_ejecutivo: Executive summary text
        edited_output: Edited report content
        report_sections: List of report sections
    """
    st.session_state.report_generated = True
    st.session_state.report_finalised = True
    st.session_state.json_str = json_str
    st.session_state.resumen_ejecutivo = resumen_ejecutivo
    st.session_state.edited_output = edited_output
    st.session_state.report_sections = report_sections
    st.session_state.markdown_content = (
        f"# Reporte ZASCA\n\n## Resumen Ejecutivo\n{resumen_ejecutivo}\n\n{edited_output}"
    )
    st.session_state.success_message = "🎉 ¡Reporte generado exitosamente!"
