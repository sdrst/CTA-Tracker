from train_tracker.train_tracker import TrainTracker
from resources import Train
from collections import defaultdict


class Locations(TrainTracker):
    def _active_trains_raw(self, lines=None):
        results = defaultdict(list)

        if not lines:
            lines = []

        for line in lines:
            line_metadata = self._get_location_metadata_by_line(line)

            for route in line_metadata["ctatt"]["route"]:
                for train in route["train"]:
                    results[line].append(train)

        return results

    def get_all_active_trains(self, lines=None, raw=False):
        if raw:
            return self._active_trains_raw(lines)

        trains = []

        if not lines:
            lines = []

        for line in lines:
            line_metadata = self._get_location_metadata_by_line(line)

            for route in line_metadata["route"]:
                for train in route["train"]:
                    train = Train(train['rn'], line, train["destNm"], train["nextStaNm"])
                    trains.append(train)

        return trains


if __name__ == "__main__":
    print(Locations().station_ids)
