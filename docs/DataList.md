# DataList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DataItem]**](DataItem.md) |  | [optional] 

## Example

```python
from codex_api_client.models.data_list import DataList

# TODO update the JSON string below
json = "{}"
# create an instance of DataList from a JSON string
data_list_instance = DataList.from_json(json)
# print the JSON string representation of the object
print(DataList.to_json())

# convert the object into a dict
data_list_dict = data_list_instance.to_dict()
# create an instance of DataList from a dict
data_list_from_dict = DataList.from_dict(data_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


