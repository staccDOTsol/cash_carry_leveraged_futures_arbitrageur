from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.trade import *
from swaps.utils import *
from swaps.utils.json_parser import default_parse_data_as_long


class PostCreateWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/dw/withdraw/api/create"

        def parse(dict_data):
            # return dict_data.get("data", 0)
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






