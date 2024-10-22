# OutputCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**data** | **str** | The return value of the executed contract method | 

## Example

```python
from qan.qan.output_call import OutputCall

# TODO update the JSON string below
json = "{}"
# create an instance of OutputCall from a JSON string
output_call_instance = OutputCall.from_json(json)
# print the JSON string representation of the object
print(OutputCall.to_json())

# convert the object into a dict
output_call_dict = output_call_instance.to_dict()
# create an instance of OutputCall from a dict
output_call_from_dict = OutputCall.from_dict(output_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


