"""UI constants and configuration."""

# Colors
BACKGROUND_COLOR = "#f9f9f9"

# Messages
MESSAGES = {
    "errors": {
        "no_file": "👆 Por favor, carga un archivo Excel con los datos del centro ZASCA para comenzar.",
        "file_error": "Error al procesar el archivo: {}",
        "data_error": "Error al procesar los datos: {}",
        "report_error": "Error durante la generación del reporte: {}",
        "unexpected_error": "Error inesperado: {}",
        "empty_suggestion": "Por favor, escribe una sugerencia antes de enviar.",
    },
    "success": {
        "report_generated": "🎉 ¡Reporte generado exitosamente!",
        "suggestion_sent": "¡Gracias por tu sugerencia! El equipo de IGL la revisará pronto.",
    },
    "info": {
        "generating_sections": "🤖 Generando contenido de secciones...",
        "generating_summary": "📝 Generando resumen ejecutivo...",
        "editing_report": "✍️ Realizando edición final...",
        "preparing_json": "💾 Preparando archivo JSON...",
        "missing_variables": "Las siguientes variables no fueron encontradas en los datos:",
    },
}

# File types
ALLOWED_EXTENSIONS = ["xlsx"]
MIME_TYPES = {
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "json": "application/json",
}

# Model options
OAI_MODEL_OPTIONS = {
    "gpt-3.5-turbo": "GPT-3.5 Turbo (Más rápido)",
    "gpt-4-0125-preview": "GPT-4 (Más preciso)",
}

GEMINI_MODEL_OPTIONS = {
    "gemini-2.0-flash": "Gemini 2.0 Flash (Más rápido)",
    "gemini-2.5-pro-exp-03-25": "Gemini 2.5 Pro (Experimental)",
}

# Help texts
HELP_TEXTS = {
    "oai_model_select": "Selecciona el modelo de OpenAI a utilizar. GPT-4 es más potente pero más lento.",
    "gemini_model_select": "Selecciona el modelo de Google Gemini a utilizar. Actualmente solo Gemini 2.0 Flash, ya que Gemini 2.5 Pro es más potente pero tiene un rate limit demasiado bajo en el free tier.",
    "generate_button": "Haz clic para generar el reporte basado en los datos y detalles proporcionados",
    "file_upload": "Selecciona un archivo Excel (.xlsx) con los datos del centro ZASCA",
    "unedited_download": "Descarga el reporte sin editar en formato Word",
    "edited_download": "Descarga el reporte editado en formato Word",
    "json_download": "Descarga los datos del reporte en formato JSON",
}
