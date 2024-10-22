# OutputGetTransactionByHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction** | [**ResponseTransaction**](ResponseTransaction.md) | The transaction response object, or null if no transaction is found | 

## Example

```python
from qan.qan.output_get_transaction_by_hash import OutputGetTransactionByHash

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetTransactionByHash from a JSON string
output_get_transaction_by_hash_instance = OutputGetTransactionByHash.from_json(json)
# print the JSON string representation of the object
print(OutputGetTransactionByHash.to_json())

# convert the object into a dict
output_get_transaction_by_hash_dict = output_get_transaction_by_hash_instance.to_dict()
# create an instance of OutputGetTransactionByHash from a dict
output_get_transaction_by_hash_from_dict = OutputGetTransactionByHash.from_dict(output_get_transaction_by_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


