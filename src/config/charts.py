"""Configuration for chart definitions and their required variables."""

from src.charts.multi_response import create_multi_response_chart
from src.charts.simple_change import create_simple_change_chart
from src.charts.categorical_changes import create_categorical_chart

# Define all possible charts and their requirements
chart_config = {
    # Optimización operativa
    "production_efficiency": {
        "type": "simple_change",
        "section": "Optimización operativa",
        "chart_func": create_simple_change_chart,
        "required_variables": ["production_efficiency"],
        "params": {
            "title": "Eficiencia de producción (production_efficiency)",
            "y_label": "Porcentaje de eficiencia (%)",
            "text_format": "{:.1f}%",
        },
    },
    "knows_standardtime": {
        "type": "simple_change",
        "section": "Optimización operativa",
        "chart_func": create_simple_change_chart,
        "required_variables": ["knows_standardtime"],
        "params": {
            "title": "Estándares de tiempo (knows_standardtime)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "text_format": "{:.1f}%",
        },
    },
    "defective_units": {
        "type": "simple_change",
        "section": "Optimización operativa",
        "chart_func": create_simple_change_chart,
        "required_variables": ["defective_units_rate"],
        "params": {
            "title": "Tasa de unidades defectuosas (defective_units_rate)",
            "y_label": "Porcentaje de unidades defectuosas (%)",
            "text_format": "{:.1f}%",
        },
    },
    "observ_productionplant": {
        "type": "categorical",
        "section": "Optimización operativa",
        "chart_func": create_categorical_chart,
        "required_variables": ["observ_productionplant"],
        "params": {
            "title": "Espacio de producción (observ_productionplant)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    "invent_control": {
        "type": "categorical",
        "section": "Optimización operativa",
        "chart_func": create_categorical_chart,
        "required_variables": ["invent_control"],
        "params": {
            "title": "Control de inventario (invent_control)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    "knowsinput": {
        "type": "simple_change",
        "section": "Optimización operativa",
        "chart_func": create_simple_change_chart,
        "required_variables": ["knowsinput"],
        "params": {
            "title": "Conocimiento de niveles óptimos de inventario (knowsinput)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "text_format": "{:.1f}%",
        },
    },
    "indicators_usage": {
        "type": "multi_response",
        "section": "Optimización operativa",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "indicadores_eficiencia",
            "indicadores_productividad",
            "hasindicators",
        ],
        "params": {
            "title": "Uso de indicadores (eff, prod, hasindicators)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": ["Eficiencia", "Productividad", "Generales"],
        },
    },
    # Mayor Calidad del Producto
    "quality_processes": {
        "type": "multi_response",
        "section": "Mayor Calidad del Producto",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "qualityprocess_sample",
            "qualityprocess_set_machinery",
            "qualityprocess_control_quality",
            "qualityprocess_none",
        ],
        "params": {
            "title": "Procesos de calidad implementados",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Muestra y contramuestra",
                "Preparación maquinaria",
                "Calidad de materiales",
                "Sin procesos de calidad",
            ],
        },
    },
    "design_tools": {
        "type": "multi_response",
        "section": "Mayor Calidad del Producto",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "software_design",
            "patterns_digitized",
            "patterns_prevcollections",
        ],
        "params": {
            "title": "Herramientas de diseño",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Software especializado",
                "Patrones digitalizados",
                "Guarda patrones previos",
            ],
        },
    },
    "newideas_datasheet": {
        "type": "categorical",
        "section": "Mayor Calidad del Producto",
        "chart_func": create_categorical_chart,
        "required_variables": ["newideas_datasheet"],
        "params": {
            "title": "Registro de nuevos diseños (newideas_datasheet)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    "packaging": {
        "type": "categorical",
        "section": "Mayor Calidad del Producto",
        "chart_func": create_categorical_chart,
        "required_variables": ["packaging"],
        "params": {
            "title": "Empaque y presentación del producto (packaging)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    # Talento Humano
    "employment_metrics": {
        "type": "simple_change",
        "section": "Talento Humano",
        "chart_func": create_simple_change_chart,
        "required_variables": ["emp_ft"],
        "params": {
            "title": "Evolución del empleo total",
            "y_label": "Número de empleados",
            "text_format": "{:.1f}",
        },
    },
    "emp_total": {
        "type": "simple_change",
        "section": "Talento Humano",
        "chart_func": create_simple_change_chart,
        "required_variables": ["emp_total"],
        "params": {
            "title": "Empleados totales (emp_total)",
            "y_label": "Número de empleados",
            "text_format": "{:.0f}",
        },
    },
    "hassalary": {
        "type": "simple_change",
        "section": "Talento Humano",
        "chart_func": create_simple_change_chart,
        "required_variables": ["hassalary"],
        "params": {
            "title": "Postulante con sueldo fijo (hassalary)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "text_format": "{:.1f}%",
        },
    },
    "income": {
        "type": "simple_change",
        "section": "Talento Humano",
        "chart_func": create_simple_change_chart,
        "required_variables": ["income"],
        "params": {
            "title": "Sueldo fijo mensual promedio (income)",
            "y_label": "Pesos colombianos (COP)",
            "text_format": "{:,.0f}",
        },
    },
    # Practicas Gerenciales
    "knowledge_indicators": {
        "type": "multi_response",
        "section": "Practicas Gerenciales",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "knows_production_cost",
            "knows_max_production",
            "knows_profit_margin",
            "knows_sales_frequency",
            "knows_detailed_income",
        ],
        "params": {
            "title": "Conocimiento de indicadores clave",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Costo por unidad",
                "Capacidad máxima",
                "Margen de ganancia",
                "Frecuencia de ventas",
                "Ingresos detallados",
            ],
        },
    },
    "product_cost_tracking": {
        "type": "multi_response",
        "section": "Practicas Gerenciales",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "productcost_materials",
            "productcost_handwork",
            "productcost_fabrication",
        ],
        "params": {
            "title": "Componentes calculados del costo",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Materiales directos",
                "Mano de obra directa",
                "Gastos de fabricación",
            ],
        },
    },
    "price_system": {
        "type": "categorical",
        "section": "Practicas Gerenciales",
        "chart_func": create_categorical_chart,
        "required_variables": ["price_system"],
        "params": {
            "title": "Sistema de fijación de precios (price_system)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    # Financiero
    "sales_evolution": {
        "type": "simple_change",
        "section": "Financiero",
        "chart_func": create_simple_change_chart,
        "required_variables": ["sales2023q1s"],
        "params": {
            "title": "Evolución de ventas trimestrales",
            "y_label": "Ventas (millones COP)",
            "text_format": "{:d}",
        },
    },
    "financial_connections": {
        "type": "multi_response",
        "section": "Financiero",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "participate_commercial",
            "connection_commercial",
            "participate_financial",
            "connection_financial",
        ],
        "params": {
            "title": "Participación en ruedas comerciales y financieras",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Participó rueda comercial",
                "Generó conexiones comerciales",
                "Participó rueda financiera",
                "Generó conexiones financieras",
            ],
        },
    },
    "sales2023": {
        "type": "simple_change",
        "section": "Financiero",
        "chart_func": create_simple_change_chart,
        "required_variables": ["sales2023"],
        "params": {
            "title": "Evolución de ventas anuales (sales2023)",
            "y_label": "Ventas (millones COP)",
            "text_format": "{:,.0f}",
        },
    },
    "salesaverage2024": {
        "type": "simple_change",
        "section": "Financiero",
        "chart_func": create_simple_change_chart,
        "required_variables": ["salesaverage2024"],
        "params": {
            "title": "Ventas mensuales promedio 2024 (salesaverage2024)",
            "y_label": "Ventas (millones COP)",
            "text_format": "{:,.0f}",
        },
    },
    "banked": {
        "type": "simple_change",
        "section": "Financiero",
        "chart_func": create_simple_change_chart,
        "required_variables": ["banked"],
        "params": {
            "title": "Cuenta bancaria (banked)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "text_format": "{:.1f}%",
        },
    },
    "bookkeeping": {
        "type": "categorical",
        "section": "Financiero",
        "chart_func": create_categorical_chart,
        "required_variables": ["bookkeeping"],
        "params": {
            "title": "Sistema de contabilidad (bookkeeping)",
            "y_label": "Porcentaje de unidades productivas (%)",
        },
    },
    # Asociatividad
    "association_purposes": {
        "type": "multi_response",
        "section": "Asociatividad",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "association_group_training",
            "association_new_machinery",
            "association_buy_supplies",
            "association_use_machinery_nobuy",
            "association_new_markets",
            "association_distribution",
            "association_have_not",
        ],
        "params": {
            "title": "Propósitos de asociatividad",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Capacitaciones grupales",
                "Adquirir maquinaria",
                "Comprar insumos",
                "Usar maquinaria compartida",
                "Acceder nuevos mercados",
                "Logística y distribución",
                "No se ha asociado",
            ],
        },
    },
    "knows_associationways": {
        "type": "simple_change",
        "section": "Asociatividad",
        "chart_func": create_simple_change_chart,
        "required_variables": ["knows_associationways"],
        "params": {
            "title": "Conocimiento de mecanismos de asociatividad (knows_associationways)",
            "y_label": "Porcentaje de unidades productivas (%)",
            "text_format": "{:.1f}%",
        },
    },
}

# TODO: Numeric (currently false %s) & Categoricals


def get_available_charts(variables_dict: dict) -> dict:
    """
    Determine which charts can be created based on available variables.

    Args:
        variables_dict: Dictionary of available processed variables

    Returns:
        Dictionary of available charts and their configurations
    """
    available_charts = {}

    for chart_id, config in chart_config.items():
        # Check if all required variables are present
        if any(var in variables_dict for var in config["required_variables"]):
            available_charts[chart_id] = config

    return available_charts
