# codex_api_client.DebugApi

All URIs are relative to *http://localhost:8080/api/codex/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_debug_info**](DebugApi.md#get_debug_info) | **GET** /debug/info | Gets node information
[**set_debug_log_level**](DebugApi.md#set_debug_log_level) | **POST** /debug/chronicles/loglevel | Set log level at run time


# **get_debug_info**
> DebugInfo get_debug_info()

Gets node information

### Example


```python
import codex_api_client
from codex_api_client.models.debug_info import DebugInfo
from codex_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api/codex/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = codex_api_client.Configuration(
    host = "http://localhost:8080/api/codex/v1"
)


# Enter a context with an instance of the API client
with codex_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codex_api_client.DebugApi(api_client)

    try:
        # Gets node information
        api_response = api_instance.get_debug_info()
        print("The response of DebugApi->get_debug_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->get_debug_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DebugInfo**](DebugInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node&#39;s information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_debug_log_level**
> set_debug_log_level(level)

Set log level at run time

### Example


```python
import codex_api_client
from codex_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api/codex/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = codex_api_client.Configuration(
    host = "http://localhost:8080/api/codex/v1"
)


# Enter a context with an instance of the API client
with codex_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codex_api_client.DebugApi(api_client)
    level = 'level_example' # str | 

    try:
        # Set log level at run time
        api_instance.set_debug_log_level(level)
    except Exception as e:
        print("Exception when calling DebugApi->set_debug_log_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully log level set |  -  |
**400** | Invalid or missing log level |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

