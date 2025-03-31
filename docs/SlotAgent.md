# SlotAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Keccak hash of the abi encoded tuple (RequestId, slot index) | [optional] 
**slot_index** | **int** | Slot Index number | [optional] 
**request_id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**request** | [**StorageRequest**](StorageRequest.md) |  | [optional] 
**reservation** | [**Reservation**](Reservation.md) |  | [optional] 
**state** | **str** | Description of the slot&#39;s | [optional] 

## Example

```python
from codex_api_client.models.slot_agent import SlotAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SlotAgent from a JSON string
slot_agent_instance = SlotAgent.from_json(json)
# print the JSON string representation of the object
print(SlotAgent.to_json())

# convert the object into a dict
slot_agent_dict = slot_agent_instance.to_dict()
# create an instance of SlotAgent from a dict
slot_agent_from_dict = SlotAgent.from_dict(slot_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


