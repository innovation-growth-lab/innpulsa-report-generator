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


def aggregate_data(df: pd.DataFrame, sections_config: dict) -> List[ReportSection]:
    """Aggregate data into report sections based on configuration.

    Processes all variables defined in sections_config according to their types and organizes them
    into report sections. Skips variables with missing columns instead of defaulting to zero.

    Args:
        df: DataFrame containing all measurements
        sections_config: Dictionary defining sections and their variables with processing
            instructions

    Returns: List of ReportSection objects containing processed variables and their 
        interpretations
    """
    report_sections = []

    for section_title, variables in sections_config.items():
        variable_data = {}
        for var_config in variables:
            var_pair, var_type, metadata = var_config

            try:
                # Process variable using appropriate processor
                processor = PROCESSORS.get(var_type)
                if not processor:
                    raise ValueError(f"Unknown variable type: {var_type}")

                variable_data_obj = processor.process(df, var_pair, metadata)

                variable_data[metadata["name"]] = variable_data_obj

                logger.info(
                    "Variable %s processed successfully: initial=%s, final=%s, change=%s",
                    metadata["name"],
                    variable_data_obj.value_initial_intervention,
                    variable_data_obj.value_final_intervention,
                    variable_data_obj.percentage_change,
                )

            except Exception as e:  # pylint: disable=broad-exception-caught
                logger.error("Error processing variable %s: %s", var_pair, str(e))
                continue

        report_sections.append(
            ReportSection(
                title=section_title,
                content="",
                variables=variable_data,
            )
        )

    return report_sections
