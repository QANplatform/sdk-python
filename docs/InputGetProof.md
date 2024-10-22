# InputGetProof


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**address** | **str** |  | 
**block_number** | **str** |  | [optional] [default to 'latest']
**storage_keys** | **List[str]** | An array of storage-keys that should be proofed and included | 

## Example

```python
from qan.qan.input_get_proof import InputGetProof

# TODO update the JSON string below
json = "{}"
# create an instance of InputGetProof from a JSON string
input_get_proof_instance = InputGetProof.from_json(json)
# print the JSON string representation of the object
print(InputGetProof.to_json())

# convert the object into a dict
input_get_proof_dict = input_get_proof_instance.to_dict()
# create an instance of InputGetProof from a dict
input_get_proof_from_dict = InputGetProof.from_dict(input_get_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


