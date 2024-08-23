# ErasureParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_chunks** | **int** |  | [optional] 

## Example

```python
from codex_client.models.erasure_parameters import ErasureParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ErasureParameters from a JSON string
erasure_parameters_instance = ErasureParameters.from_json(json)
# print the JSON string representation of the object
print(ErasureParameters.to_json())

# convert the object into a dict
erasure_parameters_dict = erasure_parameters_instance.to_dict()
# create an instance of ErasureParameters from a dict
erasure_parameters_from_dict = ErasureParameters.from_dict(erasure_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


