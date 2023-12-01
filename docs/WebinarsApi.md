# zoom.WebinarsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_batch_webinar_registrants**](WebinarsApi.md#add_batch_webinar_registrants) | **POST** /webinars/{webinarId}/batch_registrants | Perform batch registration
[**create_webinar_branding_name_tag**](WebinarsApi.md#create_webinar_branding_name_tag) | **POST** /webinars/{webinarId}/branding/name_tags | Create a webinar&#x27;s branding name tag
[**delete_webinar_branding_name_tag**](WebinarsApi.md#delete_webinar_branding_name_tag) | **DELETE** /webinars/{webinarId}/branding/name_tags | Delete a webinar&#x27;s branding name tag
[**delete_webinar_branding_vb**](WebinarsApi.md#delete_webinar_branding_vb) | **DELETE** /webinars/{webinarId}/branding/virtual_backgrounds | Delete a webinar&#x27;s branding Virtual Backgrounds
[**delete_webinar_branding_wallpaper**](WebinarsApi.md#delete_webinar_branding_wallpaper) | **DELETE** /webinars/{webinarId}/branding/wallpaper | Delete a webinar&#x27;s branding wallpaper
[**delete_webinar_chat_message_by_id**](WebinarsApi.md#delete_webinar_chat_message_by_id) | **DELETE** /live_webinars/{webinarId}/chat/messages/{messageId} | Delete a live webinar message
[**delete_webinar_registrant**](WebinarsApi.md#delete_webinar_registrant) | **DELETE** /webinars/{webinarId}/registrants/{registrantId} | Delete a webinar registrant
[**get_tracking_sources**](WebinarsApi.md#get_tracking_sources) | **GET** /webinars/{webinarId}/tracking_sources | Get webinar tracking sources
[**get_webinar_branding**](WebinarsApi.md#get_webinar_branding) | **GET** /webinars/{webinarId}/branding | Get webinar&#x27;s session branding
[**get_webinar_live_stream_details**](WebinarsApi.md#get_webinar_live_stream_details) | **GET** /webinars/{webinarId}/livestream | Get live stream details
[**list_past_webinar_poll_results**](WebinarsApi.md#list_past_webinar_poll_results) | **GET** /past_webinars/{webinarId}/polls | List past webinar poll results
[**list_past_webinar_qa**](WebinarsApi.md#list_past_webinar_qa) | **GET** /past_webinars/{webinarId}/qa | List Q&amp;As of a past webinar
[**list_webinar_participants**](WebinarsApi.md#list_webinar_participants) | **GET** /past_webinars/{webinarId}/participants | List webinar participants
[**list_webinar_templates**](WebinarsApi.md#list_webinar_templates) | **GET** /users/{userId}/webinar_templates | List webinar templates
[**past_webinars**](WebinarsApi.md#past_webinars) | **GET** /past_webinars/{webinarId}/instances | List past webinar instances
[**set_webinar_branding_vb**](WebinarsApi.md#set_webinar_branding_vb) | **PATCH** /webinars/{webinarId}/branding/virtual_backgrounds | Set webinar&#x27;s default branding Virtual Background
[**update_webinar_branding_name_tag**](WebinarsApi.md#update_webinar_branding_name_tag) | **PATCH** /webinars/{webinarId}/branding/name_tags/{nameTagId} | Update a webinar&#x27;s branding name tag
[**upload_webinar_branding_vb**](WebinarsApi.md#upload_webinar_branding_vb) | **POST** /webinars/{webinarId}/branding/virtual_backgrounds | Upload a webinar&#x27;s branding Virtual Background
[**upload_webinar_branding_wallpaper**](WebinarsApi.md#upload_webinar_branding_wallpaper) | **POST** /webinars/{webinarId}/branding/wallpaper | Upload a webinar&#x27;s branding wallpaper
[**webinar**](WebinarsApi.md#webinar) | **GET** /webinars/{webinarId} | Get a webinar
[**webinar_absentees**](WebinarsApi.md#webinar_absentees) | **GET** /past_webinars/{webinarId}/absentees | Get webinar absentees
[**webinar_create**](WebinarsApi.md#webinar_create) | **POST** /users/{userId}/webinars | Create a webinar
[**webinar_delete**](WebinarsApi.md#webinar_delete) | **DELETE** /webinars/{webinarId} | Delete a webinar
[**webinar_invite_links_create**](WebinarsApi.md#webinar_invite_links_create) | **POST** /webinars/{webinarId}/invite_links | Create webinar&#x27;s invite links
[**webinar_live_stream_status_update**](WebinarsApi.md#webinar_live_stream_status_update) | **PATCH** /webinars/{webinarId}/livestream/status | Update live stream status
[**webinar_live_stream_update**](WebinarsApi.md#webinar_live_stream_update) | **PATCH** /webinars/{webinarId}/livestream | Update a live stream
[**webinar_live_streaming_join_token**](WebinarsApi.md#webinar_live_streaming_join_token) | **GET** /webinars/{webinarId}/jointoken/live_streaming | Get a webinar&#x27;s join token for live streaming
[**webinar_local_archiving_archive_token**](WebinarsApi.md#webinar_local_archiving_archive_token) | **GET** /webinars/{webinarId}/jointoken/local_archiving | Get a webinar&#x27;s archive token for local archiving
[**webinar_local_recording_join_token**](WebinarsApi.md#webinar_local_recording_join_token) | **GET** /webinars/{webinarId}/jointoken/local_recording | Get a webinar&#x27;s join token for local recording
[**webinar_panelist_create**](WebinarsApi.md#webinar_panelist_create) | **POST** /webinars/{webinarId}/panelists | Add panelists
[**webinar_panelist_delete**](WebinarsApi.md#webinar_panelist_delete) | **DELETE** /webinars/{webinarId}/panelists/{panelistId} | Remove a panelist
[**webinar_panelists**](WebinarsApi.md#webinar_panelists) | **GET** /webinars/{webinarId}/panelists | List panelists
[**webinar_panelists_delete**](WebinarsApi.md#webinar_panelists_delete) | **DELETE** /webinars/{webinarId}/panelists | Remove webinar panelists
[**webinar_poll_create**](WebinarsApi.md#webinar_poll_create) | **POST** /webinars/{webinarId}/polls | Create a webinar&#x27;s poll
[**webinar_poll_delete**](WebinarsApi.md#webinar_poll_delete) | **DELETE** /webinars/{webinarId}/polls/{pollId} | Delete a webinar poll
[**webinar_poll_get**](WebinarsApi.md#webinar_poll_get) | **GET** /webinars/{webinarId}/polls/{pollId} | Get a webinar poll
[**webinar_poll_update**](WebinarsApi.md#webinar_poll_update) | **PUT** /webinars/{webinarId}/polls/{pollId} | Update a webinar poll
[**webinar_polls**](WebinarsApi.md#webinar_polls) | **GET** /webinars/{webinarId}/polls | List a webinar&#x27;s polls 
[**webinar_registrant_create**](WebinarsApi.md#webinar_registrant_create) | **POST** /webinars/{webinarId}/registrants | Add a webinar registrant
[**webinar_registrant_get**](WebinarsApi.md#webinar_registrant_get) | **GET** /webinars/{webinarId}/registrants/{registrantId} | Get a webinar registrant
[**webinar_registrant_question_update**](WebinarsApi.md#webinar_registrant_question_update) | **PATCH** /webinars/{webinarId}/registrants/questions | Update registration questions
[**webinar_registrant_status**](WebinarsApi.md#webinar_registrant_status) | **PUT** /webinars/{webinarId}/registrants/status | Update registrant&#x27;s status
[**webinar_registrants**](WebinarsApi.md#webinar_registrants) | **GET** /webinars/{webinarId}/registrants | List webinar registrants
[**webinar_registrants_questions_get**](WebinarsApi.md#webinar_registrants_questions_get) | **GET** /webinars/{webinarId}/registrants/questions | List registration questions
[**webinar_status**](WebinarsApi.md#webinar_status) | **PUT** /webinars/{webinarId}/status | Update webinar status
[**webinar_survey_delete**](WebinarsApi.md#webinar_survey_delete) | **DELETE** /webinars/{webinarId}/survey | Delete a webinar survey
[**webinar_survey_get**](WebinarsApi.md#webinar_survey_get) | **GET** /webinars/{webinarId}/survey | Get a webinar survey
[**webinar_survey_update**](WebinarsApi.md#webinar_survey_update) | **PATCH** /webinars/{webinarId}/survey | Update a webinar survey
[**webinar_template_create**](WebinarsApi.md#webinar_template_create) | **POST** /users/{userId}/webinar_templates | Create a webinar template
[**webinar_token**](WebinarsApi.md#webinar_token) | **GET** /webinars/{webinarId}/token | Get webinar&#x27;s token
[**webinar_update**](WebinarsApi.md#webinar_update) | **PATCH** /webinars/{webinarId} | Update a webinar
[**webinars**](WebinarsApi.md#webinars) | **GET** /users/{userId}/webinars | List webinars

# **add_batch_webinar_registrants**
> InlineResponse20123 add_batch_webinar_registrants(webinar_id, body=body)

Perform batch registration

Register up to 30 registrants at once for a scheduled webinar that requires [registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-webinar-with-registration).       **Prerequisites:**     * The webinar host must be a licensed user. * The webinar should be type `5`, a scheduled webinar. Other types of webinars are not supported by this API.           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's unique identifier.
body = zoom.WebinarIdBatchRegistrantsBody() # WebinarIdBatchRegistrantsBody |  (optional)

try:
    # Perform batch registration
    api_response = api_instance.add_batch_webinar_registrants(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->add_batch_webinar_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s unique identifier. | 
 **body** | [**WebinarIdBatchRegistrantsBody**](WebinarIdBatchRegistrantsBody.md)|  | [optional] 

### Return type

[**InlineResponse20123**](InlineResponse20123.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webinar_branding_name_tag**
> InlineResponse20124 create_webinar_branding_name_tag(webinar_id, body=body)

Create a webinar's branding name tag

Use this API to create a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag. There's a limit of 20 name tags per webinar. **Prerequisites:**  *  The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.BrandingNameTagsBody() # BrandingNameTagsBody |  (optional)

try:
    # Create a webinar's branding name tag
    api_response = api_instance.create_webinar_branding_name_tag(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->create_webinar_branding_name_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**BrandingNameTagsBody**](BrandingNameTagsBody.md)|  | [optional] 

### Return type

[**InlineResponse20124**](InlineResponse20124.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webinar_branding_name_tag**
> delete_webinar_branding_name_tag(webinar_id, name_tag_ids=name_tag_ids)

Delete a webinar's branding name tag

Use this API to delete a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag.    **Prerequisites:**  * The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
name_tag_ids = 'name_tag_ids_example' # str | A comma-separated list of the name tag IDs to delete. (optional)

try:
    # Delete a webinar's branding name tag
    api_instance.delete_webinar_branding_name_tag(webinar_id, name_tag_ids=name_tag_ids)
except ApiException as e:
    print("Exception when calling WebinarsApi->delete_webinar_branding_name_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **name_tag_ids** | **str**| A comma-separated list of the name tag IDs to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webinar_branding_vb**
> delete_webinar_branding_vb(webinar_id, ids=ids)

Delete a webinar's branding Virtual Backgrounds

Use this API to delete a webinar's session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background).    **Prerequisites:**  * The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
ids = 'ids_example' # str | A comma-separated list of the Virtual Background file IDs to delete. (optional)

try:
    # Delete a webinar's branding Virtual Backgrounds
    api_instance.delete_webinar_branding_vb(webinar_id, ids=ids)
except ApiException as e:
    print("Exception when calling WebinarsApi->delete_webinar_branding_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **ids** | **str**| A comma-separated list of the Virtual Background file IDs to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webinar_branding_wallpaper**
> delete_webinar_branding_wallpaper(webinar_id)

Delete a webinar's branding wallpaper

Use this API to delete a webinar's session branding wallpaper file.    **Prerequisites:**  * The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Delete a webinar's branding wallpaper
    api_instance.delete_webinar_branding_wallpaper(webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->delete_webinar_branding_wallpaper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webinar_chat_message_by_id**
> delete_webinar_chat_message_by_id(webinar_id, message_id, file_ids=file_ids)

Delete a live webinar message

Deletes a message in a live webinar based on ID.   **Prerequisites:**  * Have Zoom enable the DLP for the in-meeting chat feature to use this API.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
message_id = 'message_id_example' # str | The live webinar chat message's unique identifier (UUID), in base64-encoded format.
file_ids = 'file_ids_example' # str | The live webinar chat file's universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas. (optional)

try:
    # Delete a live webinar message
    api_instance.delete_webinar_chat_message_by_id(webinar_id, message_id, file_ids=file_ids)
except ApiException as e:
    print("Exception when calling WebinarsApi->delete_webinar_chat_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **message_id** | **str**| The live webinar chat message&#x27;s unique identifier (UUID), in base64-encoded format. | 
 **file_ids** | **str**| The live webinar chat file&#x27;s universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webinar_registrant**
> delete_webinar_registrant(webinar_id, registrant_id, occurrence_id=occurrence_id)

Delete a webinar registrant

Delete a webinar registrant.           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 56 # int | The webinar ID.
registrant_id = 'registrant_id_example' # str | The registrant ID.
occurrence_id = 'occurrence_id_example' # str | The webinar occurrence ID. (optional)

try:
    # Delete a webinar registrant
    api_instance.delete_webinar_registrant(webinar_id, registrant_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->delete_webinar_registrant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID. | 
 **registrant_id** | **str**| The registrant ID. | 
 **occurrence_id** | **str**| The webinar occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_sources**
> InlineResponse200107 get_tracking_sources(webinar_id)

Get webinar tracking sources

[Webinar Registration Tracking Sources](https://support.zoom.us/hc/en-us/articles/360000315683-Webinar-Registration-Source-Tracking) allow you to see where your registrants are coming from if you share the webinar registration page in multiple platforms. You can then use the source tracking to see the number of registrants generated from each platform.     Use this API to list information on all the tracking sources of a Webinar.     **Prerequisites**:     * [Webinar license](https://zoom.us/webinar). * Registration must be required for the Webinar.   **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get webinar tracking sources
    api_response = api_instance.get_tracking_sources(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->get_tracking_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webinar_branding**
> InlineResponse200101 get_webinar_branding(webinar_id)

Get webinar's session branding

Use this API to get the webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) information. Session branding lets hosts visually customize a webinar by setting a webinar wallpaper that displays behind video tiles. Session branding also lets hosts set the Virtual Background for and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers.    **Prerequisites:**  * A Pro or higher plan with the Webinar add-on.  * The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:read`,`webinar:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get webinar's session branding
    api_response = api_instance.get_webinar_branding(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->get_webinar_branding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webinar_live_stream_details**
> InlineResponse200105 get_webinar_live_stream_details(webinar_id)

Get live stream details

Get a webinar's live stream configuration details, such as Stream URL, Stream Key and Page URL.  Zoom allows users to [live stream a webinar](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform.    **Prerequisites:**     * Pro or higher plan with the webinar add-on.     * Live streaming details must have been [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.       **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's unique ID.

try:
    # Get live stream details
    api_response = api_instance.get_webinar_live_stream_details(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->get_webinar_live_stream_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s unique ID. | 

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_webinar_poll_results**
> InlineResponse20096 list_past_webinar_poll_results(webinar_id)

List past webinar poll results

The polling feature for webinar lets you create single-choice or multiple-choice polling questions for your webinars. This API endpoint retrieves the results for webinar polls of a specific webinar.  **Prerequisites:**     * [Webinar license](https://zoom.us/webinar)       **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

try:
    # List past webinar poll results
    api_response = api_instance.list_past_webinar_poll_results(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_past_webinar_poll_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_webinar_qa**
> InlineResponse20097 list_past_webinar_qa(webinar_id)

List Q&As of a past webinar

List the Q&amp;A of a specific past webinar.   The [question &amp; answer (Q&amp;A)](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) feature for webinars lets attendees ask questions during the webinar and for the panelists, co-hosts and host to answer their questions.   **Prerequisites**     * [Webinar license](https://zoom.us/webinar)       **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

try:
    # List Q&As of a past webinar
    api_response = api_instance.list_past_webinar_qa(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_past_webinar_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webinar_participants**
> InlineResponse20095 list_webinar_participants(webinar_id, page_size=page_size, next_page_token=next_page_token)

List webinar participants

Retrieve a list of all the participants who attended a webinar hosted in the past.   **Prerequisites:**  * A Pro or higher plan with a webinar add-on.  **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List webinar participants
    api_response = api_instance.list_webinar_participants(webinar_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_webinar_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webinar_templates**
> InlineResponse20098 list_webinar_templates(user_id)

List webinar templates

Display a list of a user's [webinar templates](https://support.zoom.us/hc/en-us/articles/115001079746-Webinar-Templates). For user-level apps, pass [the `me` value](/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. When you schedule a webinar, save the settings for that webinar as a template for scheduling future webinars.  To use a template when scheduling a webinar, use the `id` value in this API response in the `template_id` field of the [**Create a webinar**](/docs/api-reference/zoom-api/methods#operation/webinarCreate) API. **Prerequisites:** * A Pro or a higher account with the [Zoom Webinar plan](https://zoom.us/pricing/webinar).  **Scopes:** `webinar:read:admin`,`webinar:read`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's ID. To get a user's ID, use the [**List users**](/docs/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the `me` value instead of the user ID value.

try:
    # List webinar templates
    api_response = api_instance.list_webinar_templates(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_webinar_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s ID. To get a user&#x27;s ID, use the [**List users**](/docs/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the &#x60;me&#x60; value instead of the user ID value. | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_webinars**
> WebinarInstances past_webinars(webinar_id)

List past webinar instances

List past webinar instances.           **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # List past webinar instances
    api_response = api_instance.past_webinars(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->past_webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**WebinarInstances**](WebinarInstances.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_webinar_branding_vb**
> set_webinar_branding_vb(webinar_id, id=id, set_default_for_all_panelists=set_default_for_all_panelists)

Set webinar's default branding Virtual Background

Use this API to set a webinar's default session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background).    **Prerequisites:**  * The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
id = 'id_example' # str | The Virtual Background file ID to update. (optional)
set_default_for_all_panelists = true # bool | Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background. (optional)

try:
    # Set webinar's default branding Virtual Background
    api_instance.set_webinar_branding_vb(webinar_id, id=id, set_default_for_all_panelists=set_default_for_all_panelists)
except ApiException as e:
    print("Exception when calling WebinarsApi->set_webinar_branding_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **id** | **str**| The Virtual Background file ID to update. | [optional] 
 **set_default_for_all_panelists** | **bool**| Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webinar_branding_name_tag**
> update_webinar_branding_name_tag(webinar_id, name_tag_id, body=body)

Update a webinar's branding name tag

Use this API to update a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag. **Prerequisites:**  *  The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
name_tag_id = 'name_tag_id_example' # str | The name tag's ID.
body = zoom.NameTagsNameTagIdBody() # NameTagsNameTagIdBody |  (optional)

try:
    # Update a webinar's branding name tag
    api_instance.update_webinar_branding_name_tag(webinar_id, name_tag_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->update_webinar_branding_name_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **name_tag_id** | **str**| The name tag&#x27;s ID. | 
 **body** | [**NameTagsNameTagIdBody**](NameTagsNameTagIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_webinar_branding_vb**
> InlineResponse20125 upload_webinar_branding_vb(webinar_id, file=file, default=default, set_default_for_all_panelists=set_default_for_all_panelists)

Upload a webinar's branding Virtual Background

Use this API to upload a webinar's session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background). Hosts and panelists can select and use these Virtual Backgrounds during the webinar. Branding Virtual Background files have the following restrictions:  * A webinar cannot exceed more than 10 Virtual Background files.  * You can only upload image files that are in JPG/JPEG, GIF or PNG format.  * The Virtual Background file size cannot exceed 15 megabytes (MB).    **Prerequisites:**  *  The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
file = 'file_example' # str |  (optional)
default = true # bool |  (optional)
set_default_for_all_panelists = true # bool |  (optional)

try:
    # Upload a webinar's branding Virtual Background
    api_response = api_instance.upload_webinar_branding_vb(webinar_id, file=file, default=default, set_default_for_all_panelists=set_default_for_all_panelists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->upload_webinar_branding_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **file** | **str**|  | [optional] 
 **default** | **bool**|  | [optional] 
 **set_default_for_all_panelists** | **bool**|  | [optional] 

### Return type

[**InlineResponse20125**](InlineResponse20125.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_webinar_branding_wallpaper**
> InlineResponse20126 upload_webinar_branding_wallpaper(webinar_id, file=file)

Upload a webinar's branding wallpaper

Use this API to upload a webinar's session branding wallpaper file. Webinar branding wallpaper files have the following requirements:  * A webinar can only have one wallpaper file.  * You can only upload image files that are in JPG/JPEG, GIF, or PNG format.  * Image files must be 16:9 ratio. The recommended image size is 1920 x 1080 pixels (px).  * The wallpaper file size cannot exceed 15 megabytes (MB).    **Prerequisites:**  *  The **Webinar Session Branding** setting enabled.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
file = 'file_example' # str |  (optional)

try:
    # Upload a webinar's branding wallpaper
    api_response = api_instance.upload_webinar_branding_wallpaper(webinar_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->upload_webinar_branding_wallpaper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse20126**](InlineResponse20126.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar**
> InlineResponse200100 webinar(webinar_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)

Get a webinar

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees.    Use this API to get details of a scheduled webinar.         **Prerequisites:** * Pro or higher plan with a Webinar Add-on.  **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).
occurrence_id = 'occurrence_id_example' # str | Unique identifier for an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences. When you create a recurring Webinar using [**Create a webinar**](/docs/api-reference/zoom-api/methods#operation/webinarCreate) API, you can retrieve the Occurrence ID from the response of the API call. (optional)
show_previous_occurrences = true # bool | Set the value of this field to `true` if you would like to view Webinar details of all previous occurrences of a recurring Webinar. (optional)

try:
    # Get a webinar
    api_response = api_instance.webinar(webinar_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID). | 
 **occurrence_id** | **str**| Unique identifier for an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences. When you create a recurring Webinar using [**Create a webinar**](/docs/api-reference/zoom-api/methods#operation/webinarCreate) API, you can retrieve the Occurrence ID from the response of the API call. | [optional] 
 **show_previous_occurrences** | **bool**| Set the value of this field to &#x60;true&#x60; if you would like to view Webinar details of all previous occurrences of a recurring Webinar. | [optional] 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_absentees**
> RegistrationList1 webinar_absentees(webinar_id, occurrence_id=occurrence_id, page_size=page_size, next_page_token=next_page_token)

Get webinar absentees

List absentees of a webinar.           **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get webinar absentees
    api_response = api_instance.webinar_absentees(webinar_id, occurrence_id=occurrence_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_absentees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**RegistrationList1**](RegistrationList1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_create**
> InlineResponse20122 webinar_create(user_id, body=body)

Create a webinar

Schedule a webinar for a user (webinar host). For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.   Zoom users with a [Webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. Webinars allow a host to broadcast a Zoom meeting to up to 10,000 attendees.   **100 requests per day**. The rate limit is applied to the `userId` of the **webinar host** used to make the request.   **Prerequisites:**  * A Pro or higher plan with a Webinar add-on.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass the `me` value.
body = zoom.UserIdWebinarsBody() # UserIdWebinarsBody |  (optional)

try:
    # Create a webinar
    api_response = api_instance.webinar_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdWebinarsBody**](UserIdWebinarsBody.md)|  | [optional] 

### Return type

[**InlineResponse20122**](InlineResponse20122.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_delete**
> webinar_delete(webinar_id, occurrence_id=occurrence_id, cancel_webinar_reminder=cancel_webinar_reminder)

Delete a webinar

Delete a webinar.    **Prerequisites:**     * Pro or higher plan with the webinar add-on.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)
cancel_webinar_reminder = true # bool | `true` - Notify panelists and registrants about the webinar cancellation via email.   `false` - Do not send any email notification to webinar registrants and panelists.   The default value of this field is `false`. (optional)

try:
    # Delete a webinar
    api_instance.webinar_delete(webinar_id, occurrence_id=occurrence_id, cancel_webinar_reminder=cancel_webinar_reminder)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 
 **cancel_webinar_reminder** | **bool**| &#x60;true&#x60; - Notify panelists and registrants about the webinar cancellation via email.   &#x60;false&#x60; - Do not send any email notification to webinar registrants and panelists.   The default value of this field is &#x60;false&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_invite_links_create**
> InviteLinks1 webinar_invite_links_create(webinar_id, body=body)

Create webinar's invite links

Create a batch of invitation links for a webinar.  **Prerequisites:**  * Business, Education or API Plan with the Webinar add-on.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.InviteLinks() # InviteLinks | Webinar invite link object. (optional)

try:
    # Create webinar's invite links
    api_response = api_instance.webinar_invite_links_create(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_invite_links_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**InviteLinks**](InviteLinks.md)| Webinar invite link object. | [optional] 

### Return type

[**InviteLinks1**](InviteLinks1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_live_stream_status_update**
> webinar_live_stream_status_update(webinar_id, body=body)

Update live stream status

Let users [live stream a webinar](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Update the status of a webinar's live stream.         **Prerequisites:**     * Pro or higher plan with a Webinar Add-on.     * Live streaming details must be [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.LivestreamStatusBody1() # LivestreamStatusBody1 | Webinar (optional)

try:
    # Update live stream status
    api_instance.webinar_live_stream_status_update(webinar_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_live_stream_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**LivestreamStatusBody1**](LivestreamStatusBody1.md)| Webinar | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_live_stream_update**
> webinar_live_stream_update(webinar_id, body=body)

Update a live stream

Update a webinar's live stream information.        **Prerequisites:**     * Pro or higher plan with the webinar add-on.     * Live streaming details must be [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarIdLivestreamBody() # WebinarIdLivestreamBody | Webinar (optional)

try:
    # Update a live stream
    api_instance.webinar_live_stream_update(webinar_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_live_stream_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarIdLivestreamBody**](WebinarIdLivestreamBody.md)| Webinar | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_live_streaming_join_token**
> InlineResponse200102 webinar_live_streaming_join_token(webinar_id)

Get a webinar's join token for live streaming

Use this API to get a webinar's archive token to allow live streaming. The join token allows a recording bot implemented using Zoom meeting SDK to connect to a Zoom meeting &quot;hosted by the issuer of the token&quot;, and can call the streaming method automatically. It supports both regular live streaming, and raw streaming.    **Prerequisites:**  * A Pro or higher plan with a Webinar Add-on.  * The **Allow livestreaming of webinars** user setting enabled in the Zoom web portal.  **Scopes:** `webinar_token:read:admin:live_streaming`,`webinar_token:read:live_streaming`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get a webinar's join token for live streaming
    api_response = api_instance.webinar_live_streaming_join_token(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_live_streaming_join_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**InlineResponse200102**](InlineResponse200102.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_local_archiving_archive_token**
> InlineResponse200103 webinar_local_archiving_archive_token(webinar_id)

Get a webinar's archive token for local archiving

Use this API to get a webinar's archive token to allow local archiving. The archive token allows a meeting SDK app or bot to get archive permission to access the webinar's raw audio and video media stream in real-time.    **Prerequisites:**  * A Pro or higher plan with a Webinar Add-on.  * The **Archive meetings and webinars** account setting enabled in the Zoom web portal.  **Scopes:** `webinar_token:read:admin:local_archiving`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get a webinar's archive token for local archiving
    api_response = api_instance.webinar_local_archiving_archive_token(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_local_archiving_archive_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**InlineResponse200103**](InlineResponse200103.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_local_recording_join_token**
> InlineResponse200104 webinar_local_recording_join_token(webinar_id)

Get a webinar's join token for local recording

Use this API to get a webinar's join token to allow for local recording. The join token lets a recording bot implemented using Zoom Meeting SDK to connect to a Zoom webinar. The recording bot can then automatically start locally recording. This supports both regular and raw local recording types.    **Prerequisites:**  * A Pro or higher plan with a Webinar Add-on.  * The **Local recording** user setting enabled in the Zoom web portal.  **Scopes:** `webinar_token:read:admin:local_recording`,`webinar_token:read:local_recording`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get a webinar's join token for local recording
    api_response = api_instance.webinar_local_recording_join_token(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_local_recording_join_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelist_create**
> InlineResponse20127 webinar_panelist_create(webinar_id, body=body)

Add panelists

Panelists in a webinar can view and send video, screen share, annotate, and do much more compared to attendees in a webinar.    [Add panelists](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_7550d59e-23f5-4703-9e22-e76bded1ed70) to a scheduled webinar.         **Prerequisites:** * Pro or a higher plan with the [Webinar Add-on](https://zoom.us/webinar).       **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarIdPanelistsBody() # WebinarIdPanelistsBody |  (optional)

try:
    # Add panelists
    api_response = api_instance.webinar_panelist_create(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelist_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarIdPanelistsBody**](WebinarIdPanelistsBody.md)|  | [optional] 

### Return type

[**InlineResponse20127**](InlineResponse20127.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelist_delete**
> webinar_panelist_delete(webinar_id, panelist_id)

Remove a panelist

[Remove](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_de31f237-a91c-4fb2-912b-ecfba8ec5ffb) a single panelist from a webinar.     Retrieve the `panelistId` by calling **List Panelists API**.         **Prerequisites:**     * Pro or a higher plan with the [webinar add-on](https://zoom.us/webinar).       **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
panelist_id = 'panelist_id_example' # str | The panelist's ID or email.

try:
    # Remove a panelist
    api_instance.webinar_panelist_delete(webinar_id, panelist_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelist_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **panelist_id** | **str**| The panelist&#x27;s ID or email. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelists**
> PanelistList webinar_panelists(webinar_id)

List panelists

List all of a webinar's panelists.    Webinar panelists can view and send video, screen share, annotate, and do much more compared to webinar attendees.    **Prerequisites:**     * Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).       **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # List panelists
    api_response = api_instance.webinar_panelists(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**PanelistList**](PanelistList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelists_delete**
> webinar_panelists_delete(webinar_id)

Remove webinar panelists

Remove all the panelists from a webinar.     **Prerequisites:**     * Pro or a higher plan with the [webinar add-on](https://zoom.us/webinar).       **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Remove webinar panelists
    api_instance.webinar_panelists_delete(webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_create**
> MeetingAndWebinarPollingObject1 webinar_poll_create(webinar_id, body=body)

Create a webinar's poll

Create a [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) for a webinar.           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.MeetingAndWebinarPollingObject_() # MeetingAndWebinarPollingObject_ | Webinar poll object. (optional)

try:
    # Create a webinar's poll
    api_response = api_instance.webinar_poll_create(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**MeetingAndWebinarPollingObject_**](MeetingAndWebinarPollingObject_.md)| Webinar poll object. | [optional] 

### Return type

[**MeetingAndWebinarPollingObject1**](MeetingAndWebinarPollingObject1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_delete**
> webinar_poll_delete(webinar_id, poll_id)

Delete a webinar poll

Delete a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Delete a webinar poll
    api_instance.webinar_poll_delete(webinar_id, poll_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_get**
> MeetingAndWebinarPollingObject3 webinar_poll_get(webinar_id, poll_id)

Get a webinar poll

Get a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) details.           **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Get a webinar poll
    api_response = api_instance.webinar_poll_get(webinar_id, poll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **poll_id** | **str**| The poll ID | 

### Return type

[**MeetingAndWebinarPollingObject3**](MeetingAndWebinarPollingObject3.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_update**
> webinar_poll_update(webinar_id, poll_id, body=body)

Update a webinar poll

Update a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).           **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
poll_id = 'poll_id_example' # str | The poll ID
body = zoom.MeetingAndWebinarPollingObject4() # MeetingAndWebinarPollingObject4 | Webinar Poll (optional)

try:
    # Update a webinar poll
    api_instance.webinar_poll_update(webinar_id, poll_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **poll_id** | **str**| The poll ID | 
 **body** | [**MeetingAndWebinarPollingObject4**](MeetingAndWebinarPollingObject4.md)| Webinar Poll | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_polls**
> PollList webinar_polls(webinar_id, anonymous=anonymous)

List a webinar's polls 

List all the [polls](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) of a Webinar.           **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
anonymous = true # bool | Whether to query for polls with the **Anonymous** option enabled:  * `true` &mdash; Query for polls with the **Anonymous** option enabled.  * `false` &mdash; Do not query for polls with the **Anonymous** option enabled. (optional)

try:
    # List a webinar's polls 
    api_response = api_instance.webinar_polls(webinar_id, anonymous=anonymous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **anonymous** | **bool**| Whether to query for polls with the **Anonymous** option enabled:  * &#x60;true&#x60; &amp;mdash; Query for polls with the **Anonymous** option enabled.  * &#x60;false&#x60; &amp;mdash; Do not query for polls with the **Anonymous** option enabled. | [optional] 

### Return type

[**PollList**](PollList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_create**
> InlineResponse20128 webinar_registrant_create(webinar_id, body=body, occurrence_ids=occurrence_ids)

Add a webinar registrant

Create and submit a user's registration for a webinar. Zoom users with a [Webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. Webinars allow hosts to broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar.   **Prerequisites:**  * A Pro or higher plan with the Webinar add-on.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarIdRegistrantsBody() # WebinarIdRegistrantsBody |  (optional)
occurrence_ids = 'occurrence_ids_example' # str | A comma-separated list of webinar occurrence IDs. Get this value with the [Get a webinar](/docs/api/rest/reference/zoom-api/methods/#operation/webinar) API. Make sure the `registration_type` is 3 if updating multiple occurrences with this API. (optional)

try:
    # Add a webinar registrant
    api_response = api_instance.webinar_registrant_create(webinar_id, body=body, occurrence_ids=occurrence_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarIdRegistrantsBody**](WebinarIdRegistrantsBody.md)|  | [optional] 
 **occurrence_ids** | **str**| A comma-separated list of webinar occurrence IDs. Get this value with the [Get a webinar](/docs/api/rest/reference/zoom-api/methods/#operation/webinar) API. Make sure the &#x60;registration_type&#x60; is 3 if updating multiple occurrences with this API. | [optional] 

### Return type

[**InlineResponse20128**](InlineResponse20128.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_get**
> WebinarRegistrant webinar_registrant_get(webinar_id, registrant_id, occurrence_id=occurrence_id)

Get a webinar registrant

Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. The webinar feature lets a host broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar.    Use this API to get details on a specific user who has registered for the webinar.         **Prerequisites:**     * The account must have a webinar plan.  **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
registrant_id = 'registrant_id_example' # str | The registrant ID.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)

try:
    # Get a webinar registrant
    api_response = api_instance.webinar_registrant_get(webinar_id, registrant_id, occurrence_id=occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **registrant_id** | **str**| The registrant ID. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 

### Return type

[**WebinarRegistrant**](WebinarRegistrant.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_question_update**
> webinar_registrant_question_update(webinar_id, body=body)

Update registration questions

Update registration questions and fields of a scheduled webinar for users to answer during webinar registration. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the webinar.         **Prerequisites:**       * Pro or higher plan with a Webinar Add-on. * Registration option for Webinar should be set as required to use this API.    **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarRegistrantQuestions() # WebinarRegistrantQuestions | Webinar registrant questions (optional)

try:
    # Update registration questions
    api_instance.webinar_registrant_question_update(webinar_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarRegistrantQuestions**](WebinarRegistrantQuestions.md)| Webinar registrant questions | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_status**
> webinar_registrant_status(webinar_id, body=body, occurrence_id=occurrence_id)

Update registrant's status

Update webinar registrants' registration status. You can approve or deny a registrant, or revoke a registrant's approval.   **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.RegistrantsStatusBody2() # RegistrantsStatusBody2 |  (optional)
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)

try:
    # Update registrant's status
    api_instance.webinar_registrant_status(webinar_id, body=body, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**RegistrantsStatusBody2**](RegistrantsStatusBody2.md)|  | [optional] 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrants**
> RegistrationList webinar_registrants(webinar_id, occurrence_id=occurrence_id, status=status, tracking_source_id=tracking_source_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List webinar registrants

List all users that have registered for a given webinar. Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. The webinar functionality lets a host broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar.     **Prerequisites** * Pro or higher plan with a Webinar Add-on.       **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)
status = 'approved' # str | Query by the registrant's status.  * `pending` - The registration is pending.  * `approved` - The registrant is approved.  * `denied` - The registration is denied. (optional) (default to approved)
tracking_source_id = 'tracking_source_id_example' # str | The tracking source ID for the registrants. Useful if you share the webinar registration page in multiple locations. See [Creating source tracking links for webinar registration](https://support.zoom.us/hc/en-us/articles/360000315683-Creating-source-tracking-links-for-webinar-registration) for details. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated** This field will be deprecated. We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List webinar registrants
    api_response = api_instance.webinar_registrants(webinar_id, occurrence_id=occurrence_id, status=status, tracking_source_id=tracking_source_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 
 **status** | **str**| Query by the registrant&#x27;s status.  * &#x60;pending&#x60; - The registration is pending.  * &#x60;approved&#x60; - The registrant is approved.  * &#x60;denied&#x60; - The registration is denied. | [optional] [default to approved]
 **tracking_source_id** | **str**| The tracking source ID for the registrants. Useful if you share the webinar registration page in multiple locations. See [Creating source tracking links for webinar registration](https://support.zoom.us/hc/en-us/articles/360000315683-Creating-source-tracking-links-for-webinar-registration) for details. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated** This field will be deprecated. We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**RegistrationList**](RegistrationList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrants_questions_get**
> WebinarRegistrantQuestions webinar_registrants_questions_get(webinar_id)

List registration questions

List registration questions and fields that are to be answered by users while registering for a webinar.    Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the webinar.      **Prerequisites:**      * Pro or higher plan with the webinar add-on.   **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # List registration questions
    api_response = api_instance.webinar_registrants_questions_get(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**WebinarRegistrantQuestions**](WebinarRegistrantQuestions.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_status**
> object webinar_status(webinar_id, body=body)

Update webinar status

Update a webinar's status. Use this API to end an ongoing webinar.         **Prerequisites:**     * The account must hold a valid [Webinar plan](https://zoom.us/webinar).  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarIdStatusBody() # WebinarIdStatusBody |  (optional)

try:
    # Update webinar status
    api_response = api_instance.webinar_status(webinar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarIdStatusBody**](WebinarIdStatusBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_survey_delete**
> webinar_survey_delete(webinar_id)

Delete a webinar survey

Use this API to delete a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651).    **Prerequisites:**  * A Pro or higher plan with the Webinar Add-on.  * The [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature enabled in the host's account.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Delete a webinar survey
    api_instance.webinar_survey_delete(webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_survey_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_survey_get**
> WebinarSurveyObject webinar_survey_get(webinar_id)

Get a webinar survey

Return information about a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651).    **Prerequisites:**  * A Pro or higher plan with the Webinar add-on.  * The [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature enabled in the host's account.  **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.

try:
    # Get a webinar survey
    api_response = api_instance.webinar_survey_get(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_survey_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 

### Return type

[**WebinarSurveyObject**](WebinarSurveyObject.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_survey_update**
> webinar_survey_update(webinar_id, body=body)

Update a webinar survey

Update a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651).  **Prerequisites:** * A Pro or higher plan with the Webinar add-on. * Enable the [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature in the host's account.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarSurveyObject1() # WebinarSurveyObject1 |  (optional)

try:
    # Update a webinar survey
    api_instance.webinar_survey_update(webinar_id, body=body)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_survey_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarSurveyObject1**](WebinarSurveyObject1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_template_create**
> InlineResponse20121 webinar_template_create(user_id, body=body)

Create a webinar template

Use this API to create a webinar template from an existing webinar.     **Scopes:** `webinar:write:admin`,`webinar:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API.
body = zoom.UserIdWebinarTemplatesBody() # UserIdWebinarTemplatesBody |  (optional)

try:
    # Create a webinar template
    api_response = api_instance.webinar_template_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_template_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API. | 
 **body** | [**UserIdWebinarTemplatesBody**](UserIdWebinarTemplatesBody.md)|  | [optional] 

### Return type

[**InlineResponse20121**](InlineResponse20121.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_token**
> InlineResponse200106 webinar_token(webinar_id, type=type)

Get webinar's token

Use this API to get a webinar's [closed caption token (caption URL)](https://support.zoom.us/hc/en-us/articles/115002212983-Using-a-third-party-closed-captioning-service). This token lets you use a third-party service to stream text to their closed captioning software to the Zoom webinar.   **Prerequisites:**  * A Pro or higher plan with the Webinar add-on.  * The **Closed captioning** setting enabled in the Zoom web portal.  *  * The **Allow use of caption API Token to integrate with 3rd-party Closed Captioning services** setting enabled.  **Scopes:** `webinar:read`,`webinar:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
type = 'closed_caption_token' # str | The webinar token type:  * `closed_caption_token` &mdash; The third-party closed caption API token.   This defaults to `closed_caption_token`. (optional) (default to closed_caption_token)

try:
    # Get webinar's token
    api_response = api_instance.webinar_token(webinar_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **type** | **str**| The webinar token type:  * &#x60;closed_caption_token&#x60; &amp;mdash; The third-party closed caption API token.   This defaults to &#x60;closed_caption_token&#x60;. | [optional] [default to closed_caption_token]

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_update**
> webinar_update(webinar_id, body=body, occurrence_id=occurrence_id)

Update a webinar

Make updates to a scheduled webinar.   **100 requests per day**. The rate limit is applied to the `userId` of the **webinar host** used to make the request.   **Prerequisites**  * A Pro or higher plan with a webinar add-on.  **Scopes:** `webinar:write`,`webinar:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
webinar_id = 789 # int | The webinar's ID.
body = zoom.WebinarsWebinarIdBody() # WebinarsWebinarIdBody | Webinar. (optional)
occurrence_id = 'occurrence_id_example' # str | Webinar occurrence ID. Support change of agenda, start time, duration, and settings `host_video`, `panelist_video`, `hd_video, watermark`, `auto_recording`. (optional)

try:
    # Update a webinar
    api_instance.webinar_update(webinar_id, body=body, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar&#x27;s ID. | 
 **body** | [**WebinarsWebinarIdBody**](WebinarsWebinarIdBody.md)| Webinar. | [optional] 
 **occurrence_id** | **str**| Webinar occurrence ID. Support change of agenda, start time, duration, and settings &#x60;host_video&#x60;, &#x60;panelist_video&#x60;, &#x60;hd_video, watermark&#x60;, &#x60;auto_recording&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinars**
> InlineResponse20099 webinars(user_id, type=type, page_size=page_size, page_number=page_number)

List webinars

List all the webinars scheduled by or on behalf a webinar host. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. Webinars let a host broadcast a Zoom meeting to up to 10,000 attendees.   **Note** This API only returns a user's [unexpired webinars](https://support.zoom.us/hc/en-us/articles/201362373-Meeting-ID#h_c73f9b08-c1c0-4a1a-b538-e01ebb98e844).    **Prerequisites**  * A Pro or higher plan with the webinar add-on.  **Scopes:** `webinar:read:admin`,`webinar:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

### Example
```python
from __future__ import print_function
import time
import zoom
from zoom.rest import ApiException
from pprint import pprint

# Configure API key authorization: openapi_authorization
configuration = zoom.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: openapi_oauth
configuration = zoom.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = zoom.WebinarsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
type = 'scheduled' # str | The type of webinar.  * `scheduled` - All valid previous (unexpired) webinars, live webinars, and upcoming scheduled webinars.  * `upcoming` - All upcoming webinars, including live webinars. (optional) (default to scheduled)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)

try:
    # List webinars
    api_response = api_instance.webinars(user_id, type=type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **type** | **str**| The type of webinar.  * &#x60;scheduled&#x60; - All valid previous (unexpired) webinars, live webinars, and upcoming scheduled webinars.  * &#x60;upcoming&#x60; - All upcoming webinars, including live webinars. | [optional] [default to scheduled]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

