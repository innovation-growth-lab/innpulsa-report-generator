"""Base processor class for variable processing."""

from abc import ABC, abstractmethod
from typing import Dict, Tuple, Union, List
import pandas as pd
from src.models.variables import VariableData


class BaseProcessor(ABC):
    """Abstract base class for variable processors."""

    @abstractmethod
    def process(
        self,
        df: pd.DataFrame,
        var_pair: Tuple[Union[str, List[str], None], str],
        metadata: Dict,
    ) -> VariableData:
        """Process variable data and return VariableData object.

        Args:
            df: DataFrame containing the data
            var_pair: A tuple containing the initial and final column names.
                     For indicators, this is a tuple of tuples containing numerator and denominator columns.
                     Initial column can be None for variables that only have final values.
            metadata: Dictionary containing variable metadata including name, description,
                     and any additional configuration (e.g., mappings for categorical variables)

        Returns:
            VariableData object containing the processed variable data
        """
        pass
