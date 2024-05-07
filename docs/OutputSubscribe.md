# OutputSubscribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**subscription_id** | **str** | The hex encoded subscription ID. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe | 

## Example

```python
from openapi_client.models.output_subscribe import OutputSubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of OutputSubscribe from a JSON string
output_subscribe_instance = OutputSubscribe.from_json(json)
# print the JSON string representation of the object
print OutputSubscribe.to_json()

# convert the object into a dict
output_subscribe_dict = output_subscribe_instance.to_dict()
# create an instance of OutputSubscribe from a dict
output_subscribe_form_dict = output_subscribe.from_dict(output_subscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


