# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qan.qan.input_call import InputCall

class TestInputCall(unittest.TestCase):
    """InputCall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InputCall:
        """Test InputCall
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InputCall`
        """
        model = InputCall()
        if include_optional:
            return InputCall(
                var_schema = '',
                block_number = '',
                transaction = qan.models.params_transaction.Params_Transaction(
                    data = '', 
                    from = '', 
                    gas = '', 
                    gas_price = '', 
                    to = '', 
                    value = '', )
            )
        else:
            return InputCall(
                block_number = '',
                transaction = qan.models.params_transaction.Params_Transaction(
                    data = '', 
                    from = '', 
                    gas = '', 
                    gas_price = '', 
                    to = '', 
                    value = '', ),
        )
        """

    def testInputCall(self):
        """Test InputCall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
