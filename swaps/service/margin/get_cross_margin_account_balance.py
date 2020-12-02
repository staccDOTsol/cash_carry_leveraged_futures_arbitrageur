from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.margin import *
from swaps.utils import *



class GetCrossMarginAccountBalanceService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/cross-margin/accounts/balance"

        def parse(dict_data):
            return CrossMarginAccountBalance.json_parse(dict_data.get("data", {}))

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






