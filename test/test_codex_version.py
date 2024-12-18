# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from codex_api_client.models.codex_version import CodexVersion

class TestCodexVersion(unittest.TestCase):
    """CodexVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodexVersion:
        """Test CodexVersion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodexVersion`
        """
        model = CodexVersion()
        if include_optional:
            return CodexVersion(
                version = 'v0.1.7',
                revision = '0c647d8'
            )
        else:
            return CodexVersion(
        )
        """

    def testCodexVersion(self):
        """Test CodexVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
