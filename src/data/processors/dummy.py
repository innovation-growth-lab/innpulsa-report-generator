"""Dummy variable processor."""

from typing import Dict, Tuple, Union
import pandas as pd
import numpy as np
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor


class DummyProcessor(BaseProcessor):
    """Process dummy variables.

    A dummy variable processor handles binary (yes/no) variables where we want to calculate
    the percentage of positive responses. It can handle both:
    1. Before/after comparisons with initial and final measurements
    2. Final-only measurements where we just want the percentage after intervention

    The processor calculates the percentage of non-null/non-empty responses and formats
    appropriate interpretations for each case.

    For before/after comparisons, it:
    - Calculates percentage of positive responses at initial and final points
    - Computes the percentage change between measurements
    - Generates an interpretation describing the change

    For final-only measurements, it:
    - Calculates percentage of positive responses at final point
    - Generates an interpretation describing the final state

    The processor handles missing data by treating empty strings and dots as null values.
    All percentages are rounded to 2 decimal places.
    """

    @staticmethod
    def calculate_dummy_percentage(series: pd.Series) -> float:
        """Calculate percentage of non-null values in a series.

        Args:
            series: Pandas series to analyze

        Returns:
            Percentage of non-null values rounded to 2 decimal places
        """
        return round(
            series.replace({"": np.nan, ".": np.nan})
            .infer_objects(copy=False)
            .notna()
            .mean()
            * 100,
            2,
        )

    def process(
        self, df: pd.DataFrame, var_pair: Tuple[Union[str, None], str], metadata: Dict
    ) -> VariableData:
        """Process dummy variables."""
        initial_col, final_col = var_pair
        description = metadata["description"]

        if final_col not in df.columns:
            raise ValueError(f"Column {final_col} not found in dataframe")

        if initial_col is None:
            final_value = self.calculate_dummy_percentage(df[final_col])
            interpretation = (
                f"Para {description}, {final_value}% "
                "de las empresas respondieron afirmativamente "
                "tras su participación en el programa."
            )

            return VariableData(
                variable=final_col,
                description=description,
                value_initial_intervention="N/A",
                value_final_intervention=final_value,
                percentage_change="N/A",
                interpretation=interpretation,
            )
        else:
            if initial_col not in df.columns:
                raise ValueError(f"Column {initial_col} not found in dataframe")

        initial_value = self.calculate_dummy_percentage(df[initial_col])
        final_value = self.calculate_dummy_percentage(df[final_col])
        pct_change = calculate_percentage_change(initial_value, final_value)

        interpretation = (
            f"El porcentaje de empresas que {description} pasó del {initial_value}% "
            f"al {final_value}%, representando un cambio del {pct_change}."
        )

        return VariableData(
            variable=final_col.replace("c", ""),
            description=description,
            value_initial_intervention=initial_value,
            value_final_intervention=final_value,
            percentage_change=pct_change,
            interpretation=interpretation,
        )
