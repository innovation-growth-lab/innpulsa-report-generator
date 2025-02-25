"""Multi-response variable chart implementations."""

import plotly.graph_objects as go
import pandas as pd

# Professional color palette
COLORS = {
    "dark_blue": "#092640",  # Pantone 2965 C
    "blue": "#1F5DAD",  # Pantone 7684 C
    "coral": "#FF5836",  # Pantone 171 C
    "yellow": "#FAB61B",  # Pantone 1235 C
    "turquoise": "#00B2A2",  # Pantone 3275 C
}


def create_multi_response_chart(data: pd.DataFrame, params: dict) -> go.Figure:
    """Creates a publication-quality chart for multi-response variables."""
    # Create figure with two bar groups
    fig = go.Figure()
    
    # Wrap x-axis labels
    wrapped_labels = [label.replace(" ", "<br>") for label in params["labels"]]
    
    # Add bars for "before" data
    before_data = data[data["period"] == "Línea Base"]
    fig.add_trace(
        go.Bar(
            name="Línea Base",
            x=wrapped_labels,
            y=before_data["value"],
            text=[f"{v:.1f}%" for v in before_data["value"]],
            textposition="auto",
            marker_color=COLORS["blue"],
            width=0.3,
            textfont={"family": "Arial", "size": 14, "color": "white"},
            offset=-0.2,  # Shift left
        )
    )
    
    # Add bars for "after" data
    after_data = data[data["period"] == "Cierre de la intervención"]
    fig.add_trace(
        go.Bar(
            name="Cierre de la intervención",
            x=wrapped_labels,
            y=after_data["value"],
            text=[f"{v:.1f}%" for v in after_data["value"]],
            textposition="auto",
            marker_color=COLORS["coral"],
            width=0.3,
            textfont={"family": "Arial", "size": 14, "color": "white"},
            offset=0.2,  # Shift right
        )
    )

    fig.update_layout(
        # Axis titles and formatting
        yaxis={
            "title": {
                "text": params.get("y_label", "Porcentaje de empresas (%)"),
                "font": {"family": "Arial", "size": 16, "color": COLORS["dark_blue"]},
                "standoff": 10,
            },
            "gridcolor": "lightgray",
            "gridwidth": 0.5,
            "zeroline": True,
            "zerolinecolor": COLORS["dark_blue"],
            "zerolinewidth": 1,
            "tickfont": {"family": "Arial", "size": 14, "color": COLORS["dark_blue"]},
            "showline": True,
            "linewidth": 1,
            "linecolor": COLORS["dark_blue"],
            "mirror": False,
        },
        xaxis={
            "showgrid": False,
            "tickfont": {"family": "Arial", "size": 14, "color": COLORS["dark_blue"]},
            "showline": True,
            "linewidth": 1,
            "linecolor": COLORS["dark_blue"],
            "mirror": False,
            "tickangle": 0  # Ensure labels are horizontal
        },
        # Tighter layout
        width=500,
        height=400,
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=True,
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1
        },
        margin={
            "t": 50,  # Increased top margin for legend
            "b": 80,  # Increased bottom margin for wrapped labels
            "l": 60,
            "r": 20,
            "pad": 0,
        },
        bargap=0,  # Remove gap between bar groups
    )

    return fig
