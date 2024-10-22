# ResponseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list** | **str** | A list of addresses and storage keys that the transaction plans to access | [optional] 
**block_hash** | **str** | The hash of the block where this transaction was in. Null when it&#39;s a pending transaction | [optional] 
**block_number** | **str** | The block number where this transaction was in. Null when it&#39;s a pending transaction | [optional] 
**chain_id** | **str** | The chain id of the transaction, if any | [optional] 
**var_from** | **str** | The address of the sender | [optional] 
**gas** | **str** | The gas provided by the sender, encoded as decimal | [optional] 
**gas_price** | **str** | The gas price provided by the sender in wei encoded as decimal | [optional] 
**hash** | **str** | The hash of the transaction | [optional] 
**input** | **str** | The data sent along with the transaction | [optional] 
**max_fee_per_gas** | **str** | The maximum fee per gas set in the transaction | [optional] 
**max_priority_fee_per_gas** | **str** | The maximum priority gas fee set in the transaction | [optional] 
**nonce** | **str** | The number of transactions made by the sender prior to this one encoded as decimal | [optional] 
**r** | **str** | The R field of the signature | [optional] 
**s** | **str** | The S field of the signature | [optional] 
**to** | **str** | The address of the receiver. Null when its a contract creation transaction | [optional] 
**transaction_index** | **str** | The integer of the transaction&#39;s index position that the log was created from. Null when it&#39;s a pending log | [optional] 
**type** | **str** | The transaction type | [optional] 
**v** | **str** | The standardized V field of the signature | [optional] 
**value** | **str** | The value transferred in wei encoded as decimal | [optional] 

## Example

```python
from qan.qan.response_transaction import ResponseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTransaction from a JSON string
response_transaction_instance = ResponseTransaction.from_json(json)
# print the JSON string representation of the object
print(ResponseTransaction.to_json())

# convert the object into a dict
response_transaction_dict = response_transaction_instance.to_dict()
# create an instance of ResponseTransaction from a dict
response_transaction_from_dict = ResponseTransaction.from_dict(response_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


