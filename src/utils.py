"""Utility functions for data loading, aggregation, and JSON output generation."""

import json
import logging
from typing import List, Dict, Tuple, Union
import pandas as pd
import numpy as np
import streamlit as st
from src.models import ReportSection, VariableData  # Import VariableData from models

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Print to console
        logging.FileHandler("processing.log"),  # Save to file
    ],
)

logger = logging.getLogger(__name__)


@st.cache_data
def load_data(uploaded_file) -> pd.DataFrame:
    """Load and return the dataset from the uploaded CSV file."""
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    # Filter for complete diagnostics only
    filtered_df = df[
        (df["Diagnostico"].str.lower() == "complete")
        & (df["Cierre"].str.lower() == "complete")
    ].copy()

    if len(filtered_df) == 0:
        raise ValueError("No complete diagnostics found in dataset")

    logger.info(
        "Processing %d complete diagnostics out of %d total entries",
        len(filtered_df),
        len(df),
    )
    return filtered_df


def calculate_percentage_change(initial: float, final: float) -> str:
    """Calculate percentage change between two values."""
    if initial == 0:
        return "0%"
    return f"{round(((final - initial) / initial) * 100, 1)}%"


def process_numeric_variable(
    df: pd.DataFrame, var_pair: Tuple[Union[str, List[str], None], str], metadata: Dict
) -> VariableData:
    """Process numeric variables from the dataset and calculate their changes.

    Handles both single measurements and time series data, calculating averages and percentage changes.
    For time series, it averages across all available periods.

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of (initial_column(s), final_column) where initial can be None, str, or list
        metadata: Dictionary containing variable description and any additional metadata

    Returns:
        VariableData object containing initial/final values, percentage change and interpretation

    Raises:
        ValueError: If required columns are not found in the DataFrame
    """
    initial_cols, final_col = var_pair
    description = metadata["description"]

    if final_col not in df.columns:
        raise ValueError(f"Column {final_col} not found in dataframe")

    # Handle case where we only have final value
    if initial_cols is None:
        final_value = int(round(df[final_col].mean(), 2))
        interpretation = f"Para {description}, el valor promedio es {final_value}"

        return VariableData(
            variable=final_col,
            description=description,
            value_initial_intervention=0,  # Changed from value_initial
            value_final_intervention=final_value,  # Changed from value_final
            percentage_change="N/A",
            interpretation=interpretation,
        )

    # For multiple period variables
    if isinstance(initial_cols, list):
        valid_cols = [col for col in initial_cols if col in df.columns]
        if not valid_cols:
            raise ValueError(f"None of the columns {initial_cols} found in dataframe")
        initial_value = int(round(df[valid_cols].apply(np.mean, axis=1).mean(), 2))
    else:
        if initial_cols not in df.columns:
            raise ValueError(f"Column {initial_cols} not found in dataframe")
        initial_value = int(round(df[initial_cols].mean(), 2))

    final_value = int(round(df[final_col].mean(), 2))
    pct_change = calculate_percentage_change(initial_value, final_value)

    # Create interpretation after we have all values
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


def process_boolean_variable(
    df: pd.DataFrame, var_pair: Tuple[Union[str, None], str], metadata: Dict
) -> VariableData:
    """Process boolean variables from the dataset and calculate percentage of positive responses.

    Converts 'Sí'/'No' responses to percentages and calculates the change between periods.
    Can handle cases with only final measurements (initial_col = None).

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of (initial_column, final_column) where initial can be None
        metadata: Dictionary containing variable description and any additional metadata

    Returns:
        VariableData object containing percentage of positive responses and their change

    Raises:
        ValueError: If required columns are not found in the DataFrame
    """
    initial_col, final_col = var_pair
    description = metadata["description"]

    if final_col not in df.columns:
        raise ValueError(f"Column {final_col} not found in dataframe")

    if initial_col is None:
        final_value = round(df[final_col].map({"Sí": 1, "No": 0}).mean() * 100, 2)
        interpretation = f"Para {description}, {final_value}% de las empresas respondieron afirmativamente"

        return VariableData(
            variable=final_col,
            description=description,
            value_initial_intervention=0,
            value_final_intervention=final_value,
            percentage_change="N/A",
            interpretation=interpretation,
        )

    if initial_col not in df.columns:
        raise ValueError(f"Column {initial_col} not found in dataframe")

    initial_value = round(df[initial_col].map({"Sí": 1, "No": 0}).mean() * 100, 2)
    final_value = round(df[final_col].map({"Sí": 1, "No": 0}).mean() * 100, 2)
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


def process_dummy_variable(
    df: pd.DataFrame, var_pair: Tuple[str, str], metadata: Dict
) -> VariableData:
    """Process dummy variables where any non-empty value indicates a positive response.

    Treats any non-NaN and non-'.' value as a positive response ('Sí'). Empty values, NaN, and '.'
    are treated as negative responses ('No'). Calculates percentages of positive responses.

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of (initial_column, final_column)
        metadata: Dictionary containing variable description and any additional metadata

    Returns:
        VariableData object containing percentage of positive responses and their change

    Raises:
        ValueError: If required columns are not found in the DataFrame
    """
    initial_col, final_col = var_pair
    description = metadata["description"]

    if initial_col not in df.columns:
        raise ValueError(f"Column {initial_col} not found in dataframe")
    if final_col not in df.columns:
        raise ValueError(f"Column {final_col} not found in dataframe")

    # Convert to boolean: True for any value except NaN and "."
    def calculate_dummy_percentage(series):
        return round(
            series.replace({"": np.nan, ".": np.nan})
            .infer_objects(copy=False)
            .notna()
            .mean()
            * 100,
            2,
        )

    initial_value = calculate_dummy_percentage(df[initial_col])
    final_value = calculate_dummy_percentage(df[final_col])
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


def process_categorical_variable(
    df: pd.DataFrame, var_pair: Tuple[str, str], metadata: Dict
) -> VariableData:
    """Process categorical variables and calculate distribution changes across categories.

    Calculates the percentage distribution across predefined categories and their changes between
    periods. Requires a mapping of valid categories in metadata.

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of (initial_column, final_column)
        metadata: Dictionary containing categories mapping and description

    Returns:
        VariableData object containing category distributions and their changes

    Raises:
        ValueError: If required columns are not found or metadata lacks category mapping
    """
    initial_col, final_col = var_pair
    description = metadata["description"]

    if initial_col not in df.columns:
        raise ValueError(f"Column {initial_col} not found in dataframe")
    if final_col not in df.columns:
        raise ValueError(f"Column {final_col} not found in dataframe")

    categories = metadata.get("mapping")
    if not categories:
        raise ValueError(f"No mapping provided for categorical variable {final_col}")

    # Calculate percentage for each category
    initial_counts = (
        df[initial_col].value_counts(normalize=True) * 100
        if initial_col in df.columns
        else pd.Series()
    )
    final_counts = (
        df[final_col].value_counts(normalize=True) * 100
        if final_col in df.columns
        else pd.Series()
    )

    # Create dictionaries with percentages for each category
    initial_values = {cat: round(initial_counts.get(cat, 0), 2) for cat in categories}
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


def process_array_variable(
    df: pd.DataFrame, var_pair: Tuple[str, str], metadata: Dict
) -> VariableData:
    """Process semicolon-separated multiple-choice variables.

    Handles variables where responses can include multiple options separated by semicolons.
    Calculates the percentage of respondents selecting each option and their changes.

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of (initial_column, final_column)
        metadata: Dictionary containing variable description and any additional metadata

    Returns:
        VariableData object containing option selection percentages and their changes

    Raises:
        ValueError: If required columns are not found in the DataFrame
    """
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


def process_efficiency_indicator_variable(
    df: pd.DataFrame,
    var_pair: Tuple[
        Tuple[Union[List[str], str], Union[List[str], str]],
        Tuple[Union[List[str], str], Union[List[str], str]],
    ],
    metadata: Dict,
) -> VariableData:
    """Process indicator variables that compare actual vs target values.

    Calculates efficiency ratios and averages for both initial and final periods.

    Args:
        df: DataFrame containing the measurements
        var_pair: Tuple of ((initial_numerators, initial_denominators), (final_numerator, final_denominators))
        metadata: Dictionary containing variable description

    Returns:
        VariableData object containing calculated indicators and interpretation
    """
    (initial_nums, initial_denoms), (final_nums, final_denoms) = var_pair
    description = metadata["description"]
    calculation = metadata["calculation"]

    # Calculate ratios for both periods
    initial_value = _calculate_efficiency_ratios(df, initial_nums, initial_denoms)
    final_value = _calculate_efficiency_ratios(df, final_nums, final_denoms)

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


def _calculate_efficiency_ratios(df, numerators, denominators):
    """Helper function to calculate efficiency ratios for a period."""
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



def aggregate_data(
    df: pd.DataFrame, sections_config: dict
) -> Tuple[List[ReportSection], List[str]]:
    """Aggregate data into report sections based on configuration.

    Processes all variables defined in sections_config according to their types and organizes them
    into report sections. Skips variables with missing columns instead of defaulting to zero.

    Args:
        df: DataFrame containing all measurements
        sections_config: Dictionary defining sections and their variables with processing
            instructions

    Returns:
        Tuple containing:
        - List of ReportSection objects containing processed variables and their interpretations
        - List of missing variable names for reporting
    """
    report_sections = []
    missing_variables = []

    for section_title, variables in sections_config.items():
        variable_data = {}
        for var_config in variables:
            var_pair, var_type, metadata = var_config

            try:
                # Special handling for efficiency indicator type
                if var_type == "efficiency_indicator":
                    # Unpack the indicator structure
                    (initial_nums, initial_denoms), (final_num, final_denom) = var_pair

                    # Check initial period columns
                    if isinstance(initial_nums, list):
                        missing_nums = [
                            col for col in initial_nums if col not in df.columns
                        ]
                        missing_denoms = [
                            col for col in initial_denoms if col not in df.columns
                        ]
                        if missing_nums or missing_denoms:
                            missing_variables.append(
                                f"{section_title}: Missing initial columns - numerators: {missing_nums}, denominators: {missing_denoms}"
                            )
                            continue

                    # Check final period columns
                    if final_num not in df.columns or final_denom not in df.columns:
                        missing_variables.append(
                            f"{section_title}: Missing final columns - numerator: {final_num}, denominator: {final_denom}"
                        )
                        continue

                    variable_data_obj = process_efficiency_indicator_variable(
                        df, var_pair, metadata
                    )
                else:
                    # Original column existence check for other variable types
                    initial_col, final_col = var_pair
                    if isinstance(initial_col, list):
                        if not any(col in df.columns for col in initial_col):
                            missing_variables.append(f"{section_title}: {initial_col}")
                            continue
                    elif initial_col and initial_col not in df.columns:
                        missing_variables.append(f"{section_title}: {initial_col}")
                        continue

                    if final_col not in df.columns:
                        missing_variables.append(f"{section_title}: {final_col}")
                        continue

                    # Process other variable types as before
                    if var_type == "numeric":
                        variable_data_obj = process_numeric_variable(
                            df, var_pair, metadata
                        )
                    elif var_type == "boolean":
                        variable_data_obj = process_boolean_variable(
                            df, var_pair, metadata
                        )
                    elif var_type == "dummy":
                        variable_data_obj = process_dummy_variable(
                            df, var_pair, metadata
                        )
                    elif var_type == "categorical":
                        variable_data_obj = process_categorical_variable(
                            df, var_pair, metadata
                        )
                    elif var_type == "array":
                        variable_data_obj = process_array_variable(
                            df, var_pair, metadata
                        )
                    else:
                        raise ValueError(f"Unknown variable type: {var_type}")

                # Use base name as key
                if var_type == "efficiency_indicator":
                    dict_key = final_num.replace("c", "")
                else:
                    cierre_var = var_pair[1]
                    dict_key = (
                        cierre_var[0].rsplit("1", 1)[0]
                        if isinstance(cierre_var, list)
                        else cierre_var
                    )

                variable_data[dict_key] = variable_data_obj

                logger.info(
                    "Variable %s processed successfully: initial=%s, final=%s, change=%s",
                    dict_key,
                    variable_data_obj.value_initial_intervention,
                    variable_data_obj.value_final_intervention,
                    variable_data_obj.percentage_change,
                )

            except Exception as e:  # pylint: disable=broad-exception-caught
                logger.error("Error processing variable %s: %s", var_pair, str(e))
                missing_variables.append(
                    f"{section_title}: {var_pair} (Error: {str(e)})"
                )
                continue

        report_sections.append(
            ReportSection(
                title=section_title,
                content="",
                variables=variable_data,
            )
        )

    return report_sections, missing_variables


def generate_json_output(
    report_sections: List[ReportSection],
    executive_summary: str,
    output_filename="report.json",
) -> str:
    """Generate JSON output from the report sections."""
    report_data = {"executive_summary": executive_summary, "sections": {}}

    for section in report_sections:
        report_data["sections"][section.title] = {
            "content": section.content,
            "variables": {
                var: {
                    "description": data.description,
                    "value_initial_intervention": data.value_initial_intervention,
                    "value_final_intervention": data.value_final_intervention,
                    "percentage_change": data.percentage_change,
                    "interpretation": data.interpretation,
                }
                for var, data in section.variables.items()
            },
        }

    json_output = json.dumps(report_data, indent=4, ensure_ascii=False)

    with open(output_filename, "w", encoding="utf-8") as json_file:
        json_file.write(json_output)

    return json_output
