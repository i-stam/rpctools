from BaseTestClass import BaseTest
from rpctools import rpc_factory


class TestHTTPRPC(BaseTest):
    def make_rpc_client(self):
        return rpc_factory('http://localhost:8545', False)
