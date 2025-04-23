# StorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Request ID | 
**client** | **str** | Address of Ethereum address | 
**ask** | [**StorageAsk**](StorageAsk.md) |  | 
**content** | [**Content**](Content.md) |  | 
**expiry** | **int** | A timestamp as seconds since unix epoch at which this request expires if the Request does not find requested amount of nodes to host the data. | 
**nonce** | **str** | Random data | 

## Example

```python
from codex_api_client.models.storage_request import StorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequest from a JSON string
storage_request_instance = StorageRequest.from_json(json)
# print the JSON string representation of the object
print(StorageRequest.to_json())

# convert the object into a dict
storage_request_dict = storage_request_instance.to_dict()
# create an instance of StorageRequest from a dict
storage_request_from_dict = StorageRequest.from_dict(storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


