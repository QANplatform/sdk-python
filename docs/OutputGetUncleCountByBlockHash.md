# OutputGetUncleCountByBlockHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**uncle_count** | **str** |  | 

## Example

```python
from openapi_client.models.output_get_uncle_count_by_block_hash import OutputGetUncleCountByBlockHash

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetUncleCountByBlockHash from a JSON string
output_get_uncle_count_by_block_hash_instance = OutputGetUncleCountByBlockHash.from_json(json)
# print the JSON string representation of the object
print OutputGetUncleCountByBlockHash.to_json()

# convert the object into a dict
output_get_uncle_count_by_block_hash_dict = output_get_uncle_count_by_block_hash_instance.to_dict()
# create an instance of OutputGetUncleCountByBlockHash from a dict
output_get_uncle_count_by_block_hash_form_dict = output_get_uncle_count_by_block_hash.from_dict(output_get_uncle_count_by_block_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


