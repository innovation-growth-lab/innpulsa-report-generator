"""Multi-response variable chart implementations."""

# pylint: disable=E0402
import plotly.graph_objects as go
import pandas as pd
from .utils import process_label, get_splits, COLORS


def create_multi_response_chart(data: pd.DataFrame, params: dict) -> go.Figure:
    """Creates a publication-quality chart for multi-response variables."""
    fig = go.Figure()

    # dynamic settings based on number of labels
    n_labels = len(params["labels"])

    max_chars, break_every = get_splits(n_labels)

    wrapped_labels = [
        process_label(label, max_chars, break_every) for label in params["labels"]
    ]

    # Add bars for "before" data only if numeric values are present
    before_data = data[data["period"] == "Línea Base"]
    has_before_trace = False
    if not before_data.empty and before_data["value"].dtype in ["int64", "float64"]:
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
                offset=-0.35,  # Always offset if we're adding this trace
            )
        )
        has_before_trace = True

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
            width=(0.3 if has_before_trace else 0.6),  # Wider bars when alone
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
