import pandas as pd
from typing import List

from env_manager import get_latitutde, get_longitude, get_radius, get_path, get_timeframe
from file_handler import read_csv_to_dataframe
from connection import Connection

class Stop:
    """
    Represents a single stop in a public transport in an Area instance.
    """
    def __init__(self, stop_id: str, stop_name: str, latitude: float, longitude: float):
        """
        Initialize a Stop instance and populate its ID, name and geographical location.
        The values are retrieved from stops.txt from the VMS's GTFS-compatible data.

        Then, get departures from stop_times.txt within the selected timeframe
        and save each as a Connection instance.

        :param stop_id: Unique identifier of the stop.
        :type stop_id: str
        :param stop_name: Human-readable name of the stop.
        :type stop_name: str
        :param latitude: Latitude of the selected position.
        :type latitude: float
        :param longitude: Longitude of the selected position.
        :type longitude: float

        :param timeframe: Time in minutes defined by the user where transport data is retrieved from.
            The values are retrieved from *.env defined by the user.
        :type timestrame: int

        :param connections: Departures within the selected timeframe.
        :type connections: List[Connection]
        """
        self.stop_id: str = stop_id
        self.stop_name: str = stop_name
        self.latitude: float = latitude
        self.longitude: float = longitude

        self.timeframe: int = get_timeframe()

        self.connections: List[Connection] = self.set_connections()

    def set_connections(self) -> None:
        pass


class Area:
    """
    Represents a geographic area defined by the user where transport data is retrieved from.
    """
    def __init__(self):
        """
        Initialize an Area instance and populate its geographical location values, as defined by the user in *.env.
        Then, find and save stops within the defined Area.

        :param latitude: Latitude of the selected position.
        :type latitude: float
        :param longitude: Longitude of the selected position.
        :type longitude: float
        :param radius: Radius of interest defined in meters around the selected position.
        :type radius: float

        :param stops: List of stops found within the defined Area.
        :type stops: List[Stop]
        """
        self.latitude: float = get_latitutde()
        self.longitude: float = get_longitude()
        self.radius: float = get_radius()

        self.stops: List[Stop] = self.set_stops()

    def set_stops(self) -> None:
        """
        Populate the list of Stops in this Area instance.
        """
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'stops.txt'
        df = read_csv_to_dataframe(input_file)

        # For every self.latitude + self.longitude within self.radius
        #   Add a stop: Stop(stop_id, stop_name, stop_latitude, longitude)

        pass


if __name__ == '__main__':
    pass