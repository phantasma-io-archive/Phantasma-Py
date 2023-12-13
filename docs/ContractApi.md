# swagger_client.ContractApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_get_contract_by_address_get**](ContractApi.md#api_v1_get_contract_by_address_get) | **GET** /api/v1/GetContractByAddress | 
[**api_v1_get_contract_get**](ContractApi.md#api_v1_get_contract_get) | **GET** /api/v1/GetContract | 
[**api_v1_get_contracts_get**](ContractApi.md#api_v1_get_contracts_get) | **GET** /api/v1/GetContracts | 

# **api_v1_get_contract_by_address_get**
> ContractResult api_v1_get_contract_by_address_get(chain_address_or_name=chain_address_or_name, contract_address=contract_address)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
contract_address = 'contract_address_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_contract_by_address_get(chain_address_or_name=chain_address_or_name, contract_address=contract_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->api_v1_get_contract_by_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **contract_address** | **str**|  | [optional] 

### Return type

[**ContractResult**](ContractResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_contract_get**
> ContractResult api_v1_get_contract_get(chain_address_or_name=chain_address_or_name, contract_name=contract_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
contract_name = 'contract_name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_contract_get(chain_address_or_name=chain_address_or_name, contract_name=contract_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->api_v1_get_contract_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 
 **contract_name** | **str**|  | [optional] 

### Return type

[**ContractResult**](ContractResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_get_contracts_get**
> list[ContractResult] api_v1_get_contracts_get(chain_address_or_name=chain_address_or_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_contracts_get(chain_address_or_name=chain_address_or_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->api_v1_get_contracts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_address_or_name** | **str**|  | [optional] 

### Return type

[**list[ContractResult]**](ContractResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

