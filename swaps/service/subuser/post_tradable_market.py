from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.subuser.trade_market import TradeMarket
from swaps.utils import *


class PostTradableMarketService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/tradable-market"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", {}), TradeMarket)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
