# OutputGasPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**gas_price** | **str** | The decimal value of the current gas price in wei | 

## Example

```python
from qan.qan.output_gas_price import OutputGasPrice

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGasPrice from a JSON string
output_gas_price_instance = OutputGasPrice.from_json(json)
# print the JSON string representation of the object
print(OutputGasPrice.to_json())

# convert the object into a dict
output_gas_price_dict = output_gas_price_instance.to_dict()
# create an instance of OutputGasPrice from a dict
output_gas_price_from_dict = OutputGasPrice.from_dict(output_gas_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


