# ApiSysGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cfg** | [**ApiSysGet200ResponseCfg**](ApiSysGet200ResponseCfg.md) |  | 
**stat** | [**ApiSysGet200ResponseStat**](ApiSysGet200ResponseStat.md) |  | 

## Example

```python
from woj.models.api_sys_get200_response import ApiSysGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSysGet200Response from a JSON string
api_sys_get200_response_instance = ApiSysGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiSysGet200Response.to_json()

# convert the object into a dict
api_sys_get200_response_dict = api_sys_get200_response_instance.to_dict()
# create an instance of ApiSysGet200Response from a dict
api_sys_get200_response_form_dict = api_sys_get200_response.from_dict(api_sys_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


