from train_tracker.locations import Locations
from train_tracker.follower import Follower
from resources import Train
import re

trains = Locations()

#print(trains.station_ids)

for x, y in trains.station_ids.items():
    if re.search("", x, re.IGNORECASE):
        print(x, y)


