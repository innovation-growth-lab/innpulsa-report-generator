"""Numeric variable processor."""

from typing import Dict, Tuple, Union, List
import pandas as pd
import numpy as np
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor

class NumericProcessor(BaseProcessor):
    def process(
        self,
        df: pd.DataFrame,
        var_pair: Tuple[Union[str, List[str], None], str],
        metadata: Dict
    ) -> VariableData:
        initial_cols, final_col = var_pair
        description = metadata["description"]

        if final_col not in df.columns:
            raise ValueError(f"Column {final_col} not found in dataframe")

        # Handle case where we only have final value
        if initial_cols is None:
            final_value = int(df[final_col].mean())
            interpretation = f"Para {description}, el valor promedio es {final_value}"

            return VariableData(
                variable=final_col,
                description=description,
                value_initial_intervention=0,
                value_final_intervention=final_value,
                percentage_change="N/A",
                interpretation=interpretation,
            )

        # For multiple period variables
        if isinstance(initial_cols, list):
            valid_cols = [col for col in initial_cols if col in df.columns]
            if not valid_cols:
                raise ValueError(f"None of the columns {initial_cols} found in dataframe")
            initial_value = int(df[valid_cols].apply(np.mean, axis=1).mean())
        else:
            if initial_cols not in df.columns:
                raise ValueError(f"Column {initial_cols} not found in dataframe")
            initial_value = int(df[initial_cols].mean())

        final_value = int(df[final_col].mean())
        pct_change = calculate_percentage_change(initial_value, final_value)

        # Create interpretation
        if isinstance(initial_cols, list):
            interpretation = (
                f"Para {description}, el promedio pasó de {initial_value} "
                f"(promedio de {len(valid_cols)} meses) a {final_value}, "
                f"representando un cambio del {pct_change}."
            )
        else:
            interpretation = (
                f"Para {description}, el promedio pasó de {initial_value} a {final_value}, "
                f"representando un cambio del {pct_change}."
            )

        return VariableData(
            variable=final_col.replace("c", ""),
            description=description,
            value_initial_intervention=initial_value,
            value_final_intervention=final_value,
            percentage_change=pct_change,
            interpretation=interpretation,
        ) 