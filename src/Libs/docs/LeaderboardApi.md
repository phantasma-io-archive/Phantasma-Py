# swagger_client.LeaderboardApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_leaderboard_get**](LeaderboardApi.md#api_v1_get_leaderboard_get) | **GET** /api/v1/GetLeaderboard | 

# **api_v1_get_leaderboard_get**
> LeaderboardResult api_v1_get_leaderboard_get(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeaderboardApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_leaderboard_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardApi->api_v1_get_leaderboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**LeaderboardResult**](LeaderboardResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

