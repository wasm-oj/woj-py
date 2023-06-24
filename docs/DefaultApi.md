# woj.DefaultApi

All URIs are relative to *https://woj.csie.cool*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_me_get**](DefaultApi.md#api_me_get) | **GET** /api/me | 
[**api_sys_get**](DefaultApi.md#api_sys_get) | **GET** /api/sys | 


# **api_me_get**
> ApiMeGet200Response api_me_get()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import woj
from woj.models.api_me_get200_response import ApiMeGet200Response
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
    api_instance = woj.DefaultApi(api_client)

    try:
        api_response = api_instance.api_me_get()
        print("The response of DefaultApi->api_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_me_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiMeGet200Response**](ApiMeGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input (path parameters, query string, or body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sys_get**
> ApiSysGet200Response api_sys_get()



### Example

```python
import time
import os
import woj
from woj.models.api_sys_get200_response import ApiSysGet200Response
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
    api_instance = woj.DefaultApi(api_client)

    try:
        api_response = api_instance.api_sys_get()
        print("The response of DefaultApi->api_sys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_sys_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSysGet200Response**](ApiSysGet200Response.md)

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

