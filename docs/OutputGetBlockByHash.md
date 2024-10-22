# OutputGetBlockByHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**block** | [**ResponseBlock**](ResponseBlock.md) | A block object, or null when no block was found | 

## Example

```python
from qan.qan.output_get_block_by_hash import OutputGetBlockByHash

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetBlockByHash from a JSON string
output_get_block_by_hash_instance = OutputGetBlockByHash.from_json(json)
# print the JSON string representation of the object
print(OutputGetBlockByHash.to_json())

# convert the object into a dict
output_get_block_by_hash_dict = output_get_block_by_hash_instance.to_dict()
# create an instance of OutputGetBlockByHash from a dict
output_get_block_by_hash_from_dict = OutputGetBlockByHash.from_dict(output_get_block_by_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


