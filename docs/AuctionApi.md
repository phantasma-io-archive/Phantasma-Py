# swagger_client.AuctionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_auction_get**](AuctionApi.md#api_v1_get_auction_get) | **GET** /api/v1/GetAuction | 
[**api_v1_get_auctions_count_get**](AuctionApi.md#api_v1_get_auctions_count_get) | **GET** /api/v1/GetAuctionsCount | 
[**api_v1_get_auctions_get**](AuctionApi.md#api_v1_get_auctions_get) | **GET** /api/v1/GetAuctions | 

# **api_v1_get_auction_get**
> AuctionResult api_v1_get_auction_get(chain_address_or_name=chain_address_or_name, symbol=symbol, i_dtext=i_dtext)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_auction_get(chain_address_or_name=chain_address_or_name, symbol=symbol, i_dtext=i_dtext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **i_dtext** | **str**|  | [optional] 

### Return type

[**AuctionResult**](AuctionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_auctions_count_get**
> int api_v1_get_auctions_count_get(chain_address_or_name=chain_address_or_name, symbol=symbol)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_auctions_count_get(chain_address_or_name=chain_address_or_name, symbol=symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auctions_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_auctions_get**
> PaginatedResult api_v1_get_auctions_get(chain_address_or_name=chain_address_or_name, symbol=symbol, page=page, page_size=page_size)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
page_size = 99999 # int |  (optional) (default to 99999)

try:
    api_response = api_instance.api_v1_get_auctions_get(chain_address_or_name=chain_address_or_name, symbol=symbol, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auctions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 99999]

### Return type

[**PaginatedResult**](PaginatedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

