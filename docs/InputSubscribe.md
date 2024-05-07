# InputSubscribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**data** | **object** |  | 
**flag** | **bool** | If true, method will return the full transaction data, otherwise only the transaction hash | [default to False]
**subscription_name** | **str** | The type of event you want to subscribe to (i.e., newHeads, logs, newPendingTransactions) | 

## Example

```python
from openapi_client.models.input_subscribe import InputSubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of InputSubscribe from a JSON string
input_subscribe_instance = InputSubscribe.from_json(json)
# print the JSON string representation of the object
print InputSubscribe.to_json()

# convert the object into a dict
input_subscribe_dict = input_subscribe_instance.to_dict()
# create an instance of InputSubscribe from a dict
input_subscribe_form_dict = input_subscribe.from_dict(input_subscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


