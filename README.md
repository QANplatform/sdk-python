# QAN Python SDK

This repository is guaranteed up-to-date with the upstream QAN API definitions, and leverages OpenAPI technology to stay consistent.

Versioning is based on SEMVER, meaning:

- Stable releases guarantee backwards compatibility for the same major versions.
- Minor releases will not contain breaking changes.
- Patch releases only focus on fixing issues.

## Documentation for API Endpoints

All URIs are relative to *https://rpc-testnet.qanplatform.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qan_block_number**](docs/QANApi.md#qan_block_number) | **GET** /blockNumber/ | Returns the latest block number of the blockchain.
[**qan_call**](docs/QANApi.md#qan_call) | **POST** /call/ | Executes a new message call immediately without creating a transaction on the block chain.
[**qan_chain_id**](docs/QANApi.md#qan_chain_id) | **GET** /chainId/ | Returns the current network/chain ID, used to sign replay-protected transaction introduced in EIP-155.
[**qan_estimate_gas**](docs/QANApi.md#qan_estimate_gas) | **POST** /estimateGas/ | Returns an estimation of gas for a given transaction.
[**qan_fee_history**](docs/QANApi.md#qan_fee_history) | **POST** /feeHistory/ | Returns the collection of historical gas information.
[**qan_gas_price**](docs/QANApi.md#qan_gas_price) | **GET** /gasPrice/ | Returns the current gas price on the network in wei.
[**qan_get_balance**](docs/QANApi.md#qan_get_balance) | **GET** /getBalance/{Address}/ | Returns the balance of the account of given address.
[**qan_get_block_by_hash**](docs/QANApi.md#qan_get_block_by_hash) | **GET** /getBlockByHash/{Hash}/{TransactionDetailFlag}/ | Returns information of the block matching the given block hash.
[**qan_get_block_by_number**](docs/QANApi.md#qan_get_block_by_number) | **GET** /getBlockByNumber/{BlockNumber}/{TransactionDetailFlag}/ | Returns information of the block matching the given block number.
[**qan_get_block_receipts**](docs/QANApi.md#qan_get_block_receipts) | **GET** /getBlockReceipts/{BlockNumber}/ | Returns all transaction receipts for a given block.
[**qan_get_block_transaction_count_by_hash**](docs/QANApi.md#qan_get_block_transaction_count_by_hash) | **GET** /getBlockTransactionCountByHash/{Hash}/ | Returns the number of transactions for the block matching the given block hash.
[**qan_get_block_transaction_count_by_number**](docs/QANApi.md#qan_get_block_transaction_count_by_number) | **GET** /getBlockTransactionCountByNumber/{BlockNumber}/ | Returns the number of transactions for the block matching the given block number.
[**qan_get_code**](docs/QANApi.md#qan_get_code) | **GET** /getCode/{Address}/ | Returns the compiled bytecode of a smart contract.
[**qan_get_filter_changes**](docs/QANApi.md#qan_get_filter_changes) | **GET** /getFilterChanges/{FilterId}/ | Polling method for a filter, which returns an array of events that have occurred since the last poll.
[**qan_get_filter_logs**](docs/QANApi.md#qan_get_filter_logs) | **GET** /getFilterLogs/{Id}/ | Returns an array of all logs matching filter with given id.
[**qan_get_logs**](docs/QANApi.md#qan_get_logs) | **POST** /getLogs/ | Returns an array of all logs matching a given filter object.
[**qan_get_proof**](docs/QANApi.md#qan_get_proof) | **POST** /getProof/ | Returns the account and storage values of the specified account including the Merkle-proof.
[**qan_get_storage_at**](docs/QANApi.md#qan_get_storage_at) | **POST** /getStorageAt/ | Returns the value from a storage position at a given address.
[**qan_get_transaction_by_block_hash_and_index**](docs/QANApi.md#qan_get_transaction_by_block_hash_and_index) | **GET** /getTransactionByBlockHashAndIndex/{blockHash}/{index}/ | Returns information about a transaction given a blockhash and transaction index position.
[**qan_get_transaction_by_block_number_and_index**](docs/QANApi.md#qan_get_transaction_by_block_number_and_index) | **GET** /getTransactionByBlockNumberAndIndex/{blockNumber}/{index}/ | Returns information about a transaction given a block number and transaction index position.
[**qan_get_transaction_by_hash**](docs/QANApi.md#qan_get_transaction_by_hash) | **GET** /getTransactionByHash/{hash}/ | Returns the information about a transaction from a transaction hash.
[**qan_get_transaction_count**](docs/QANApi.md#qan_get_transaction_count) | **GET** /getTransactionCount/{Address}/{BlockNumber}/ | Returns the number of transactions sent from an address.
[**qan_get_transaction_receipt**](docs/QANApi.md#qan_get_transaction_receipt) | **GET** /getTransactionReceipt/{Hash}/ | Returns the receipt of a transaction by transaction hash.
[**qan_max_priority_fee_per_gas**](docs/QANApi.md#qan_max_priority_fee_per_gas) | **GET** /maxPriorityFeePerGas/ | Get the priority fee needed to be included in a block.
[**qan_new_block_filter**](docs/QANApi.md#qan_new_block_filter) | **GET** /newBlockFilter/ | Creates a filter in the node, to notify when a new block arrives.
[**qan_new_filter**](docs/QANApi.md#qan_new_filter) | **POST** /newFilter/ | Creates a filter object, based on filter options, to notify when the state changes (logs).
[**qan_new_pending_transaction_filter**](docs/QANApi.md#qan_new_pending_transaction_filter) | **GET** /newPendingTransactionFilter/ | Creates a filter in the node to notify when new pending transactions arrive.
[**qan_send_raw_transaction**](docs/QANApi.md#qan_send_raw_transaction) | **POST** /sendRawTransaction/ | Creates new message call transaction or a contract creation for signed transactions.
[**qan_syncing**](docs/QANApi.md#qan_syncing) | **GET** /syncing/ | Returns an object with the sync status of the node if the node is out-of-sync and is syncing. Returns null when the node is already in sync.
[**qan_uninstall_filter**](docs/QANApi.md#qan_uninstall_filter) | **GET** /uninstallFilter/{FilterId}/ | Uninstalls a filter with the given filter id.
[**qan_xlink_valid**](docs/QANApi.md#qan_xlink_valid) | **GET** /xlinkValid/{Address}/ | Returns the xlink validity time of the account of given address.


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
