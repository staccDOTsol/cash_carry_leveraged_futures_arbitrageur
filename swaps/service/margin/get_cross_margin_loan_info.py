from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.margin import *
from swaps.utils import *



class GetCrossMarginLoanInfoService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/cross-margin/loan-info"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", []), CrossMarginLoanInfo, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






