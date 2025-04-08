"""Categorical changes chart implementation."""

# pylint: disable=E0402
import plotly.graph_objects as go
import pandas as pd
from .utils import process_label, get_splits, COLORS


def create_categorical_chart(data: pd.DataFrame, params: dict) -> go.Figure:
    """Creates a publication-quality chart for categorical variable changes.

    Args:
        data: DataFrame with columns 'category', 'period', and 'value'
        params: Dictionary containing chart parameters

    Returns:
        Plotly figure object
    """
    fig = go.Figure()

    # filter out categories that have 0%
    categories_to_keep = []
    for category in data["category"].unique():
        cat_data = data[data["category"] == category]
        before_val = cat_data[cat_data["period"] == "Línea Base"]["value"].iloc[0]
        after_val = cat_data[cat_data["period"] == "Cierre de la intervención"][
            "value"
        ].iloc[0]
        if before_val > 0 or after_val > 0:
            categories_to_keep.append(category)

    # Filter data to keep only non-zero categories
    data = data[data["category"].isin(categories_to_keep)]

    # dynamic settings based on number of categories
    n_categories = len(categories_to_keep)

    max_chars, break_every = get_splits(n_categories)

    # Process category labels
    data["category_short"] = data["category"].apply(
        lambda x: process_label(x, max_chars, break_every)
    )

    categories = data["category_short"].unique()

    # Add bars for "before" data
    before_data = data[data["period"] == "Línea Base"]
    if not before_data.empty and before_data["value"].dtype in ["int64", "float64"]:
        fig.add_trace(
            go.Bar(
                name="Línea Base",
                x=categories,
                y=before_data["value"],
                text=[f"{v:.1f}%" for v in before_data["value"]],
                textposition="auto",
                marker_color=COLORS["blue"],
                width=0.3,
                textfont={"family": "Arial", "size": 14, "color": "white"},
                offset=-0.35,
            )
        )
        has_before_trace = True
    else:
        has_before_trace = False

    # Add bars for "after" data
    after_data = data[data["period"] == "Cierre de la intervención"]
    fig.add_trace(
        go.Bar(
            name="Cierre de la intervención",
            x=categories,
            y=after_data["value"],
            text=[f"{v:.1f}%" for v in after_data["value"]],
            textposition="auto",
            marker_color=COLORS["coral"],
            width=(0.3 if has_before_trace else 0.6),
            textfont={"family": "Arial", "size": 14, "color": "white"},
            offset=(0.05 if has_before_trace else -0.3),
        )
    )

    fig.update_layout(
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
            "tickangle": 0,
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
            "x": 1,
        },
        margin={
            "t": 50,
            "b": 80,
            "l": 60,
            "r": 20,
            "pad": 0,
        },
        bargap=0,
    )

    return fig
