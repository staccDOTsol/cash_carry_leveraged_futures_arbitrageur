from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.utils import *
from swaps.model.etf import *



class PostEftSwapInService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/etf/swap/in"

        def parse(dict_data):
            return default_parse_fill_directly(dict_data, EtfSwapInOut)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)









