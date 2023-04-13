# swagger_client.ChainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_chains_get**](ChainApi.md#api_v1_get_chains_get) | **GET** /api/v1/GetChains | 

# **api_v1_get_chains_get**
> list[ChainResult] api_v1_get_chains_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChainApi()

try:
    api_response = api_instance.api_v1_get_chains_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainApi->api_v1_get_chains_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChainResult]**](ChainResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

