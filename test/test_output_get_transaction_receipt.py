# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qan.qan.output_get_transaction_receipt import OutputGetTransactionReceipt

class TestOutputGetTransactionReceipt(unittest.TestCase):
    """OutputGetTransactionReceipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutputGetTransactionReceipt:
        """Test OutputGetTransactionReceipt
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutputGetTransactionReceipt`
        """
        model = OutputGetTransactionReceipt()
        if include_optional:
            return OutputGetTransactionReceipt(
                var_schema = '',
                transaction_receipt = qan.models.response_transaction_receipt.Response_TransactionReceipt(
                    block_hash = '', 
                    block_number = '', 
                    contract_address = '', 
                    cumulative_gas_used = '', 
                    effective_gas_price = '', 
                    from = '', 
                    gas_used = '', 
                    logs = [
                        qan.models.response_log.Response_Log(
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
                            transaction_index = '', )
                        ], 
                    logs_bloom = '', 
                    status = '', 
                    to = '', 
                    transaction_hash = '', 
                    transaction_index = '', 
                    type = '', )
            )
        else:
            return OutputGetTransactionReceipt(
                transaction_receipt = qan.models.response_transaction_receipt.Response_TransactionReceipt(
                    block_hash = '', 
                    block_number = '', 
                    contract_address = '', 
                    cumulative_gas_used = '', 
                    effective_gas_price = '', 
                    from = '', 
                    gas_used = '', 
                    logs = [
                        qan.models.response_log.Response_Log(
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
                            transaction_index = '', )
                        ], 
                    logs_bloom = '', 
                    status = '', 
                    to = '', 
                    transaction_hash = '', 
                    transaction_index = '', 
                    type = '', ),
        )
        """

    def testOutputGetTransactionReceipt(self):
        """Test OutputGetTransactionReceipt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
