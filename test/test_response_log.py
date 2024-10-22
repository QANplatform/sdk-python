# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qan.qan.response_log import ResponseLog

class TestResponseLog(unittest.TestCase):
    """ResponseLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseLog:
        """Test ResponseLog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseLog`
        """
        model = ResponseLog()
        if include_optional:
            return ResponseLog(
                address = '',
                block_hash = '',
                block_number = '',
                data = '',
                log_index = '',
                removed = True,
                topics = [
                    ''
                    ],
                transaction_hash = '',
                transaction_index = ''
            )
        else:
            return ResponseLog(
                address = '',
                block_hash = '',
                block_number = '',
                data = '',
                log_index = '',
                removed = True,
                topics = [
                    ''
                    ],
                transaction_hash = '',
                transaction_index = '',
        )
        """

    def testResponseLog(self):
        """Test ResponseLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
