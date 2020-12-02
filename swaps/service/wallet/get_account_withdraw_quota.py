from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant import *
from swaps.model.wallet import *
from swaps.utils import *


class GetAccountWithdrawQuotaService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/account/withdraw/quota"

        def parse(dict_data):
            data = dict_data.get("data", {})
            chains = data.get("chains", [])
            return default_parse_list_dict(chains, WithdrawQuota)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






