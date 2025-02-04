import asyncio
import streamlit as st
from src.sections_config import sections_config
from src.utils import load_data, aggregate_data, generate_json_output
from src.openai_helpers import (
    generate_section_contents,
    generate_executive_summary,
    edit_report_sections,
)

st.set_page_config(
    layout="centered", page_title="Generador de Reportes ZASCA", page_icon="📊"
)
st.image("assets/zasca_logo.png")

# Application Title
st.title("\U0001F4DA Generador de Reportes ZASCA")


# Description Section
st.markdown(
    """
    <hr style="margin: 20px 0;">
    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px;">
        <p>
            Esta herramienta está diseñada para ayudar a <strong>INNPULSA</strong> a 
            crear los informes de cierre de los centros <strong>ZASCA</strong> que 
            apoyan la estrategia de reindustrialización en Colombia.
        </p>
        <hr>
        <p>
            Con esta aplicación, puedes cargar tus datos de un centro ZASCA en formato 
            <strong>XLSX</strong>, proporcionar detalles específicos sobre la cohorte y 
            el centro ZASCA, y generar un informe completo que incluye un <strong>resumen 
            ejecutivo</strong>. Por el momento, este no crea el reporte PDF, sino 
            únicamente el contenido.
        </p>
        <hr>
        <p>
            Además, tienes la opción de seleccionar el modelo de <strong>OpenAI</strong> 
            que prefieras utilizar para generar el contenido del informe. 
            Los modelos disponibles son <b>gpt-3.5-turbo</b> y <b>gpt-4o-2024-08-06</b>. 
            Elige el modelo que mejor se adapte a tus necesidades y preferencias una vez 
            hayas cargado los datos, en el menú de la izquierda.
        </p>
        <hr>
        <p>
            Una vez generado el informe, podrás descargarlo en formato <strong>JSON</strong> 
            y visualizar el contenido editado directamente en la página.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# File Upload Section
st.sidebar.markdown("### 📂 Subir un archivo de datos")
with st.container():
    uploaded_file = st.sidebar.file_uploader(
        "Carga tu conjunto de datos (XLSX)", type="xlsx"
    )
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        df = load_data(st.session_state.uploaded_file)
        st.markdown("### Vista previa de los datos cargados")
        st.dataframe(df, use_container_width=True)

        # Sidebar Input Fields
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
                "Información adicional", placeholder="Ej.: Fechas"
            ),
        }
        COHORT_INFO_STR = ", ".join(
            f"{key}: {value}" for key, value in cohort_details.items() if value
        )

        st.sidebar.markdown("---")
        model_name = st.sidebar.selectbox(
            "Modelo de OpenAI", ["gpt-3.5-turbo", "gpt-4o-2024-08-06"], index=0
        )

        # Generate Report Button
        if st.button(
            "Generar Reporte",
            help="Haz clic para generar el reporte basado en los datos y detalles proporcionados",
        ):
            # Create containers for progress information
            progress_container = st.container()
            with progress_container:
                st.info("🚀 Iniciando generación del reporte...")

                # Progress bar for sections
                progress_bar = st.progress(0)
                status_text = st.empty()

                # Generate sections
                report_sections = aggregate_data(df, sections_config)
                asyncio.run(
                    generate_section_contents(
                        report_sections, COHORT_INFO_STR, model_name, progress_bar
                    )
                )

                # Update status for executive summary
                status_text.info("📝 Generando resumen ejecutivo...")
                resumen_ejecutivo = asyncio.run(
                    generate_executive_summary(
                        report_sections, COHORT_INFO_STR, model_name
                    )
                )

                # Update status for final edits
                status_text.info("✍️ Realizando edición final...")
                edited_output = asyncio.run(edit_report_sections(report_sections))

                # Generate JSON
                status_text.info("💾 Preparando archivo JSON...")
                raw_json_output = generate_json_output(
                    report_sections, resumen_ejecutivo
                )

                # Clear progress indicators and show success
                progress_container.empty()
                st.success("🎉 ¡Reporte generado exitosamente!")

            # Success Message and Download Options
            st.download_button(
                label="Descargar Reporte en JSON",
                data=edited_output.replace("\n", "<br>"),
                file_name="reporte_zasca.json",
                mime="application/json",
                help="Descarga el reporte generado como un archivo JSON",
            )

            with st.expander("\U0001F4C4 Ver Reporte sin editar en JSON"):
                st.json(raw_json_output)

            st.markdown("### Contenido del Reporte")
            st.markdown("#### Resumen Ejecutivo")
            st.markdown(resumen_ejecutivo)
            st.markdown(edited_output)


# Footer with Logos
st.markdown("---")
_, col1, _, col3, _ = st.columns([1, 2, 3, 2, 1])

with col1:
    st.image("assets/innpulsa_logo.png", use_container_width=True)

with col3:
    st.image("assets/igl_logo.png", use_container_width=True)
