# woj.SubmissionApi

All URIs are relative to *https://woj.csie.cool*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_submission_get**](SubmissionApi.md#api_submission_get) | **GET** /api/submission | 
[**api_submission_id_get**](SubmissionApi.md#api_submission_id_get) | **GET** /api/submission/{id} | 
[**submit**](SubmissionApi.md#submit) | **POST** /api/submission | 


# **api_submission_get**
> ApiSubmissionGet200Response api_submission_get(page=page, lang=lang, problem=problem, status=status, submitter=submitter)



### Example

```python
import time
import os
import woj
from woj.models.api_submission_get200_response import ApiSubmissionGet200Response
from woj.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://woj.csie.cool
# See configuration.py for a list of all supported configuration parameters.
configuration = woj.Configuration(
    host = "https://woj.csie.cool"
)


# Enter a context with an instance of the API client
with woj.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = woj.SubmissionApi(api_client)
    page = '1' # str |  (optional) (default to '1')
    lang = 'lang_example' # str |  (optional)
    problem = 'problem_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    submitter = 'submitter_example' # str |  (optional)

    try:
        api_response = api_instance.api_submission_get(page=page, lang=lang, problem=problem, status=status, submitter=submitter)
        print("The response of SubmissionApi->api_submission_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionApi->api_submission_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | [optional] [default to &#39;1&#39;]
 **lang** | **str**|  | [optional] 
 **problem** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **submitter** | **str**|  | [optional] 

### Return type

[**ApiSubmissionGet200Response**](ApiSubmissionGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input (path parameters, query string, or body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_submission_id_get**
> ApiSubmissionIdGet200Response api_submission_id_get(id)



### Example

```python
import time
import os
import woj
from woj.models.api_submission_id_get200_response import ApiSubmissionIdGet200Response
from woj.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://woj.csie.cool
# See configuration.py for a list of all supported configuration parameters.
configuration = woj.Configuration(
    host = "https://woj.csie.cool"
)


# Enter a context with an instance of the API client
with woj.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = woj.SubmissionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_submission_id_get(id)
        print("The response of SubmissionApi->api_submission_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionApi->api_submission_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiSubmissionIdGet200Response**](ApiSubmissionIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input (path parameters, query string, or body) |  -  |
**404** | Submission not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> Submit200Response submit(submit_request=submit_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import woj
from woj.models.submit200_response import Submit200Response
from woj.models.submit_request import SubmitRequest
from woj.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://woj.csie.cool
# See configuration.py for a list of all supported configuration parameters.
configuration = woj.Configuration(
    host = "https://woj.csie.cool"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = woj.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with woj.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = woj.SubmissionApi(api_client)
    submit_request = woj.SubmitRequest() # SubmitRequest |  (optional)

    try:
        api_response = api_instance.submit(submit_request=submit_request)
        print("The response of SubmissionApi->submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubmissionApi->submit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_request** | [**SubmitRequest**](SubmitRequest.md)|  | [optional] 

### Return type

[**Submit200Response**](Submit200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

