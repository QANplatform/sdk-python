# InputEstimateGas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**object** | [**EstimateGasObject**](EstimateGasObject.md) | The state override set with address-to-state mapping where each address maps to an object containing | [optional] 
**transaction** | [**ParamsTransaction**](ParamsTransaction.md) | The transaction call object | 

## Example

```python
from qan.qan.input_estimate_gas import InputEstimateGas

# TODO update the JSON string below
json = "{}"
# create an instance of InputEstimateGas from a JSON string
input_estimate_gas_instance = InputEstimateGas.from_json(json)
# print the JSON string representation of the object
print(InputEstimateGas.to_json())

# convert the object into a dict
input_estimate_gas_dict = input_estimate_gas_instance.to_dict()
# create an instance of InputEstimateGas from a dict
input_estimate_gas_from_dict = InputEstimateGas.from_dict(input_estimate_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


