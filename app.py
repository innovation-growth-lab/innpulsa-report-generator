"""Main application file for the ZASCA Report Generator."""

import asyncio
import streamlit as st
from src.ui import tabs, data_tabs, report, sidebar
from src.data.loaders import load_data
from src.utils.state import init_session_state
from src.utils.errors import safe_operation, show_error
from src.utils.constants import MESSAGES


async def main() -> None:
    """Main application function."""
    # Initialize session state
    session_state = init_session_state()

    # Page config
    st.set_page_config(
        layout="centered", page_title="Generador de Reportes ZASCA", page_icon="📊"
    )

    # Header
    st.image("assets/zasca_logo.png")
    st.title("📚 Generador de Reportes ZASCA")

    # Render main information tabs
    tabs.render_info_tabs()

    # Render sidebar elements
    uploaded_file = sidebar.render_file_uploader()
    model_name, generate_report = sidebar.render_sidebar_controls()

    if uploaded_file:
        try:
            # Load and process data
            df = safe_operation(load_data, "file_error", uploaded_file)
            if df is None:
                return

            # Render data tabs
            data_tab1, data_tab2, data_tab3 = tabs.render_data_tabs()

            with data_tab1:
                cohort_info = data_tabs.render_cohort_info()

            with data_tab2:
                data_tabs.render_data_preview(df)

            with data_tab3:
                data_tabs.render_variable_selector(df)

            if generate_report:
                error_message = await sidebar.handle_report_generation(
                    df, cohort_info, model_name
                )
                if error_message:
                    show_error(error_message)

            # Show variable exclusion warning if needed
            sidebar.show_variable_exclusion_warning()

            # Display download buttons and results if report is finalized
            if session_state.report_finalized:
                # Show persistent success message
                if session_state.success_message:
                    st.sidebar.success(session_state.success_message)

                report.render_download_buttons(session_state)
                report.render_report_results(session_state)

        except Exception as e:  # pylint: disable=broad-except
            show_error(MESSAGES["errors"]["unexpected_error"].format(str(e)))

    # Footer with Logos
    st.markdown("---")
    _, col1, _, col3, _ = st.columns([1, 2, 3, 2, 1])
    with col1:
        st.image("assets/innpulsa_logo.png", use_container_width=True)
    with col3:
        st.image("assets/igl_logo.png", use_container_width=True)


if __name__ == "__main__":
    asyncio.run(main())
