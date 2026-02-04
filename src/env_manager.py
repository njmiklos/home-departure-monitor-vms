import os
from dotenv import load_dotenv
from pathlib import Path


def get_path(var_name: str) -> Path:
    """
    Retrieve a directory path from the .env file and return it as a Path object.

    :param var_name: Name of the environment variable containing a filesystem path.
    :type var_name: str

    :raises ValueError: If the environment variable is not defined in the .env file.

    :return: Path corresponding to the value of the specified environment variable.
    :rtype: Path
    """
    load_dotenv()
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f'{var_name} is not set in the .env file.')
    return Path(value)

def get_longitude() -> float:
    """
    Retrieve the longitude of the current position from the .env file and return it 
    as a float rounded to 8 decimal places.

    :raises ValueError: If the LONGITUDE variable is not defined in the .env file.

    :return: Longitude of the current position.
    :rtype: float
    """
    load_dotenv() 
    longitude = os.getenv('LONGITUDE')
    if not longitude:
        raise ValueError('LONGITUDE is not set in the .env file.')
    
    return round(float(longitude), 8)

def get_latitutde() -> float:
    """
    Retrieve the latitude of the current position from the .env file and return it
    as a float rounded to 8 decimal places.

    :raises ValueError: If the LATITUDE variable is not defined in the .env file.

    :return: Latitude of the current position.
    :rtype: float
    """
    load_dotenv()
    latitutde = os.getenv('LATITUDE')
    if not latitutde:
        raise ValueError('LATITUDE is not set in the .env file.')
    
    return round(float(latitutde), 8)

def get_radius() -> int:
    """
    Retrieve the search radius in meters from the .env file and return it as an integer.

    :raises ValueError: If the RADIUS variable is not defined in the .env file.

    :return: Search radius in meters.
    :rtype: int
    """
    load_dotenv()
    radius = os.getenv('RADIUS')
    if not radius:
        raise ValueError('RADIUS is not set in the .env file.')
    
    return int(radius)

def get_timeframe() -> int:
    """
    Retrieve the time frame for departure searches from the .env file and return it as a float.

    :raises ValueError: If the TIMEFRAME variable is not defined in the .env file.

    :return: Time frame in minutes.
    :rtype: int
    """
    load_dotenv()
    timeframe = os.getenv('TIMEFRAME')
    if not timeframe:
        raise ValueError('TIMEFRAME is not set in the .env file.')
    
    return int(timeframe)