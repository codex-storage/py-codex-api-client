# StorageAsk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | **int** | Number of slots (eq. hosts) that the Request want to have the content spread over | 
**slot_size** | **int** | Amount of storage per slot in bytes | 
**duration** | **int** | The duration of the request in seconds | 
**proof_probability** | **str** | How often storage proofs are required as decimal string | 
**price_per_byte_per_second** | **str** | The amount of tokens paid per byte per second per slot to hosts the client is willing to pay | 
**collateral_per_byte** | **str** | Number as decimal string that represents how much collateral per byte is asked from hosts that wants to fill a slots | 
**max_slot_loss** | **int** | Max slots that can be lost without data considered to be lost | 

## Example

```python
from codex_api_client.models.storage_ask import StorageAsk

# TODO update the JSON string below
json = "{}"
# create an instance of StorageAsk from a JSON string
storage_ask_instance = StorageAsk.from_json(json)
# print the JSON string representation of the object
print(StorageAsk.to_json())

# convert the object into a dict
storage_ask_dict = storage_ask_instance.to_dict()
# create an instance of StorageAsk from a dict
storage_ask_from_dict = StorageAsk.from_dict(storage_ask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


