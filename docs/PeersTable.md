# PeersTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_node** | [**Node**](Node.md) |  | 
**nodes** | [**List[Node]**](Node.md) |  | 

## Example

```python
from codex_api_client.models.peers_table import PeersTable

# TODO update the JSON string below
json = "{}"
# create an instance of PeersTable from a JSON string
peers_table_instance = PeersTable.from_json(json)
# print the JSON string representation of the object
print(PeersTable.to_json())

# convert the object into a dict
peers_table_dict = peers_table_instance.to_dict()
# create an instance of PeersTable from a dict
peers_table_from_dict = PeersTable.from_dict(peers_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


