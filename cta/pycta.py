import os


class PyCTA:
    def __init__(self):
        self._auth()
        self._map_station_ids()

    def _auth(self):
        token = os.environ.get("CTA_TOKEN")  # FIXME: scuffed use case as hell
        self.token = token

    def _map_station_ids(self):
        self.station_ids = {}

        with open("stops.txt", "r") as stopfile:
            stops = stopfile.readlines()

        for stop in stops:
            stop = stop.strip("\n")
            stop_info = stop.split()

            self.station_ids[" ".join(stop_info[:-1])] = stop_info[-1]

            #s = " ".join(stop_info[2:-1]).split(")")[0] + ")"

