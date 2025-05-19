# codex_api_client.DataApi

All URIs are relative to *http://localhost:8080/api/codex/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_local**](DataApi.md#delete_local) | **DELETE** /data/{cid} | Deletes either a single block or an entire dataset from the local node.
[**download_local**](DataApi.md#download_local) | **GET** /data/{cid} | Download a file from the local node in a streaming manner. If the file is not available locally, a 404 is returned.
[**download_network**](DataApi.md#download_network) | **POST** /data/{cid}/network | Download a file from the network to the local node if it&#39;s not available locally. Note: Download is performed async. Call can return before download is completed.
[**download_network_manifest**](DataApi.md#download_network_manifest) | **GET** /data/{cid}/network/manifest | Download only the dataset manifest from the network to the local node if it&#39;s not available locally.
[**download_network_stream**](DataApi.md#download_network_stream) | **GET** /data/{cid}/network/stream | Download a file from the network in a streaming manner. If the file is not available locally, it will be retrieved from other nodes in the network if able.
[**list_data**](DataApi.md#list_data) | **GET** /data | Lists manifest CIDs stored locally in node.
[**space**](DataApi.md#space) | **GET** /space | Gets a summary of the storage space allocation of the node.
[**upload**](DataApi.md#upload) | **POST** /data | Upload a file in a streaming manner. Once finished, the file is stored in the node and can be retrieved by any node in the network using the returned CID.


# **delete_local**
> delete_local(cid)

Deletes either a single block or an entire dataset from the local node.

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
    api_instance = codex_api_client.DataApi(api_client)
    cid = 'cid_example' # str | Block or dataset to be deleted.

    try:
        # Deletes either a single block or an entire dataset from the local node.
        api_instance.delete_local(cid)
    except Exception as e:
        print("Exception when calling DataApi->delete_local: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Block or dataset to be deleted. | 

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
**204** | Data was successfully deleted. |  -  |
**400** | Invalid CID is specified |  -  |
**500** | There was an error during deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_local**
> bytearray download_local(cid)

Download a file from the local node in a streaming manner. If the file is not available locally, a 404 is returned.

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
    api_instance = codex_api_client.DataApi(api_client)
    cid = 'cid_example' # str | File to be downloaded.

    try:
        # Download a file from the local node in a streaming manner. If the file is not available locally, a 404 is returned.
        api_response = api_instance.download_local(cid)
        print("The response of DataApi->download_local:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_local: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| File to be downloaded. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved content specified by CID |  -  |
**400** | Invalid CID is specified |  -  |
**404** | Content specified by the CID is unavailable locally |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_network**
> DataItem download_network(cid)

Download a file from the network to the local node if it's not available locally. Note: Download is performed async. Call can return before download is completed.

### Example


```python
import codex_api_client
from codex_api_client.models.data_item import DataItem
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
    api_instance = codex_api_client.DataApi(api_client)
    cid = 'cid_example' # str | File to be downloaded.

    try:
        # Download a file from the network to the local node if it's not available locally. Note: Download is performed async. Call can return before download is completed.
        api_response = api_instance.download_network(cid)
        print("The response of DataApi->download_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| File to be downloaded. | 

### Return type

[**DataItem**](DataItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manifest information for download that has been started. |  -  |
**400** | Invalid CID is specified |  -  |
**404** | Failed to download dataset manifest |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_network_manifest**
> DataItem download_network_manifest(cid)

Download only the dataset manifest from the network to the local node if it's not available locally.

### Example


```python
import codex_api_client
from codex_api_client.models.data_item import DataItem
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
    api_instance = codex_api_client.DataApi(api_client)
    cid = 'cid_example' # str | File for which the manifest is to be downloaded.

    try:
        # Download only the dataset manifest from the network to the local node if it's not available locally.
        api_response = api_instance.download_network_manifest(cid)
        print("The response of DataApi->download_network_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_network_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| File for which the manifest is to be downloaded. | 

### Return type

[**DataItem**](DataItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manifest information. |  -  |
**400** | Invalid CID is specified |  -  |
**404** | Failed to download dataset manifest |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_network_stream**
> bytearray download_network_stream(cid)

Download a file from the network in a streaming manner. If the file is not available locally, it will be retrieved from other nodes in the network if able.

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
    api_instance = codex_api_client.DataApi(api_client)
    cid = 'cid_example' # str | File to be downloaded.

    try:
        # Download a file from the network in a streaming manner. If the file is not available locally, it will be retrieved from other nodes in the network if able.
        api_response = api_instance.download_network_stream(cid)
        print("The response of DataApi->download_network_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_network_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| File to be downloaded. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved content specified by CID |  -  |
**400** | Invalid CID is specified |  -  |
**404** | Content specified by the CID is not found |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data**
> DataList list_data()

Lists manifest CIDs stored locally in node.

### Example


```python
import codex_api_client
from codex_api_client.models.data_list import DataList
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
    api_instance = codex_api_client.DataApi(api_client)

    try:
        # Lists manifest CIDs stored locally in node.
        api_response = api_instance.list_data()
        print("The response of DataApi->list_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->list_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataList**](DataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved list of content CIDs |  -  |
**400** | Invalid CID is specified |  -  |
**404** | Content specified by the CID is not found |  -  |
**422** | The content type is not a valid content type or the filename is not valid |  -  |
**500** | Well it was bad-bad |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space**
> Space space()

Gets a summary of the storage space allocation of the node.

### Example


```python
import codex_api_client
from codex_api_client.models.space import Space
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
    api_instance = codex_api_client.DataApi(api_client)

    try:
        # Gets a summary of the storage space allocation of the node.
        api_response = api_instance.space()
        print("The response of DataApi->space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->space: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of storage allocation |  -  |
**500** | It&#39;s not working as planned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> str upload(content_type=content_type, content_disposition=content_disposition, body=body)

Upload a file in a streaming manner. Once finished, the file is stored in the node and can be retrieved by any node in the network using the returned CID.

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
    api_instance = codex_api_client.DataApi(api_client)
    content_type = 'image/png' # str | The content type of the file. Must be valid. (optional)
    content_disposition = 'attachment; filename=\"codex.png\"' # str | The content disposition used to send the filename. (optional)
    body = None # bytearray |  (optional)

    try:
        # Upload a file in a streaming manner. Once finished, the file is stored in the node and can be retrieved by any node in the network using the returned CID.
        api_response = api_instance.upload(content_type=content_type, content_disposition=content_disposition, body=body)
        print("The response of DataApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the file. Must be valid. | [optional] 
 **content_disposition** | **str**| The content disposition used to send the filename. | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CID of uploaded file |  -  |
**422** | The mimetype of the filename is invalid |  -  |
**500** | Well it was bad-bad and the upload did not work out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

