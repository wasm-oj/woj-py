# ApiSubmissionGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submissions** | [**List[ApiSubmissionGet200ResponseSubmissionsInner]**](ApiSubmissionGet200ResponseSubmissionsInner.md) |  | 

## Example

```python
from woj.models.api_submission_get200_response import ApiSubmissionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubmissionGet200Response from a JSON string
api_submission_get200_response_instance = ApiSubmissionGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiSubmissionGet200Response.to_json()

# convert the object into a dict
api_submission_get200_response_dict = api_submission_get200_response_instance.to_dict()
# create an instance of ApiSubmissionGet200Response from a dict
api_submission_get200_response_form_dict = api_submission_get200_response.from_dict(api_submission_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


