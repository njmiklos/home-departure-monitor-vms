import os
from dotenv import load_dotenv
from typing import Tuple
from pathlib import Path


def get_path(var_name: str) -> Path:
    """
    Fetches the directory path of the specified variable from the .env file.

    Raises a ValueError if it is not defined in the .env file.

    Returns:
        Path: The path of the specified variable.
    """
    load_dotenv()
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f'{var_name} is not set in the .env file.')
    return Path(value)

def get_position() -> Tuple[float, float]:
    """
    Fetches the longtitude and latitutde of the current position specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.

    Returns:
        float, float: 
    """
    load_dotenv()
    latitutde = os.getenv('LAT')
    if not latitutde:
        raise ValueError('LAT is not set in the .env file.')
    
    longtitude = os.getenv('LON')
    if not longtitude:
        raise ValueError('LON is not set in the .env file.')
    
    return (latitutde, longtitude)

def get_radius() -> float:
    """
    Fetches the radius in meters from the current position specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.

    Returns:
        float: 
    """
    load_dotenv()
    radius = os.getenv('RAD')
    if not radius:
        raise ValueError('RAD is not set in the .env file.')
    
    return radius