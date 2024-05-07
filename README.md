# QAN Python SDK

This repository is guaranteed up-to-date with the upstream QAN API definitions, and leverages OpenAPI technology to stay consistent.

Versioning is based on SEMVER, meaning:

- Stable releases guarantee backwards compatibility for the same major versions.
- Minor releases will not contain breaking changes.
- Patch releases only focus on fixing issues.

## Documentation for API Endpoints

All URIs are relative to *https://rpc-testnet.qanplatform.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**qan_accounts**](docs/DefaultApi.md#qan_accounts) | **GET** /accounts/ | 
*DefaultApi* | [**qan_blob_base_fee**](docs/DefaultApi.md#qan_blob_base_fee) | **GET** /blobBaseFee/ | 
*DefaultApi* | [**qan_block_number**](docs/DefaultApi.md#qan_block_number) | **GET** /blockNumber/ | 
*DefaultApi* | [**qan_call**](docs/DefaultApi.md#qan_call) | **POST** /call/ | 
*DefaultApi* | [**qan_chain_id**](docs/DefaultApi.md#qan_chain_id) | **GET** /chainId/ | 
*DefaultApi* | [**qan_estimate_gas**](docs/DefaultApi.md#qan_estimate_gas) | **POST** /estimateGas/ | 
*DefaultApi* | [**qan_fee_history**](docs/DefaultApi.md#qan_fee_history) | **POST** /feeHistory/ | 
*DefaultApi* | [**qan_gas_price**](docs/DefaultApi.md#qan_gas_price) | **GET** /gasPrice/ | 
*DefaultApi* | [**qan_get_account**](docs/DefaultApi.md#qan_get_account) | **GET** /getAccount/{Address}/{BlockReference}/ | 
*DefaultApi* | [**qan_get_balance**](docs/DefaultApi.md#qan_get_balance) | **GET** /getBalance/{Address}/ | 
*DefaultApi* | [**qan_get_block_by_hash**](docs/DefaultApi.md#qan_get_block_by_hash) | **GET** /getBlockByHash/{Hash}/{TransactionDetailFlag}/ | 
*DefaultApi* | [**qan_get_block_by_number**](docs/DefaultApi.md#qan_get_block_by_number) | **GET** /getBlockByNumber/{BlockNumber}/{TransactionDetailFlag}/ | 
*DefaultApi* | [**qan_get_block_receipts**](docs/DefaultApi.md#qan_get_block_receipts) | **GET** /getBlockReceipts/{BlockNumber}/ | 
*DefaultApi* | [**qan_get_block_transaction_count_by_hash**](docs/DefaultApi.md#qan_get_block_transaction_count_by_hash) | **GET** /getBlockTransactionCountByHash/{Hash}/ | 
*DefaultApi* | [**qan_get_block_transaction_count_by_number**](docs/DefaultApi.md#qan_get_block_transaction_count_by_number) | **GET** /getBlockTransactionCountByNumber/{BlockNumber}/ | 
*DefaultApi* | [**qan_get_code**](docs/DefaultApi.md#qan_get_code) | **GET** /getCode/{Address}/ | 
*DefaultApi* | [**qan_get_filter_changes**](docs/DefaultApi.md#qan_get_filter_changes) | **GET** /getFilterChanges/{FilterId}/ | 
*DefaultApi* | [**qan_get_filter_logs**](docs/DefaultApi.md#qan_get_filter_logs) | **GET** /getFilterLogs/{Id}/ | 
*DefaultApi* | [**qan_get_logs**](docs/DefaultApi.md#qan_get_logs) | **POST** /getLogs/ | 
*DefaultApi* | [**qan_get_proof**](docs/DefaultApi.md#qan_get_proof) | **POST** /getProof/ | 
*DefaultApi* | [**qan_get_storage_at**](docs/DefaultApi.md#qan_get_storage_at) | **POST** /getStorageAt/ | 
*DefaultApi* | [**qan_get_transaction_by_block_hash_and_index**](docs/DefaultApi.md#qan_get_transaction_by_block_hash_and_index) | **GET** /getTransactionByBlockHashAndIndex/{blockHash}/{index}/ | 
*DefaultApi* | [**qan_get_transaction_by_block_number_and_index**](docs/DefaultApi.md#qan_get_transaction_by_block_number_and_index) | **GET** /getTransactionByBlockNumberAndIndex/{blockNumber}/{index}/ | 
*DefaultApi* | [**qan_get_transaction_by_hash**](docs/DefaultApi.md#qan_get_transaction_by_hash) | **GET** /getTransactionByHash/{hash}/ | 
*DefaultApi* | [**qan_get_transaction_count**](docs/DefaultApi.md#qan_get_transaction_count) | **GET** /getTransactionCount/{Address}/{BlockNumber}/ | 
*DefaultApi* | [**qan_get_transaction_receipt**](docs/DefaultApi.md#qan_get_transaction_receipt) | **GET** /getTransactionReceipt/{Hash}/ | 
*DefaultApi* | [**qan_get_uncle_count_by_block_hash**](docs/DefaultApi.md#qan_get_uncle_count_by_block_hash) | **GET** /getUncleCountByBlockHash/{Hash}/ | 
*DefaultApi* | [**qan_get_uncle_count_by_block_number**](docs/DefaultApi.md#qan_get_uncle_count_by_block_number) | **GET** /getUncleCountByBlockNumber/{BlockNumber}/ | 
*DefaultApi* | [**qan_max_priority_fee_per_gas**](docs/DefaultApi.md#qan_max_priority_fee_per_gas) | **GET** /maxPriorityFeePerGas/ | 
*DefaultApi* | [**qan_new_block_filter**](docs/DefaultApi.md#qan_new_block_filter) | **GET** /newBlockFilter/ | 
*DefaultApi* | [**qan_new_filter**](docs/DefaultApi.md#qan_new_filter) | **POST** /newFilter/ | 
*DefaultApi* | [**qan_new_pending_transaction_filter**](docs/DefaultApi.md#qan_new_pending_transaction_filter) | **GET** /newPendingTransactionFilter/ | 
*DefaultApi* | [**qan_send_raw_transaction**](docs/DefaultApi.md#qan_send_raw_transaction) | **POST** /sendRawTransaction/ | 
*DefaultApi* | [**qan_subscribe**](docs/DefaultApi.md#qan_subscribe) | **POST** /subscribe/ | 
*DefaultApi* | [**qan_syncing**](docs/DefaultApi.md#qan_syncing) | **GET** /syncing/ | 
*DefaultApi* | [**qan_uninstall_filter**](docs/DefaultApi.md#qan_uninstall_filter) | **GET** /uninstallFilter/{FilterId}/ | 
*DefaultApi* | [**qan_unsubscribe**](docs/DefaultApi.md#qan_unsubscribe) | **GET** /unsubscribe/{SubscriptionId}/ | 
*DefaultApi* | [**qan_xlink_valid**](docs/DefaultApi.md#qan_xlink_valid) | **GET** /xlinkValid/ | 


## Documentation For Models

 - [ErrorDetail](docs/ErrorDetail.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [EstimateGasObject](docs/EstimateGasObject.md)
 - [FilterObject](docs/FilterObject.md)
 - [InputCall](docs/InputCall.md)
 - [InputEstimateGas](docs/InputEstimateGas.md)
 - [InputFeeHistory](docs/InputFeeHistory.md)
 - [InputGetLogs](docs/InputGetLogs.md)
 - [InputGetProof](docs/InputGetProof.md)
 - [InputGetStorageAt](docs/InputGetStorageAt.md)
 - [InputNewFilter](docs/InputNewFilter.md)
 - [InputSendRawTransaction](docs/InputSendRawTransaction.md)
 - [InputSubscribe](docs/InputSubscribe.md)
 - [OutputAccounts](docs/OutputAccounts.md)
 - [OutputBlobBaseFee](docs/OutputBlobBaseFee.md)
 - [OutputBlockNumber](docs/OutputBlockNumber.md)
 - [OutputCall](docs/OutputCall.md)
 - [OutputChainId](docs/OutputChainId.md)
 - [OutputEstimateGas](docs/OutputEstimateGas.md)
 - [OutputFeeHistory](docs/OutputFeeHistory.md)
 - [OutputGasPrice](docs/OutputGasPrice.md)
 - [OutputGetAccount](docs/OutputGetAccount.md)
 - [OutputGetBalance](docs/OutputGetBalance.md)
 - [OutputGetBlockByHash](docs/OutputGetBlockByHash.md)
 - [OutputGetBlockByNumber](docs/OutputGetBlockByNumber.md)
 - [OutputGetBlockReceipts](docs/OutputGetBlockReceipts.md)
 - [OutputGetBlockTransactionCountByHash](docs/OutputGetBlockTransactionCountByHash.md)
 - [OutputGetBlockTransactionCountByNumber](docs/OutputGetBlockTransactionCountByNumber.md)
 - [OutputGetCode](docs/OutputGetCode.md)
 - [OutputGetFilterChanges](docs/OutputGetFilterChanges.md)
 - [OutputGetFilterLogs](docs/OutputGetFilterLogs.md)
 - [OutputGetLogs](docs/OutputGetLogs.md)
 - [OutputGetProof](docs/OutputGetProof.md)
 - [OutputGetStorageAt](docs/OutputGetStorageAt.md)
 - [OutputGetTransactionByBlockHashAndIndex](docs/OutputGetTransactionByBlockHashAndIndex.md)
 - [OutputGetTransactionByBlockNumberAndIndex](docs/OutputGetTransactionByBlockNumberAndIndex.md)
 - [OutputGetTransactionByHash](docs/OutputGetTransactionByHash.md)
 - [OutputGetTransactionCount](docs/OutputGetTransactionCount.md)
 - [OutputGetTransactionReceipt](docs/OutputGetTransactionReceipt.md)
 - [OutputGetUncleCountByBlockHash](docs/OutputGetUncleCountByBlockHash.md)
 - [OutputGetUncleCountByBlockNumber](docs/OutputGetUncleCountByBlockNumber.md)
 - [OutputMaxPriorityFeePerGas](docs/OutputMaxPriorityFeePerGas.md)
 - [OutputNewBlockFilter](docs/OutputNewBlockFilter.md)
 - [OutputNewFilter](docs/OutputNewFilter.md)
 - [OutputNewPendingTransactionFilter](docs/OutputNewPendingTransactionFilter.md)
 - [OutputSendRawTransaction](docs/OutputSendRawTransaction.md)
 - [OutputSubscribe](docs/OutputSubscribe.md)
 - [OutputSyncing](docs/OutputSyncing.md)
 - [OutputUninstallFilter](docs/OutputUninstallFilter.md)
 - [OutputUnsubscribe](docs/OutputUnsubscribe.md)
 - [ParamsTransaction](docs/ParamsTransaction.md)
 - [QanXlinkValidResponse](docs/QanXlinkValidResponse.md)
 - [ResponseBlock](docs/ResponseBlock.md)
 - [ResponseLog](docs/ResponseLog.md)
 - [ResponseStorageEntry](docs/ResponseStorageEntry.md)
 - [ResponseTransaction](docs/ResponseTransaction.md)
 - [ResponseTransactionReceipt](docs/ResponseTransactionReceipt.md)
 - [ResponseWithdrawals](docs/ResponseWithdrawals.md)
 - [SyncStatus](docs/SyncStatus.md)

## Acknowledgements

We would like to thank Smartbear and OpenAPITools tech for making building declarative APIs possible.
A huge benefit for the whole industry!
