# Purchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Description of the Request&#39;s state | 
**error** | **str** | If Request failed, then here is presented the error message | [optional] 
**request** | [**StorageRequest**](StorageRequest.md) |  | [optional] 
**request_id** | **str** | 32bits identifier encoded in hex-decimal string. | 

## Example

```python
from codex_api_client.models.purchase import Purchase

# TODO update the JSON string below
json = "{}"
# create an instance of Purchase from a JSON string
purchase_instance = Purchase.from_json(json)
# print the JSON string representation of the object
print(Purchase.to_json())

# convert the object into a dict
purchase_dict = purchase_instance.to_dict()
# create an instance of Purchase from a dict
purchase_from_dict = Purchase.from_dict(purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


