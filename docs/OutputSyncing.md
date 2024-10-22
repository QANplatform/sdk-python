# OutputSyncing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**sync_status** | [**SyncStatus**](SyncStatus.md) | Returns null when the node is fully synchronized, otherwise returns the sync status | 

## Example

```python
from qan.qan.output_syncing import OutputSyncing

# TODO update the JSON string below
json = "{}"
# create an instance of OutputSyncing from a JSON string
output_syncing_instance = OutputSyncing.from_json(json)
# print the JSON string representation of the object
print(OutputSyncing.to_json())

# convert the object into a dict
output_syncing_dict = output_syncing_instance.to_dict()
# create an instance of OutputSyncing from a dict
output_syncing_from_dict = OutputSyncing.from_dict(output_syncing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


