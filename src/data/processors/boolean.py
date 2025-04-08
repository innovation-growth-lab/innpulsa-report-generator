"""Boolean variable processor."""

from typing import Dict, Tuple, Union
import pandas as pd
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor


class BooleanProcessor(BaseProcessor):
    def process(
        self, df: pd.DataFrame, var_pair: Tuple[Union[str, None], str], metadata: Dict
    ) -> VariableData:
        initial_col, final_col = var_pair
        description = metadata["description"]

        if final_col not in df.columns:
            raise ValueError(f"Column {final_col} not found in dataframe")

        if initial_col is None:
            final_value = int(
                df[final_col].map({"Sí": 1, "No": 0, "SI": 1, "NO": 0}).mean() * 100
            )
            interpretation = (
                f"Para {description}, {final_value}% de las empresas respondieron afirmativamente "
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

        if initial_col not in df.columns:
            raise ValueError(f"Column {initial_col} not found in dataframe")

        initial_value = int(
            df[initial_col].map({"Sí": 1, "No": 0, "SI": 1, "NO": 0}).mean() * 100
        )
        final_value = int(
            df[final_col].map({"Sí": 1, "No": 0, "SI": 1, "NO": 0}).mean() * 100
        )
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
