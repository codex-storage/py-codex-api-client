# SalesAvailabilityCREATE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**total_size** | **int** | Total size of availability&#39;s storage in bytes | 
**duration** | **int** | The duration of the request in seconds | 
**min_price_per_byte_per_second** | **str** | Minimal price per byte per second paid (in amount of tokens) for the hosted request&#39;s slot for the request&#39;s duration as decimal string | 
**total_collateral** | **str** | Total collateral (in amount of tokens) that can be used for matching requests | 

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


