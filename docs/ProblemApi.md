# woj.ProblemApi

All URIs are relative to *https://woj.csie.cool*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_problem_get**](ProblemApi.md#api_problem_get) | **GET** /api/problem | 
[**api_problem_id_get**](ProblemApi.md#api_problem_id_get) | **GET** /api/problem/{id} | 


# **api_problem_get**
> ApiProblemGet200Response api_problem_get()



### Example

```python
import time
import os
import woj
from woj.models.api_problem_get200_response import ApiProblemGet200Response
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
    api_instance = woj.ProblemApi(api_client)

    try:
        api_response = api_instance.api_problem_get()
        print("The response of ProblemApi->api_problem_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProblemApi->api_problem_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiProblemGet200Response**](ApiProblemGet200Response.md)

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

# **api_problem_id_get**
> ApiProblemIdGet200Response api_problem_id_get(id)



### Example

```python
import time
import os
import woj
from woj.models.api_problem_id_get200_response import ApiProblemIdGet200Response
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
    api_instance = woj.ProblemApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_problem_id_get(id)
        print("The response of ProblemApi->api_problem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProblemApi->api_problem_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiProblemIdGet200Response**](ApiProblemIdGet200Response.md)

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

