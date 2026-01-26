from env_manager import get_position, get_distance, get_path
from file_handler import read_csv_to_dataframe
from typing import List


class Connection:
    def __init__(self, stop_id, stop_name, departures):
        self.stop_id: str = stop_id
        self.location: str = stop_name
        #self.direction = direction
        self.departures = departures # panda df

class Area:
    def __init__(self, latitude = 0.0, longtitude = 0.0, distance = 0.0):
        self.latitude: float = latitude
        self.longtitude: float = longtitude
        self.distance: float = distance # Radius in m from position to find stops

        self.connections: List[Connection] = []
    
    def set_area(self) -> None:
        self.latitude, self.latitude = get_position()
        self.distance = get_distance()
    
    def set_connections(self) -> None:
        self.connections = self.get_nearby_connections()

    def get_nearby_connections(self) -> List[Connection]:
        intput_dir = get_path('INPUT_PATH') 
        input_file = intput_dir / 'stops.txt'
        df = read_csv_to_dataframe(input_file)
        pass


if __name__ == '__main__':
    intput_filename = ""