"""Data processing module."""

import logging
from typing import List, Tuple
import pandas as pd
from src.models.sections import ReportSection
from src.data.processors import (
    ArrayProcessor,
    BooleanProcessor,
    CategoricalProcessor,
    DummyProcessor,
    IndicatorProcessor,
    NumericProcessor,
)

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

# Initialize processors
PROCESSORS = {
    "numeric": NumericProcessor(),
    "boolean": BooleanProcessor(),
    "categorical": CategoricalProcessor(),
    "array": ArrayProcessor(),
    "dummy": DummyProcessor(),
    "indicator": IndicatorProcessor(),
}


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
                if var_type == "indicator":
                    # Unpack the indicator structure
                    (initial_nums, initial_denoms), (final_nums, final_denoms) = (
                        var_pair
                    )
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
                    if isinstance(final_nums, list):
                        missing_nums = [
                            col for col in final_nums if col not in df.columns
                        ]
                        missing_denoms = [
                            col for col in final_denoms if col not in df.columns
                        ]
                        if missing_nums or missing_denoms:
                            missing_variables.append(
                                f"{section_title}: Missing final columns - numerators: {missing_nums}, denominators: {missing_denoms}"
                            )
                            continue
                    else:
                        # Check final period columns
                        if (
                            final_nums not in df.columns
                            or final_denoms not in df.columns
                        ):
                            missing_variables.append(
                                f"{section_title}: Missing final columns - numerator: {final_nums}, denominator: {final_denoms}"
                            )
                            continue

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

                # Process variable using appropriate processor
                processor = PROCESSORS.get(var_type)
                if not processor:
                    raise ValueError(f"Unknown variable type: {var_type}")

                variable_data_obj = processor.process(df, var_pair, metadata)

                variable_data[metadata["description"]] = variable_data_obj

                logger.info(
                    "Variable %s processed successfully: initial=%s, final=%s, change=%s",
                    metadata["description"],
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
