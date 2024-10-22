# FilterObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The contract address or a list of addresses from which logs should originate | 
**from_block** | **str** |  | 
**to_block** | **str** |  | 
**topics** | **List[str]** |  | 

## Example

```python
from qan.qan.filter_object import FilterObject

# TODO update the JSON string below
json = "{}"
# create an instance of FilterObject from a JSON string
filter_object_instance = FilterObject.from_json(json)
# print the JSON string representation of the object
print(FilterObject.to_json())

# convert the object into a dict
filter_object_dict = filter_object_instance.to_dict()
# create an instance of FilterObject from a dict
filter_object_from_dict = FilterObject.from_dict(filter_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


