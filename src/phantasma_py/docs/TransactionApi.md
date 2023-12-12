# swagger_client.TransactionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_address_transaction_count_get**](TransactionApi.md#api_v1_get_address_transaction_count_get) | **GET** /api/v1/GetAddressTransactionCount | 
[**api_v1_get_address_transactions_get**](TransactionApi.md#api_v1_get_address_transactions_get) | **GET** /api/v1/GetAddressTransactions | 
[**api_v1_get_transaction_by_block_hash_and_index_get**](TransactionApi.md#api_v1_get_transaction_by_block_hash_and_index_get) | **GET** /api/v1/GetTransactionByBlockHashAndIndex | 
[**api_v1_get_transaction_get**](TransactionApi.md#api_v1_get_transaction_get) | **GET** /api/v1/GetTransaction | 
[**api_v1_invoke_raw_script_get**](TransactionApi.md#api_v1_invoke_raw_script_get) | **GET** /api/v1/InvokeRawScript | 
[**api_v1_send_raw_transaction_get**](TransactionApi.md#api_v1_send_raw_transaction_get) | **GET** /api/v1/SendRawTransaction | 

# **api_v1_get_address_transaction_count_get**
> int api_v1_get_address_transaction_count_get(account=account, chain_input=chain_input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
account = 'account_example' # str |  (optional)
chain_input = 'main' # str |  (optional) (default to main)

try:
    api_response = api_instance.api_v1_get_address_transaction_count_get(account=account, chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_get_address_transaction_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 
 **chain_input** | **str**|  | [optional] [default to main]

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_address_transactions_get**
> PaginatedResult api_v1_get_address_transactions_get(account=account, page=page, page_size=page_size)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
account = 'account_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
page_size = 99999 # int |  (optional) (default to 99999)

try:
    api_response = api_instance.api_v1_get_address_transactions_get(account=account, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_get_address_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 99999]

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_transaction_by_block_hash_and_index_get**
> TransactionResult api_v1_get_transaction_by_block_hash_and_index_get(chain_address_or_name=chain_address_or_name, block_hash=block_hash, index=index)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
block_hash = 'block_hash_example' # str |  (optional)
index = 56 # int |  (optional)

try:
    api_response = api_instance.api_v1_get_transaction_by_block_hash_and_index_get(chain_address_or_name=chain_address_or_name, block_hash=block_hash, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_get_transaction_by_block_hash_and_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **block_hash** | **str**|  | [optional] 
 **index** | **int**|  | [optional] 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_transaction_get**
> TransactionResult api_v1_get_transaction_get(hash_text=hash_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
hash_text = 'hash_text_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_transaction_get(hash_text=hash_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_get_transaction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_text** | **str**|  | [optional] 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_invoke_raw_script_get**
> ScriptResult api_v1_invoke_raw_script_get(chain_input=chain_input, script_data=script_data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
chain_input = 'chain_input_example' # str |  (optional)
script_data = 'script_data_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_invoke_raw_script_get(chain_input=chain_input, script_data=script_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_invoke_raw_script_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 
 **script_data** | **str**|  | [optional] 

### Return type

[**ScriptResult**](ScriptResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_send_raw_transaction_get**
> str api_v1_send_raw_transaction_get(tx_data=tx_data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionApi()
tx_data = 'tx_data_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_send_raw_transaction_get(tx_data=tx_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->api_v1_send_raw_transaction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_data** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

