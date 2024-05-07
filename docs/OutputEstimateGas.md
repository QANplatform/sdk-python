# OutputEstimateGas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**estimated_gas** | **str** | The estimated amount of gas used | 

## Example

```python
from openapi_client.models.output_estimate_gas import OutputEstimateGas

# TODO update the JSON string below
json = "{}"
# create an instance of OutputEstimateGas from a JSON string
output_estimate_gas_instance = OutputEstimateGas.from_json(json)
# print the JSON string representation of the object
print OutputEstimateGas.to_json()

# convert the object into a dict
output_estimate_gas_dict = output_estimate_gas_instance.to_dict()
# create an instance of OutputEstimateGas from a dict
output_estimate_gas_form_dict = output_estimate_gas.from_dict(output_estimate_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


