# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.output_block_number import OutputBlockNumber

class TestOutputBlockNumber(unittest.TestCase):
    """OutputBlockNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutputBlockNumber:
        """Test OutputBlockNumber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutputBlockNumber`
        """
        model = OutputBlockNumber()
        if include_optional:
            return OutputBlockNumber(
                var_schema = '',
                block_number = ''
            )
        else:
            return OutputBlockNumber(
                block_number = '',
        )
        """

    def testOutputBlockNumber(self):
        """Test OutputBlockNumber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()