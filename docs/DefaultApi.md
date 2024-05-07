# openapi_client.DefaultApi

All URIs are relative to *https://rpc-testnet.qanplatform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qan_accounts**](DefaultApi.md#qan_accounts) | **GET** /accounts/ | 
[**qan_blob_base_fee**](DefaultApi.md#qan_blob_base_fee) | **GET** /blobBaseFee/ | 
[**qan_block_number**](DefaultApi.md#qan_block_number) | **GET** /blockNumber/ | 
[**qan_call**](DefaultApi.md#qan_call) | **POST** /call/ | 
[**qan_chain_id**](DefaultApi.md#qan_chain_id) | **GET** /chainId/ | 
[**qan_estimate_gas**](DefaultApi.md#qan_estimate_gas) | **POST** /estimateGas/ | 
[**qan_fee_history**](DefaultApi.md#qan_fee_history) | **POST** /feeHistory/ | 
[**qan_gas_price**](DefaultApi.md#qan_gas_price) | **GET** /gasPrice/ | 
[**qan_get_account**](DefaultApi.md#qan_get_account) | **GET** /getAccount/{Address}/{BlockReference}/ | 
[**qan_get_balance**](DefaultApi.md#qan_get_balance) | **GET** /getBalance/{Address}/ | 
[**qan_get_block_by_hash**](DefaultApi.md#qan_get_block_by_hash) | **GET** /getBlockByHash/{Hash}/{TransactionDetailFlag}/ | 
[**qan_get_block_by_number**](DefaultApi.md#qan_get_block_by_number) | **GET** /getBlockByNumber/{BlockNumber}/{TransactionDetailFlag}/ | 
[**qan_get_block_receipts**](DefaultApi.md#qan_get_block_receipts) | **GET** /getBlockReceipts/{BlockNumber}/ | 
[**qan_get_block_transaction_count_by_hash**](DefaultApi.md#qan_get_block_transaction_count_by_hash) | **GET** /getBlockTransactionCountByHash/{Hash}/ | 
[**qan_get_block_transaction_count_by_number**](DefaultApi.md#qan_get_block_transaction_count_by_number) | **GET** /getBlockTransactionCountByNumber/{BlockNumber}/ | 
[**qan_get_code**](DefaultApi.md#qan_get_code) | **GET** /getCode/{Address}/ | 
[**qan_get_filter_changes**](DefaultApi.md#qan_get_filter_changes) | **GET** /getFilterChanges/{FilterId}/ | 
[**qan_get_filter_logs**](DefaultApi.md#qan_get_filter_logs) | **GET** /getFilterLogs/{Id}/ | 
[**qan_get_logs**](DefaultApi.md#qan_get_logs) | **POST** /getLogs/ | 
[**qan_get_proof**](DefaultApi.md#qan_get_proof) | **POST** /getProof/ | 
[**qan_get_storage_at**](DefaultApi.md#qan_get_storage_at) | **POST** /getStorageAt/ | 
[**qan_get_transaction_by_block_hash_and_index**](DefaultApi.md#qan_get_transaction_by_block_hash_and_index) | **GET** /getTransactionByBlockHashAndIndex/{blockHash}/{index}/ | 
[**qan_get_transaction_by_block_number_and_index**](DefaultApi.md#qan_get_transaction_by_block_number_and_index) | **GET** /getTransactionByBlockNumberAndIndex/{blockNumber}/{index}/ | 
[**qan_get_transaction_by_hash**](DefaultApi.md#qan_get_transaction_by_hash) | **GET** /getTransactionByHash/{hash}/ | 
[**qan_get_transaction_count**](DefaultApi.md#qan_get_transaction_count) | **GET** /getTransactionCount/{Address}/{BlockNumber}/ | 
[**qan_get_transaction_receipt**](DefaultApi.md#qan_get_transaction_receipt) | **GET** /getTransactionReceipt/{Hash}/ | 
[**qan_get_uncle_count_by_block_hash**](DefaultApi.md#qan_get_uncle_count_by_block_hash) | **GET** /getUncleCountByBlockHash/{Hash}/ | 
[**qan_get_uncle_count_by_block_number**](DefaultApi.md#qan_get_uncle_count_by_block_number) | **GET** /getUncleCountByBlockNumber/{BlockNumber}/ | 
[**qan_max_priority_fee_per_gas**](DefaultApi.md#qan_max_priority_fee_per_gas) | **GET** /maxPriorityFeePerGas/ | 
[**qan_new_block_filter**](DefaultApi.md#qan_new_block_filter) | **GET** /newBlockFilter/ | 
[**qan_new_filter**](DefaultApi.md#qan_new_filter) | **POST** /newFilter/ | 
[**qan_new_pending_transaction_filter**](DefaultApi.md#qan_new_pending_transaction_filter) | **GET** /newPendingTransactionFilter/ | 
[**qan_send_raw_transaction**](DefaultApi.md#qan_send_raw_transaction) | **POST** /sendRawTransaction/ | 
[**qan_subscribe**](DefaultApi.md#qan_subscribe) | **POST** /subscribe/ | 
[**qan_syncing**](DefaultApi.md#qan_syncing) | **GET** /syncing/ | 
[**qan_uninstall_filter**](DefaultApi.md#qan_uninstall_filter) | **GET** /uninstallFilter/{FilterId}/ | 
[**qan_unsubscribe**](DefaultApi.md#qan_unsubscribe) | **GET** /unsubscribe/{SubscriptionId}/ | 
[**qan_xlink_valid**](DefaultApi.md#qan_xlink_valid) | **GET** /xlinkValid/ | 


# **qan_accounts**
> OutputAccounts qan_accounts()



Returns a list of addresses owned by client.

### Example


```python
import openapi_client
from openapi_client.models.output_accounts import OutputAccounts
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_accounts()
        print("The response of DefaultApi->qan_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputAccounts**](OutputAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_blob_base_fee**
> OutputBlobBaseFee qan_blob_base_fee()



Returns the expected base fee for blobs in the next block.

### Example


```python
import openapi_client
from openapi_client.models.output_blob_base_fee import OutputBlobBaseFee
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_blob_base_fee()
        print("The response of DefaultApi->qan_blob_base_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_blob_base_fee: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputBlobBaseFee**](OutputBlobBaseFee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_block_number**
> OutputBlockNumber qan_block_number()



Returns the latest block number of the blockchain.

### Example


```python
import openapi_client
from openapi_client.models.output_block_number import OutputBlockNumber
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_block_number()
        print("The response of DefaultApi->qan_block_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_block_number: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputBlockNumber**](OutputBlockNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_call**
> OutputCall qan_call(input_call)



Executes a new message call immediately without creating a transaction on the block chain.

### Example


```python
import openapi_client
from openapi_client.models.input_call import InputCall
from openapi_client.models.output_call import OutputCall
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_call = openapi_client.InputCall() # InputCall | 

    try:
        api_response = api_instance.qan_call(input_call)
        print("The response of DefaultApi->qan_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_call** | [**InputCall**](InputCall.md)|  | 

### Return type

[**OutputCall**](OutputCall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_chain_id**
> OutputChainId qan_chain_id()



Returns the current network/chain ID, used to sign replay-protected transaction introduced in EIP-155.

### Example


```python
import openapi_client
from openapi_client.models.output_chain_id import OutputChainId
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_chain_id()
        print("The response of DefaultApi->qan_chain_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_chain_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputChainId**](OutputChainId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_estimate_gas**
> OutputEstimateGas qan_estimate_gas(input_estimate_gas)



Returns an estimation of gas for a given transaction.

### Example


```python
import openapi_client
from openapi_client.models.input_estimate_gas import InputEstimateGas
from openapi_client.models.output_estimate_gas import OutputEstimateGas
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_estimate_gas = openapi_client.InputEstimateGas() # InputEstimateGas | 

    try:
        api_response = api_instance.qan_estimate_gas(input_estimate_gas)
        print("The response of DefaultApi->qan_estimate_gas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_estimate_gas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_estimate_gas** | [**InputEstimateGas**](InputEstimateGas.md)|  | 

### Return type

[**OutputEstimateGas**](OutputEstimateGas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_fee_history**
> OutputFeeHistory qan_fee_history(input_fee_history)



Returns the collection of historical gas information.

### Example


```python
import openapi_client
from openapi_client.models.input_fee_history import InputFeeHistory
from openapi_client.models.output_fee_history import OutputFeeHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_fee_history = openapi_client.InputFeeHistory() # InputFeeHistory | 

    try:
        api_response = api_instance.qan_fee_history(input_fee_history)
        print("The response of DefaultApi->qan_fee_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_fee_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_fee_history** | [**InputFeeHistory**](InputFeeHistory.md)|  | 

### Return type

[**OutputFeeHistory**](OutputFeeHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_gas_price**
> OutputGasPrice qan_gas_price()



Returns the current gas price on the network in wei.

### Example


```python
import openapi_client
from openapi_client.models.output_gas_price import OutputGasPrice
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_gas_price()
        print("The response of DefaultApi->qan_gas_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_gas_price: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputGasPrice**](OutputGasPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_account**
> OutputGetAccount qan_get_account(address, block_reference)



Retrieves account details by specifying an address and a block number/tag.

### Example


```python
import openapi_client
from openapi_client.models.output_get_account import OutputGetAccount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | The account address for which the information is to be retrieved
    block_reference = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation

    try:
        api_response = api_instance.qan_get_account(address, block_reference)
        print("The response of DefaultApi->qan_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The account address for which the information is to be retrieved | 
 **block_reference** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | 

### Return type

[**OutputGetAccount**](OutputGetAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_balance**
> OutputGetBalance qan_get_balance(address, block_number=block_number)



Returns the balance of the account of given address.

### Example


```python
import openapi_client
from openapi_client.models.output_get_balance import OutputGetBalance
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | A 20 bytes long hexadecimal value representing an Ethereum address
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation (optional) (default to 'latest')

    try:
        api_response = api_instance.qan_get_balance(address, block_number=block_number)
        print("The response of DefaultApi->qan_get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| A 20 bytes long hexadecimal value representing an Ethereum address | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | [optional] [default to &#39;latest&#39;]

### Return type

[**OutputGetBalance**](OutputGetBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_block_by_hash**
> OutputGetBlockByHash qan_get_block_by_hash(hash, transaction_detail_flag)



Returns information of the block matching the given block hash.

### Example


```python
import openapi_client
from openapi_client.models.output_get_block_by_hash import OutputGetBlockByHash
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash (32 bytes) of the block
    transaction_detail_flag = False # bool | The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions (default to False)

    try:
        api_response = api_instance.qan_get_block_by_hash(hash, transaction_detail_flag)
        print("The response of DefaultApi->qan_get_block_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_block_by_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| The hash (32 bytes) of the block | 
 **transaction_detail_flag** | **bool**| The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions | [default to False]

### Return type

[**OutputGetBlockByHash**](OutputGetBlockByHash.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_block_by_number**
> OutputGetBlockByNumber qan_get_block_by_number(block_number, transaction_detail_flag)



Returns information of the block matching the given block number.

### Example


```python
import openapi_client
from openapi_client.models.output_get_block_by_number import OutputGetBlockByNumber
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation (default to 'latest')
    transaction_detail_flag = False # bool | The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions (default to False)

    try:
        api_response = api_instance.qan_get_block_by_number(block_number, transaction_detail_flag)
        print("The response of DefaultApi->qan_get_block_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_block_by_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | [default to &#39;latest&#39;]
 **transaction_detail_flag** | **bool**| The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions | [default to False]

### Return type

[**OutputGetBlockByNumber**](OutputGetBlockByNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_block_receipts**
> OutputGetBlockReceipts qan_get_block_receipts(block_number)



Returns all transaction receipts for a given block.

### Example


```python
import openapi_client
from openapi_client.models.output_get_block_receipts import OutputGetBlockReceipts
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation (default to 'latest')

    try:
        api_response = api_instance.qan_get_block_receipts(block_number)
        print("The response of DefaultApi->qan_get_block_receipts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_block_receipts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | [default to &#39;latest&#39;]

### Return type

[**OutputGetBlockReceipts**](OutputGetBlockReceipts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_block_transaction_count_by_hash**
> OutputGetBlockTransactionCountByHash qan_get_block_transaction_count_by_hash(hash)



Returns the number of transactions for the block matching the given block hash.

### Example


```python
import openapi_client
from openapi_client.models.output_get_block_transaction_count_by_hash import OutputGetBlockTransactionCountByHash
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash of the block

    try:
        api_response = api_instance.qan_get_block_transaction_count_by_hash(hash)
        print("The response of DefaultApi->qan_get_block_transaction_count_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_block_transaction_count_by_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| The hash of the block | 

### Return type

[**OutputGetBlockTransactionCountByHash**](OutputGetBlockTransactionCountByHash.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_block_transaction_count_by_number**
> OutputGetBlockTransactionCountByNumber qan_get_block_transaction_count_by_number(block_number)



Returns the number of transactions for the block matching the given block number.

### Example


```python
import openapi_client
from openapi_client.models.output_get_block_transaction_count_by_number import OutputGetBlockTransactionCountByNumber
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation

    try:
        api_response = api_instance.qan_get_block_transaction_count_by_number(block_number)
        print("The response of DefaultApi->qan_get_block_transaction_count_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_block_transaction_count_by_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | 

### Return type

[**OutputGetBlockTransactionCountByNumber**](OutputGetBlockTransactionCountByNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_code**
> OutputGetCode qan_get_code(address, block_number=block_number)



Returns the compiled bytecode of a smart contract.

### Example


```python
import openapi_client
from openapi_client.models.output_get_code import OutputGetCode
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | The address of the smart contract from which the bytecode will be obtained
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation (optional) (default to 'latest')

    try:
        api_response = api_instance.qan_get_code(address, block_number=block_number)
        print("The response of DefaultApi->qan_get_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the smart contract from which the bytecode will be obtained | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | [optional] [default to &#39;latest&#39;]

### Return type

[**OutputGetCode**](OutputGetCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_filter_changes**
> OutputGetFilterChanges qan_get_filter_changes(filter_id)



Polling method for a filter, which returns an array of events that have occurred since the last poll.

### Example


```python
import openapi_client
from openapi_client.models.output_get_filter_changes import OutputGetFilterChanges
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    filter_id = 'filter_id_example' # str | The filter id that is returned from eth_newFilter, eth_newBlockFilter or eth_newPendingTransactionFilter

    try:
        api_response = api_instance.qan_get_filter_changes(filter_id)
        print("The response of DefaultApi->qan_get_filter_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_filter_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The filter id that is returned from eth_newFilter, eth_newBlockFilter or eth_newPendingTransactionFilter | 

### Return type

[**OutputGetFilterChanges**](OutputGetFilterChanges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_filter_logs**
> OutputGetFilterLogs qan_get_filter_logs(id)



Returns an array of all logs matching filter with given id.

### Example


```python
import openapi_client
from openapi_client.models.output_get_filter_logs import OutputGetFilterLogs
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | The filter ID

    try:
        api_response = api_instance.qan_get_filter_logs(id)
        print("The response of DefaultApi->qan_get_filter_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_filter_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The filter ID | 

### Return type

[**OutputGetFilterLogs**](OutputGetFilterLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_logs**
> OutputGetLogs qan_get_logs(input_get_logs)



Returns an array of all logs matching a given filter object.

### Example


```python
import openapi_client
from openapi_client.models.input_get_logs import InputGetLogs
from openapi_client.models.output_get_logs import OutputGetLogs
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_get_logs = openapi_client.InputGetLogs() # InputGetLogs | 

    try:
        api_response = api_instance.qan_get_logs(input_get_logs)
        print("The response of DefaultApi->qan_get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_get_logs** | [**InputGetLogs**](InputGetLogs.md)|  | 

### Return type

[**OutputGetLogs**](OutputGetLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_proof**
> OutputGetProof qan_get_proof(input_get_proof)



Returns the account and storage values of the specified account including the Merkle-proof.

### Example


```python
import openapi_client
from openapi_client.models.input_get_proof import InputGetProof
from openapi_client.models.output_get_proof import OutputGetProof
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_get_proof = openapi_client.InputGetProof() # InputGetProof | 

    try:
        api_response = api_instance.qan_get_proof(input_get_proof)
        print("The response of DefaultApi->qan_get_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_proof: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_get_proof** | [**InputGetProof**](InputGetProof.md)|  | 

### Return type

[**OutputGetProof**](OutputGetProof.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_storage_at**
> OutputGetStorageAt qan_get_storage_at(input_get_storage_at)



Returns the value from a storage position at a given address.

### Example


```python
import openapi_client
from openapi_client.models.input_get_storage_at import InputGetStorageAt
from openapi_client.models.output_get_storage_at import OutputGetStorageAt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_get_storage_at = openapi_client.InputGetStorageAt() # InputGetStorageAt | 

    try:
        api_response = api_instance.qan_get_storage_at(input_get_storage_at)
        print("The response of DefaultApi->qan_get_storage_at:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_storage_at: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_get_storage_at** | [**InputGetStorageAt**](InputGetStorageAt.md)|  | 

### Return type

[**OutputGetStorageAt**](OutputGetStorageAt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_transaction_by_block_hash_and_index**
> OutputGetTransactionByBlockHashAndIndex qan_get_transaction_by_block_hash_and_index(block_hash, index)



Returns information about a transaction given a blockhash and transaction index position.

### Example


```python
import openapi_client
from openapi_client.models.output_get_transaction_by_block_hash_and_index import OutputGetTransactionByBlockHashAndIndex
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | 
    index = '0' # str | An integer of the transaction index position

    try:
        api_response = api_instance.qan_get_transaction_by_block_hash_and_index(block_hash, index)
        print("The response of DefaultApi->qan_get_transaction_by_block_hash_and_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_transaction_by_block_hash_and_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**|  | 
 **index** | **str**| An integer of the transaction index position | 

### Return type

[**OutputGetTransactionByBlockHashAndIndex**](OutputGetTransactionByBlockHashAndIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_transaction_by_block_number_and_index**
> OutputGetTransactionByBlockNumberAndIndex qan_get_transaction_by_block_number_and_index(block_number, index)



Returns information about a transaction given a block number and transaction index position.

### Example


```python
import openapi_client
from openapi_client.models.output_get_transaction_by_block_number_and_index import OutputGetTransactionByBlockNumberAndIndex
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation
    index = '0' # str | An integer of the transaction index position

    try:
        api_response = api_instance.qan_get_transaction_by_block_number_and_index(block_number, index)
        print("The response of DefaultApi->qan_get_transaction_by_block_number_and_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_transaction_by_block_number_and_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | 
 **index** | **str**| An integer of the transaction index position | 

### Return type

[**OutputGetTransactionByBlockNumberAndIndex**](OutputGetTransactionByBlockNumberAndIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_transaction_by_hash**
> OutputGetTransactionByHash qan_get_transaction_by_hash(hash)



Returns the information about a transaction from a transaction hash.

### Example


```python
import openapi_client
from openapi_client.models.output_get_transaction_by_hash import OutputGetTransactionByHash
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    hash = '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060' # str | The hash of a transaction

    try:
        api_response = api_instance.qan_get_transaction_by_hash(hash)
        print("The response of DefaultApi->qan_get_transaction_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_transaction_by_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| The hash of a transaction | 

### Return type

[**OutputGetTransactionByHash**](OutputGetTransactionByHash.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_transaction_count**
> OutputGetTransactionCount qan_get_transaction_count(address, block_number)



Returns the number of transactions sent from an address.

### Example


```python
import openapi_client
from openapi_client.models.output_get_transaction_count import OutputGetTransactionCount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | The address from which the transaction count to be checked
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation

    try:
        api_response = api_instance.qan_get_transaction_count(address, block_number)
        print("The response of DefaultApi->qan_get_transaction_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_transaction_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address from which the transaction count to be checked | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | 

### Return type

[**OutputGetTransactionCount**](OutputGetTransactionCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_transaction_receipt**
> OutputGetTransactionReceipt qan_get_transaction_receipt(hash)



Returns the receipt of a transaction by transaction hash.

### Example


```python
import openapi_client
from openapi_client.models.output_get_transaction_receipt import OutputGetTransactionReceipt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash of a transaction

    try:
        api_response = api_instance.qan_get_transaction_receipt(hash)
        print("The response of DefaultApi->qan_get_transaction_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_transaction_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| The hash of a transaction | 

### Return type

[**OutputGetTransactionReceipt**](OutputGetTransactionReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_uncle_count_by_block_hash**
> OutputGetUncleCountByBlockHash qan_get_uncle_count_by_block_hash(hash)



Returns the number of uncles for the block matching the given block hash.

### Example


```python
import openapi_client
from openapi_client.models.output_get_uncle_count_by_block_hash import OutputGetUncleCountByBlockHash
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    hash = '0x4e216c95f527e9ba0f1161a1c4609b893302c704f05a520da8141ca91878f63e' # str | The hash of the block to get uncles for

    try:
        api_response = api_instance.qan_get_uncle_count_by_block_hash(hash)
        print("The response of DefaultApi->qan_get_uncle_count_by_block_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_uncle_count_by_block_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| The hash of the block to get uncles for | 

### Return type

[**OutputGetUncleCountByBlockHash**](OutputGetUncleCountByBlockHash.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_get_uncle_count_by_block_number**
> OutputGetUncleCountByBlockNumber qan_get_uncle_count_by_block_number(block_number)



Returns the number of uncles for the block matching the given block number.

### Example


```python
import openapi_client
from openapi_client.models.output_get_uncle_count_by_block_number import OutputGetUncleCountByBlockNumber
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    block_number = '15537381' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation

    try:
        api_response = api_instance.qan_get_uncle_count_by_block_number(block_number)
        print("The response of DefaultApi->qan_get_uncle_count_by_block_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_get_uncle_count_by_block_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending, see the default block parameter description in the official Ethereum documentation | 

### Return type

[**OutputGetUncleCountByBlockNumber**](OutputGetUncleCountByBlockNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_max_priority_fee_per_gas**
> OutputMaxPriorityFeePerGas qan_max_priority_fee_per_gas()



Get the priority fee needed to be included in a block.

### Example


```python
import openapi_client
from openapi_client.models.output_max_priority_fee_per_gas import OutputMaxPriorityFeePerGas
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_max_priority_fee_per_gas()
        print("The response of DefaultApi->qan_max_priority_fee_per_gas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_max_priority_fee_per_gas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputMaxPriorityFeePerGas**](OutputMaxPriorityFeePerGas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_new_block_filter**
> OutputNewBlockFilter qan_new_block_filter()



Creates a filter in the node, to notify when a new block arrives.

### Example


```python
import openapi_client
from openapi_client.models.output_new_block_filter import OutputNewBlockFilter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_new_block_filter()
        print("The response of DefaultApi->qan_new_block_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_new_block_filter: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputNewBlockFilter**](OutputNewBlockFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_new_filter**
> OutputNewFilter qan_new_filter(input_new_filter)



Creates a filter object, based on filter options, to notify when the state changes (logs).

### Example


```python
import openapi_client
from openapi_client.models.input_new_filter import InputNewFilter
from openapi_client.models.output_new_filter import OutputNewFilter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_new_filter = openapi_client.InputNewFilter() # InputNewFilter | 

    try:
        api_response = api_instance.qan_new_filter(input_new_filter)
        print("The response of DefaultApi->qan_new_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_new_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_new_filter** | [**InputNewFilter**](InputNewFilter.md)|  | 

### Return type

[**OutputNewFilter**](OutputNewFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_new_pending_transaction_filter**
> OutputNewPendingTransactionFilter qan_new_pending_transaction_filter()



Creates a filter in the node to notify when new pending transactions arrive.

### Example


```python
import openapi_client
from openapi_client.models.output_new_pending_transaction_filter import OutputNewPendingTransactionFilter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_new_pending_transaction_filter()
        print("The response of DefaultApi->qan_new_pending_transaction_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_new_pending_transaction_filter: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputNewPendingTransactionFilter**](OutputNewPendingTransactionFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_send_raw_transaction**
> OutputSendRawTransaction qan_send_raw_transaction(input_send_raw_transaction)



Creates new message call transaction or a contract creation for signed transactions.

### Example


```python
import openapi_client
from openapi_client.models.input_send_raw_transaction import InputSendRawTransaction
from openapi_client.models.output_send_raw_transaction import OutputSendRawTransaction
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_send_raw_transaction = openapi_client.InputSendRawTransaction() # InputSendRawTransaction | 

    try:
        api_response = api_instance.qan_send_raw_transaction(input_send_raw_transaction)
        print("The response of DefaultApi->qan_send_raw_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_send_raw_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_send_raw_transaction** | [**InputSendRawTransaction**](InputSendRawTransaction.md)|  | 

### Return type

[**OutputSendRawTransaction**](OutputSendRawTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_subscribe**
> OutputSubscribe qan_subscribe(input_subscribe)



Starts a subscription to a specific event.

### Example


```python
import openapi_client
from openapi_client.models.input_subscribe import InputSubscribe
from openapi_client.models.output_subscribe import OutputSubscribe
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    input_subscribe = openapi_client.InputSubscribe() # InputSubscribe | 

    try:
        api_response = api_instance.qan_subscribe(input_subscribe)
        print("The response of DefaultApi->qan_subscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_subscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_subscribe** | [**InputSubscribe**](InputSubscribe.md)|  | 

### Return type

[**OutputSubscribe**](OutputSubscribe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_syncing**
> OutputSyncing qan_syncing()



Returns an object with the sync status of the node if the node is out-of-sync and is syncing. Returns null when the node is already in sync.

### Example


```python
import openapi_client
from openapi_client.models.output_syncing import OutputSyncing
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_syncing()
        print("The response of DefaultApi->qan_syncing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_syncing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutputSyncing**](OutputSyncing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_uninstall_filter**
> OutputUninstallFilter qan_uninstall_filter(filter_id)



Uninstalls a filter with the given filter id.

### Example


```python
import openapi_client
from openapi_client.models.output_uninstall_filter import OutputUninstallFilter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    filter_id = 'filter_id_example' # str | The filter ID that needs to be uninstalled. It should always be called when watch is no longer needed. Additionally, Filters timeout when they aren't requested with eth_getFilterChanges for a period of time

    try:
        api_response = api_instance.qan_uninstall_filter(filter_id)
        print("The response of DefaultApi->qan_uninstall_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_uninstall_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The filter ID that needs to be uninstalled. It should always be called when watch is no longer needed. Additionally, Filters timeout when they aren&#39;t requested with eth_getFilterChanges for a period of time | 

### Return type

[**OutputUninstallFilter**](OutputUninstallFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_unsubscribe**
> OutputUnsubscribe qan_unsubscribe(subscription_id)



Cancels an existing subscription so that no further events are sent.

### Example


```python
import openapi_client
from openapi_client.models.output_unsubscribe import OutputUnsubscribe
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    subscription_id = 'subscription_id_example' # str | A subscription ID that was previously generated in a eth_subscribe RPC request

    try:
        api_response = api_instance.qan_unsubscribe(subscription_id)
        print("The response of DefaultApi->qan_unsubscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_unsubscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A subscription ID that was previously generated in a eth_subscribe RPC request | 

### Return type

[**OutputUnsubscribe**](OutputUnsubscribe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qan_xlink_valid**
> QanXlinkValidResponse qan_xlink_valid()



### Example


```python
import openapi_client
from openapi_client.models.qan_xlink_valid_response import QanXlinkValidResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.qan_xlink_valid()
        print("The response of DefaultApi->qan_xlink_valid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->qan_xlink_valid: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QanXlinkValidResponse**](QanXlinkValidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

