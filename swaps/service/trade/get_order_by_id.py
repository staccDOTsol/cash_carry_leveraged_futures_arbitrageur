from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.trade import *
from swaps.utils import *


class GetOrderByIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]
        def get_channel():
            path = "/v1/order/orders/{}"
            return path.format(order_id)

        def parse(dict_data):
            data_dict = dict_data.get("data")
            return Order.json_parse(data_dict)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)






