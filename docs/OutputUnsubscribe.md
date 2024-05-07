# OutputUnsubscribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**result** | **bool** | A boolean value indicating if the subscription was canceled successfully | 

## Example

```python
from openapi_client.models.output_unsubscribe import OutputUnsubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of OutputUnsubscribe from a JSON string
output_unsubscribe_instance = OutputUnsubscribe.from_json(json)
# print the JSON string representation of the object
print OutputUnsubscribe.to_json()

# convert the object into a dict
output_unsubscribe_dict = output_unsubscribe_instance.to_dict()
# create an instance of OutputUnsubscribe from a dict
output_unsubscribe_form_dict = output_unsubscribe.from_dict(output_unsubscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


