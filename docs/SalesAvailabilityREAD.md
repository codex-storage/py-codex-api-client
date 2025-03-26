# SalesAvailabilityREAD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 32bits identifier encoded in hex-decimal string. | [optional] 
**total_size** | **str** | Total size of availability&#39;s storage in bytes as decimal string | [optional] 
**duration** | **str** | The duration of the request in seconds as decimal string | [optional] 
**min_price_per_byte_per_second** | **str** | Minimal price per byte per second paid (in amount of tokens) for the hosted request&#39;s slot for the request&#39;s duration as decimal string | [optional] 
**total_collateral** | **str** | Total collateral (in amount of tokens) that can be used for matching requests | [optional] 
**free_size** | **str** | Unused size of availability&#39;s storage in bytes as decimal string | [optional] 

## Example

```python
from codex_api_client.models.sales_availability_read import SalesAvailabilityREAD

# TODO update the JSON string below
json = "{}"
# create an instance of SalesAvailabilityREAD from a JSON string
sales_availability_read_instance = SalesAvailabilityREAD.from_json(json)
# print the JSON string representation of the object
print(SalesAvailabilityREAD.to_json())

# convert the object into a dict
sales_availability_read_dict = sales_availability_read_instance.to_dict()
# create an instance of SalesAvailabilityREAD from a dict
sales_availability_read_from_dict = SalesAvailabilityREAD.from_dict(sales_availability_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


