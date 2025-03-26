# StorageRequestCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The duration of the request in seconds as decimal string | 
**price_per_byte_per_second** | **str** | The amount of tokens paid per byte per second per slot to hosts the client is willing to pay | 
**proof_probability** | **str** | How often storage proofs are required as decimal string | 
**nodes** | **int** | Minimal number of nodes the content should be stored on | [optional] [default to 1]
**tolerance** | **int** | Additional number of nodes on top of the &#x60;nodes&#x60; property that can be lost before pronouncing the content lost | [optional] [default to 0]
**collateral_per_byte** | **str** | Number as decimal string that represents how much collateral per byte is asked from hosts that wants to fill a slots | 
**expiry** | **str** | Number as decimal string that represents expiry threshold in seconds from when the Request is submitted. When the threshold is reached and the Request does not find requested amount of nodes to host the data, the Request is voided. The number of seconds can not be higher then the Request&#39;s duration itself. | 

## Example

```python
from codex_api_client.models.storage_request_creation import StorageRequestCreation

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequestCreation from a JSON string
storage_request_creation_instance = StorageRequestCreation.from_json(json)
# print the JSON string representation of the object
print(StorageRequestCreation.to_json())

# convert the object into a dict
storage_request_creation_dict = storage_request_creation_instance.to_dict()
# create an instance of StorageRequestCreation from a dict
storage_request_creation_from_dict = StorageRequestCreation.from_dict(storage_request_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


