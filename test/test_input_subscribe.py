# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.input_subscribe import InputSubscribe

class TestInputSubscribe(unittest.TestCase):
    """InputSubscribe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InputSubscribe:
        """Test InputSubscribe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InputSubscribe`
        """
        model = InputSubscribe()
        if include_optional:
            return InputSubscribe(
                var_schema = '',
                data = None,
                flag = True,
                subscription_name = ''
            )
        else:
            return InputSubscribe(
                data = None,
                flag = True,
                subscription_name = '',
        )
        """

    def testInputSubscribe(self):
        """Test InputSubscribe"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()