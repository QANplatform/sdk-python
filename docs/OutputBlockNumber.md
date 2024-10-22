# OutputBlockNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**block_number** | **str** | An integer value of the latest block number encoded as decimal | 

## Example

```python
from qan.qan.output_block_number import OutputBlockNumber

# TODO update the JSON string below
json = "{}"
# create an instance of OutputBlockNumber from a JSON string
output_block_number_instance = OutputBlockNumber.from_json(json)
# print the JSON string representation of the object
print(OutputBlockNumber.to_json())

# convert the object into a dict
output_block_number_dict = output_block_number_instance.to_dict()
# create an instance of OutputBlockNumber from a dict
output_block_number_from_dict = OutputBlockNumber.from_dict(output_block_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


