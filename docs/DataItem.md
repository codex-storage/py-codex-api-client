# DataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **str** | Content Identifier as specified at https://github.com/multiformats/cid | 
**manifest** | [**ManifestItem**](ManifestItem.md) |  | 

## Example

```python
from codex_api_client.models.data_item import DataItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataItem from a JSON string
data_item_instance = DataItem.from_json(json)
# print the JSON string representation of the object
print(DataItem.to_json())

# convert the object into a dict
data_item_dict = data_item_instance.to_dict()
# create an instance of DataItem from a dict
data_item_from_dict = DataItem.from_dict(data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


