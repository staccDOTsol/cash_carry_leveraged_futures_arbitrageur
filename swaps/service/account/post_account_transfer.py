from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.account import *
from swaps.utils import *


class PostAccountTransferService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/account/transfer"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountTransferResult, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
