# OutputChainId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**chain_id** | **str** | A decimal value in string format which represents an integer of the chain ID | 

## Example

```python
from qan.qan.output_chain_id import OutputChainId

# TODO update the JSON string below
json = "{}"
# create an instance of OutputChainId from a JSON string
output_chain_id_instance = OutputChainId.from_json(json)
# print the JSON string representation of the object
print(OutputChainId.to_json())

# convert the object into a dict
output_chain_id_dict = output_chain_id_instance.to_dict()
# create an instance of OutputChainId from a dict
output_chain_id_from_dict = OutputChainId.from_dict(output_chain_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


