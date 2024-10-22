# OutputGetFilterChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**result** | **object** |  | 

## Example

```python
from qan.qan.output_get_filter_changes import OutputGetFilterChanges

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetFilterChanges from a JSON string
output_get_filter_changes_instance = OutputGetFilterChanges.from_json(json)
# print the JSON string representation of the object
print(OutputGetFilterChanges.to_json())

# convert the object into a dict
output_get_filter_changes_dict = output_get_filter_changes_instance.to_dict()
# create an instance of OutputGetFilterChanges from a dict
output_get_filter_changes_from_dict = OutputGetFilterChanges.from_dict(output_get_filter_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


