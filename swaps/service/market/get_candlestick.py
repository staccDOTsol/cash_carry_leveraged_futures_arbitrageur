from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.market import *
from swaps.utils import *



class GetCandleStickService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/history/kline"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", []), Candlestick)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






