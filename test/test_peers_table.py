# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from codex_api_client.models.peers_table import PeersTable

class TestPeersTable(unittest.TestCase):
    """PeersTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeersTable:
        """Test PeersTable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeersTable`
        """
        model = PeersTable()
        if include_optional:
            return PeersTable(
                local_node = codex_api_client.models.node.Node(
                    node_id = '', 
                    peer_id = '', 
                    record = '', 
                    address = '', 
                    seen = True, ),
                nodes = [
                    codex_api_client.models.node.Node(
                        node_id = '', 
                        peer_id = '', 
                        record = '', 
                        address = '', 
                        seen = True, )
                    ]
            )
        else:
            return PeersTable(
        )
        """

    def testPeersTable(self):
        """Test PeersTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
