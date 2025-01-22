"""Aplicación."""

import asyncio
import streamlit as st

from src.sections_config import sections_config
from src.utils import load_data, aggregate_data, generate_json_output
from src.openai_helpers import (
    generate_section_contents,
    generate_executive_summary,
    edit_report_sections,
)


# Título principal
st.title("Generador de Reportes ZASCA")

# Descripción de la aplicación
st.markdown(
    """
    Bienvenido al Generador de Reportes ZASCA. 
    Crea reportes para apoyar la estrategia de reindustrialización ZASCA en Colombia. 
    Proporciona un formato profesional que incluye un resumen ejecutivo y análisis de datos.
    """
)

# Sección para carga de archivo
uploaded_file = st.file_uploader("Carga tu conjunto de datos (XLSX)", type="xlsx")
if uploaded_file is not None:
    # persist trick
    st.session_state.uploaded_file = uploaded_file
    # cargar y mostrar el conjunto de datos
    df = load_data(st.session_state.uploaded_file)
    st.markdown("### 📊 Vista previa de los datos cargados")
    st.dataframe(df, use_container_width=True)

    # Solicitar detalles adicionales en la barra lateral
    st.sidebar.header("Detalles del Reporte")
    cohort_details = {
        "centro": st.sidebar.text_input(
            "Nombre del Centro ZASCA", placeholder="Ej.: Ciudad Bolívar"
        ),
        "cohorte": st.sidebar.text_input(
            "Número de la Cohorte", placeholder="Ej.: Primera Cohorte"
        ),
        "sector": st.sidebar.text_input(
            "Sector", placeholder="Ej.: Textiles, Manufactura, Servicios"
        ),
        "informacion_adicional": st.sidebar.text_input(
            "Información adicional: ", placeholder="Ej.: Fechas"
        ),
    }
    COHORT_INFO_STR = ", ".join(
        f"{key}: {value}" for key, value in cohort_details.items() if value
    )

    # botón para generar el reporte
    if st.button("Generar Reporte"):
        st.info("Generando el reporte...")

        # agregar datos y generar reporte
        report_sections = aggregate_data(df, sections_config)

        # generar contenido para cada sección
        asyncio.run(generate_section_contents(report_sections, COHORT_INFO_STR))

        # generar resumen ejecutivo
        resumen_ejecutivo = asyncio.run(
            generate_executive_summary(report_sections, COHORT_INFO_STR)
        )

        # editar contenido de las secciones
        edited_output = asyncio.run(edit_report_sections(report_sections))

        # crear el archivo JSON
        json_output = generate_json_output(report_sections, resumen_ejecutivo)

        # mostrar opciones de descarga y vista previa
        st.success("¡Reporte generado!")
        st.download_button(
            label="📥 Descargar Reporte en JSON",
            data=json_output,
            file_name="reporte_zasca.json",
            mime="application/json",
        )
        with st.expander("Ver Reporte en JSON"):
            st.json(json_output)

        # mostrar contenido editado de las secciones
        st.markdown("### 📄 Contenido Editado de las Secciones")
        st.markdown("#### Resumen Ejecutivo")
        st.markdown(resumen_ejecutivo)
        st.markdown(edited_output)
else:
    st.info("Carga un archivo para comenzar.")
