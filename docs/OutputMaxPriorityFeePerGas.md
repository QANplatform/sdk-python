# OutputMaxPriorityFeePerGas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**max_priority_fee_per_gas** | **str** | The hex value of the priority fee needed to be included in a block | 

## Example

```python
from qan.qan.output_max_priority_fee_per_gas import OutputMaxPriorityFeePerGas

# TODO update the JSON string below
json = "{}"
# create an instance of OutputMaxPriorityFeePerGas from a JSON string
output_max_priority_fee_per_gas_instance = OutputMaxPriorityFeePerGas.from_json(json)
# print the JSON string representation of the object
print(OutputMaxPriorityFeePerGas.to_json())

# convert the object into a dict
output_max_priority_fee_per_gas_dict = output_max_priority_fee_per_gas_instance.to_dict()
# create an instance of OutputMaxPriorityFeePerGas from a dict
output_max_priority_fee_per_gas_from_dict = OutputMaxPriorityFeePerGas.from_dict(output_max_priority_fee_per_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


