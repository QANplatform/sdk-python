# OutputGetTransactionReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction_receipt** | [**ResponseTransactionReceipt**](ResponseTransactionReceipt.md) | A transaction receipt object, or null when the transaction is not available | 

## Example

```python
from qan.qan.output_get_transaction_receipt import OutputGetTransactionReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetTransactionReceipt from a JSON string
output_get_transaction_receipt_instance = OutputGetTransactionReceipt.from_json(json)
# print the JSON string representation of the object
print(OutputGetTransactionReceipt.to_json())

# convert the object into a dict
output_get_transaction_receipt_dict = output_get_transaction_receipt_instance.to_dict()
# create an instance of OutputGetTransactionReceipt from a dict
output_get_transaction_receipt_from_dict = OutputGetTransactionReceipt.from_dict(output_get_transaction_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


