"""Array variable processor."""

from typing import Dict, Tuple
import pandas as pd
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor

class ArrayProcessor(BaseProcessor):
    def process(
        self,
        df: pd.DataFrame,
        var_pair: Tuple[str, str],
        metadata: Dict
    ) -> VariableData:
        initial_col, final_col = var_pair
        description = metadata["description"]

        def get_all_options(series):
            options = set()
            for x in series.dropna():
                options.update(str(x).split(";"))
            return sorted(list(options))

        # Get all possible options from both columns
        all_options = get_all_options(
            pd.concat([df[initial_col], df[final_col]])
            if final_col in df.columns
            else df[initial_col]
        )

        def calculate_percentages(series):
            total = len(series)
            counts = {opt: 0 for opt in all_options}
            for x in series.dropna():
                selected = str(x).split(";")
                for opt in selected:
                    counts[opt] += 1
            return {opt: round((count / total) * 100, 2) for opt, count in counts.items()}

        initial_values = (
            calculate_percentages(df[initial_col])
            if initial_col in df.columns
            else {opt: 0 for opt in all_options}
        )
        final_values = (
            calculate_percentages(df[final_col])
            if final_col in df.columns
            else {opt: 0 for opt in all_options}
        )

        pct_changes = {
            opt: calculate_percentage_change(initial_values[opt], final_values[opt])
            for opt in all_options
        }

        # Create interpretation
        interpretation_parts = []
        for opt in all_options:
            if initial_values[opt] > 0 or final_values[opt] > 0:
                interpretation_parts.append(
                    f"'{opt}': {initial_values[opt]}% → {final_values[opt]}% ({pct_changes[opt]})"
                )

        interpretation = f"{description}:\n" + "\n".join(interpretation_parts)

        return VariableData(
            variable=final_col.replace("c", ""),
            description=description,
            value_initial_intervention=initial_values,
            value_final_intervention=final_values,
            percentage_change=pct_changes,
            interpretation=interpretation,
        ) 