"""UI components for the sidebar."""

import base64
from typing import Tuple, Optional, IO, Any
import streamlit as st
import pandas as pd
from src.data.process import aggregate_data
from src.services.openai_helpers import (
    generate_section_contents,
    generate_executive_summary,
    edit_report_sections,
)
from src.utils.output import generate_json_output
from src.utils.constants import MODEL_OPTIONS, HELP_TEXTS, MESSAGES, ALLOWED_EXTENSIONS
from src.utils.errors import safe_operation, ReportGenerationError
from src.utils.state import update_report_state
from src.utils.plot_downloads import create_downloadable_chart
from src.config.charts import get_available_charts


def render_file_uploader() -> Optional[IO]:
    """
    Render the file uploader in the sidebar.

    Returns:
        Uploaded file object if successful, None otherwise
    """
    uploaded_file = st.sidebar.file_uploader(
        "Cargar archivo Excel", type=ALLOWED_EXTENSIONS, help=HELP_TEXTS["file_upload"]
    )

    if not uploaded_file:
        st.sidebar.info(MESSAGES["errors"]["no_file"])

    return uploaded_file


def render_sidebar_controls() -> Tuple[str, bool]:
    """
    Render the sidebar controls.

    Returns:
        Tuple containing the selected model name and whether to generate report
    """
    st.sidebar.markdown("---")
    model_name = st.sidebar.selectbox(
        "Modelo de OpenAI",
        list(MODEL_OPTIONS.keys()),
        format_func=lambda x: MODEL_OPTIONS[x],
        index=0,
        help=HELP_TEXTS["model_select"],
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    generate_report = st.sidebar.button(
        "🚀 Generar Reporte",
        help=HELP_TEXTS["generate_button"],
        use_container_width=True,
    )

    return model_name, generate_report


def render_progress_indicators() -> Tuple[Any, Any]:
    """
    Render the progress indicators in the sidebar.

    Returns:
        Tuple containing the progress bar and status text container
    """
    progress_bar = st.progress(0)
    status_text = st.empty()
    return progress_bar, status_text


async def handle_report_generation(
    df: pd.DataFrame, cohort_info: str, model_name: str
) -> Optional[str]:
    """
    Handle the report generation process.

    Args:
        df: DataFrame containing the data
        cohort_info: String containing cohort information
        model_name: Name of the OpenAI model to use

    Returns:
        Optional error message if something goes wrong
    """
    try:
        # Create progress indicators in sidebar
        with st.sidebar:
            progress_bar, status_text = render_progress_indicators()

        # Generate sections using filtered config
        try:
            report_sections, missing_variables = safe_operation(
                aggregate_data,
                "data_error",
                df,
                st.session_state.filtered_sections_config,
            )
            if report_sections is None:
                raise ReportGenerationError("Failed to aggregate data")
        except Exception as e:  # pylint: disable=W0718
            return MESSAGES["errors"]["data_error"].format(str(e))

        # Show warning in sidebar if variables are missing
        if missing_variables:
            with st.sidebar:
                st.markdown("### Variables no encontradas")
                st.warning(
                    MESSAGES["info"]["missing_variables"],
                    icon="⚠️",
                )
                for var in missing_variables:
                    st.markdown(f"- {var}")

        try:
            # Generate section contents
            with st.sidebar:
                status_text.info(MESSAGES["info"]["generating_sections"])
            await generate_section_contents(
                report_sections, cohort_info, model_name, progress_bar
            )

            # Generate executive summary
            with st.sidebar:
                status_text.info(MESSAGES["info"]["generating_summary"])
            # resumen_ejecutivo = await generate_executive_summary(
            #     report_sections, cohort_info, model_name
            # )
            resumen_ejecutivo = "" # [HACK: Reduce cost]

            # Edit report sections
            with st.sidebar:
                status_text.info(MESSAGES["info"]["editing_report"])
            edited_output = await edit_report_sections(
                report_sections, model_name, True
            )  # [HACK: Reduce cost]

            # Prepare JSON output
            with st.sidebar:
                status_text.info(MESSAGES["info"]["preparing_json"])
            json_str = generate_json_output(report_sections, resumen_ejecutivo)

        except Exception as e:  # pylint: disable=W0718
            return MESSAGES["errors"]["report_error"].format(str(e))

        # Clear progress indicators and update state
        with st.sidebar:
            status_text.empty()
            progress_bar.empty()
            update_report_state(
                json_str=json_str,
                resumen_ejecutivo=resumen_ejecutivo,
                edited_output=edited_output,
                report_sections=report_sections,
            )

        return None

    except Exception as e:  # pylint: disable=W0718
        return MESSAGES["errors"]["unexpected_error"].format(str(e))


def show_variable_exclusion_warning() -> None:
    """Show warning about excluded variables."""
    if st.session_state.get("report_generated"):
        excluded_count = sum(
            1
            for section_title, variables in st.session_state.filtered_sections_config.items()
            for var_config in variables
            if not st.session_state.get(f"section_{section_title}", {}).get(
                var_config[2]["name"], True
            )
        )
        if excluded_count > 0:
            st.sidebar.markdown(
                f"ℹ️ {excluded_count} variable{'s' if excluded_count != 1 else ''} "
                f"excluida{'s' if excluded_count != 1 else ''} del reporte"
            )


def render_download_visualisations(session_state):
    """Render visualisation download options in the sidebar."""
    if not session_state.report_finalized or not session_state.report_sections:
        return

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Gráficos disponibles")

    # Get all variables from all sections
    all_variables = {}
    for section in session_state.report_sections:
        all_variables.update(section.variables)

    # Get available charts based on variables
    available_charts = get_available_charts(all_variables)

    # Group charts by section
    charts_by_section = {}
    for chart_id, config in available_charts.items():
        section = config.get("section", "Otros indicadores")
        if section not in charts_by_section:
            charts_by_section[section] = {}
        charts_by_section[section][chart_id] = config

    # Create expandable sections
    for section_name, section_charts in charts_by_section.items():
        if section_charts:
            with st.sidebar.expander(f"📈 {section_name}"):
                for chart_id, config in section_charts.items():
                    chart, b64_str = create_downloadable_chart(chart_id, all_variables)
                    if chart and b64_str:
                        st.download_button(
                            label=f"📊 {config['params']['title']}",
                            data=base64.b64decode(b64_str),
                            file_name=f"{chart_id}.png",
                            mime="image/png",
                            key=f"download_viz_{chart_id}",
                        )
