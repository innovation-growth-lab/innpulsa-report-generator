"""Utilities for generating JSON output."""
import json
from typing import List
from src.models.sections import ReportSection  # Import VariableData from models


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
