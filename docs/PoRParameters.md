# PoRParameters

Parameters for Proof of Retrievability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**u** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from codex_client.models.po_r_parameters import PoRParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PoRParameters from a JSON string
po_r_parameters_instance = PoRParameters.from_json(json)
# print the JSON string representation of the object
print(PoRParameters.to_json())

# convert the object into a dict
po_r_parameters_dict = po_r_parameters_instance.to_dict()
# create an instance of PoRParameters from a dict
po_r_parameters_from_dict = PoRParameters.from_dict(po_r_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


