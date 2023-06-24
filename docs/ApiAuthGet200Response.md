# ApiAuthGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** | Whether the token is valid | 
**new** | **bool** | Whether the user is new | 

## Example

```python
from woj.models.api_auth_get200_response import ApiAuthGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAuthGet200Response from a JSON string
api_auth_get200_response_instance = ApiAuthGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiAuthGet200Response.to_json()

# convert the object into a dict
api_auth_get200_response_dict = api_auth_get200_response_instance.to_dict()
# create an instance of ApiAuthGet200Response from a dict
api_auth_get200_response_form_dict = api_auth_get200_response.from_dict(api_auth_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


