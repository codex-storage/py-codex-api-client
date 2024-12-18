# Space


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_blocks** | **int** | Number of blocks stored by the node | [optional] 
**quota_max_bytes** | **int** | Maximum storage space (in bytes) available for the node in Codex&#39;s local repository. | [optional] 
**quota_used_bytes** | **int** | Amount of storage space (in bytes) currently used for storing files in Codex&#39;s local repository. | [optional] 
**quota_reserved_bytes** | **int** | Amount of storage reserved (in bytes) in the Codex&#39;s local repository for future use when storage requests will be picked up and hosted by the node using node&#39;s availabilities. This does not include the storage currently in use. | [optional] 

## Example

```python
from codex_api_client.models.space import Space

# TODO update the JSON string below
json = "{}"
# create an instance of Space from a JSON string
space_instance = Space.from_json(json)
# print the JSON string representation of the object
print(Space.to_json())

# convert the object into a dict
space_dict = space_instance.to_dict()
# create an instance of Space from a dict
space_from_dict = Space.from_dict(space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


