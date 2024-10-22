# ResponseBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee_per_gas** | **str** | A string of the base fee encoded in decimal format. Please note that this response field will not be included in a block requested before the EIP-1559 upgrade | 
**difficulty** | **str** | The integer of the difficulty for this block encoded as a decimal | 
**extra_data** | **str** | The “extra data” field of this block | 
**gas_limit** | **str** | The maximum gas allowed in this block encoded as a decimal | 
**gas_used** | **str** | The total used gas by all transactions in this block encoded as a decimal | 
**hash** | **str** | The block hash of the requested block. null if pending | 
**logs_bloom** | **str** | The bloom filter for the logs of the block. null if pending | 
**miner** | **str** | The address of the beneficiary to whom the mining rewards were given | 
**mix_hash** | **str** | A string of a 256-bit hash encoded as a decimal | 
**nonce** | **str** | The hash of the generated proof-of-work. null if pending | 
**number** | **str** | The block number of the requested block encoded as a decimal. null if pending | 
**parent_hash** | **str** | The hash of the parent block | 
**receipts_root** | **str** | The root of the receipts trie of the bloc | 
**sha3_uncles** | **str** | The SHA3 of the uncles data in the block | 
**size** | **str** | The size of this block in bytes as an Integer value encoded as decimal | 
**state_root** | **str** | The root of the final state trie of the block | 
**timestamp** | **str** | The unix timestamp for when the block was collated | 
**total_difficulty** | **str** | The integer of the total difficulty of the chain until this block encoded as a decimal | 
**transactions** | [**List[ResponseTransaction]**](ResponseTransaction.md) | An array of transaction objects - please see getTransactionByHash for exact shape | 
**transactions_root** | **str** | The root of the transaction trie of the block | 
**uncles** | **List[str]** | An array of uncle hashes | 
**withdrawals** | [**ResponseWithdrawals**](ResponseWithdrawals.md) | A withdrawals object contains information about withdrawals made by validators. Please note that this field will not be included in a block requested before the EIP-4895 upgrade | 
**withdrawals_root** | **str** | The Merkle root of withdrawal data. Also, please note that this field will not be included in a block requested before the EIP-4895 upgrade | 

## Example

```python
from qan.qan.response_block import ResponseBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBlock from a JSON string
response_block_instance = ResponseBlock.from_json(json)
# print the JSON string representation of the object
print(ResponseBlock.to_json())

# convert the object into a dict
response_block_dict = response_block_instance.to_dict()
# create an instance of ResponseBlock from a dict
response_block_from_dict = ResponseBlock.from_dict(response_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


