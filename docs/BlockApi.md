# swagger_client.BlockApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_block_by_hash_get**](BlockApi.md#api_v1_get_block_by_hash_get) | **GET** /api/v1/GetBlockByHash | 
[**api_v1_get_block_by_height_get**](BlockApi.md#api_v1_get_block_by_height_get) | **GET** /api/v1/GetBlockByHeight | 
[**api_v1_get_block_height_get**](BlockApi.md#api_v1_get_block_height_get) | **GET** /api/v1/GetBlockHeight | 
[**api_v1_get_block_transaction_count_by_hash_get**](BlockApi.md#api_v1_get_block_transaction_count_by_hash_get) | **GET** /api/v1/GetBlockTransactionCountByHash | 
[**api_v1_get_latest_block_get**](BlockApi.md#api_v1_get_latest_block_get) | **GET** /api/v1/GetLatestBlock | 
[**api_v1_get_raw_block_by_hash_get**](BlockApi.md#api_v1_get_raw_block_by_hash_get) | **GET** /api/v1/GetRawBlockByHash | 
[**api_v1_get_raw_block_by_height_get**](BlockApi.md#api_v1_get_raw_block_by_height_get) | **GET** /api/v1/GetRawBlockByHeight | 
[**api_v1_get_raw_latest_block_get**](BlockApi.md#api_v1_get_raw_latest_block_get) | **GET** /api/v1/GetRawLatestBlock | 

# **api_v1_get_block_by_hash_get**
> BlockResult api_v1_get_block_by_hash_get(block_hash=block_hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_by_hash_get(block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_by_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**|  | [optional] 

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_block_by_height_get**
> BlockResult api_v1_get_block_by_height_get(chain_input=chain_input, height=height)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)
height = 'height_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_by_height_get(chain_input=chain_input, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_by_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 
 **height** | **str**|  | [optional] 

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_block_height_get**
> str api_v1_get_block_height_get(chain_input=chain_input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_height_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_block_transaction_count_by_hash_get**
> int api_v1_get_block_transaction_count_by_hash_get(chain_address_or_name=chain_address_or_name, block_hash=block_hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_transaction_count_by_hash_get(chain_address_or_name=chain_address_or_name, block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_transaction_count_by_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **block_hash** | **str**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_latest_block_get**
> BlockResult api_v1_get_latest_block_get(chain_input=chain_input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_latest_block_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_latest_block_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_raw_block_by_hash_get**
> str api_v1_get_raw_block_by_hash_get(block_hash=block_hash)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_block_by_hash_get(block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_block_by_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_raw_block_by_height_get**
> str api_v1_get_raw_block_by_height_get(chain_input=chain_input, height=height)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)
height = 'height_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_block_by_height_get(chain_input=chain_input, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_block_by_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 
 **height** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_raw_latest_block_get**
> str api_v1_get_raw_latest_block_get(chain_input=chain_input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_latest_block_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_latest_block_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_input** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

