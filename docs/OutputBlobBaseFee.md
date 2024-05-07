# OutputBlobBaseFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**base_fee** | **str** | The expected base fee in wei, represented in decimal format | 

## Example

```python
from openapi_client.models.output_blob_base_fee import OutputBlobBaseFee

# TODO update the JSON string below
json = "{}"
# create an instance of OutputBlobBaseFee from a JSON string
output_blob_base_fee_instance = OutputBlobBaseFee.from_json(json)
# print the JSON string representation of the object
print OutputBlobBaseFee.to_json()

# convert the object into a dict
output_blob_base_fee_dict = output_blob_base_fee_instance.to_dict()
# create an instance of OutputBlobBaseFee from a dict
output_blob_base_fee_form_dict = output_blob_base_fee.from_dict(output_blob_base_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


