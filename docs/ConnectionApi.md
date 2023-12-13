# swagger_client.ConnectionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_abci_query_get**](ConnectionApi.md#api_v1_abci_query_get) | **GET** /api/v1/abci_query | 
[**api_v1_get_validators_settings_get**](ConnectionApi.md#api_v1_get_validators_settings_get) | **GET** /api/v1/GetValidatorsSettings | 
[**api_v1_health_get**](ConnectionApi.md#api_v1_health_get) | **GET** /api/v1/health | 
[**api_v1_net_info_get**](ConnectionApi.md#api_v1_net_info_get) | **GET** /api/v1/net_info | 
[**api_v1_request_block_get**](ConnectionApi.md#api_v1_request_block_get) | **GET** /api/v1/request_block | 
[**api_v1_status_get**](ConnectionApi.md#api_v1_status_get) | **GET** /api/v1/status | 

# **api_v1_abci_query_get**
> ResultAbciQuery api_v1_abci_query_get(path=path, data=data, height=height, prove=prove)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
path = 'path_example' # str |  (optional)
data = 'data_example' # str |  (optional)
height = 0 # int |  (optional) (default to 0)
prove = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_abci_query_get(path=path, data=data, height=height, prove=prove)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_abci_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 
 **data** | **str**|  | [optional] 
 **height** | **int**|  | [optional] [default to 0]
 **prove** | **bool**|  | [optional] [default to false]

### Return type

[**ResultAbciQuery**](ResultAbciQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_validators_settings_get**
> list[ValidatorSettings] api_v1_get_validators_settings_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_get_validators_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_get_validators_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ValidatorSettings]**](ValidatorSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_health_get**
> ResultHealth api_v1_health_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultHealth**](ResultHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_net_info_get**
> ResultNetInfo api_v1_net_info_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_net_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_net_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultNetInfo**](ResultNetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_request_block_get**
> ResultAbciQuery api_v1_request_block_get(height=height)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
height = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.api_v1_request_block_get(height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_request_block_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**|  | [optional] [default to 0]

### Return type

[**ResultAbciQuery**](ResultAbciQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_status_get**
> ResultStatus api_v1_status_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResultStatus**](ResultStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

