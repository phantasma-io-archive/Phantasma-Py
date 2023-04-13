# swagger_client.RpcApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_post**](RpcApi.md#rpc_post) | **POST** /rpc | 

# **rpc_post**
> RpcResponse rpc_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RpcApi()
body = swagger_client.RpcRequest() # RpcRequest |  (optional)

try:
    api_response = api_instance.rpc_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RpcApi->rpc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RpcRequest**](RpcRequest.md)|  | [optional] 

### Return type

[**RpcResponse**](RpcResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

