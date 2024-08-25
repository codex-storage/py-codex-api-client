# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from codex_client.models.slot_agent import SlotAgent

class TestSlotAgent(unittest.TestCase):
    """SlotAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlotAgent:
        """Test SlotAgent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlotAgent`
        """
        model = SlotAgent()
        if include_optional:
            return SlotAgent(
                id = '268a781e0db3f7cf36b18e5f4fdb7f586ec9edd08e5500b17c0e518a769f114a',
                slot_index = '',
                request_id = '0x...',
                request = codex_client.models.storage_request.StorageRequest(
                    id = '', 
                    client = '', 
                    ask = codex_client.models.storage_ask.StorageAsk(
                        slots = 56, 
                        slot_size = '', 
                        duration = '', 
                        proof_probability = '', 
                        reward = '', 
                        max_slot_loss = 56, ), 
                    content = codex_client.models.content.Content(
                        cid = 'QmYyQSo1c1Ym7orWxLYvCrM2EmxFTANf8wXmmE7DWjhx5N', 
                        erasure = codex_client.models.erasure_parameters.ErasureParameters(
                            total_chunks = 56, ), 
                        por = codex_client.models.po_r_parameters.PoRParameters(
                            u = '', 
                            public_key = '', 
                            name = '', ), ), 
                    expiry = '10 minutes', 
                    nonce = '', ),
                reservation = codex_client.models.reservation.Reservation(
                    id = '0x...', 
                    availability_id = '0x...', 
                    size = '', 
                    request_id = '0x...', 
                    slot_index = '', ),
                state = 'SaleCancelled'
            )
        else:
            return SlotAgent(
        )
        """

    def testSlotAgent(self):
        """Test SlotAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()