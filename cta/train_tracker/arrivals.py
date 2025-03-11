import re
from train_tracker.train_tracker import TrainTracker


class Arrivals(TrainTracker):
    def get_station_arrivals(self, station):
        possible_stops = {}

        for name, value in self.station_ids.items():
            if re.search(station, name, re.IGNORECASE):
                possible_stops[name] = self._get_arrival_metadata_by_station(value)

        return possible_stops


if __name__ == "__main__":
    arrivals = Arrivals()
    print(arrivals.get_station_arrivals("Clark/Lake"))

