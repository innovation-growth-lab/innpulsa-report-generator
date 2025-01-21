"""
Toma.
"""

from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class VariableData(BaseModel):
    """Variable data model."""
    variable: str = Field(..., description="Name of the variable.")
    description: str = Field(..., description="Description of the variable.")
    value_initial_intervention: float = Field(
        ..., description="Average value before the intervention."
    )
    value_final_intervention: float = Field(
        ..., description="Average value after the intervention."
    )
    percentage_change: str = Field(
        ..., description="Percentage change from before to after the intervention."
    )


class ReportSection(BaseModel):
    """
    Report section model.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Title of the report section, must be between 1 and 100 characters.",
    )
    content: str = Field(..., description="Content generated for the report section.")
    variables: Dict[str, VariableData] = Field(
        ...,
        description="Mapping of variable names to their before and after average values.",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the section was created.",
    )

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "title": "Introduction",
                "content": "This section introduces the topic.",
                "variables": ["variable1", "variable2"],
                "created_at": "2025-01-17T16:13:20+01:00",
            }
        }


class Report(BaseModel):
    """
    Report model.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Title of the report, must be between 1 and 100 characters.",
    )
    sections: List[ReportSection] = Field(
        ..., description="List of sections included in the report."
    )
    generated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the report was generated.",
    )

    class Config:
        """Pydantic model configuration"""

        json_schema_extra = {
            "example": {
                "title": "Informe de Cierre",
                "sections": [
                    {
                        "title": "Introduction",
                        "content": "This section introduces the topic.",
                        "variables": ["variable1", "variable2"],
                        "created_at": "2025-01-17T16:13:20+01:00",
                    }
                ],
                "generated_at": "2025-01-17T16:13:20+01:00",
            }
        }


class User(BaseModel):
    """
    Class representing a user.
    """

    id: int = Field(..., description="Unique identifier for the user.")
    email: str = Field(
        ...,
        description="Email address of the user.",
        pattern=r"^\S+@\S+\.\S+$",
    )

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {"example": {"id": 1, "email": "david.ampudia@nesta.co.uk"}}


class APIResponse(BaseModel):
    """
    API response model.
    """

    status: str = Field(
        ..., description="Status of the API response, e.g., 'success' or 'error'."
    )
    message: Optional[str] = Field(
        None,
        description="Optional message providing additional information about the response.",
    )
    data: Optional[dict] = Field(
        None, description="Optional data returned from the API."
    )

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Report generated successfully.",
                "data": {"report_id": 123, "generated_at": "2025-01-17T16:13:20+01:00"},
            }
        }


# Additional utility functions for validation or processing can be added here
def validate_report(report: Report):
    """Validates the report object."""
    if not report.sections:
        raise ValueError("Report must contain at least one section.")
    return True
