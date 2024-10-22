# OutputGetCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**bytecode** | **str** | The bytecode from a given address | 

## Example

```python
from qan.qan.output_get_code import OutputGetCode

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetCode from a JSON string
output_get_code_instance = OutputGetCode.from_json(json)
# print the JSON string representation of the object
print(OutputGetCode.to_json())

# convert the object into a dict
output_get_code_dict = output_get_code_instance.to_dict()
# create an instance of OutputGetCode from a dict
output_get_code_from_dict = OutputGetCode.from_dict(output_get_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


