from train_tracker.follower import Follower


class Train:
    def __init__(self, run_id, line, destination, station=None):
        self.id = run_id
        self.line = line
        self.destination = destination
        self.next_station = station
        self.latitude = None
        self.longitude = None
        self.heading = None
        self.is_approaching = None
        self.follower = None

    def __repr__(self):
        return f"{self.line}-{self.id}"

    def __str__(self):
        return f"{self.line}-{self.id}"

    def update(self):
        self.follower = Follower()
        current_update = self.follower.get_train_progress(self.id)
        position = current_update["position"]

        self.latitude = position["lat"]
        self.longitude = position["lon"]
        self.heading = position["heading"]

        if current_update.get("eta"):
            self.next_station = current_update["eta"][0]["staNm"]
            self.is_approaching = current_update["eta"][0]["isApp"]

    @property
    def is_approaching(self):
        return True if self.is_approaching == "1" else False

    @is_approaching.setter
    def is_approaching(self, app):
        self.is_approaching = app
