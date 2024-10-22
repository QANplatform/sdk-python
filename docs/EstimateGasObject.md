# EstimateGasObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **str** | Fake balance to set for the account before executing the call | [optional] 
**code** | **int** | Fake EVM bytecode to inject into the account before executing the call | [optional] 
**nonce** | **str** | Fake nonce to set for the account before executing the call | [optional] 
**state** | **str** | Fake key-value mapping to override all slots in the account storage before executing the call | [optional] 
**state_diff** | **str** | Fake key-value mapping to override individual slots in the account storage before executing the call | [optional] 

## Example

```python
from qan.qan.estimate_gas_object import EstimateGasObject

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateGasObject from a JSON string
estimate_gas_object_instance = EstimateGasObject.from_json(json)
# print the JSON string representation of the object
print(EstimateGasObject.to_json())

# convert the object into a dict
estimate_gas_object_dict = estimate_gas_object_instance.to_dict()
# create an instance of EstimateGasObject from a dict
estimate_gas_object_from_dict = EstimateGasObject.from_dict(estimate_gas_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


