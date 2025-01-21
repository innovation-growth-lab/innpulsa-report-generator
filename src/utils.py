"""Utility functions for data loading, aggregation, and JSON output generation."""

import json
from typing import List
import pandas as pd
from src.models import ReportSection, VariableData


def load_data(uploaded_file) -> pd.DataFrame:
    """Load and return the dataset from the uploaded CSV file."""
    return pd.read_excel(uploaded_file, engine="openpyxl")


def aggregate_data(df: pd.DataFrame, sections_config: dict) -> List[ReportSection]:
    """Aggregate data into report sections based on the predefined configuration."""
    report_sections = []

    for section_title, variables in sections_config.items():
        variable_data = {}
        for variable in variables:

            variable_data[variable] = VariableData(
                variable=variable,
                description=f"This variable captures the {variable} data.",
                value_initial_intervention=round(
                    df.get(f"{variable}_initial", pd.Series([])).mean(), 2
                ),
                value_final_intervention=round(
                    df.get(f"{variable}_final", pd.Series([])).mean(), 2
                ),
                percentage_change=(
                    str(
                        round(
                            (
                                (
                                    (
                                        df.get(
                                            f"{variable}_final", pd.Series([])
                                        ).mean()
                                        - df.get(
                                            f"{variable}_initial", pd.Series([])
                                        ).mean()
                                    )
                                    / df.get(
                                        f"{variable}_initial", pd.Series([])
                                    ).mean()
                                )
                                * 100
                                if df.get(f"{variable}_initial", pd.Series([])).mean()
                                != 0
                                else 0
                            ),
                            1,
                        ),
                    )
                    + "%"
                ),
            )

        report_sections.append(
            ReportSection(
                title=section_title,
                content="Placeholder content",
                variables=variable_data,
            )
        )

    return report_sections


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
                }
                for var, data in section.variables.items()
            },
        }

    json_output = json.dumps(report_data, indent=4)

    with open(output_filename, "w", encoding="utf-8") as json_file:
        json_file.write(json_output)

    return json_output
