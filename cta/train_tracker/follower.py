from train_tracker.train_tracker import TrainTracker


class Follower(TrainTracker):
    def __init__(self):
        super().__init__()

    def get_train_progress(self, train_id):
        run_data = self._follow_train_metadata(train_id)

        return run_data

    def get_approaching_station(self, run):
        follower = self._follow_train_metadata(run)

        station_name = follower["eta"][0]["staNm"]
        station_id = follower["eta"][0]["staId"]

        return station_name, station_id



