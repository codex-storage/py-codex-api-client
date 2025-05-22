# codex_api_client.MarketplaceApi

All URIs are relative to *http://localhost:8080/api/codex/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_request**](MarketplaceApi.md#create_storage_request) | **POST** /storage/request/{cid} | Creates a new Request for storage
[**get_active_slot_by_id**](MarketplaceApi.md#get_active_slot_by_id) | **GET** /sales/slots/{slotId} | Returns active slot with id {slotId} for the host
[**get_active_slots**](MarketplaceApi.md#get_active_slots) | **GET** /sales/slots | Returns active slots
[**get_availabilities**](MarketplaceApi.md#get_availabilities) | **GET** /sales/availability | Returns storage that is for sale
[**get_purchase**](MarketplaceApi.md#get_purchase) | **GET** /storage/purchases/{id} | Returns purchase details
[**get_purchases**](MarketplaceApi.md#get_purchases) | **GET** /storage/purchases | Returns list of purchase IDs
[**get_reservations**](MarketplaceApi.md#get_reservations) | **GET** /sales/availability/{id}/reservations | Get availability&#39;s reservations
[**offer_storage**](MarketplaceApi.md#offer_storage) | **POST** /sales/availability | Offers storage for sale
[**update_offered_storage**](MarketplaceApi.md#update_offered_storage) | **PATCH** /sales/availability/{id} | Updates availability


# **create_storage_request**
> str create_storage_request(cid, storage_request_creation=storage_request_creation)

Creates a new Request for storage

### Example


```python
import codex_api_client
from codex_api_client.models.storage_request_creation import StorageRequestCreation
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    cid = 'cid_example' # str | CID of the uploaded data that should be stored
    storage_request_creation = codex_api_client.StorageRequestCreation() # StorageRequestCreation |  (optional)

    try:
        # Creates a new Request for storage
        api_response = api_instance.create_storage_request(cid, storage_request_creation=storage_request_creation)
        print("The response of MarketplaceApi->create_storage_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->create_storage_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| CID of the uploaded data that should be stored | 
 **storage_request_creation** | [**StorageRequestCreation**](StorageRequestCreation.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the Request ID as decimal string |  -  |
**400** | Invalid or missing Request ID |  -  |
**422** | The storage request parameters are not valid |  -  |
**404** | Request ID not found |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_slot_by_id**
> SlotAgent get_active_slot_by_id(slot_id)

Returns active slot with id {slotId} for the host

### Example


```python
import codex_api_client
from codex_api_client.models.slot_agent import SlotAgent
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    slot_id = 'slot_id_example' # str | File to be downloaded.

    try:
        # Returns active slot with id {slotId} for the host
        api_response = api_instance.get_active_slot_by_id(slot_id)
        print("The response of MarketplaceApi->get_active_slot_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_active_slot_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_id** | **str**| File to be downloaded. | 

### Return type

[**SlotAgent**](SlotAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved active slot |  -  |
**400** | Invalid or missing SlotId |  -  |
**404** | Host is not in an active sale for the slot |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_slots**
> List[Slot] get_active_slots()

Returns active slots

### Example


```python
import codex_api_client
from codex_api_client.models.slot import Slot
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
    api_instance = codex_api_client.MarketplaceApi(api_client)

    try:
        # Returns active slots
        api_response = api_instance.get_active_slots()
        print("The response of MarketplaceApi->get_active_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_active_slots: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Slot]**](Slot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved active slots |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availabilities**
> List[SalesAvailabilityREAD] get_availabilities()

Returns storage that is for sale

### Example


```python
import codex_api_client
from codex_api_client.models.sales_availability_read import SalesAvailabilityREAD
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
    api_instance = codex_api_client.MarketplaceApi(api_client)

    try:
        # Returns storage that is for sale
        api_response = api_instance.get_availabilities()
        print("The response of MarketplaceApi->get_availabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_availabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SalesAvailabilityREAD]**](SalesAvailabilityREAD.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved storage availabilities of the node |  -  |
**500** | Error getting unused availabilities |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase**
> Purchase get_purchase(id)

Returns purchase details

### Example


```python
import codex_api_client
from codex_api_client.models.purchase import Purchase
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | Hexadecimal ID of a Purchase

    try:
        # Returns purchase details
        api_response = api_instance.get_purchase(id)
        print("The response of MarketplaceApi->get_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hexadecimal ID of a Purchase | 

### Return type

[**Purchase**](Purchase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Purchase details |  -  |
**400** | Invalid or missing Purchase ID |  -  |
**404** | Purchase not found |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchases**
> List[str] get_purchases()

Returns list of purchase IDs

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
    api_instance = codex_api_client.MarketplaceApi(api_client)

    try:
        # Returns list of purchase IDs
        api_response = api_instance.get_purchases()
        print("The response of MarketplaceApi->get_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_purchases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets all purchase IDs stored in node |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations**
> List[Reservation] get_reservations(id)

Get availability's reservations

Return's list of Reservations for ongoing Storage Requests that the node hosts.

### Example


```python
import codex_api_client
from codex_api_client.models.reservation import Reservation
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | ID of Availability

    try:
        # Get availability's reservations
        api_response = api_instance.get_reservations(id)
        print("The response of MarketplaceApi->get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Availability | 

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved storage availabilities of the node |  -  |
**400** | Invalid Availability ID |  -  |
**404** | Availability not found |  -  |
**500** | Error getting reservations |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offer_storage**
> SalesAvailabilityREAD offer_storage(sales_availability=sales_availability)

Offers storage for sale

### Example


```python
import codex_api_client
from codex_api_client.models.sales_availability import SalesAvailability
from codex_api_client.models.sales_availability_read import SalesAvailabilityREAD
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    sales_availability = codex_api_client.SalesAvailability() # SalesAvailability |  (optional)

    try:
        # Offers storage for sale
        api_response = api_instance.offer_storage(sales_availability=sales_availability)
        print("The response of MarketplaceApi->offer_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->offer_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_availability** | [**SalesAvailability**](SalesAvailability.md)|  | [optional] 

### Return type

[**SalesAvailabilityREAD**](SalesAvailabilityREAD.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created storage availability |  -  |
**400** | Invalid data input |  -  |
**422** | Not enough node&#39;s storage quota available or the provided parameters did not pass validation |  -  |
**500** | Error reserving availability |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offered_storage**
> update_offered_storage(id, sales_availability=sales_availability)

Updates availability

The new parameters will be only considered for new requests.
Existing Requests linked to this Availability will continue as is.


### Example


```python
import codex_api_client
from codex_api_client.models.sales_availability import SalesAvailability
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
    api_instance = codex_api_client.MarketplaceApi(api_client)
    id = 'id_example' # str | ID of Availability
    sales_availability = codex_api_client.SalesAvailability() # SalesAvailability |  (optional)

    try:
        # Updates availability
        api_instance.update_offered_storage(id, sales_availability=sales_availability)
    except Exception as e:
        print("Exception when calling MarketplaceApi->update_offered_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Availability | 
 **sales_availability** | [**SalesAvailability**](SalesAvailability.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Availability successfully updated |  -  |
**400** | Invalid data input |  -  |
**404** | Availability not found |  -  |
**422** | The provided parameters did not pass validation |  -  |
**500** | Error reserving availability |  -  |
**503** | Persistence is not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

