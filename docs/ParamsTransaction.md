# ParamsTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The hash of the method signature and encoded parameters. For more information, see the Contract ABI description in the Solidity documentation. | [optional] 
**var_from** | **str** | The address from which the transaction is sent | [optional] 
**gas** | **str** | The integer of gas provided for the transaction execution | [optional] 
**gas_price** | **str** | The integer of gasPrice used for each paid gas encoded as hexadecimal | [optional] 
**to** | **str** | The address to which the transaction is addressed | 
**value** | **str** | The integer of value sent with this transaction encoded as hexadecimal | [optional] 

## Example

```python
from qan.qan.params_transaction import ParamsTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsTransaction from a JSON string
params_transaction_instance = ParamsTransaction.from_json(json)
# print the JSON string representation of the object
print(ParamsTransaction.to_json())

# convert the object into a dict
params_transaction_dict = params_transaction_instance.to_dict()
# create an instance of ParamsTransaction from a dict
params_transaction_from_dict = ParamsTransaction.from_dict(params_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


