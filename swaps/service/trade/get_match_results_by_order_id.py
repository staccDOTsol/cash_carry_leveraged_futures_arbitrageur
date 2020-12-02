from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.trade import *
from swaps.utils import *


class GetMatchResultsByOrderIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]
        def get_channel():
            path = "/v1/order/orders/{}/matchresults"
            return path.format(order_id)

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, MatchResult, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)






