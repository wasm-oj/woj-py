# ApiMeGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | [optional] 
**email** | **str** | User&#39;s email | [optional] 
**exp** | **float** | Token expiration time, in seconds since epoch | [optional] 
**pea** | **str** | The PEA login URL that this app uses | 

## Example

```python
from woj.models.api_me_get200_response import ApiMeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMeGet200Response from a JSON string
api_me_get200_response_instance = ApiMeGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiMeGet200Response.to_json()

# convert the object into a dict
api_me_get200_response_dict = api_me_get200_response_instance.to_dict()
# create an instance of ApiMeGet200Response from a dict
api_me_get200_response_form_dict = api_me_get200_response.from_dict(api_me_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


