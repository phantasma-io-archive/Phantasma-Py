# swagger_client.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_account_get**](AccountApi.md#api_v1_get_account_get) | **GET** /api/v1/GetAccount | 
[**api_v1_get_accounts_get**](AccountApi.md#api_v1_get_accounts_get) | **GET** /api/v1/GetAccounts | 
[**api_v1_get_addresses_by_symbol_get**](AccountApi.md#api_v1_get_addresses_by_symbol_get) | **GET** /api/v1/GetAddressesBySymbol | 
[**api_v1_look_up_name_get**](AccountApi.md#api_v1_look_up_name_get) | **GET** /api/v1/LookUpName | 

# **api_v1_get_account_get**
> AccountResult api_v1_get_account_get(account=account)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account = 'account_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_account_get(account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 

### Return type

[**AccountResult**](AccountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_accounts_get**
> list[AccountResult] api_v1_get_accounts_get(account_text=account_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account_text = 'account_text_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_accounts_get(account_text=account_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_text** | **str**|  | [optional] 

### Return type

[**list[AccountResult]**](AccountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_addresses_by_symbol_get**
> list[AccountResult] api_v1_get_addresses_by_symbol_get(symbol=symbol, extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
symbol = 'symbol_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_addresses_by_symbol_get(symbol=symbol, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_addresses_by_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**list[AccountResult]**](AccountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_look_up_name_get**
> str api_v1_look_up_name_get(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_look_up_name_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_look_up_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

