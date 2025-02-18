"""Pydantic models for the ZASCA report generation API."""

from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from .variables import VariableData


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
        description="Variables and their data in this section.",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the section was created.",
    )
    cohort_details: Optional[str] = Field(
        None, description="Details about the ZASCA cohort."
    )

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "title": "Introduction",
                "content": "This section introduces the topic.",
                "variables": ["variable1", "variable2"],
                "created_at": "2025-01-17T16:13:20+01:00",
                "cohort_details": "ZASCA Bucaramanga 2024-Q1",
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
