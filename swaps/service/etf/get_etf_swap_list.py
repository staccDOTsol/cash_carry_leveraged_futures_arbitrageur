from swaps.connection.restapi_sync_client import RestApiSyncClient
from swaps.constant.system import HttpMethod
from swaps.model.etf import *

class GetEtfSwapListService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
      channel = "/etf/swap/list"

      def parse(dict_data):
        return EtfSwapList.json_parse_list(dict_data.get("data", []))

      return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)







