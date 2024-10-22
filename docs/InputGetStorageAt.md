# InputGetStorageAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**address** | **str** | The address to check for storage | 
**block_number** | **str** |  | 
**position** | **str** | The integer of the position in storage | 

## Example

```python
from qan.qan.input_get_storage_at import InputGetStorageAt

# TODO update the JSON string below
json = "{}"
# create an instance of InputGetStorageAt from a JSON string
input_get_storage_at_instance = InputGetStorageAt.from_json(json)
# print the JSON string representation of the object
print(InputGetStorageAt.to_json())

# convert the object into a dict
input_get_storage_at_dict = input_get_storage_at_instance.to_dict()
# create an instance of InputGetStorageAt from a dict
input_get_storage_at_from_dict = InputGetStorageAt.from_dict(input_get_storage_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


