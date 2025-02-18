"""Data loading utilities for processing diagnostic data.

This module provides functions for loading and preprocessing diagnostic data from uploaded files.
It includes caching functionality through Streamlit to improve performance on repeated loads.
"""
import logging
import pandas as pd
import streamlit as st

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


@st.cache_data
def load_data(uploaded_file) -> pd.DataFrame:
    """Load and return the dataset from the uploaded CSV file."""
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    # Filter for complete diagnostics only
    filtered_df = df[
        (df["Diagnostico"].str.lower() == "complete")
        & (df["Cierre"].str.lower() == "complete")
    ].copy()

    if len(filtered_df) == 0:
        raise ValueError("No complete diagnostics found in dataset")

    logger.info(
        "Processing %d complete diagnostics out of %d total entries",
        len(filtered_df),
        len(df),
    )
    return filtered_df
