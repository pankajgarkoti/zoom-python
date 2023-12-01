# swagger_client.TrackingFieldApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trackingfield_create**](TrackingFieldApi.md#trackingfield_create) | **POST** /tracking_fields | Create a tracking field
[**trackingfield_delete**](TrackingFieldApi.md#trackingfield_delete) | **DELETE** /tracking_fields/{fieldId} | Delete a tracking field
[**trackingfield_get**](TrackingFieldApi.md#trackingfield_get) | **GET** /tracking_fields/{fieldId} | Get a tracking field
[**trackingfield_list**](TrackingFieldApi.md#trackingfield_list) | **GET** /tracking_fields | List tracking fields
[**trackingfield_update**](TrackingFieldApi.md#trackingfield_update) | **PATCH** /tracking_fields/{fieldId} | Update a tracking field

# **trackingfield_create**
> TrackingField1 trackingfield_create(body=body)

Create a tracking field

Use this API to create a new [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). Tracking fields let you analyze usage by various fields within an organization. When scheduling a meeting, tracking fields will be included in the meeting options.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackingField() # TrackingField | Tracking Field (optional)

try:
    # Create a tracking field
    api_response = api_instance.trackingfield_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingField**](TrackingField.md)| Tracking Field | [optional] 

### Return type

[**TrackingField1**](TrackingField1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_delete**
> trackingfield_delete(field_id)

Delete a tracking field

Use this API to delete a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
field_id = 'field_id_example' # str | The Tracking Field ID

try:
    # Delete a tracking field
    api_instance.trackingfield_delete(field_id)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| The Tracking Field ID | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_get**
> TrackingField1 trackingfield_get(field_id)

Get a tracking field

Use this API to return information about a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
field_id = 'field_id_example' # str | The Tracking Field ID

try:
    # Get a tracking field
    api_response = api_instance.trackingfield_get(field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| The Tracking Field ID | 

### Return type

[**TrackingField1**](TrackingField1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_list**
> InlineResponse20082 trackingfield_list()

List tracking fields

Use this API to list all the [tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) on your Zoom account. Tracking fields let you analyze usage by various fields within an organization.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))

try:
    # List tracking fields
    api_response = api_instance.trackingfield_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_update**
> trackingfield_update(field_id, body=body)

Update a tracking field

Use this API to update a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
field_id = 'field_id_example' # str | The Tracking Field ID
body = swagger_client.TrackingField2() # TrackingField2 |  (optional)

try:
    # Update a tracking field
    api_instance.trackingfield_update(field_id, body=body)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| The Tracking Field ID | 
 **body** | [**TrackingField2**](TrackingField2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

