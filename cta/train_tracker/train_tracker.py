import os
import requests
import json

from pycta import PyCTA
cta_token = os.environ.get("CTA_TOKEN")


class TrainTracker(PyCTA):
    def __init__(self):
        super().__init__()

        self.base_url = "http://lapi.transitchicago.com/api/1.0/"
        self.params = {"key": self.token, "outputType": "JSON"}

    def _api_call(self, uri, **kwparams):
        res = requests.get(self.base_url + uri, params={**self.params, **kwparams})
        formatted_data = json.loads(res.content)

        return formatted_data

    def _get_location_metadata_by_line(self, line, **kwargs):
        locations_uri = "ttpositions.aspx"
        params = {"rt": line, **kwargs}

        route_data = self._api_call(locations_uri, **params)
        return route_data.get("ctatt")

    def _follow_train_metadata(self, run, **kwargs):
        follow_uri = "ttfollow.aspx"
        params = {"runnumber": run, **kwargs}

        res = self._api_call(follow_uri, **params)
        return res.get("ctatt")

    def _get_arrival_metadata_by_station(self, station, **kwargs):
        arrival_uri = "ttarrivals.aspx"
        params = {"mapid": self.station_ids[station], **kwargs}

        res = self._api_call(arrival_uri, **params)
        return res



