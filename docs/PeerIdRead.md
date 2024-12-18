# PeerIdRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Peer Identity reference as specified at https://docs.libp2p.io/concepts/fundamentals/peers/ | [optional] 

## Example

```python
from codex_api_client.models.peer_id_read import PeerIdRead

# TODO update the JSON string below
json = "{}"
# create an instance of PeerIdRead from a JSON string
peer_id_read_instance = PeerIdRead.from_json(json)
# print the JSON string representation of the object
print(PeerIdRead.to_json())

# convert the object into a dict
peer_id_read_dict = peer_id_read_instance.to_dict()
# create an instance of PeerIdRead from a dict
peer_id_read_from_dict = PeerIdRead.from_dict(peer_id_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


