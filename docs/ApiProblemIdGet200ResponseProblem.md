# ApiProblemIdGet200ResponseProblem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**description** | **str** |  | 
**policy** | [**List[ApiProblemIdGet200ResponseProblemPolicyInner]**](ApiProblemIdGet200ResponseProblemPolicyInner.md) |  | 
**testcase** | [**List[ApiProblemIdGet200ResponseProblemTestcaseInner]**](ApiProblemIdGet200ResponseProblemTestcaseInner.md) |  | 
**input** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from woj.models.api_problem_id_get200_response_problem import ApiProblemIdGet200ResponseProblem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemIdGet200ResponseProblem from a JSON string
api_problem_id_get200_response_problem_instance = ApiProblemIdGet200ResponseProblem.from_json(json)
# print the JSON string representation of the object
print ApiProblemIdGet200ResponseProblem.to_json()

# convert the object into a dict
api_problem_id_get200_response_problem_dict = api_problem_id_get200_response_problem_instance.to_dict()
# create an instance of ApiProblemIdGet200ResponseProblem from a dict
api_problem_id_get200_response_problem_form_dict = api_problem_id_get200_response_problem.from_dict(api_problem_id_get200_response_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


