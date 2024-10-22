# OutputGetBlockReceipts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**transaction_receipts** | [**List[ResponseTransactionReceipt]**](ResponseTransactionReceipt.md) | An array of transaction receipt objects | 

## Example

```python
from qan.qan.output_get_block_receipts import OutputGetBlockReceipts

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetBlockReceipts from a JSON string
output_get_block_receipts_instance = OutputGetBlockReceipts.from_json(json)
# print the JSON string representation of the object
print(OutputGetBlockReceipts.to_json())

# convert the object into a dict
output_get_block_receipts_dict = output_get_block_receipts_instance.to_dict()
# create an instance of OutputGetBlockReceipts from a dict
output_get_block_receipts_from_dict = OutputGetBlockReceipts.from_dict(output_get_block_receipts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


