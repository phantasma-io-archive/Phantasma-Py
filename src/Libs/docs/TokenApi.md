# swagger_client.TokenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_nft_get**](TokenApi.md#api_v1_get_nft_get) | **GET** /api/v1/GetNFT | 
[**api_v1_get_nfts_get**](TokenApi.md#api_v1_get_nfts_get) | **GET** /api/v1/GetNFTs | 
[**api_v1_get_token_balance_get**](TokenApi.md#api_v1_get_token_balance_get) | **GET** /api/v1/GetTokenBalance | 
[**api_v1_get_token_data_get**](TokenApi.md#api_v1_get_token_data_get) | **GET** /api/v1/GetTokenData | 
[**api_v1_get_token_get**](TokenApi.md#api_v1_get_token_get) | **GET** /api/v1/GetToken | 
[**api_v1_get_tokens_get**](TokenApi.md#api_v1_get_tokens_get) | **GET** /api/v1/GetTokens | 

# **api_v1_get_nft_get**
> TokenDataResult api_v1_get_nft_get(symbol=symbol, i_dtext=i_dtext, extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nft_get(symbol=symbol, i_dtext=i_dtext, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_nft_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **i_dtext** | **str**|  | [optional] 
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**TokenDataResult**](TokenDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_nfts_get**
> list[TokenDataResult] api_v1_get_nfts_get(symbol=symbol, id_text=id_text, extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
id_text = 'id_text_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nfts_get(symbol=symbol, id_text=id_text, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_nfts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **id_text** | **str**|  | [optional] 
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**list[TokenDataResult]**](TokenDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_token_balance_get**
> BalanceResult api_v1_get_token_balance_get(account=account, token_symbol=token_symbol, chain_input=chain_input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
account = 'account_example' # str |  (optional)
token_symbol = 'token_symbol_example' # str |  (optional)
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_token_balance_get(account=account, token_symbol=token_symbol, chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 
 **token_symbol** | **str**|  | [optional] 
 **chain_input** | **str**|  | [optional] 

### Return type

[**BalanceResult**](BalanceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_token_data_get**
> TokenDataResult api_v1_get_token_data_get(symbol=symbol, i_dtext=i_dtext)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_token_data_get(symbol=symbol, i_dtext=i_dtext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **i_dtext** | **str**|  | [optional] 

### Return type

[**TokenDataResult**](TokenDataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_token_get**
> TokenResult api_v1_get_token_get(symbol=symbol, extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_token_get(symbol=symbol, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**TokenResult**](TokenResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_tokens_get**
> list[TokenResult] api_v1_get_tokens_get(extended=extended)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_tokens_get(extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_tokens_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended** | **bool**|  | [optional] [default to false]

### Return type

[**list[TokenResult]**](TokenResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

