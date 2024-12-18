# Reservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**availability_id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**size** | **str** | Integer represented as decimal string | [optional] 
**request_id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**slot_index** | **str** | Slot Index as decimal string | [optional] 

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


