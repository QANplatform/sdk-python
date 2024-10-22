# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qan.qan.output_get_block_by_hash import OutputGetBlockByHash

class TestOutputGetBlockByHash(unittest.TestCase):
    """OutputGetBlockByHash unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutputGetBlockByHash:
        """Test OutputGetBlockByHash
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutputGetBlockByHash`
        """
        model = OutputGetBlockByHash()
        if include_optional:
            return OutputGetBlockByHash(
                var_schema = '',
                block = qan.models.response_block.Response_Block(
                    base_fee_per_gas = '', 
                    difficulty = '', 
                    extra_data = '', 
                    gas_limit = '', 
                    gas_used = '', 
                    hash = '', 
                    logs_bloom = '', 
                    miner = '', 
                    mix_hash = '', 
                    nonce = '', 
                    number = '', 
                    parent_hash = '', 
                    receipts_root = '', 
                    sha3_uncles = '', 
                    size = '', 
                    state_root = '', 
                    timestamp = '', 
                    total_difficulty = '', 
                    transactions = [
                        qan.models.response_transaction.Response_Transaction(
                            access_list = '', 
                            block_hash = '', 
                            block_number = '', 
                            chain_id = '', 
                            from = '', 
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
                            value = '', )
                        ], 
                    transactions_root = '', 
                    uncles = [
                        ''
                        ], 
                    withdrawals = qan.models.response_withdrawals.Response_Withdrawals(
                        address = '', 
                        amount = '', 
                        index = 56, 
                        validator_index = 56, ), 
                    withdrawals_root = '', )
            )
        else:
            return OutputGetBlockByHash(
                block = qan.models.response_block.Response_Block(
                    base_fee_per_gas = '', 
                    difficulty = '', 
                    extra_data = '', 
                    gas_limit = '', 
                    gas_used = '', 
                    hash = '', 
                    logs_bloom = '', 
                    miner = '', 
                    mix_hash = '', 
                    nonce = '', 
                    number = '', 
                    parent_hash = '', 
                    receipts_root = '', 
                    sha3_uncles = '', 
                    size = '', 
                    state_root = '', 
                    timestamp = '', 
                    total_difficulty = '', 
                    transactions = [
                        qan.models.response_transaction.Response_Transaction(
                            access_list = '', 
                            block_hash = '', 
                            block_number = '', 
                            chain_id = '', 
                            from = '', 
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
                            value = '', )
                        ], 
                    transactions_root = '', 
                    uncles = [
                        ''
                        ], 
                    withdrawals = qan.models.response_withdrawals.Response_Withdrawals(
                        address = '', 
                        amount = '', 
                        index = 56, 
                        validator_index = 56, ), 
                    withdrawals_root = '', ),
        )
        """

    def testOutputGetBlockByHash(self):
        """Test OutputGetBlockByHash"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
