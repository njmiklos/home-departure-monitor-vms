import pandas as pd
from typing import List

from env_manager import get_latitutde, get_longtitude, get_radius, get_path
from file_handler import read_csv_to_dataframe


class Connection:
    """
    Represents a single transport connection at a specific stop.
    """
    def __init__(self, stop_id: str, stop_name: str, latitude: float, longtitude: float):
        """
        Initialize a Connection instance.

        :param stop_id: Unique identifier of the stop from the VMS's GTFS-compatible data.
        :type stop_id: str
        :param stop_name: Human-readable name of the stop from the VMS's GTFS-compatible data.
        :type stop_name: str
        :param latitude: Latitude of the selected position.
        :type latitude: float
        :param longtitude: Longitude of the selected position.
        :type longtitude: float

        :param route_short_name: #TODO
        :type route_short_name: str
        :param route_long_name: #TODO
        :type route_long_name: str

        :param departures: Departure information for the stop from the VMS's GTFS-compatible data.
        :type departures: pd.DataFrame
        """
        # given by the Area class based on stops.txt
        self.stop_id: str = stop_id
        self.stop_name: str = stop_name
        self.latitude: float = latitude
        self.longtitude: float = longtitude

        # TODO with https://gtfs.org/documentation/schedule/examples/routes-stops-trips/
        
        # routes.txt
        self.route_short_name: str = self.set_short_name()
        self.route_long_name: str = self.set_long_name()

        # stop_times.txt
        self.departures: pd.DataFrame = self.set_departures()

class Area:
    """
    Represents a geographic area defined by a selected central position (defined by latitude and longitude) 
    and radius.

    The Area object can be populated with nearby transport connections.
    """
    def __init__(self):
        """
        Initialize an Area instance and populate the area's latitude, longitude, and radius values.

        The values are retrieved from environment configuration using
        helper functions.

        :param latitude: Latitude of the selected position.
        :type latitude: float
        :param longtitude: Longitude of the selected position.
        :type longtitude: float
        :param radius: Radius of the area around the selected position.
        :type radius: float
        """
        self.latitude: float = get_latitutde()
        self.longtitude: float = get_longtitude()
        self.radius: float = get_radius()

        self.connections: List[Connection] = []
    
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

    latitude = get_latitutde()
    longtitude = get_longtitude()
    assert area.latitude == latitude
    assert area.longtitude == longtitude

    radius = get_radius()
    assert area.radius == radius