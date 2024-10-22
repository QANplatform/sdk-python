# ResponseTransactionReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_hash** | **str** | The hash of the block. null when pending | [optional] 
**block_number** | **str** |  | [optional] 
**contract_address** | **str** | The contract address created if the transaction was a contract creation, otherwise null | [optional] 
**cumulative_gas_used** | **str** | The total amount of gas used when this transaction was executed in the block | [optional] 
**effective_gas_price** | **str** | The actual value per gas deducted from the sender account | [optional] 
**var_from** | **str** | The address of the sender | [optional] 
**gas_used** | **str** | The amount of gas used by this specific transaction alone | [optional] 
**logs** | [**List[ResponseLog]**](ResponseLog.md) | An array of log objects that generated this transaction | [optional] 
**logs_bloom** | **str** | The bloom filter for light clients to quickly retrieve related logs | [optional] 
**status** | **str** | It is either 1 (success) or 0 (failure) encoded as a decimal | [optional] 
**to** | **str** | The address of the receiver. null when it&#39;s a contract creation transaction | [optional] 
**transaction_hash** | **str** | The hash of the transaction | [optional] 
**transaction_index** | **str** | An index of the transaction in the block | [optional] 
**type** | **str** | The value type | [optional] 

## Example

```python
from qan.qan.response_transaction_receipt import ResponseTransactionReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTransactionReceipt from a JSON string
response_transaction_receipt_instance = ResponseTransactionReceipt.from_json(json)
# print the JSON string representation of the object
print(ResponseTransactionReceipt.to_json())

# convert the object into a dict
response_transaction_receipt_dict = response_transaction_receipt_instance.to_dict()
# create an instance of ResponseTransactionReceipt from a dict
response_transaction_receipt_from_dict = ResponseTransactionReceipt.from_dict(response_transaction_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


