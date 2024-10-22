# OutputFeeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**base_fee_per_gas** | **List[str]** | An array of block base fees per gas. This includes the next block after the newest of the returned range, because this value can be derived from the newest block. Zeroes are returned for pre-EIP-1559 blocks | 
**gas_used_ratio** | **List[float]** | An array of block gas used ratios. These are calculated as the ratio of gasUsed and gasLimit | 
**oldest_block** | **str** | The lowest number block of the returned range encoded in decimal format | 
**reward** | **List[List[str]]** | An array of effective priority fees per gas data points from a single block. All zeroes are returned if the block is empty | 

## Example

```python
from qan.qan.output_fee_history import OutputFeeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of OutputFeeHistory from a JSON string
output_fee_history_instance = OutputFeeHistory.from_json(json)
# print the JSON string representation of the object
print(OutputFeeHistory.to_json())

# convert the object into a dict
output_fee_history_dict = output_fee_history_instance.to_dict()
# create an instance of OutputFeeHistory from a dict
output_fee_history_from_dict = OutputFeeHistory.from_dict(output_fee_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


