# InputGetLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**address** | **str** | The contract address or a list of addresses from which logs should originate | [optional] 
**block_hash** | **str** | With the addition of EIP-234, blockHash is a new filter option that restricts the logs returned to the block number referenced in the blockHash. Using the blockHash field is equivalent to setting the fromBlock and toBlock to the block number the blockHash references. If blockHash is present in the filter criteria, neither fromBlock nor toBlock is allowed | [optional] 
**from_block** | **str** | The block number as a string in decimal format or tags. The supported tag values include earliest for the earliest/genesis block, latest for the latest mined block, pending for the pending state/transactions. | [optional] 
**to_block** | **str** | The block number as a string in decimal format or tags. The supported tag values include earliest for the earliest/genesis block, latest for the latest mined block, pending for the pending state/transactions. | [optional] 
**topics** | **List[str]** | An array of DATA topics and also, the topics are order-dependent. Visit this official page to learn more about topics | [optional] 

## Example

```python
from qan.qan.input_get_logs import InputGetLogs

# TODO update the JSON string below
json = "{}"
# create an instance of InputGetLogs from a JSON string
input_get_logs_instance = InputGetLogs.from_json(json)
# print the JSON string representation of the object
print(InputGetLogs.to_json())

# convert the object into a dict
input_get_logs_dict = input_get_logs_instance.to_dict()
# create an instance of InputGetLogs from a dict
input_get_logs_from_dict = InputGetLogs.from_dict(input_get_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


