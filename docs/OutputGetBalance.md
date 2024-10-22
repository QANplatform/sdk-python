# OutputGetBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**balance** | **str** | The balance of the specified address in decimal value, measured in wei | 

## Example

```python
from qan.qan.output_get_balance import OutputGetBalance

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetBalance from a JSON string
output_get_balance_instance = OutputGetBalance.from_json(json)
# print the JSON string representation of the object
print(OutputGetBalance.to_json())

# convert the object into a dict
output_get_balance_dict = output_get_balance_instance.to_dict()
# create an instance of OutputGetBalance from a dict
output_get_balance_from_dict = OutputGetBalance.from_dict(output_get_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


