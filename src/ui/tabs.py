"""UI components for the main tabs."""

import streamlit as st
from typing import List, Tuple
from src.services.feedback import save_suggestion
from src.utils.constants import MESSAGES, BACKGROUND_COLOR
from src.utils.errors import safe_operation

def render_description_tab() -> None:
    """Render the description tab content."""
    st.markdown(
        f"""
        <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px;">
            <div style="margin-bottom: 20px;">
                <p>
                    Esta herramienta está diseñada para ayudar a <strong>INNPULSA</strong> a 
                    crear los informes de cierre de los centros <strong>ZASCA</strong> que 
                    apoyan la estrategia de reindustrialización en Colombia.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div style="height: 20px;"></div>""",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px; height: 100%;">
                <h5 style="color: #2c3e50;">✅ Lo que hace</h5>
                <ul style="margin-left: 20px;">
                    <li>Genera un primer borrador estructurado que sirve como base para el informe final</li>
                    <li>Calcula automáticamente indicadores clave a partir de los datos</li>
                    <li>Proporciona interpretaciones preliminares de los cambios observados</li>
                    <li>Estructura la información en secciones temáticas coherentes</li>
                    <li>Genera un resumen ejecutivo inicial</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px; height: 100%;">
                <h5 style="color: #2c3e50;">❌ Lo que NO hace</h5>
                <ul style="margin-left: 20px;">
                    <li>No produce un informe final listo para publicar</li>
                    <li>No reemplaza el análisis experto del equipo técnico</li>
                    <li>No genera el documento en formato PDF o Word</li>
                    <li>No valida la calidad o coherencia de los datos de entrada</li>
                    <li>No incorpora automáticamente información contextual no proporcionada</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

def render_process_tab() -> None:
    """Render the process tab content."""
    st.markdown(
        f"""
        <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px;">
            <ol>
                <li><strong>Preparación de Datos</strong>
                    <ul>
                        <li>Cargar el archivo Excel con los datos de diagnóstico y cierre</li>
                        <li>Revisar las variables disponibles en el menú lateral</li>
                        <li>Verificar qué variables están ausentes o incompletas</li>
                    </ul>
                </li>
                <li><strong>Generación del Reporte</strong>
                    <ul>
                        <li>Completar la información contextual del centro ZASCA</li>
                        <li>Seleccionar el modelo de IA según necesidad de precisión</li>
                        <li>Generar el reporte inicial</li>
                    </ul>
                </li>
                <li><strong>Revisión y Edición</strong>
                    <ul>
                        <li>Verificar la precisión de los cálculos e interpretaciones</li>
                        <li>Evaluar la relevancia de las variables incluidas</li>
                        <li>Considerar el contexto específico del centro</li>
                    </ul>
                </li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_considerations_tab() -> None:
    """Render the considerations tab content."""
    st.markdown(
        f"""
        <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px;">
            <div style="margin-bottom: 20px;">
                <h4 style="color: #2c3e50;">🔍 Verificación de Datos</h4>
                <p style="margin-left: 20px;">
                    El reporte generado debe ser revisado cuidadosamente. Los cálculos son 
                    automáticos pero requieren validación humana para asegurar su precisión
                    en el contexto específico.
                </p>
            </div>
            <!-- ... rest of the considerations content ... -->
        </div>
        """,
        unsafe_allow_html=True,
    )

def handle_suggestion_submission(
    suggestion_text: str,
    suggestion_category: str,
    suggestion_details: str
) -> None:
    """
    Handle the submission of a suggestion.
    
    Args:
        suggestion_text: Main suggestion text
        suggestion_category: Category of the suggestion
        suggestion_details: Additional details
    """
    if suggestion_text.strip():
        safe_operation(
            save_suggestion,
            "unexpected_error",
            suggestion=suggestion_text,
            category=suggestion_category,
            details=suggestion_details
        )
        st.success(MESSAGES["success"]["suggestion_sent"])
    else:
        st.error(MESSAGES["errors"]["empty_suggestion"])

def render_feedback_tab() -> None:
    """Render the feedback tab content."""
    st.markdown("### Sugerencias y Solicitudes")
    st.markdown(
        f"""
        <div style="background-color: {BACKGROUND_COLOR}; padding: 20px; border-radius: 10px;">
            <p>¿Tienes alguna sugerencia para mejorar la herramienta o necesitas alguna funcionalidad adicional?
            Compártela con nosotros.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    suggestion_category = st.selectbox(
        "Categoría",
        ["Mejora de funcionalidad", "Nueva característica", "Reporte de error", "Otro"],
    )

    suggestion_text = st.text_area(
        "Sugerencia",
        placeholder="Describe tu sugerencia o solicitud..."
    )

    suggestion_details = st.text_area(
        "Detalles adicionales",
        placeholder="Proporciona cualquier detalle adicional que nos ayude a entender mejor tu solicitud...",
    )

    if st.button("Enviar sugerencia"):
        handle_suggestion_submission(suggestion_text, suggestion_category, suggestion_details)

def render_info_tabs() -> None:
    """Render all information tabs."""
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Descripción General",
        "📋 Proceso de Uso",
        "⚠️ Consideraciones",
        "💡 Sugerencias",
    ])

    with tab1:
        render_description_tab()
    with tab2:
        render_process_tab()
    with tab3:
        render_considerations_tab()
    with tab4:
        render_feedback_tab()

def render_data_tabs() -> Tuple[st.tabs, st.tabs, st.tabs]:
    """
    Render the data processing tabs.
    
    Returns:
        Tuple of three tab objects for information, data, and variables
    """
    return st.tabs(["📋 Información", "📊 Datos", "🔍 Variables"]) 