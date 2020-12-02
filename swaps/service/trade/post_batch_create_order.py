from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.trade.batch_create_order import BatchCreateOrder
from swaps.utils import *

class PostBatchCreateOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/batch-orders"

        def parse(dict_data):
            data = dict_data.get("data", [])
            return default_parse_list_dict(data, BatchCreateOrder, [])

        return RestApiSyncClient(**kwargs).request_process_post_batch(HttpMethod.POST_SIGN, channel, self.params, parse)






