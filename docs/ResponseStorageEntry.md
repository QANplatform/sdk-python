# ResponseStorageEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The requested storage key | 
**proof** | **str** | An array of rlp-serialized MerkleTree-Nodes which starts with the stateRoot-Node and follows the path of the SHA3 address as key | 
**value** | **str** | The storage value | 

## Example

```python
from qan.qan.response_storage_entry import ResponseStorageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseStorageEntry from a JSON string
response_storage_entry_instance = ResponseStorageEntry.from_json(json)
# print the JSON string representation of the object
print(ResponseStorageEntry.to_json())

# convert the object into a dict
response_storage_entry_dict = response_storage_entry_instance.to_dict()
# create an instance of ResponseStorageEntry from a dict
response_storage_entry_from_dict = ResponseStorageEntry.from_dict(response_storage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


