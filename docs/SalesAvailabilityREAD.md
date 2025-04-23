# SalesAvailabilityREAD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_size** | **int** | Total size of availability&#39;s storage in bytes | 
**duration** | **int** | The duration of the request in seconds | 
**min_price_per_byte_per_second** | **str** | Minimal price per byte per second paid (in amount of tokens) for the hosted request&#39;s slot for the request&#39;s duration as decimal string | 
**total_collateral** | **str** | Total collateral (in amount of tokens) that can be used for matching requests | 
**enabled** | **bool** | Enable the ability to receive sales on this availability. | [optional] [default to True]
**until** | **int** | Specifies the latest timestamp, after which the availability will no longer host any slots. If set to 0, there will be no restrictions. | [optional] [default to 0]
**id** | **str** | 32bits identifier encoded in hex-decimal string. | 
**free_size** | **int** | Unused size of availability&#39;s storage in bytes as decimal string | [optional] [readonly] 
**total_remaining_collateral** | **str** | Total collateral effective (in amount of tokens) that can be used for matching requests | [readonly] 

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


