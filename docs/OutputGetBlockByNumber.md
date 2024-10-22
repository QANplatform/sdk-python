# OutputGetBlockByNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**block** | [**ResponseBlock**](ResponseBlock.md) | A block object, or null when no block was found | 

## Example

```python
from qan.qan.output_get_block_by_number import OutputGetBlockByNumber

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetBlockByNumber from a JSON string
output_get_block_by_number_instance = OutputGetBlockByNumber.from_json(json)
# print the JSON string representation of the object
print(OutputGetBlockByNumber.to_json())

# convert the object into a dict
output_get_block_by_number_dict = output_get_block_by_number_instance.to_dict()
# create an instance of OutputGetBlockByNumber from a dict
output_get_block_by_number_from_dict = OutputGetBlockByNumber.from_dict(output_get_block_by_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


