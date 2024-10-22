# OutputGetTransactionByBlockNumberAndIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction** | [**ResponseTransaction**](ResponseTransaction.md) | The transaction response object, or null if no transaction is found | 

## Example

```python
from qan.qan.output_get_transaction_by_block_number_and_index import OutputGetTransactionByBlockNumberAndIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetTransactionByBlockNumberAndIndex from a JSON string
output_get_transaction_by_block_number_and_index_instance = OutputGetTransactionByBlockNumberAndIndex.from_json(json)
# print the JSON string representation of the object
print(OutputGetTransactionByBlockNumberAndIndex.to_json())

# convert the object into a dict
output_get_transaction_by_block_number_and_index_dict = output_get_transaction_by_block_number_and_index_instance.to_dict()
# create an instance of OutputGetTransactionByBlockNumberAndIndex from a dict
output_get_transaction_by_block_number_and_index_from_dict = OutputGetTransactionByBlockNumberAndIndex.from_dict(output_get_transaction_by_block_number_and_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


