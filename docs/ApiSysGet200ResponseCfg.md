# ApiSysGet200ResponseCfg


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compilers** | **float** | Number of compilers configured | 
**runners** | **float** | Number of runners configured | 

## Example

```python
from woj.models.api_sys_get200_response_cfg import ApiSysGet200ResponseCfg

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSysGet200ResponseCfg from a JSON string
api_sys_get200_response_cfg_instance = ApiSysGet200ResponseCfg.from_json(json)
# print the JSON string representation of the object
print ApiSysGet200ResponseCfg.to_json()

# convert the object into a dict
api_sys_get200_response_cfg_dict = api_sys_get200_response_cfg_instance.to_dict()
# create an instance of ApiSysGet200ResponseCfg from a dict
api_sys_get200_response_cfg_form_dict = api_sys_get200_response_cfg.from_dict(api_sys_get200_response_cfg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


