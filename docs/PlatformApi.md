# swagger_client.PlatformApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_interop_get**](PlatformApi.md#api_v1_get_interop_get) | **GET** /api/v1/GetInterop | 
[**api_v1_get_platform_get**](PlatformApi.md#api_v1_get_platform_get) | **GET** /api/v1/GetPlatform | 
[**api_v1_get_platforms_get**](PlatformApi.md#api_v1_get_platforms_get) | **GET** /api/v1/GetPlatforms | 

# **api_v1_get_interop_get**
> InteropResult api_v1_get_interop_get(platform=platform)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlatformApi()
platform = 'platform_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_interop_get(platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->api_v1_get_interop_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional] 

### Return type

[**InteropResult**](InteropResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_platform_get**
> PlatformResult api_v1_get_platform_get(platform=platform)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlatformApi()
platform = 'platform_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_platform_get(platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->api_v1_get_platform_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional] 

### Return type

[**PlatformResult**](PlatformResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_platforms_get**
> list[PlatformResult] api_v1_get_platforms_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlatformApi()

try:
    api_response = api_instance.api_v1_get_platforms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->api_v1_get_platforms_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PlatformResult]**](PlatformResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

