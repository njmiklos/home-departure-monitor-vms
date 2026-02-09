import pandas as pd

from env_manager import get_path
from file_handler import read_csv_to_dataframe


class Connection:
    """
    Represents a single transport connection at a Stop instance.
    """
    def __init__(self, trip_id):
        """
        Initialize a Connection instance and populate its ID, departure time,
        route names, and vehicle type.

        The values are retrieved from GTFS-compatible data files. Since there is
        no direct connection between stop_times.txt and routes.txt, trips.txt
        is used as a linking table.

        :param trip_id: ID of the Connection instance, given by the Stop instance.
            The trip_id must exist in trips.txt and its route_id must exist in routes.txt.
        :type trip_id: str

        :param route_id: ID of the route from trips.txt, based on trip_id.
        :type route_id: str

        :param route_short_name: Short, abstract name of a route, e.g., "32", "100X", "Green".
        :type route_short_name: str
        :param route_long_name: Full name of a route.
        :type route_long_name: str
        :param vehicle: Type of vehicle (e.g., bus, tram) mapped based on route_type code.
        :type vehicle: str

        :raises KeyError: If trip_id or route_id cannot be found in the corresponding GTFS files.
        """
        self.trip_id: str = trip_id

        self._trips_df = self.load_trips_df()
        self.route_id: str = self.get_route_id()

        self._routes_df: pd.DataFrame = self.load_routes_df()
        self.route_short_name: str = self.get_short_name()
        self.route_long_name: str = self.get_long_name()
        self.vehicle: str = self.get_vehicle_type()

    def load_trips_df(self) -> pd.DataFrame:
        """
        Load the trips GTFS file into a pandas DataFrame.

        The DataFrame is indexed by trip_id to allow efficient lookups.

        :return: DataFrame containing trips data indexed by trip_id.
        :rtype: pd.DataFrame
        """
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'trips.txt'
        df = read_csv_to_dataframe(input_file)
        return df.set_index('trip_id')

    def get_route_id(self) -> str:
        """
        Retrieve the route_id associated with the current trip_id in the trips GTFS data.

        :return: Route ID corresponding to the trip.
        :rtype: str

        :raises KeyError: If the trip_id does not exist in the trips DataFrame.
        """
        return str(self._trips_df.at[self.trip_id, 'route_id'])

    def load_routes_df(self) -> pd.DataFrame:
        """
        Load the routes GTFS file into a pandas DataFrame.

        The DataFrame is indexed by route_id to allow efficient lookups.

        :return: DataFrame containing routes data indexed by route_id.
        :rtype: pd.DataFrame
        """
        input_dir = get_path('INPUT_PATH') 
        input_file = input_dir / 'routes.txt'
        df = read_csv_to_dataframe(input_file)
        return df.set_index('route_id')

    def get_short_name(self) -> str:
        """
        Retrieve the short name of the route.

        :return: Short, abstract name of the route (e.g., "32", "100X", "Green").
        :rtype: str
        """
        return str(self._routes_df.at[self.route_id, 'route_short_name'])

    def get_long_name(self) -> str:
        """
        Retrieve the long, descriptive name of the route.

        :return: Full name of the route.
        :rtype: str
        """
        return str(self._routes_df.at[self.route_id, 'route_long_name'])

    def map_route_type(self, route_type: str) -> str:
        """
        Map a GTFS route_type code to a human-readable vehicle type.

        The mappings follow the GTFS specification:
        https://gtfs.org/documentation/schedule/reference/#routestxt

        :param route_type: GTFS route_type code.
        :type route_type: str

        :return: Human-readable vehicle type (e.g., "Bus", "Straßenbahn").
        :rtype: str
        """
        mappings = {
            '0' : 'Straßenbahn',
            '2' : 'City-Bahn',
            '3' : 'Bus',
            '7' : 'Drahtseilbahn',
        }
        return mappings[route_type] if route_type in mappings else '???'

    def get_vehicle_type(self) -> str:
        """
        Determine the vehicle type used on the route associated with this trip.

        :return: Vehicle type (e.g., bus, tram).
        :rtype: str
        """
        route_type = str(self._routes_df.at[self.route_id, 'route_type'])
        mapped_route_type = self.map_route_type(route_type)
        return mapped_route_type