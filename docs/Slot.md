# Slot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Keccak hash of the abi encoded tuple (RequestId, slot index) | [optional] 
**request** | [**StorageRequest**](StorageRequest.md) |  | [optional] 
**slot_index** | **str** | Slot Index as decimal string | [optional] 

## Example

```python
from codex_api_client.models.slot import Slot

# TODO update the JSON string below
json = "{}"
# create an instance of Slot from a JSON string
slot_instance = Slot.from_json(json)
# print the JSON string representation of the object
print(Slot.to_json())

# convert the object into a dict
slot_dict = slot_instance.to_dict()
# create an instance of Slot from a dict
slot_from_dict = Slot.from_dict(slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


