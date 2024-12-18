# ManifestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tree_cid** | **str** | Content Identifier as specified at https://github.com/multiformats/cid | [optional] 
**dataset_size** | **int** | Length of original content in bytes | [optional] 
**block_size** | **int** | Size of blocks | [optional] 
**protected** | **bool** | Indicates if content is protected by erasure-coding | [optional] 
**filename** | **str** | The original name of the uploaded content (optional) | [optional] 
**mimetype** | **str** | The original mimetype of the uploaded content (optional) | [optional] 
**uploaded_at** | **int** | The UTC upload timestamp in seconds | [optional] 

## Example

```python
from codex_api_client.models.manifest_item import ManifestItem

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestItem from a JSON string
manifest_item_instance = ManifestItem.from_json(json)
# print the JSON string representation of the object
print(ManifestItem.to_json())

# convert the object into a dict
manifest_item_dict = manifest_item_instance.to_dict()
# create an instance of ManifestItem from a dict
manifest_item_from_dict = ManifestItem.from_dict(manifest_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


