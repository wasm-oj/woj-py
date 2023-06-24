# ApiSysGet200ResponseStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **float** | Number of users | 
**submission** | **float** | Number of submissions | 
**problem** | **float** | Number of problems | 

## Example

```python
from woj.models.api_sys_get200_response_stat import ApiSysGet200ResponseStat

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSysGet200ResponseStat from a JSON string
api_sys_get200_response_stat_instance = ApiSysGet200ResponseStat.from_json(json)
# print the JSON string representation of the object
print ApiSysGet200ResponseStat.to_json()

# convert the object into a dict
api_sys_get200_response_stat_dict = api_sys_get200_response_stat_instance.to_dict()
# create an instance of ApiSysGet200ResponseStat from a dict
api_sys_get200_response_stat_form_dict = api_sys_get200_response_stat.from_dict(api_sys_get200_response_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


