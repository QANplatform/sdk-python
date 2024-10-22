# InputNewFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**filter_object** | [**FilterObject**](FilterObject.md) |  | 

## Example

```python
from qan.qan.input_new_filter import InputNewFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InputNewFilter from a JSON string
input_new_filter_instance = InputNewFilter.from_json(json)
# print the JSON string representation of the object
print(InputNewFilter.to_json())

# convert the object into a dict
input_new_filter_dict = input_new_filter_instance.to_dict()
# create an instance of InputNewFilter from a dict
input_new_filter_from_dict = InputNewFilter.from_dict(input_new_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


