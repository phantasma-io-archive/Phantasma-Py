# swagger_client.SaleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_latest_sale_hash_get**](SaleApi.md#api_v1_get_latest_sale_hash_get) | **GET** /api/v1/GetLatestSaleHash | 
[**api_v1_get_sale_get**](SaleApi.md#api_v1_get_sale_get) | **GET** /api/v1/GetSale | 

# **api_v1_get_latest_sale_hash_get**
> str api_v1_get_latest_sale_hash_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SaleApi()

try:
    api_response = api_instance.api_v1_get_latest_sale_hash_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->api_v1_get_latest_sale_hash_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_sale_get**
> CrowdsaleResult api_v1_get_sale_get(hash_text=hash_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SaleApi()
hash_text = 'hash_text_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_sale_get(hash_text=hash_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->api_v1_get_sale_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_text** | **str**|  | [optional] 

### Return type

[**CrowdsaleResult**](CrowdsaleResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

