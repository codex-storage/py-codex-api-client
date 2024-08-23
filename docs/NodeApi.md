# codex_client.NodeApi

All URIs are relative to *http://localhost:8080/api/codex/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_peer**](NodeApi.md#connect_peer) | **GET** /connect/{peerId} | Connect to a peer
[**get_peer_id**](NodeApi.md#get_peer_id) | **GET** /node/peerid | Get Node&#39;s PeerID
[**get_spr**](NodeApi.md#get_spr) | **GET** /node/spr | Get Node&#39;s SPR


# **connect_peer**
> connect_peer(peer_id, addrs=addrs)

Connect to a peer

If `addrs` param is supplied, it will be used to dial the peer, otherwise the `peerId` is used to invoke peer discovery, if it succeeds the returned addresses will be used to dial. 

### Example


```python
import codex_client
from codex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api/codex/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = codex_client.Configuration(
    host = "http://localhost:8080/api/codex/v1"
)


# Enter a context with an instance of the API client
with codex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codex_client.NodeApi(api_client)
    peer_id = 'peer_id_example' # str | Peer that should be dialed.
    addrs = ['addrs_example'] # List[str] | If supplied, it will be used to dial the peer. The address has to target the listening address of the peer, which is specified with the `--listen-addrs` CLI flag.  (optional)

    try:
        # Connect to a peer
        api_instance.connect_peer(peer_id, addrs=addrs)
    except Exception as e:
        print("Exception when calling NodeApi->connect_peer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_id** | **str**| Peer that should be dialed. | 
 **addrs** | [**List[str]**](str.md)| If supplied, it will be used to dial the peer. The address has to target the listening address of the peer, which is specified with the &#x60;--listen-addrs&#x60; CLI flag.  | [optional] 

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
**200** | Successfully connected to peer |  -  |
**400** | Peer either not found or was not possible to dial |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_id**
> str get_peer_id()

Get Node's PeerID

### Example


```python
import codex_client
from codex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api/codex/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = codex_client.Configuration(
    host = "http://localhost:8080/api/codex/v1"
)


# Enter a context with an instance of the API client
with codex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codex_client.NodeApi(api_client)

    try:
        # Get Node's PeerID
        api_response = api_instance.get_peer_id()
        print("The response of NodeApi->get_peer_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_peer_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: plain/text, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node&#39;s Peer ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spr**
> str get_spr()

Get Node's SPR

### Example


```python
import codex_client
from codex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api/codex/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = codex_client.Configuration(
    host = "http://localhost:8080/api/codex/v1"
)


# Enter a context with an instance of the API client
with codex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codex_client.NodeApi(api_client)

    try:
        # Get Node's SPR
        api_response = api_instance.get_spr()
        print("The response of NodeApi->get_spr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_spr: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: plain/text, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node&#39;s SPR |  -  |
**503** | Node SPR not ready, try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

