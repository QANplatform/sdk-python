# InputSendRawTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**data** | **str** | The signed transaction (typically signed with a library, using your private key) | 

## Example

```python
from qan.qan.input_send_raw_transaction import InputSendRawTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InputSendRawTransaction from a JSON string
input_send_raw_transaction_instance = InputSendRawTransaction.from_json(json)
# print the JSON string representation of the object
print(InputSendRawTransaction.to_json())

# convert the object into a dict
input_send_raw_transaction_dict = input_send_raw_transaction_instance.to_dict()
# create an instance of InputSendRawTransaction from a dict
input_send_raw_transaction_from_dict = InputSendRawTransaction.from_dict(input_send_raw_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


