"""Configuration for chart definitions and their required variables."""

from src.charts.multi_response import create_multi_response_chart
from src.charts.indicators import create_before_after_chart

# Define all possible charts and their requirements
chart_config = {
    "production_efficiency_c1": {
        "type": "efficiency",
        "chart_func": create_before_after_chart,
        "required_variables": [
            "production_efficiency_c1"
        ],
        "params": {
            "title": "Evolución de la eficiencia",
            "y_label": "Porcentaje de eficiencia (%)"
        }
    },
    "production_efficiency_c4": {
        "type": "efficiency",
        "chart_func": create_before_after_chart,
        "required_variables": [
            "production_efficiency_c4"
        ],
    },
    "quality_processes": {
        "type": "multi_response",
        "chart_func": create_multi_response_chart,
        "required_variables": [
            "qualityprocess_sample",
            "qualityprocess_set_machinery",
            "qualityprocess_control_quality",
            "qualityprocess_none"
        ],
        "params": {
            "title": "Procesos de calidad implementados",
            "y_label": "Porcentaje de unidades productivas (%)",
            "labels": [
                "Muestra y contramuestra",
                "Preparación maquinaria",
                "Calidad de materiales",
                "Sin procesos de calidad"
            ]
        }
    },
    # [TODO] Add more charts here...
}

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