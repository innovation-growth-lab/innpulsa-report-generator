"""Indicator-specific chart implementations."""

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


def create_simple_change_chart(data: pd.DataFrame, params: dict) -> go.Figure:
    """Creates a publication-quality chart for before and after variables.
    
    Args:
        data: DataFrame with 'period' and 'value' columns
        params: Dictionary containing:
            - y_label: Label for y-axis
            - text_format: Optional format string (e.g. '{:.1f}%' or '{:,.0f}')
                         Defaults to '{:.1f}%' for percentages
    """
    # Get text format from params or use percentage as default
    text_format = params.get('text_format', '{:.1f}%')
    
    fig = go.Figure(
        data=[
            go.Bar(
                x=data["period"],
                y=data["value"],
                text=[text_format.format(v) for v in data["value"]],
                textposition="auto",
                marker_color=[COLORS["blue"], COLORS["coral"]],
                width=0.6,
                textfont={"family": "Arial", "size": 14, "color": "white"},
            )
        ]
    )

    fig.update_layout(
        # Axis titles and formatting
        yaxis={
            "title": {
                "text": params.get("y_label", ""),
                "font": {"family": "Arial", "size": 16, "color": COLORS["dark_blue"]},
                "standoff": 10,  # Reduced space between title and axis
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
        },
        # Tighter layout
        width=500,
        height=400,
        plot_bgcolor="white",
        paper_bgcolor="white",
        showlegend=False,
        margin={
            "t": 30,  # Reduced top margin
            "b": 50,  # Reduced bottom margin
            "l": 60,  # Reduced left margin
            "r": 20,  # Reduced right margin
            "pad": 0,  # Remove padding
        },
    )

    return fig
