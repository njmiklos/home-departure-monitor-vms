"""
This script provides file handling utilities for reading, writing, and managing data files such as CSV and JSON. 

Refer to `README.md` for full setup, usage instructions, and formatting requirements.
"""
import pandas as pd
from pathlib import Path


def read_csv_to_dataframe(path_file: Path) -> pd.DataFrame:
    """
    Reads a CSV file into a pandas DataFrame.

    Args:
        path_file (Path): The file path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(path_file)
    return df 