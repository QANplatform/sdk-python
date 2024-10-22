# InputCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**block_number** | **str** |  | 
**transaction** | [**ParamsTransaction**](ParamsTransaction.md) | The transaction call object | 

## Example

```python
from qan.qan.input_call import InputCall

# TODO update the JSON string below
json = "{}"
# create an instance of InputCall from a JSON string
input_call_instance = InputCall.from_json(json)
# print the JSON string representation of the object
print(InputCall.to_json())

# convert the object into a dict
input_call_dict = input_call_instance.to_dict()
# create an instance of InputCall from a dict
input_call_from_dict = InputCall.from_dict(input_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


