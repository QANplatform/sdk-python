# OutputNewBlockFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**filter_id** | **str** | A filter id to be used when calling getFilterChanges | 

## Example

```python
from qan.qan.output_new_block_filter import OutputNewBlockFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OutputNewBlockFilter from a JSON string
output_new_block_filter_instance = OutputNewBlockFilter.from_json(json)
# print the JSON string representation of the object
print(OutputNewBlockFilter.to_json())

# convert the object into a dict
output_new_block_filter_dict = output_new_block_filter_instance.to_dict()
# create an instance of OutputNewBlockFilter from a dict
output_new_block_filter_from_dict = OutputNewBlockFilter.from_dict(output_new_block_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


