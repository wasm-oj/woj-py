# ApiSubmissionIdGet200ResponseSubmission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**submitter_id** | **str** |  | 
**status** | **str** |  | 
**code** | **str** |  | 
**code_lang** | **str** |  | 
**problem_id** | **str** |  | 
**compiler_version** | **str** |  | 
**runner_version** | **str** |  | 
**score** | **float** |  | 
**cost** | **float** |  | 
**memory** | **float** |  | 
**details** | **str** |  | 

## Example

```python
from woj.models.api_submission_id_get200_response_submission import ApiSubmissionIdGet200ResponseSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubmissionIdGet200ResponseSubmission from a JSON string
api_submission_id_get200_response_submission_instance = ApiSubmissionIdGet200ResponseSubmission.from_json(json)
# print the JSON string representation of the object
print ApiSubmissionIdGet200ResponseSubmission.to_json()

# convert the object into a dict
api_submission_id_get200_response_submission_dict = api_submission_id_get200_response_submission_instance.to_dict()
# create an instance of ApiSubmissionIdGet200ResponseSubmission from a dict
api_submission_id_get200_response_submission_form_dict = api_submission_id_get200_response_submission.from_dict(api_submission_id_get200_response_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


