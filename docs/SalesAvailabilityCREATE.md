# SalesAvailabilityCREATE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**total_size** | **str** | Total size of availability&#39;s storage in bytes as decimal string | 
**duration** | **str** | The duration of the request in seconds as decimal string | 
**min_price** | **str** | Minimal price paid (in amount of tokens) for the whole hosted request&#39;s slot for the request&#39;s duration as decimal string | 
**max_collateral** | **str** | Maximum collateral user is willing to pay per filled Slot (in amount of tokens) as decimal string | 

## Example

```python
from codex_api_client.models.sales_availability_create import SalesAvailabilityCREATE

# TODO update the JSON string below
json = "{}"
# create an instance of SalesAvailabilityCREATE from a JSON string
sales_availability_create_instance = SalesAvailabilityCREATE.from_json(json)
# print the JSON string representation of the object
print(SalesAvailabilityCREATE.to_json())

# convert the object into a dict
sales_availability_create_dict = sales_availability_create_instance.to_dict()
# create an instance of SalesAvailabilityCREATE from a dict
sales_availability_create_from_dict = SalesAvailabilityCREATE.from_dict(sales_availability_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


