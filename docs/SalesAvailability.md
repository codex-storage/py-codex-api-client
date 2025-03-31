# SalesAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**total_size** | **int** | Total size of availability&#39;s storage in bytes | [optional] 
**duration** | **int** | The duration of the request in seconds | [optional] 
**min_price_per_byte_per_second** | **str** | Minimal price per byte per second paid (in amount of tokens) for the hosted request&#39;s slot for the request&#39;s duration as decimal string | [optional] 
**total_collateral** | **str** | Total collateral (in amount of tokens) that can be used for matching requests | [optional] 

## Example

```python
from codex_api_client.models.sales_availability import SalesAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of SalesAvailability from a JSON string
sales_availability_instance = SalesAvailability.from_json(json)
# print the JSON string representation of the object
print(SalesAvailability.to_json())

# convert the object into a dict
sales_availability_dict = sales_availability_instance.to_dict()
# create an instance of SalesAvailability from a dict
sales_availability_from_dict = SalesAvailability.from_dict(sales_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


