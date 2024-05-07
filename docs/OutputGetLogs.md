# OutputGetLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**logs** | [**List[ResponseLog]**](ResponseLog.md) | An array of log objects, or an empty array if nothing has changed since last poll | 

## Example

```python
from openapi_client.models.output_get_logs import OutputGetLogs

# TODO update the JSON string below
json = "{}"
# create an instance of OutputGetLogs from a JSON string
output_get_logs_instance = OutputGetLogs.from_json(json)
# print the JSON string representation of the object
print OutputGetLogs.to_json()

# convert the object into a dict
output_get_logs_dict = output_get_logs_instance.to_dict()
# create an instance of OutputGetLogs from a dict
output_get_logs_form_dict = output_get_logs.from_dict(output_get_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


