import pandas as pd
from typing import List

from env_manager import get_position, get_radius, get_path
from file_handler import read_csv_to_dataframe


class Connection:
    """
    Represents a single transport connection at a specific stop.
    """
    def __init__(self, stop_id: str, stop_name: str, departures: pd.DataFrame):
        """
        Initialize a Connection instance.

        :param stop_id: Unique identifier of the stop from the VMS's GTFS-compatible data.
        :type stop_id: str
        :param stop_name: Human-readable name of the stop from the VMS's GTFS-compatible data.
        :type stop_name: str
        :param departures: Departure information for the stop from the VMS's GTFS-compatible data.
        :type departures: pd.DataFrame
        """
        self.stop_id: str = stop_id
        self.location: str = stop_name
        self.departures: pd.DataFrame = departures

class Area:
    """
    Represents a geographic area defined by a selected central position (defined by latitude and longitude) 
    and radius.

    The Area object can be populated with nearby transport connections.
    """
    def __init__(self, latitude: float = 0.0, longtitude: float = 0.0, radius: float = 0.0):
        """
        Initialize an Area instance.

        :param latitude: Latitude of the selected position.
        :type latitude: float
        :param longtitude: Longitude of the selected position.
        :type longtitude: float
        :param radius: Radius of the area around the selected position.
        :type radius: float
        """
        self.latitude: float = latitude
        self.longtitude: float = longtitude
        self.radius: float = radius

        self.connections: List[Connection] = []
    
    def set_area(self) -> None:
        """
        Populate the area's latitude, longitude, and radius values.

        The values are retrieved from environment configuration using
        helper functions.
        """
        self.latitude, self.longtitude = get_position()
        self.radius = get_radius()
    
    def set_connections(self) -> None:
        """
        Populate the list of nearby connections for this area.
        """
        self.connections = self.get_nearby_connections()

    def get_nearby_connections(self) -> List[Connection]:
        """
        Retrieve transport connections located within the area.

        Reads stop data from the VMS's GTFS-compatible data and processes
        it to determine which connections fall within the defined area.

        :return: A list of nearby Connection objects.
        :rtype: List[Connection]
        """
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'stops.txt'
        df = read_csv_to_dataframe(input_file)

        # TODO
        pass


if __name__ == '__main__':
    area = Area()
    area.set_area()

    latitude, longtitude = get_position()
    assert area.latitude == latitude
    assert area.longtitude == longtitude

    radius = get_radius()
    assert area.radius == radius