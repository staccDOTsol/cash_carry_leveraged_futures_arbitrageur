from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.market import *
from swaps.utils import *


class GetMarketTradeService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/trade"

        def parse(dict_data):
            tick = dict_data.get("tick", {})
            data = tick.get("data", [])
            return default_parse_list_dict(data, Trade, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






