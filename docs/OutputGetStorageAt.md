# OutputGetStorageAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**value** | **str** | The value from a storage position at a given address | 

## Example

```python
from qan.qan.output_get_storage_at import OutputGetStorageAt

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetStorageAt from a JSON string
output_get_storage_at_instance = OutputGetStorageAt.from_json(json)
# print the JSON string representation of the object
print(OutputGetStorageAt.to_json())

# convert the object into a dict
output_get_storage_at_dict = output_get_storage_at_instance.to_dict()
# create an instance of OutputGetStorageAt from a dict
output_get_storage_at_from_dict = OutputGetStorageAt.from_dict(output_get_storage_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


