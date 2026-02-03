import pandas as pd
from typing import List

from env_manager import get_latitutde, get_longtitude, get_radius, get_path, get_timeframe
from file_handler import read_csv_to_dataframe


class Connection:
    """
    Represents a single transport connection at a Stop instance.
    """
    def __init__(self, departure_time):
        """
        Initialize a Connection instance and populate its departure time, names and type of vehicle.
        The values are retrieved from routes.txt from the VMS's GTFS-compatible data, but since 
        there is no direct connection between stop_times.txt and routes.txt,
        the file trips.txt is leveraged as a connection between them.

        :param departure_time: Time of departure of the Connection instance, given by the Stop instance.
        :type departure_time: str

        :param route_short_name: Short, abstract name of a route, e.g., "32", "100X", "Green".
        :type route_short_name: str
        :param route_long_name: Full name of a route.
        :type route_long_name: str
        :param vehicle: Type of vehicle (e.g., bus, tram) mapped based on `route_type` code.
        :type vehicle: str
        """
        self.departure_time: str = departure_time

        self.connection_id: str = self.set_connection_id()
        self.route_short_name: str = self.set_short_name()
        self.route_long_name: str = self.set_long_name()
        self.vehicle: str = self.set_vehicle()

    def set_connection_id(self) -> None:
        pass

    def set_short_name(self) -> None:
        pass

    def set_long_name(self) -> None:
        pass

    def map_long_name(self, route_type: str):
        """
        Return type of vehicle (e.g., bus, tram) available in the area, based on `route_type` code.
        More types: https://gtfs.org/documentation/schedule/reference/#routestxt 
        
        :param self: Description
        :param route_type: Description
        :type route_type: str
        """
        mappings = {
            '0' : 'Straßenbahn',
            '2' : 'City-Bahn',
            '3' : 'Bus',
            '7' : 'Drahtseilbahn',
        }
        return mappings[route_type] if route_type in mappings else '???'

    def set_vehicle(self, route_id: str):
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'routes.txt'
        df = read_csv_to_dataframe(input_file)
        route_type_col = df["route_type"]
        route_type = route_type_col.get(route_id, default='???')
        return route_type


class Stop:
    """
    Represents a single stop in a public transport in an Area instance.
    """
    def __init__(self, stop_id: str, stop_name: str, latitude: float, longtitude: float):
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
        :param longtitude: Longitude of the selected position.
        :type longtitude: float

        :param timeframe: Time in minutes defined by the user where transport data is retrieved from.
            The values are retrieved from *.env defined by the user.
        :type timestrame: int

        :param connections: Departures within the selected timeframe.
        :type connections: List[Connection]
        """
        self.stop_id: str = stop_id
        self.stop_name: str = stop_name
        self.latitude: float = latitude
        self.longtitude: float = longtitude

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
        :param longtitude: Longitude of the selected position.
        :type longtitude: float
        :param radius: Radius of interest defined in meters around the selected position.
        :type radius: float

        :param stops: List of stops found within the defined Area.
        :type stops: List[Stop]
        """
        self.latitude: float = get_latitutde()
        self.longtitude: float = get_longtitude()
        self.radius: float = get_radius()

        self.stops: List[Stop] = self.set_stops()

    def set_stops(self) -> None:
        """
        Populate the list of Stops in this Area instance.
        """
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'stops.txt'
        df = read_csv_to_dataframe(input_file)

        # For every self.latitude + self.longtitude within self.radius
        #   Add a stop: Stop(stop_id, stop_name, stop_latitude, stop_longtitude)

        pass


if __name__ == '__main__':
    '''
    area = Area()

    latitude = get_latitutde()
    longtitude = get_longtitude()
    assert area.latitude == latitude
    assert area.longtitude == longtitude

    radius = get_radius()
    assert area.radius == radius
    '''