# ApiSubmissionGet200ResponseSubmissionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code_lang** | **str** |  | 
**problem_id** | **str** |  | 
**status** | **str** |  | 
**submitter_id** | **str** |  | 
**score** | **float** |  | 
**cost** | **float** |  | 
**memory** | **float** |  | 

## Example

```python
from woj.models.api_submission_get200_response_submissions_inner import ApiSubmissionGet200ResponseSubmissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubmissionGet200ResponseSubmissionsInner from a JSON string
api_submission_get200_response_submissions_inner_instance = ApiSubmissionGet200ResponseSubmissionsInner.from_json(json)
# print the JSON string representation of the object
print ApiSubmissionGet200ResponseSubmissionsInner.to_json()

# convert the object into a dict
api_submission_get200_response_submissions_inner_dict = api_submission_get200_response_submissions_inner_instance.to_dict()
# create an instance of ApiSubmissionGet200ResponseSubmissionsInner from a dict
api_submission_get200_response_submissions_inner_form_dict = api_submission_get200_response_submissions_inner.from_dict(api_submission_get200_response_submissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


