# DebugInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Peer Identity reference as specified at https://docs.libp2p.io/concepts/fundamentals/peers/ | [optional] 
**addrs** | **List[str]** |  | [optional] 
**repo** | **str** | Path of the data repository where all nodes data are stored | [optional] 
**spr** | **str** | Signed Peer Record (libp2p) | [optional] 
**announce_addresses** | **List[str]** |  | [optional] 
**table** | [**PeersTable**](PeersTable.md) |  | [optional] 
**codex** | [**CodexVersion**](CodexVersion.md) |  | [optional] 

## Example

```python
from codex_api_client.models.debug_info import DebugInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DebugInfo from a JSON string
debug_info_instance = DebugInfo.from_json(json)
# print the JSON string representation of the object
print(DebugInfo.to_json())

# convert the object into a dict
debug_info_dict = debug_info_instance.to_dict()
# create an instance of DebugInfo from a dict
debug_info_from_dict = DebugInfo.from_dict(debug_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


