# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.response_transaction import ResponseTransaction

class TestResponseTransaction(unittest.TestCase):
    """ResponseTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseTransaction:
        """Test ResponseTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseTransaction`
        """
        model = ResponseTransaction()
        if include_optional:
            return ResponseTransaction(
                access_list = '',
                block_hash = '',
                block_number = '',
                chain_id = '',
                var_from = '',
                gas = '',
                gas_price = '',
                hash = '',
                input = '',
                max_fee_per_gas = '',
                max_priority_fee_per_gas = '',
                nonce = '',
                r = '',
                s = '',
                to = '',
                transaction_index = '',
                type = '',
                v = '',
                value = ''
            )
        else:
            return ResponseTransaction(
        )
        """

    def testResponseTransaction(self):
        """Test ResponseTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()