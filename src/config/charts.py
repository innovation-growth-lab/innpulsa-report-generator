"""Configuration for chart definitions and their required variables."""

from src.charts.multi_response import create_multi_response_chart
from src.charts.percentage_change import create_percentage_change_chart

# Define all possible charts and their requirements
chart_config = {
    # Optimización operativa
    "production_efficiency": {
        "type": "percentage_change",
        "section": "Optimización operativa",
        "chart_func": create_percentage_change_chart,
        "required_variables": ["production_efficiency"],
        "params": {
            "title": "Evolución de la eficiencia de producción",
            "y_label": "Porcentaje de eficiencia (%)",
        },
    },
    "defective_units": {
        "type": "percentage_change",
        "section": "Optimización operativa",
        "chart_func": create_percentage_change_chart,
        "required_variables": ["defective_units_rate"],
        "params": {
            "title": "Evolución de la tasa de unidades defectuosas",
            "y_label": "Porcentaje de unidades defectuosas (%)",
        },
    },
    "indicators_usage": {
        "type": "multi_response",
        "section": "Optimización operativa",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "indicadores_eficiencia",
            "indicadores_productividad",
            "index",
        ],
        "params": {
            "title": "Uso de indicadores",
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
    # Talento Humano
    "employment_metrics": {
        "type": "percentage_change",
        "section": "Talento Humano",
        "chart_func": create_percentage_change_chart,
        "required_variables": ["emp_ft"],
        "params": {
            "title": "Evolución del empleo total",
            "y_label": "Número de empleados",
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
    # Financiero
    "sales_evolution": {
        "type": "percentage_change",
        "section": "Financiero",
        "chart_func": create_percentage_change_chart,
        "required_variables": ["sales2023q1s"],
        "params": {
            "title": "Evolución de ventas trimestrales",
            "y_label": "Ventas (millones COP)",
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
