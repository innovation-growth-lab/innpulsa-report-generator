from typing import Optional, Dict, Union
from pydantic import BaseModel, Field


class VariableData(BaseModel):
    """Variable data model."""

    variable: str = Field(..., description="Name of the variable.")
    description: str = Field(..., description="Description of what the variable measures.")
    value_initial_intervention: Optional[Union[str, float, Dict[str, float]]] = Field(
        None, description="Initial value - either average or category percentages."
    )
    value_final_intervention: Union[float, Dict[str, float]] = Field(
        ..., description="Final value - either average or category percentages."
    )
    percentage_change: Optional[Union[str, Dict[str, str]]] = Field(
        None, description="Percentage change - either overall or per category."
    )
    interpretation: str = Field(
        ..., description="Human-readable interpretation of the results."
    )