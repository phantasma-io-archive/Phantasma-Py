# swagger_client.ValidatorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_validators_get**](ValidatorApi.md#api_v1_get_validators_get) | **GET** /api/v1/GetValidators | 
[**api_v1_get_validators_type_get**](ValidatorApi.md#api_v1_get_validators_type_get) | **GET** /api/v1/GetValidators/{type} | 

# **api_v1_get_validators_get**
> list[ValidatorResult] api_v1_get_validators_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidatorApi()

try:
    api_response = api_instance.api_v1_get_validators_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidatorApi->api_v1_get_validators_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ValidatorResult]**](ValidatorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_validators_type_get**
> list[ValidatorResult] api_v1_get_validators_type_get(type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidatorApi()
type = 'type_example' # str | 

try:
    api_response = api_instance.api_v1_get_validators_type_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidatorApi->api_v1_get_validators_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**list[ValidatorResult]**](ValidatorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

