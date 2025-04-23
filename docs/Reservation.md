# Reservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | 
**availability_id** | **str** | 32bits identifier encoded in hex-decimal string. | 
**size** | **int** | Size of the slot in bytes | 
**request_id** | **str** | 32bits identifier encoded in hex-decimal string. | 
**slot_index** | **int** | Slot Index number | 
**valid_until** | **int** | Timestamp after which the reservation will no longer be valid. | 

## Example

```python
from codex_api_client.models.reservation import Reservation

# TODO update the JSON string below
json = "{}"
# create an instance of Reservation from a JSON string
reservation_instance = Reservation.from_json(json)
# print the JSON string representation of the object
print(Reservation.to_json())

# convert the object into a dict
reservation_dict = reservation_instance.to_dict()
# create an instance of Reservation from a dict
reservation_from_dict = Reservation.from_dict(reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


