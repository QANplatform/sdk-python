# OutputAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**accounts** | **List[str]** | An array of addresses owned by the client | 

## Example

```python
from openapi_client.models.output_accounts import OutputAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of OutputAccounts from a JSON string
output_accounts_instance = OutputAccounts.from_json(json)
# print the JSON string representation of the object
print OutputAccounts.to_json()

# convert the object into a dict
output_accounts_dict = output_accounts_instance.to_dict()
# create an instance of OutputAccounts from a dict
output_accounts_form_dict = output_accounts.from_dict(output_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


