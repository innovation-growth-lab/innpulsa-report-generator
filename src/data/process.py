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
    into report sections. For each variable, tries each possible column name combination until one works.
    Skips variables with missing columns instead of defaulting to zero.

    Args:
        df: DataFrame containing all measurements
        sections_config: Dictionary defining sections and their variables. Each section contains
            a dictionary of variables, where each variable has:
            - var_pairs: List of possible column name combinations
            - type: Variable type (NUMERIC, BOOLEAN, etc.)
            - metadata: Variable metadata (name, description, etc.)

    Returns: List of ReportSection objects containing processed variables and their
        interpretations
    """
    report_sections = []

    for section_title, variables in sections_config.items():
        variable_data = {}
        for var_name, var_config in variables.items():
            try:
                # Process variable using appropriate processor
                processor = PROCESSORS.get(var_config["type"])
                if not processor:
                    raise ValueError(f"Unknown variable type: {var_config['type']}")

                # Try each variable pair until one works
                for var_pair in var_config["var_pairs"]:
                    try:
                        variable_data_obj = processor.process(
                            df, var_pair, var_config["metadata"]
                        )
                        variable_data[var_name] = variable_data_obj

                        logger.info(
                            "Variable %s processed successfully: initial=%s, final=%s, change=%s",
                            var_name,
                            variable_data_obj.value_initial_intervention,
                            variable_data_obj.value_final_intervention,
                            variable_data_obj.percentage_change,
                        )
                        break  # Stop trying pairs if one works
                    except Exception as e:  # pylint: disable=broad-exception-caught
                        logger.debug("Variable pair %s failed: %s", var_pair, str(e))
                        continue

            except Exception as e:  # pylint: disable=broad-exception-caught
                logger.error("Error processing variable %s: %s", var_name, str(e))
                continue

        report_sections.append(
            ReportSection(
                title=section_title,
                content="",
                variables=variable_data,
            )
        )

    return report_sections
