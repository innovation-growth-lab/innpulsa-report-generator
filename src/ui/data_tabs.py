"""UI components for the data input and processing tabs."""

from typing import Dict, Tuple, Any
import streamlit as st
import pandas as pd
from src.config.sections import get_sections_config


def render_cohort_info() -> str:
    """
    Render the cohort information input form.

    Returns:
        String containing formatted cohort information
    """
    st.markdown("### Información del Centro ZASCA")
    cohort_details = {
        "centro": st.text_input(
            "Nombre del Centro ZASCA", placeholder="Ej.: Ciudad Bolívar"
        ),
        "cohorte": st.text_input(
            "Número de la Cohorte", placeholder="Ej.: Primera Cohorte"
        ),
        "sector": st.text_input(
            "Sector", placeholder="Ej.: Textiles, Manufactura, Servicios"
        ),
        "informacion_adicional": st.text_input(
            "Información adicional", placeholder="Ej.: Fechas"
        ),
    }
    return ", ".join(
        f"{key}: {value}" for key, value in cohort_details.items() if value
    )


def render_data_preview(df: pd.DataFrame) -> None:
    """
    Render the data preview table.

    Args:
        df: DataFrame to display
    """
    st.markdown("### Vista previa de los datos cargados")
    st.dataframe(df, use_container_width=True)


@st.cache_data
def check_variable_availability(
    df: pd.DataFrame, var_config: dict
) -> Tuple[bool, Dict[str, Any]]:
    """
    Check if variables are available in the dataframe.

    Args:
        df: DataFrame containing the data
        var_config: Dictionary containing variable configuration

    Returns:
        Tuple containing:
        - Boolean indicating if variable is available
        - Dictionary with variable metadata
    """
    var_type = var_config["type"]
    metadata = var_config["metadata"]
    var_pairs = var_config["var_pairs"]

    # Try each variable pair until we find one that works
    for var_pair in var_pairs:
        is_available = True

        if not isinstance(var_type, list):
            var_type = [var_type]

        for var_type in var_type:
            if var_type == "indicator":
                (initial_nums, initial_denoms), (final_nums, final_denoms) = var_pair
                if isinstance(initial_nums, list):
                    if not any(col in df.columns for col in initial_nums):
                        is_available = False
                    if not any(col in df.columns for col in initial_denoms):
                        is_available = False
                elif initial_nums not in df.columns or initial_denoms not in df.columns:
                    is_available = False

                if isinstance(final_nums, list):
                    if not any(col in df.columns for col in final_nums):
                        is_available = False
                    if not any(col in df.columns for col in final_denoms):
                        is_available = False
                elif final_nums not in df.columns or final_denoms not in df.columns:
                    is_available = False
            else:
                initial, final = var_pair
                if initial:
                    if isinstance(initial, list):
                        if not any(col in df.columns for col in initial):
                            is_available = False
                    elif initial not in df.columns:
                        is_available = False
                if final not in df.columns:
                    is_available = False

            if is_available:
                return True, metadata

    return False, metadata


def process_sections_config(df: pd.DataFrame) -> Tuple[dict, dict, dict]:
    """
    Process sections configuration once to identify available and missing variables.

    Args:
        df: DataFrame containing the data

    Returns:
        Tuple containing:
        - Dictionary of sections configuration
        - Dictionary of available variables by section
        - Dictionary of missing variables by section
    """
    sections_config = get_sections_config(df)
    available_vars = {}
    missing_vars = {}

    for section_title, variables in sections_config.items():
        section_available = {}
        section_missing = []

        for var_name, var_config in variables.items():
            is_available, metadata = check_variable_availability(df, var_config)
            if is_available:
                section_available[var_name] = var_config
            else:
                var_desc = f"{metadata['description']} ({metadata['name']})"
                section_missing.append(var_desc)

        if section_available:
            available_vars[section_title] = section_available
        if section_missing:
            missing_vars[section_title] = section_missing

    return sections_config, available_vars, missing_vars


def render_variable_selector(df: pd.DataFrame) -> None:
    """
    Render the variable selection interface.

    Args:
        df: DataFrame containing the data
    """
    st.markdown("### Selección de Variables por Sección")

    # Initialise selection states if not exists
    if "variable_selections" not in st.session_state:
        st.session_state.variable_selections = {}

    # Process config and identify variables only once
    if (
        "sections_config" not in st.session_state
        or "available_vars" not in st.session_state
        or "missing_vars" not in st.session_state
    ):
        (
            st.session_state.sections_config,
            st.session_state.available_vars,
            st.session_state.missing_vars,
        ) = process_sections_config(df)

        # Initialise filtered config
        st.session_state.filtered_sections_config = {
            section: vars for section, vars in st.session_state.available_vars.items()
        }

    # Process each section
    for section_title, _ in st.session_state.sections_config.items():
        with st.expander(f"### {section_title}"):
            available_vars = st.session_state.available_vars.get(section_title, {})

            if available_vars:
                # Create selection table
                selection_data = []
                section_key = f"section_{section_title}"

                # Initialise section selections if not exists
                if section_key not in st.session_state.variable_selections:
                    st.session_state.variable_selections[section_key] = {
                        var_config["metadata"]["description"]: True
                        for var_config in available_vars.values()
                    }

                # Create selection data
                for var_name, var_config in available_vars.items():
                    metadata = var_config["metadata"]
                    selection_data.append(
                        {
                            "Incluir": st.session_state.variable_selections[
                                section_key
                            ][metadata["description"]],
                            "Descripción": f"{metadata['description']} ({metadata['name']})",
                            "Tipo": var_config["type"],
                        }
                    )

                # Display editable table
                edited_df = st.data_editor(
                    pd.DataFrame(selection_data),
                    column_config={
                        "Incluir": st.column_config.CheckboxColumn("Incluir"),
                        "Descripción": st.column_config.TextColumn(
                            "Descripción", width="large"
                        ),
                        "Tipo": st.column_config.TextColumn("Tipo", width="small"),
                    },
                    disabled=["Descripción", "Tipo"],
                    hide_index=True,
                    key=f"editor_{section_title}",
                    use_container_width=True,
                )

                # Update selections and filtered config
                selected_vars = {}
                for indx, row in edited_df.iterrows():
                    var_name = list(available_vars.keys())[indx]
                    metadata = available_vars[var_name]["metadata"]
                    st.session_state.variable_selections[section_key][
                        metadata["description"]
                    ] = row["Incluir"]
                    if row["Incluir"]:
                        selected_vars[var_name] = available_vars[var_name]

                st.session_state.filtered_sections_config[section_title] = selected_vars

            # Show missing variables from session state
            if section_title in st.session_state.missing_vars:
                st.markdown("---")
                st.markdown("**Variables no disponibles en los datos:**")
                for var_name in st.session_state.missing_vars[section_title]:
                    st.markdown(f"- {var_name}")
