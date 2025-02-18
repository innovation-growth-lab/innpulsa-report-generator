"""Indicator processor."""

from typing import Dict, List, Tuple, Union
import numpy as np
import pandas as pd
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor

class IndicatorProcessor(BaseProcessor):
    def process(
        self,
        df: pd.DataFrame,
        var_pair: Tuple[Tuple[Union[List[str], str], Union[List[str], str]], Tuple[str, str]],
        metadata: Dict
    ) -> VariableData:
        (initial_nums, initial_denoms), (final_nums, final_denoms) = var_pair
        description = metadata["description"]
        calculation = metadata["calculation"]

        # Calculate ratios for both periods
        initial_value = self._calculate_indicator_ratios(df, initial_nums, initial_denoms)
        final_value = self._calculate_indicator_ratios(df, final_nums, final_denoms)

        # Format values as percentages
        initial_value = int(initial_value * 100)
        final_value = int(final_value * 100)
        pct_change = calculate_percentage_change(initial_value, final_value)

        interpretation = (
            f"{description}. {calculation} El promedio del índice de eficiencia pasó del {initial_value}% "
            f"al {final_value}%."
        )

        return VariableData(
            variable=(
                final_nums.replace("c", "")
                if isinstance(final_nums, str)
                else final_nums[0].replace("c", "")
            ),
            description=description,
            value_initial_intervention=initial_value,
            value_final_intervention=final_value,
            percentage_change=pct_change,
            interpretation=interpretation,
        )

    def _calculate_indicator_ratios(self, df, numerators, denominators):
        """Helper function to calculate indicator ratios for a period."""
        ratios = []
        if isinstance(numerators, list) and isinstance(denominators, list):
            for num_col, denom_col in zip(numerators, denominators):
                assert (
                    num_col in df.columns and denom_col in df.columns
                ), f"Columns {num_col} and {denom_col} must exist in DataFrame"
                df[f"{num_col}_ratio"] = df[num_col] / df[denom_col]
                df[f"{num_col}_ratio"] = df[f"{num_col}_ratio"].where(df[denom_col] != 0)
                ratios.append(f"{num_col}_ratio")
            return np.nanmean(df[ratios].values.flatten())
        elif isinstance(numerators, str) and isinstance(denominators, str):
            assert (
                numerators in df.columns and denominators in df.columns
            ), f"Columns {numerators} and {denominators} must exist in DataFrame"
            df[f"{numerators}_ratio"] = df[numerators] / df[denominators]
            df[f"{numerators}_ratio"] = df[f"{numerators}_ratio"].where(
                df[denominators] != 0
            )
            return df[f"{numerators}_ratio"].mean()
        else:
            raise KeyError(
                "Numerators and denominators must be either both lists or both strings"
            ) 