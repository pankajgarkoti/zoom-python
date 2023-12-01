# swagger_client.AppsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_app_deeplink**](AppsApi.md#generate_app_deeplink) | **POST** /zoomapp/deeplink | Generate an app deeplink
[**sendappnotifications**](AppsApi.md#sendappnotifications) | **POST** /app/notifications | Send app notifications

# **generate_app_deeplink**
> InlineResponse2005 generate_app_deeplink(body=body)

Generate an app deeplink

Create an app deeplink.      **Scopes:** `app:deeplink:write`,`app:deeplink:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ZoomappDeeplinkBody() # ZoomappDeeplinkBody |  (optional)

try:
    # Generate an app deeplink
    api_response = api_instance.generate_app_deeplink(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->generate_app_deeplink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoomappDeeplinkBody**](ZoomappDeeplinkBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendappnotifications**
> sendappnotifications(body=body)

Send app notifications

Send app notifications to the Zoom \"Activity Center\". (Note: This API only supports OAuth 2.0.)  **Scopes:** `app:notification:read`,`app:notification:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppNotificationsBody() # AppNotificationsBody |  (optional)

try:
    # Send app notifications
    api_instance.sendappnotifications(body=body)
except ApiException as e:
    print("Exception when calling AppsApi->sendappnotifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppNotificationsBody**](AppNotificationsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

