# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qan.qan.response_withdrawals import ResponseWithdrawals

class TestResponseWithdrawals(unittest.TestCase):
    """ResponseWithdrawals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseWithdrawals:
        """Test ResponseWithdrawals
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseWithdrawals`
        """
        model = ResponseWithdrawals()
        if include_optional:
            return ResponseWithdrawals(
                address = '',
                amount = '',
                index = 56,
                validator_index = 56
            )
        else:
            return ResponseWithdrawals(
                address = '',
                amount = '',
                index = 56,
                validator_index = 56,
        )
        """

    def testResponseWithdrawals(self):
        """Test ResponseWithdrawals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
