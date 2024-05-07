# OutputGetAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**balance** | **str** | The current balance of the account in wei | 
**code_hash** | **str** | A 32 byte hash of the code of the account | 
**nonce** | **str** | The transaction count of an account | 
**storage_root** | **str** | The hash of the account&#39;s storage data | 

## Example

```python
from openapi_client.models.output_get_account import OutputGetAccount

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetAccount from a JSON string
output_get_account_instance = OutputGetAccount.from_json(json)
# print the JSON string representation of the object
print OutputGetAccount.to_json()

# convert the object into a dict
output_get_account_dict = output_get_account_instance.to_dict()
# create an instance of OutputGetAccount from a dict
output_get_account_form_dict = output_get_account.from_dict(output_get_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


