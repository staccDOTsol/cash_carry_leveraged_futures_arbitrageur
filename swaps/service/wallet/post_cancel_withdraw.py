from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.trade import *
from swaps.utils import *
from swaps.utils.json_parser import default_parse_data_as_long


class PostCancelWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        withdraw_id_params = self.params["withdraw-id"]
        def get_channel():
            path = "/v1/dw/withdraw-virtual/{}/cancel"
            return path.format(withdraw_id_params)

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






