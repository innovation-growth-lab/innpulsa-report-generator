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
        var_pair: Tuple[
            Tuple[Union[List[str], str], Union[List[str], str]], Tuple[str, str]
        ],
        metadata: Dict,
    ) -> VariableData:
        (initial_nums, initial_denoms), (final_nums, final_denoms) = var_pair
        description = metadata["description"]
        calculation = metadata["calculation"]

        # Calculate ratios for both periods
        initial_value = self._calculate_indicator_ratios(
            df, initial_nums, initial_denoms
        )
        final_value = self._calculate_indicator_ratios(df, final_nums, final_denoms)

        # Format values as percentages
        initial_value = int(initial_value * 100)
        final_value = int(final_value * 100)
        pct_change = calculate_percentage_change(initial_value, final_value)

        interpretation = (
            f"{description}. {calculation} El promedio del índice pasó del {initial_value}% "
            f"al {final_value}%."
        )

        return VariableData(
            variable=(
                final_nums.rsplit("_", 1)[0]
                if isinstance(final_nums, str)
                else final_nums[0].rsplit("_", 1)[0]
            ),
            description=description,
            value_initial_intervention=initial_value,
            value_final_intervention=final_value,
            percentage_change=pct_change,
            interpretation=interpretation,
        )

    def _calculate_indicator_ratios(self, df, numerators, denominators):
        """Helper function to calculate indicator ratios for a period."""
        df_copy = df.copy()
        ratios = []
        if isinstance(numerators, list) and isinstance(denominators, list):
            for num_col, denom_col in zip(numerators, denominators):
                assert (
                    num_col in df_copy.columns and denom_col in df_copy.columns
                ), f"Columns {num_col} and {denom_col} must exist in DataFrame"
                df_copy[f"{num_col}_ratio"] = df_copy[num_col] / df_copy[denom_col]
                df_copy[f"{num_col}_ratio"] = df_copy[f"{num_col}_ratio"].where(
                    df_copy[denom_col] != 0
                )
                ratios.append(f"{num_col}_ratio")
            return np.nanmean(df_copy[ratios].mean(axis=1))
        elif isinstance(numerators, str) and isinstance(denominators, str):
            assert (
                numerators in df_copy.columns and denominators in df_copy.columns
            ), f"Columns {numerators} and {denominators} must exist in DataFrame"
            df_copy[f"{numerators}_ratio"] = df_copy[numerators] / df_copy[denominators]
            df_copy[f"{numerators}_ratio"] = df_copy[f"{numerators}_ratio"].where(
                df_copy[denominators] != 0
            )
            return df_copy[f"{numerators}_ratio"].mean()
        else:
            raise KeyError(
                "Numerators and denominators must be either both lists or both strings"
            )
