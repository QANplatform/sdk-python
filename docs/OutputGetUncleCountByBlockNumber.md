# OutputGetUncleCountByBlockNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**uncle_count** | **str** |  | 

## Example

```python
from openapi_client.models.output_get_uncle_count_by_block_number import OutputGetUncleCountByBlockNumber

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetUncleCountByBlockNumber from a JSON string
output_get_uncle_count_by_block_number_instance = OutputGetUncleCountByBlockNumber.from_json(json)
# print the JSON string representation of the object
print OutputGetUncleCountByBlockNumber.to_json()

# convert the object into a dict
output_get_uncle_count_by_block_number_dict = output_get_uncle_count_by_block_number_instance.to_dict()
# create an instance of OutputGetUncleCountByBlockNumber from a dict
output_get_uncle_count_by_block_number_form_dict = output_get_uncle_count_by_block_number.from_dict(output_get_uncle_count_by_block_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


