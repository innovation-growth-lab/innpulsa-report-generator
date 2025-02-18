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
        """Process variable data and return VariableData object."""
