# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.output_fee_history import OutputFeeHistory

class TestOutputFeeHistory(unittest.TestCase):
    """OutputFeeHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutputFeeHistory:
        """Test OutputFeeHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutputFeeHistory`
        """
        model = OutputFeeHistory()
        if include_optional:
            return OutputFeeHistory(
                var_schema = '',
                base_fee_per_gas = [
                    ''
                    ],
                gas_used_ratio = [
                    1.337
                    ],
                oldest_block = '',
                reward = [
                    [
                        ''
                        ]
                    ]
            )
        else:
            return OutputFeeHistory(
                base_fee_per_gas = [
                    ''
                    ],
                gas_used_ratio = [
                    1.337
                    ],
                oldest_block = '',
                reward = [
                    [
                        ''
                        ]
                    ],
        )
        """

    def testOutputFeeHistory(self):
        """Test OutputFeeHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()