"""Error handling utilities."""

from typing import Optional, Any
import streamlit as st
from src.utils.constants import MESSAGES


class ReportGenerationError(Exception):
    """Custom exception for report generation errors."""
    pass


def handle_error(error: Exception, error_type: str) -> str:
    """
    Handle different types of errors and return appropriate error message.

    Args:
        error: The exception that was raised
        error_type: Type of error (file, data, report, unexpected)

    Returns:
        Formatted error message
    """
    error_msg = str(error)
    return (
        MESSAGES["errors"]
        .get(error_type, MESSAGES["errors"]["unexpected_error"])
        .format(error_msg)
    )


def show_error(error_msg: str, error_type: str = "error") -> None:
    """
    Display error message in Streamlit.

    Args:
        error_msg: Error message to display
        error_type: Type of error display (error, warning, info)
    """
    display_func = getattr(st, error_type)
    display_func(error_msg)


def safe_operation(
    operation: callable, error_type: str, *args, **kwargs
) -> Optional[Any]:
    """
    Safely execute an operation with error handling.

    Args:
        operation: Function to execute
        error_type: Type of error if operation fails
        *args: Positional arguments for operation
        **kwargs: Keyword arguments for operation

    Returns:
        Result of operation if successful, None if failed
    """
    try:
        return operation(*args, **kwargs)
    except Exception as e:
        error_msg = handle_error(e, error_type)
        show_error(error_msg)
        return None
