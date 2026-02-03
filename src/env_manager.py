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

def get_longtitude() -> float:
    """
    Fetches the longtitude of the current position specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.
    """
    load_dotenv() 
    longtitude = os.getenv('LONGTITUDE')
    if not longtitude:
        raise ValueError('LONGTITUDE is not set in the .env file.')
    
    return longtitude

def get_latitutde() -> float:
    """
    Fetches the latitutde of the current position specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.
    """
    load_dotenv()
    latitutde = os.getenv('LATITUDE')
    if not latitutde:
        raise ValueError('LATITUDE is not set in the .env file.')
    
    return latitutde

def get_radius() -> int:
    """
    Fetches the radius in meters from the current position specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.
    """
    load_dotenv()
    radius = os.getenv('RADIUS')
    if not radius:
        raise ValueError('RADIUS is not set in the .env file.')
    
    return radius

def get_timeframe() -> int:
    """
    Fetches the time in minutes for search of departures, specified in the .env file.

    Raises a ValueError if it is not defined in the .env file.
    """
    load_dotenv()
    timeframe = os.getenv('TIMEFRAME')
    if not timeframe:
        raise ValueError('TIMEFRAME is not set in the .env file.')
    
    return timeframe