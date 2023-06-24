# ApiProblemIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**problem** | [**ApiProblemIdGet200ResponseProblem**](ApiProblemIdGet200ResponseProblem.md) |  | 

## Example

```python
from woj.models.api_problem_id_get200_response import ApiProblemIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemIdGet200Response from a JSON string
api_problem_id_get200_response_instance = ApiProblemIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiProblemIdGet200Response.to_json()

# convert the object into a dict
api_problem_id_get200_response_dict = api_problem_id_get200_response_instance.to_dict()
# create an instance of ApiProblemIdGet200Response from a dict
api_problem_id_get200_response_form_dict = api_problem_id_get200_response.from_dict(api_problem_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


