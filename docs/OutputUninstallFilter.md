# OutputUninstallFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**result** | **bool** | Returns true if the filter was successfully uninstalled, otherwise false | 

## Example

```python
from qan.qan.output_uninstall_filter import OutputUninstallFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OutputUninstallFilter from a JSON string
output_uninstall_filter_instance = OutputUninstallFilter.from_json(json)
# print the JSON string representation of the object
print(OutputUninstallFilter.to_json())

# convert the object into a dict
output_uninstall_filter_dict = output_uninstall_filter_instance.to_dict()
# create an instance of OutputUninstallFilter from a dict
output_uninstall_filter_from_dict = OutputUninstallFilter.from_dict(output_uninstall_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


