from pycta import PyCTA


class CustomerAlerts(PyCTA):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.transitchicago.com/api/1.0/"
