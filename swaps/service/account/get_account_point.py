from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.account import *
from swaps.utils import *


class GetAccountPointService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/point/account"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountPointResult, {})

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
