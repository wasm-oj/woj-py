# ApiAuthSendPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User&#39;s email address | 
**ttl** | **int** | Token&#39;s time to live in days | [default to 1]

## Example

```python
from woj.models.api_auth_send_post_request import ApiAuthSendPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAuthSendPostRequest from a JSON string
api_auth_send_post_request_instance = ApiAuthSendPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiAuthSendPostRequest.to_json()

# convert the object into a dict
api_auth_send_post_request_dict = api_auth_send_post_request_instance.to_dict()
# create an instance of ApiAuthSendPostRequest from a dict
api_auth_send_post_request_form_dict = api_auth_send_post_request.from_dict(api_auth_send_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


