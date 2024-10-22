# ResponseWithdrawals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to which the withdrawn amount is sent | 
**amount** | **str** | The amount of value, provided in decimal format, corresponding to a certain value in gwei | 
**index** | **int** | The index of the withdrawal to uniquely identify each withdrawal | 
**validator_index** | **int** | The index of the validator who initiated the withdrawal | 

## Example

```python
from qan.qan.response_withdrawals import ResponseWithdrawals

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseWithdrawals from a JSON string
response_withdrawals_instance = ResponseWithdrawals.from_json(json)
# print the JSON string representation of the object
print(ResponseWithdrawals.to_json())

# convert the object into a dict
response_withdrawals_dict = response_withdrawals_instance.to_dict()
# create an instance of ResponseWithdrawals from a dict
response_withdrawals_from_dict = ResponseWithdrawals.from_dict(response_withdrawals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


