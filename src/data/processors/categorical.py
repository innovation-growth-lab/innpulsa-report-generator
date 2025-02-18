"""Categorical variable processor."""

from typing import Dict, Tuple
import pandas as pd
from src.models.variables import VariableData
from src.utils.calculations import calculate_percentage_change
from .base import BaseProcessor


class CategoricalProcessor(BaseProcessor):
    def process(
        self, df: pd.DataFrame, var_pair: Tuple[str, str], metadata: Dict
    ) -> VariableData:
        initial_col, final_col = var_pair
        description = metadata["description"]

        if initial_col not in df.columns:
            raise ValueError(f"Column {initial_col} not found in dataframe")
        if final_col not in df.columns:
            raise ValueError(f"Column {final_col} not found in dataframe")

        categories = metadata.get("mapping")
        if not categories:
            raise ValueError(
                f"No mapping provided for categorical variable {final_col}"
            )

        # Calculate percentage for each category
        initial_counts = df[initial_col].value_counts(normalize=True) * 100
        final_counts = df[final_col].value_counts(normalize=True) * 100

        # Create dictionaries with percentages for each category
        initial_values = {
            cat: round(initial_counts.get(cat, 0), 2) for cat in categories
        }
        final_values = {cat: round(final_counts.get(cat, 0), 2) for cat in categories}

        # Calculate percentage changes for each category
        pct_changes = {
            cat: calculate_percentage_change(initial_values[cat], final_values[cat])
            for cat in categories
        }

        interpretation_parts = [f"Para {description}:"]
        for cat in categories:
            if initial_values[cat] > 0 or final_values[cat] > 0:
                interpretation_parts.append(
                    f"- {cat}: pasó de {initial_values[cat]}% a {final_values[cat]}% ({pct_changes[cat]})"
                )

        interpretation = "\n".join(interpretation_parts)

        return VariableData(
            variable=final_col.replace("c", ""),
            description=description,
            value_initial_intervention=initial_values,
            value_final_intervention=final_values,
            percentage_change=pct_changes,
            interpretation=interpretation,
        )
