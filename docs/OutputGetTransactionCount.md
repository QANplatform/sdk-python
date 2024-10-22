# OutputGetTransactionCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction_count** | **str** | The integer of the number of transactions sent from an address encoded as decimal | 

## Example

```python
from qan.qan.output_get_transaction_count import OutputGetTransactionCount

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetTransactionCount from a JSON string
output_get_transaction_count_instance = OutputGetTransactionCount.from_json(json)
# print the JSON string representation of the object
print(OutputGetTransactionCount.to_json())

# convert the object into a dict
output_get_transaction_count_dict = output_get_transaction_count_instance.to_dict()
# create an instance of OutputGetTransactionCount from a dict
output_get_transaction_count_from_dict = OutputGetTransactionCount.from_dict(output_get_transaction_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


