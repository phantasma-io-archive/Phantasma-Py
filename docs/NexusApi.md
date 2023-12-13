# swagger_client.NexusApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_nexus_get**](NexusApi.md#api_v1_get_nexus_get) | **GET** /api/v1/GetNexus | 

# **api_v1_get_nexus_get**
> NexusResult api_v1_get_nexus_get(extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NexusApi()
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nexus_get(extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NexusApi->api_v1_get_nexus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**NexusResult**](NexusResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

