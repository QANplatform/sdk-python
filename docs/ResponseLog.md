# ResponseLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An address from which this log originated | 
**block_hash** | **str** | The hash of the block where this log was in. null when its a pending log | 
**block_number** | **str** | The block number where this log was in. null when its a pending log | 
**data** | **str** | It contains one or more 32 Bytes non-indexed arguments of the log | 
**log_index** | **str** | The integer of the log index position in the block. null when its a pending log | 
**removed** | **bool** | It is true when the log was removed due to a chain reorganization, and false if it&#39;s a valid log | 
**topics** | **List[str]** | An array of zero to four 32 Bytes DATA of indexed log arguments. In Solidity, the first topic is the hash of the signature of the event (e.g. Deposit(address, bytes32, uint256)), except you declare the event with the anonymous specifier | 
**transaction_hash** | **str** | The hash of the transactions this log was created from. null when its a pending log | 
**transaction_index** | **str** | The integer of the transaction&#39;s index position that the log was created from. null when it&#39;s a pending log | 

## Example

```python
from qan.qan.response_log import ResponseLog

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseLog from a JSON string
response_log_instance = ResponseLog.from_json(json)
# print the JSON string representation of the object
print(ResponseLog.to_json())

# convert the object into a dict
response_log_dict = response_log_instance.to_dict()
# create an instance of ResponseLog from a dict
response_log_from_dict = ResponseLog.from_dict(response_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


