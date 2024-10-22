# OutputSendRawTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction_hash** | **str** | The transaction hash, or the zero hash if the transaction is not yet available | 

## Example

```python
from qan.qan.output_send_raw_transaction import OutputSendRawTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of OutputSendRawTransaction from a JSON string
output_send_raw_transaction_instance = OutputSendRawTransaction.from_json(json)
# print the JSON string representation of the object
print(OutputSendRawTransaction.to_json())

# convert the object into a dict
output_send_raw_transaction_dict = output_send_raw_transaction_instance.to_dict()
# create an instance of OutputSendRawTransaction from a dict
output_send_raw_transaction_from_dict = OutputSendRawTransaction.from_dict(output_send_raw_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


