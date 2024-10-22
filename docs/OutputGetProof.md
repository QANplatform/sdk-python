# OutputGetProof


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**account_proof** | **str** | An array of rlp-serialized MerkleTree-Nodes which starts with the stateRoot-Node and follows the path of the SHA3 address as key | 
**address** | **str** | The address associated with the account | 
**balance** | **str** | The current balance of the account in wei | 
**code_hash** | **str** | A 32 byte hash of the code of the account | 
**nonce** | **str** | The hash of the generated proof-of-work. Null if pending | 
**storage_hash** | **str** | A 32 byte SHA3 of the storageRoot. All storage will deliver a MerkleProof starting with this rootHash | 
**storage_proof** | [**List[ResponseStorageEntry]**](ResponseStorageEntry.md) | An array of storage-entries as requested. Each entry is an object with the following fields: | 

## Example

```python
from qan.qan.output_get_proof import OutputGetProof

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetProof from a JSON string
output_get_proof_instance = OutputGetProof.from_json(json)
# print the JSON string representation of the object
print(OutputGetProof.to_json())

# convert the object into a dict
output_get_proof_dict = output_get_proof_instance.to_dict()
# create an instance of OutputGetProof from a dict
output_get_proof_from_dict = OutputGetProof.from_dict(output_get_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


