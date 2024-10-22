# qan.QANApi

All URIs are relative to *https://rpc-testnet.qanplatform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qan_block_number**](QANApi.md#qan_block_number) | **GET** /blockNumber/ | Returns the latest block number of the blockchain.
[**qan_call**](QANApi.md#qan_call) | **POST** /call/ | Executes a new message call immediately without creating a transaction on the block chain.
[**qan_chain_id**](QANApi.md#qan_chain_id) | **GET** /chainId/ | Returns the current network/chain ID, used to sign replay-protected transaction introduced in EIP-155.
[**qan_estimate_gas**](QANApi.md#qan_estimate_gas) | **POST** /estimateGas/ | Returns an estimation of gas for a given transaction.
[**qan_fee_history**](QANApi.md#qan_fee_history) | **POST** /feeHistory/ | Returns the collection of historical gas information.
[**qan_gas_price**](QANApi.md#qan_gas_price) | **GET** /gasPrice/ | Returns the current gas price on the network in wei.
[**qan_get_balance**](QANApi.md#qan_get_balance) | **GET** /getBalance/{Address}/ | Returns the balance of the account of given address.
[**qan_get_block_by_hash**](QANApi.md#qan_get_block_by_hash) | **GET** /getBlockByHash/{Hash}/{TransactionDetailFlag}/ | Returns information of the block matching the given block hash.
[**qan_get_block_by_number**](QANApi.md#qan_get_block_by_number) | **GET** /getBlockByNumber/{BlockNumber}/{TransactionDetailFlag}/ | Returns information of the block matching the given block number.
[**qan_get_block_receipts**](QANApi.md#qan_get_block_receipts) | **GET** /getBlockReceipts/{BlockNumber}/ | Returns all transaction receipts for a given block.
[**qan_get_block_transaction_count_by_hash**](QANApi.md#qan_get_block_transaction_count_by_hash) | **GET** /getBlockTransactionCountByHash/{Hash}/ | Returns the number of transactions for the block matching the given block hash.
[**qan_get_block_transaction_count_by_number**](QANApi.md#qan_get_block_transaction_count_by_number) | **GET** /getBlockTransactionCountByNumber/{BlockNumber}/ | Returns the number of transactions for the block matching the given block number.
[**qan_get_code**](QANApi.md#qan_get_code) | **GET** /getCode/{Address}/ | Returns the compiled bytecode of a smart contract.
[**qan_get_filter_changes**](QANApi.md#qan_get_filter_changes) | **GET** /getFilterChanges/{FilterId}/ | Polling method for a filter, which returns an array of events that have occurred since the last poll.
[**qan_get_filter_logs**](QANApi.md#qan_get_filter_logs) | **GET** /getFilterLogs/{Id}/ | Returns an array of all logs matching filter with given id.
[**qan_get_logs**](QANApi.md#qan_get_logs) | **POST** /getLogs/ | Returns an array of all logs matching a given filter object.
[**qan_get_proof**](QANApi.md#qan_get_proof) | **POST** /getProof/ | Returns the account and storage values of the specified account including the Merkle-proof.
[**qan_get_storage_at**](QANApi.md#qan_get_storage_at) | **POST** /getStorageAt/ | Returns the value from a storage position at a given address.
[**qan_get_transaction_by_block_hash_and_index**](QANApi.md#qan_get_transaction_by_block_hash_and_index) | **GET** /getTransactionByBlockHashAndIndex/{blockHash}/{index}/ | Returns information about a transaction given a blockhash and transaction index position.
[**qan_get_transaction_by_block_number_and_index**](QANApi.md#qan_get_transaction_by_block_number_and_index) | **GET** /getTransactionByBlockNumberAndIndex/{blockNumber}/{index}/ | Returns information about a transaction given a block number and transaction index position.
[**qan_get_transaction_by_hash**](QANApi.md#qan_get_transaction_by_hash) | **GET** /getTransactionByHash/{hash}/ | Returns the information about a transaction from a transaction hash.
[**qan_get_transaction_count**](QANApi.md#qan_get_transaction_count) | **GET** /getTransactionCount/{Address}/{BlockNumber}/ | Returns the number of transactions sent from an address.
[**qan_get_transaction_receipt**](QANApi.md#qan_get_transaction_receipt) | **GET** /getTransactionReceipt/{Hash}/ | Returns the receipt of a transaction by transaction hash.
[**qan_max_priority_fee_per_gas**](QANApi.md#qan_max_priority_fee_per_gas) | **GET** /maxPriorityFeePerGas/ | Get the priority fee needed to be included in a block.
[**qan_new_block_filter**](QANApi.md#qan_new_block_filter) | **GET** /newBlockFilter/ | Creates a filter in the node, to notify when a new block arrives.
[**qan_new_filter**](QANApi.md#qan_new_filter) | **POST** /newFilter/ | Creates a filter object, based on filter options, to notify when the state changes (logs).
[**qan_new_pending_transaction_filter**](QANApi.md#qan_new_pending_transaction_filter) | **GET** /newPendingTransactionFilter/ | Creates a filter in the node to notify when new pending transactions arrive.
[**qan_send_raw_transaction**](QANApi.md#qan_send_raw_transaction) | **POST** /sendRawTransaction/ | Creates new message call transaction or a contract creation for signed transactions.
[**qan_syncing**](QANApi.md#qan_syncing) | **GET** /syncing/ | Returns an object with the sync status of the node if the node is out-of-sync and is syncing. Returns null when the node is already in sync.
[**qan_uninstall_filter**](QANApi.md#qan_uninstall_filter) | **GET** /uninstallFilter/{FilterId}/ | Uninstalls a filter with the given filter id.
[**qan_xlink_valid**](QANApi.md#qan_xlink_valid) | **GET** /xlinkValid/{Address}/ | Returns the xlink validity time of the account of given address.


# **qan_block_number**
> OutputBlockNumber qan_block_number()

Returns the latest block number of the blockchain.

### Example


```python
import qan
from qan.models.output_block_number import OutputBlockNumber
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Returns the latest block number of the blockchain.
        api_response = api_instance.qan_block_number()
        print("The response of QANApi->qan_block_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_block_number: %s\n" % e)
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
import qan
from qan.models.input_call import InputCall
from qan.models.output_call import OutputCall
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_call = qan.InputCall() # InputCall | 

    try:
        # Executes a new message call immediately without creating a transaction on the block chain.
        api_response = api_instance.qan_call(input_call)
        print("The response of QANApi->qan_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_call: %s\n" % e)
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
import qan
from qan.models.output_chain_id import OutputChainId
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Returns the current network/chain ID, used to sign replay-protected transaction introduced in EIP-155.
        api_response = api_instance.qan_chain_id()
        print("The response of QANApi->qan_chain_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_chain_id: %s\n" % e)
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
import qan
from qan.models.input_estimate_gas import InputEstimateGas
from qan.models.output_estimate_gas import OutputEstimateGas
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_estimate_gas = qan.InputEstimateGas() # InputEstimateGas | 

    try:
        # Returns an estimation of gas for a given transaction.
        api_response = api_instance.qan_estimate_gas(input_estimate_gas)
        print("The response of QANApi->qan_estimate_gas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_estimate_gas: %s\n" % e)
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
import qan
from qan.models.input_fee_history import InputFeeHistory
from qan.models.output_fee_history import OutputFeeHistory
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_fee_history = qan.InputFeeHistory() # InputFeeHistory | 

    try:
        # Returns the collection of historical gas information.
        api_response = api_instance.qan_fee_history(input_fee_history)
        print("The response of QANApi->qan_fee_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_fee_history: %s\n" % e)
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
import qan
from qan.models.output_gas_price import OutputGasPrice
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Returns the current gas price on the network in wei.
        api_response = api_instance.qan_gas_price()
        print("The response of QANApi->qan_gas_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_gas_price: %s\n" % e)
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

# **qan_get_balance**
> OutputGetBalance qan_get_balance(address, block_number=block_number)

Returns the balance of the account of given address.

### Example


```python
import qan
from qan.models.output_get_balance import OutputGetBalance
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | A 20 bytes long hexadecimal value representing an address
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending (optional) (default to 'latest')

    try:
        # Returns the balance of the account of given address.
        api_response = api_instance.qan_get_balance(address, block_number=block_number)
        print("The response of QANApi->qan_get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| A 20 bytes long hexadecimal value representing an address | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | [optional] [default to &#39;latest&#39;]

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
import qan
from qan.models.output_get_block_by_hash import OutputGetBlockByHash
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash (32 bytes) of the block
    transaction_detail_flag = False # bool | The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions (default to False)

    try:
        # Returns information of the block matching the given block hash.
        api_response = api_instance.qan_get_block_by_hash(hash, transaction_detail_flag)
        print("The response of QANApi->qan_get_block_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_block_by_hash: %s\n" % e)
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
import qan
from qan.models.output_get_block_by_number import OutputGetBlockByNumber
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending (default to 'latest')
    transaction_detail_flag = False # bool | The method returns the full transaction objects when this value is true otherwise, it returns only the hashes of the transactions (default to False)

    try:
        # Returns information of the block matching the given block number.
        api_response = api_instance.qan_get_block_by_number(block_number, transaction_detail_flag)
        print("The response of QANApi->qan_get_block_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_block_by_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | [default to &#39;latest&#39;]
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
import qan
from qan.models.output_get_block_receipts import OutputGetBlockReceipts
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending (default to 'latest')

    try:
        # Returns all transaction receipts for a given block.
        api_response = api_instance.qan_get_block_receipts(block_number)
        print("The response of QANApi->qan_get_block_receipts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_block_receipts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | [default to &#39;latest&#39;]

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
import qan
from qan.models.output_get_block_transaction_count_by_hash import OutputGetBlockTransactionCountByHash
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash of the block

    try:
        # Returns the number of transactions for the block matching the given block hash.
        api_response = api_instance.qan_get_block_transaction_count_by_hash(hash)
        print("The response of QANApi->qan_get_block_transaction_count_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_block_transaction_count_by_hash: %s\n" % e)
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
import qan
from qan.models.output_get_block_transaction_count_by_number import OutputGetBlockTransactionCountByNumber
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending

    try:
        # Returns the number of transactions for the block matching the given block number.
        api_response = api_instance.qan_get_block_transaction_count_by_number(block_number)
        print("The response of QANApi->qan_get_block_transaction_count_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_block_transaction_count_by_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | 

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
import qan
from qan.models.output_get_code import OutputGetCode
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | The address of the smart contract from which the bytecode will be obtained
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending (optional) (default to 'latest')

    try:
        # Returns the compiled bytecode of a smart contract.
        api_response = api_instance.qan_get_code(address, block_number=block_number)
        print("The response of QANApi->qan_get_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the smart contract from which the bytecode will be obtained | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | [optional] [default to &#39;latest&#39;]

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
import qan
from qan.models.output_get_filter_changes import OutputGetFilterChanges
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    filter_id = 'filter_id_example' # str | The filter id that is returned from getFilterChangesnewFilter, getFilterChangesnewBlockFilter or getFilterChangesnewPendingTransactionFilter

    try:
        # Polling method for a filter, which returns an array of events that have occurred since the last poll.
        api_response = api_instance.qan_get_filter_changes(filter_id)
        print("The response of QANApi->qan_get_filter_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_filter_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The filter id that is returned from getFilterChangesnewFilter, getFilterChangesnewBlockFilter or getFilterChangesnewPendingTransactionFilter | 

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
import qan
from qan.models.output_get_filter_logs import OutputGetFilterLogs
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    id = 'id_example' # str | The filter ID

    try:
        # Returns an array of all logs matching filter with given id.
        api_response = api_instance.qan_get_filter_logs(id)
        print("The response of QANApi->qan_get_filter_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_filter_logs: %s\n" % e)
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
import qan
from qan.models.input_get_logs import InputGetLogs
from qan.models.output_get_logs import OutputGetLogs
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_get_logs = qan.InputGetLogs() # InputGetLogs | 

    try:
        # Returns an array of all logs matching a given filter object.
        api_response = api_instance.qan_get_logs(input_get_logs)
        print("The response of QANApi->qan_get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_logs: %s\n" % e)
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
import qan
from qan.models.input_get_proof import InputGetProof
from qan.models.output_get_proof import OutputGetProof
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_get_proof = qan.InputGetProof() # InputGetProof | 

    try:
        # Returns the account and storage values of the specified account including the Merkle-proof.
        api_response = api_instance.qan_get_proof(input_get_proof)
        print("The response of QANApi->qan_get_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_proof: %s\n" % e)
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
import qan
from qan.models.input_get_storage_at import InputGetStorageAt
from qan.models.output_get_storage_at import OutputGetStorageAt
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_get_storage_at = qan.InputGetStorageAt() # InputGetStorageAt | 

    try:
        # Returns the value from a storage position at a given address.
        api_response = api_instance.qan_get_storage_at(input_get_storage_at)
        print("The response of QANApi->qan_get_storage_at:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_storage_at: %s\n" % e)
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
import qan
from qan.models.output_get_transaction_by_block_hash_and_index import OutputGetTransactionByBlockHashAndIndex
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    block_hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | 
    index = '0' # str | An integer of the transaction index position

    try:
        # Returns information about a transaction given a blockhash and transaction index position.
        api_response = api_instance.qan_get_transaction_by_block_hash_and_index(block_hash, index)
        print("The response of QANApi->qan_get_transaction_by_block_hash_and_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_transaction_by_block_hash_and_index: %s\n" % e)
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
import qan
from qan.models.output_get_transaction_by_block_number_and_index import OutputGetTransactionByBlockNumberAndIndex
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending
    index = '0' # str | An integer of the transaction index position

    try:
        # Returns information about a transaction given a block number and transaction index position.
        api_response = api_instance.qan_get_transaction_by_block_number_and_index(block_number, index)
        print("The response of QANApi->qan_get_transaction_by_block_number_and_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_transaction_by_block_number_and_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | 
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
import qan
from qan.models.output_get_transaction_by_hash import OutputGetTransactionByHash
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    hash = '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060' # str | The hash of a transaction

    try:
        # Returns the information about a transaction from a transaction hash.
        api_response = api_instance.qan_get_transaction_by_hash(hash)
        print("The response of QANApi->qan_get_transaction_by_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_transaction_by_hash: %s\n" % e)
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
import qan
from qan.models.output_get_transaction_count import OutputGetTransactionCount
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    address = '0xa1e4380a3b1f749673e270229993ee55f35663b4' # str | The address from which the transaction count to be checked
    block_number = 'latest' # str | The block number in hexadecimal or decimal format or the string latest, earliest, pending

    try:
        # Returns the number of transactions sent from an address.
        api_response = api_instance.qan_get_transaction_count(address, block_number)
        print("The response of QANApi->qan_get_transaction_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_transaction_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address from which the transaction count to be checked | 
 **block_number** | **str**| The block number in hexadecimal or decimal format or the string latest, earliest, pending | 

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
import qan
from qan.models.output_get_transaction_receipt import OutputGetTransactionReceipt
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    hash = '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd' # str | The hash of a transaction

    try:
        # Returns the receipt of a transaction by transaction hash.
        api_response = api_instance.qan_get_transaction_receipt(hash)
        print("The response of QANApi->qan_get_transaction_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_get_transaction_receipt: %s\n" % e)
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

# **qan_max_priority_fee_per_gas**
> OutputMaxPriorityFeePerGas qan_max_priority_fee_per_gas()

Get the priority fee needed to be included in a block.

### Example


```python
import qan
from qan.models.output_max_priority_fee_per_gas import OutputMaxPriorityFeePerGas
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Get the priority fee needed to be included in a block.
        api_response = api_instance.qan_max_priority_fee_per_gas()
        print("The response of QANApi->qan_max_priority_fee_per_gas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_max_priority_fee_per_gas: %s\n" % e)
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
import qan
from qan.models.output_new_block_filter import OutputNewBlockFilter
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Creates a filter in the node, to notify when a new block arrives.
        api_response = api_instance.qan_new_block_filter()
        print("The response of QANApi->qan_new_block_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_new_block_filter: %s\n" % e)
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
import qan
from qan.models.input_new_filter import InputNewFilter
from qan.models.output_new_filter import OutputNewFilter
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_new_filter = qan.InputNewFilter() # InputNewFilter | 

    try:
        # Creates a filter object, based on filter options, to notify when the state changes (logs).
        api_response = api_instance.qan_new_filter(input_new_filter)
        print("The response of QANApi->qan_new_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_new_filter: %s\n" % e)
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
import qan
from qan.models.output_new_pending_transaction_filter import OutputNewPendingTransactionFilter
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Creates a filter in the node to notify when new pending transactions arrive.
        api_response = api_instance.qan_new_pending_transaction_filter()
        print("The response of QANApi->qan_new_pending_transaction_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_new_pending_transaction_filter: %s\n" % e)
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
import qan
from qan.models.input_send_raw_transaction import InputSendRawTransaction
from qan.models.output_send_raw_transaction import OutputSendRawTransaction
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    input_send_raw_transaction = qan.InputSendRawTransaction() # InputSendRawTransaction | 

    try:
        # Creates new message call transaction or a contract creation for signed transactions.
        api_response = api_instance.qan_send_raw_transaction(input_send_raw_transaction)
        print("The response of QANApi->qan_send_raw_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_send_raw_transaction: %s\n" % e)
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

# **qan_syncing**
> OutputSyncing qan_syncing()

Returns an object with the sync status of the node if the node is out-of-sync and is syncing. Returns null when the node is already in sync.

### Example


```python
import qan
from qan.models.output_syncing import OutputSyncing
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)

    try:
        # Returns an object with the sync status of the node if the node is out-of-sync and is syncing. Returns null when the node is already in sync.
        api_response = api_instance.qan_syncing()
        print("The response of QANApi->qan_syncing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_syncing: %s\n" % e)
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
import qan
from qan.models.output_uninstall_filter import OutputUninstallFilter
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    filter_id = 'filter_id_example' # str | The filter ID that needs to be uninstalled. It should always be called when watch is no longer needed. Additionally, Filters timeout when they aren't requested with getFilterChanges for a period of time

    try:
        # Uninstalls a filter with the given filter id.
        api_response = api_instance.qan_uninstall_filter(filter_id)
        print("The response of QANApi->qan_uninstall_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_uninstall_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The filter ID that needs to be uninstalled. It should always be called when watch is no longer needed. Additionally, Filters timeout when they aren&#39;t requested with getFilterChanges for a period of time | 

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

# **qan_xlink_valid**
> OutputXlinkValid qan_xlink_valid(address)

Returns the xlink validity time of the account of given address.

### Example


```python
import qan
from qan.models.output_xlink_valid import OutputXlinkValid
from qan.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rpc-testnet.qanplatform.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qan.Configuration(
    host = "https://rpc-testnet.qanplatform.com"
)


# Enter a context with an instance of the API client
with qan.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qan.QANApi(api_client)
    address = 'address_example' # str | 

    try:
        # Returns the xlink validity time of the account of given address.
        api_response = api_instance.qan_xlink_valid(address)
        print("The response of QANApi->qan_xlink_valid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QANApi->qan_xlink_valid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

### Return type

[**OutputXlinkValid**](OutputXlinkValid.md)

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

