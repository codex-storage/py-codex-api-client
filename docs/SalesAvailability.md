# SalesAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_size** | **int** | Total size of availability&#39;s storage in bytes | 
**duration** | **int** | The duration of the request in seconds | 
**min_price_per_byte_per_second** | **str** | Minimal price per byte per second paid (in amount of tokens) for the hosted request&#39;s slot for the request&#39;s duration as decimal string | 
**total_collateral** | **str** | Total collateral (in amount of tokens) that can be used for matching requests | 
**enabled** | **bool** | Enable the ability to receive sales on this availability. | [optional] [default to True]
**until** | **int** | Specifies the latest timestamp, after which the availability will no longer host any slots. If set to 0, there will be no restrictions. | [optional] [default to 0]

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


