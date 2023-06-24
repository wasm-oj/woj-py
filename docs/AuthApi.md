# woj.AuthApi

All URIs are relative to *https://woj.csie.cool*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_auth_get**](AuthApi.md#api_auth_get) | **GET** /api/auth | 
[**api_auth_send_post**](AuthApi.md#api_auth_send_post) | **POST** /api/auth/send | 


# **api_auth_get**
> ApiAuthGet200Response api_auth_get(token)



### Example

```python
import time
import os
import woj
from woj.models.api_auth_get200_response import ApiAuthGet200Response
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
    api_instance = woj.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.api_auth_get(token)
        print("The response of AuthApi->api_auth_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->api_auth_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**ApiAuthGet200Response**](ApiAuthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Token is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_auth_send_post**
> ApiAuthSendPost200Response api_auth_send_post(api_auth_send_post_request=api_auth_send_post_request)



### Example

```python
import time
import os
import woj
from woj.models.api_auth_send_post200_response import ApiAuthSendPost200Response
from woj.models.api_auth_send_post_request import ApiAuthSendPostRequest
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
    api_instance = woj.AuthApi(api_client)
    api_auth_send_post_request = woj.ApiAuthSendPostRequest() # ApiAuthSendPostRequest |  (optional)

    try:
        api_response = api_instance.api_auth_send_post(api_auth_send_post_request=api_auth_send_post_request)
        print("The response of AuthApi->api_auth_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->api_auth_send_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_send_post_request** | [**ApiAuthSendPostRequest**](ApiAuthSendPostRequest.md)|  | [optional] 

### Return type

[**ApiAuthSendPost200Response**](ApiAuthSendPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input (path parameters, query string, or body) |  -  |
**502** | Failed to send email |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

