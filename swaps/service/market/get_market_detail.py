from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.market import *
from swaps.utils import *



class GetMarketDetailService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/detail"

        def parse(dict_data):
            tick = dict_data.get("tick", {})
            return default_parse(tick, MarketDetail)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






