# OutputXlinkValid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**validity** | **str** | The xlink validity time of the specified address. | 

## Example

```python
from qan.qan.output_xlink_valid import OutputXlinkValid

# TODO update the JSON string below
json = "{}"
# create an instance of OutputXlinkValid from a JSON string
output_xlink_valid_instance = OutputXlinkValid.from_json(json)
# print the JSON string representation of the object
print(OutputXlinkValid.to_json())

# convert the object into a dict
output_xlink_valid_dict = output_xlink_valid_instance.to_dict()
# create an instance of OutputXlinkValid from a dict
output_xlink_valid_from_dict = OutputXlinkValid.from_dict(output_xlink_valid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


