# ApiProblemGet200ResponseProblemsInner

Problem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **Dict[str, float]** | Submission count of each status | 
**id** | **str** | Problem ID | 
**name** | **str** | Problem name | 
**tags** | **List[str]** | Problem tags | 

## Example

```python
from woj.models.api_problem_get200_response_problems_inner import ApiProblemGet200ResponseProblemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemGet200ResponseProblemsInner from a JSON string
api_problem_get200_response_problems_inner_instance = ApiProblemGet200ResponseProblemsInner.from_json(json)
# print the JSON string representation of the object
print ApiProblemGet200ResponseProblemsInner.to_json()

# convert the object into a dict
api_problem_get200_response_problems_inner_dict = api_problem_get200_response_problems_inner_instance.to_dict()
# create an instance of ApiProblemGet200ResponseProblemsInner from a dict
api_problem_get200_response_problems_inner_form_dict = api_problem_get200_response_problems_inner.from_dict(api_problem_get200_response_problems_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


