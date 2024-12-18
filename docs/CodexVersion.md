# CodexVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 

## Example

```python
from codex_api_client.models.codex_version import CodexVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CodexVersion from a JSON string
codex_version_instance = CodexVersion.from_json(json)
# print the JSON string representation of the object
print(CodexVersion.to_json())

# convert the object into a dict
codex_version_dict = codex_version_instance.to_dict()
# create an instance of CodexVersion from a dict
codex_version_from_dict = CodexVersion.from_dict(codex_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


