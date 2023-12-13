# swagger_client.StorageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_read_image_get**](StorageApi.md#api_v1_read_image_get) | **GET** /api/v1/ReadImage | 

# **api_v1_read_image_get**
> api_v1_read_image_get(hash_text=hash_text, format=format)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
hash_text = 'hash_text_example' # str |  (optional)
format = 'png' # str |  (optional) (default to png)

try:
    api_instance.api_v1_read_image_get(hash_text=hash_text, format=format)
except ApiException as e:
    print("Exception when calling StorageApi->api_v1_read_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_text** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to png]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

