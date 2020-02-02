from locust import Locust
from .dubbo_protocol import DubboClient


class DubboLocust(Locust):
    """
    This is the abstract Locust class which should be subclassed. It provides an dubbo client
    that can be used to make dubbo requests that will be tracked in Locust's statistics.
    """
    def __init__(self, *args, **kwargs):
        super(DubboLocust, self).__init__(*args, **kwargs)
        self.client = DubboClient(self.host, self.port)