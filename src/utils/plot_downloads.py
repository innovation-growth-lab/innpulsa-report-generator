import base64
import pandas as pd
from src.config.charts import chart_config


def create_downloadable_chart(chart_id: str, variables_dict: dict):
    """
    Creates a downloadable chart if all required variables are available

    Args:
        chart_id: ID of the chart to create
        variables_dict: Dictionary of available processed variables

    Returns:
        tuple: (chart object, base64 string for download) or (None, None) if chart cannot be created
    """
    config = chart_config.get(chart_id)
    if not config:
        return None, None

    # Check if we have all required variables
    if not all(var in variables_dict for var in config["required_variables"]):
        return None, None

    # Prepare data based on chart type
    if config["type"] == "multi_response":
        # Create rows for each variable and period
        rows = []
        for var_name in config["required_variables"]:
            rows.extend(
                [
                    {
                        "period": "Línea Base",
                        "value": variables_dict[var_name].value_initial_intervention,
                        "variable": var_name,
                    },
                    {
                        "period": "Cierre de la intervención",
                        "value": variables_dict[var_name].value_final_intervention,
                        "variable": var_name,
                    },
                ]
            )
        data = pd.DataFrame(rows)

    elif config["type"] == "percentage_change":
        var = variables_dict[config["required_variables"][0]]
        data = pd.DataFrame(
            {
                "period": ["Línea Base", "Cierre de la intervención"],
                "value": [var.value_initial_intervention, var.value_final_intervention],
            }
        )
    else:
        raise ValueError(f"Unsupported chart type: {config['type']}")

    # Create and return chart
    fig = config["chart_func"](data, config["params"])
    img_bytes = fig.to_image(format="png", scale=2)
    b64 = base64.b64encode(img_bytes).decode()

    return fig, b64
