# OutputGetBlockTransactionCountByHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction_count** | **str** | The number of transactions associated with a specific block, in decimal value | 

## Example

```python
from openapi_client.models.output_get_block_transaction_count_by_hash import OutputGetBlockTransactionCountByHash

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetBlockTransactionCountByHash from a JSON string
output_get_block_transaction_count_by_hash_instance = OutputGetBlockTransactionCountByHash.from_json(json)
# print the JSON string representation of the object
print OutputGetBlockTransactionCountByHash.to_json()

# convert the object into a dict
output_get_block_transaction_count_by_hash_dict = output_get_block_transaction_count_by_hash_instance.to_dict()
# create an instance of OutputGetBlockTransactionCountByHash from a dict
output_get_block_transaction_count_by_hash_form_dict = output_get_block_transaction_count_by_hash.from_dict(output_get_block_transaction_count_by_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


