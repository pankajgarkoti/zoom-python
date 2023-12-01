# swagger_client.CloudRecordingApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_details**](CloudRecordingApi.md#analytics_details) | **GET** /meetings/{meetingId}/recordings/analytics_details | Get Meeting Recording&#x27;s Analytics Details
[**analytics_summary**](CloudRecordingApi.md#analytics_summary) | **GET** /meetings/{meetingId}/recordings/analytics_summary | Get Meeting Recording&#x27;s Analytics Summary
[**meeting_recording_registrant_create**](CloudRecordingApi.md#meeting_recording_registrant_create) | **POST** /meetings/{meetingId}/recordings/registrants | Create a recording registrant
[**meeting_recording_registrant_status**](CloudRecordingApi.md#meeting_recording_registrant_status) | **PUT** /meetings/{meetingId}/recordings/registrants/status | Update registrant&#x27;s status
[**meeting_recording_registrants**](CloudRecordingApi.md#meeting_recording_registrants) | **GET** /meetings/{meetingId}/recordings/registrants | List recording registrants
[**recording_delete**](CloudRecordingApi.md#recording_delete) | **DELETE** /meetings/{meetingId}/recordings | Delete meeting recordings
[**recording_delete_one**](CloudRecordingApi.md#recording_delete_one) | **DELETE** /meetings/{meetingId}/recordings/{recordingId} | Delete a meeting recording file
[**recording_get**](CloudRecordingApi.md#recording_get) | **GET** /meetings/{meetingId}/recordings | Get meeting recordings
[**recording_registrant_question_update**](CloudRecordingApi.md#recording_registrant_question_update) | **PATCH** /meetings/{meetingId}/recordings/registrants/questions | Update registration questions
[**recording_registrants_questions_get**](CloudRecordingApi.md#recording_registrants_questions_get) | **GET** /meetings/{meetingId}/recordings/registrants/questions | Get registration questions
[**recording_setting_update**](CloudRecordingApi.md#recording_setting_update) | **GET** /meetings/{meetingId}/recordings/settings | Get meeting recording settings
[**recording_settings_update**](CloudRecordingApi.md#recording_settings_update) | **PATCH** /meetings/{meetingId}/recordings/settings | Update meeting recording settings
[**recording_status_update**](CloudRecordingApi.md#recording_status_update) | **PUT** /meetings/{meetingUUID}/recordings/status | Recover meeting recordings
[**recording_status_update_one**](CloudRecordingApi.md#recording_status_update_one) | **PUT** /meetings/{meetingId}/recordings/{recordingId}/status | Recover a single recording
[**recordings_list**](CloudRecordingApi.md#recordings_list) | **GET** /users/{userId}/recordings | List all recordings

# **analytics_details**
> InlineResponse20010 analytics_details(meeting_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, type=type)

Get Meeting Recording's Analytics Details

Use this API to return a meeting recording's [analytics details](https://support.zoom.us/hc/en-us/articles/205347605-Managing-cloud-recordings#h_0b665029-ce74-4849-9794-d1aa0320d163). **Maximum duration: 1 Month**. To access a password-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header. For example,    `curl -H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot; https://{{base-domain}}/rec/archive/download/xyz`      **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
_from = '2013-10-20' # date | The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date. (optional)
to = '2013-10-20' # date | The end date for the monthly range to query. The maximum range can be a month. (optional)
type = 'type_example' # str | The type of analytics details:  * `by_view` &mdash; by_view.  * `by_download` &mdash; by_download. (optional)

try:
    # Get Meeting Recording's Analytics Details
    api_response = api_instance.analytics_details(meeting_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->analytics_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **_from** | **date**| The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date. | [optional] 
 **to** | **date**| The end date for the monthly range to query. The maximum range can be a month. | [optional] 
 **type** | **str**| The type of analytics details:  * &#x60;by_view&#x60; &amp;mdash; by_view.  * &#x60;by_download&#x60; &amp;mdash; by_download. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_summary**
> InlineResponse20011 analytics_summary(meeting_id, _from=_from, to=to)

Get Meeting Recording's Analytics Summary

Use this API to return a meeting recording's [analytics summary](https://support.zoom.us/hc/en-us/articles/205347605-Managing-cloud-recordings#h_0b665029-ce74-4849-9794-d1aa0320d163). **Maximum duration: 1 Month**. To access a password-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header. For example,    `curl -H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot; https://{{base-domain}}/rec/archive/download/xyz`      **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
_from = '2013-10-20' # date | The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date. (optional)
to = '2013-10-20' # date | The end date for the monthly range to query. The maximum range can be a month. (optional)

try:
    # Get Meeting Recording's Analytics Summary
    api_response = api_instance.analytics_summary(meeting_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->analytics_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **_from** | **date**| The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date. | [optional] 
 **to** | **date**| The end date for the monthly range to query. The maximum range can be a month. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrant_create**
> InlineResponse2011 meeting_recording_registrant_create(meeting_id, body=body)

Create a recording registrant

Cloud Recordings of past Zoom Meetings can be made [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings). Users should be [registered](/docs/api-reference/zoom-api/methods#operation/meetingRecordingRegistrantCreate) to view these recordings.  Use this API to register a user to gain access to **On-demand Cloud Recordings** of a past meeting.       **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = swagger_client.RecordingsRegistrantsBody() # RecordingsRegistrantsBody |  (optional)

try:
    # Create a recording registrant
    api_response = api_instance.meeting_recording_registrant_create(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**RecordingsRegistrantsBody**](RecordingsRegistrantsBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrant_status**
> meeting_recording_registrant_status(meeting_id, body=body)

Update registrant's status

A registrant can either be approved or denied from viewing the [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) recording.  Use this API to update a registrant's status.    **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = swagger_client.RegistrantsStatusBody() # RegistrantsStatusBody |  (optional)

try:
    # Update registrant's status
    api_instance.meeting_recording_registrant_status(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**RegistrantsStatusBody**](RegistrantsStatusBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrants**
> MeetingCloudRecordingRegistration meeting_recording_registrants(meeting_id, status=status, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List recording registrants

Use this API to list registrants of a past meeting's [on-demand cloud recordings](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-recordings). Users must [register](/docs/api-reference/zoom-api/methods#operation/meetingRecordingRegistrantCreate) to view the recordings.      **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
status = 'approved' # str | Query by the registrant's status:  * `pending` &mdash; The registration is pending.  * `approved` &mdash; The registrant is approved.  * `denied` &mdash; The registration is denied. (optional) (default to approved)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List recording registrants
    api_response = api_instance.meeting_recording_registrants(meeting_id, status=status, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **status** | **str**| Query by the registrant&#x27;s status:  * &#x60;pending&#x60; &amp;mdash; The registration is pending.  * &#x60;approved&#x60; &amp;mdash; The registrant is approved.  * &#x60;denied&#x60; &amp;mdash; The registration is denied. | [optional] [default to approved]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**MeetingCloudRecordingRegistration**](MeetingCloudRecordingRegistration.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_delete**
> recording_delete(meeting_id, action=action)

Delete meeting recordings

Delete all recording files of a meeting.          **Prerequisites**: * Cloud Recording should be enabled on the user's account.       **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
action = 'trash' # str | The recording delete actions:    `trash` - Move recording to trash.    `delete` - Delete recording permanently. (optional) (default to trash)

try:
    # Delete meeting recordings
    api_instance.recording_delete(meeting_id, action=action)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **action** | **str**| The recording delete actions:    &#x60;trash&#x60; - Move recording to trash.    &#x60;delete&#x60; - Delete recording permanently. | [optional] [default to trash]

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_delete_one**
> recording_delete_one(meeting_id, recording_id, action=action)

Delete a meeting recording file

Delete a specific recording file from a meeting.&lt;p style=&quot;background-color:#e1f5fe; color:#01579b; padding:8px&quot;&gt; &lt;b&gt;Note:&lt;/b&gt; To use this API, you must enable the &lt;b&gt;The host can delete cloud recordings&lt;/b&gt; setting. You can find this setting in the &lt;b&gt;Recording&lt;/b&gt; tab of the &lt;b&gt;Settings&lt;/b&gt; interface in the [Zoom web portal](https://zoom.us/).&lt;/p&gt;    **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
recording_id = 'recording_id_example' # str | The recording ID.
action = 'trash' # str | The recording delete actions:    `trash` - Move recording to trash.    `delete` - Delete recording permanently. (optional) (default to trash)

try:
    # Delete a meeting recording file
    api_instance.recording_delete_one(meeting_id, recording_id, action=action)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_delete_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **recording_id** | **str**| The recording ID. | 
 **action** | **str**| The recording delete actions:    &#x60;trash&#x60; - Move recording to trash.    &#x60;delete&#x60; - Delete recording permanently. | [optional] [default to trash]

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_get**
> InlineResponse2009 recording_get(meeting_id, include_fields=include_fields, ttl=ttl)

Get meeting recordings

Returns all of a meeting's [recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording#h_7420acb5-1897-4061-87b4-5b76e99c03b4).   Use the `download_url` property listed in the response to download the recording files.  To access a passcode-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header.     Example:  `curl -H 'Authorization: Bearer <ACCESS_TOKEN>' https://{{base-domain}}/rec/archive/download/xyz`    **Scopes:** `recording:read`,`phone_recording:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get a meeting's cloud recordings, provide the meeting ID or UUID. If providing the meeting ID instead of UUID, the response will be for the latest meeting instance.   To get a webinar's cloud recordings, provide the webinar's ID or UUID. If providing the webinar ID instead of UUID, the response will be for the latest webinar instance.   If a UUID starts with `/` or contains `//` (example: `/ajXp112QmuoKj4854875==`), **[double encode](/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the UUID** before making an API request. 
include_fields = 'include_fields_example' # str | The `download_access_token` value for downloading the meeting's recordings. (optional)
ttl = 56 # int | The `download_access_token` Time to Live (TTL) value. This parameter is only valid if the `include_fields` query parameter contains the `download_access_token` value. (optional)

try:
    # Get meeting recordings
    api_response = api_instance.recording_get(meeting_id, include_fields=include_fields, ttl=ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get a meeting&#x27;s cloud recordings, provide the meeting ID or UUID. If providing the meeting ID instead of UUID, the response will be for the latest meeting instance.   To get a webinar&#x27;s cloud recordings, provide the webinar&#x27;s ID or UUID. If providing the webinar ID instead of UUID, the response will be for the latest webinar instance.   If a UUID starts with &#x60;/&#x60; or contains &#x60;//&#x60; (example: &#x60;/ajXp112QmuoKj4854875&#x3D;&#x3D;&#x60;), **[double encode](/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the UUID** before making an API request.  | 
 **include_fields** | **str**| The &#x60;download_access_token&#x60; value for downloading the meeting&#x27;s recordings. | [optional] 
 **ttl** | **int**| The &#x60;download_access_token&#x60; Time to Live (TTL) value. This parameter is only valid if the &#x60;include_fields&#x60; query parameter contains the &#x60;download_access_token&#x60; value. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_registrant_question_update**
> recording_registrant_question_update(meeting_id, body=body)

Update registration questions

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.  Use this API to update registration questions that are to be answered by users while registering to view a recording.       **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
body = swagger_client.RecordingRegistrantQuestions1() # RecordingRegistrantQuestions1 | Recording Registrant Questions (optional)

try:
    # Update registration questions
    api_instance.recording_registrant_question_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **body** | [**RecordingRegistrantQuestions1**](RecordingRegistrantQuestions1.md)| Recording Registrant Questions | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_registrants_questions_get**
> RecordingRegistrantQuestions recording_registrants_questions_get(meeting_id)

Get registration questions

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.  Use this API to retrieve a list of questions that are displayed for users to complete when registering to view the recording of a specific meeting.       **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

try:
    # Get registration questions
    api_response = api_instance.recording_registrants_questions_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 

### Return type

[**RecordingRegistrantQuestions**](RecordingRegistrantQuestions.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_setting_update**
> RecordingSettings recording_setting_update(meeting_id)

Get meeting recording settings

Retrieves settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording).           **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID enables you to get cloud recording of a: - Meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   - Webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **double encode** the UUID before making an API request. 

try:
    # Get meeting recording settings
    api_response = api_instance.recording_setting_update(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_setting_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID enables you to get cloud recording of a: - Meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   - Webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

[**RecordingSettings**](RecordingSettings.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_settings_update**
> recording_settings_update(meeting_id, body=body)

Update meeting recording settings

Updates settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording).        **Scopes:** `recording:write`,`recording:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **double encode** the UUID before making an API request. 
body = swagger_client.RecordingSettings1() # RecordingSettings1 |  (optional)

try:
    # Update meeting recording settings
    api_instance.recording_settings_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **double encode** the UUID before making an API request.  | 
 **body** | [**RecordingSettings1**](RecordingSettings1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_status_update**
> recording_status_update(meeting_uuid, body=body)

Recover meeting recordings

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover all deleted [Cloud Recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) of a specific meeting.         **Prerequisites**:     * A Pro user with Cloud Recording enabled.  **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_uuid = 'meeting_uuid_example' # str | The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.
body = swagger_client.RecordingsStatusBody() # RecordingsStatusBody |  (optional)

try:
    # Recover meeting recordings
    api_instance.recording_status_update(meeting_uuid, body=body)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_uuid** | **str**| The meeting&#x27;s universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a &#x60;/&#x60; character or contains a &#x60;//&#x60; character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls. | 
 **body** | [**RecordingsStatusBody**](RecordingsStatusBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_status_update_one**
> recording_status_update_one(meeting_id, recording_id, body=body)

Recover a single recording

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover a single recording file from the meeting.       **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 
recording_id = 'recording_id_example' # str | The recording ID.
body = swagger_client.RecordingIdStatusBody() # RecordingIdStatusBody |  (optional)

try:
    # Recover a single recording
    api_instance.recording_status_update_one(meeting_id, recording_id, body=body)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_status_update_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &amp;quot;/&amp;quot; or contains &amp;quot;//&amp;quot; (example: &amp;quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;&amp;quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request.  | 
 **recording_id** | **str**| The recording ID. | 
 **body** | [**RecordingIdStatusBody**](RecordingIdStatusBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recordings_list**
> InlineResponse20012 recordings_list(user_id, page_size=page_size, next_page_token=next_page_token, mc=mc, trash=trash, _from=_from, to=to, trash_type=trash_type, meeting_id=meeting_id)

List all recordings

Lists all [cloud recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) for a user.    For user-level apps, pass the [`me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  To access a user's passcode protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a bearer token in the authorization header.    Example:  `curl -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://{{base-domain}}/rec/archive/download/xyz`    **Prerequisites:**   * Must have a Pro or a higher plan.   * Must enable Cloud Recording on the user's account.  **Scopes:** `recording:read:admin`,`recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's ID or email address. For user-level apps, pass the `me` value.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
mc = 'false' # str | The query metadata of the recording if using an on-premise meeting connector for the meeting. (optional) (default to false)
trash = false # bool | The query trash. * `true` - List recordings from trash.   * `false` - Do not list recordings from the trash.    The default value is `false`. If you set it to `true`, you can use the `trash_type` property to indicate the type of Cloud recording that you need to retrieve.  (optional) (default to false)
_from = '2013-10-20' # date | The start date in 'yyyy-mm-dd' UTC format for the date range where you would like to retrieve recordings. The maximum range can be a month. If no value is provided for this field, the default will be current date.   For example, if you make the API request on June 30, 2020, without providing the &ldquo;from&rdquo; and &ldquo;to&rdquo; parameters, by default the value of 'from' field will be &ldquo;2020-06-30&rdquo; and the value of the 'to' field will be &ldquo;2020-07-01&rdquo;.   **Note**: The &quot;trash&quot; files cannot be filtered by date range and thus, the &quot;from&quot; and &quot;to&quot; fields should not be used for trash files. (optional)
to = '2013-10-20' # date | The end date in 'yyyy-mm-dd' 'yyyy-mm-dd' UTC format.  (optional)
trash_type = 'meeting_recordings' # str | The type of cloud recording to retrieve from the trash.     *   `meeting_recordings`: List all meeting recordings from the trash.    *  `recording_file`: List all individual recording files from the trash.  (optional) (default to meeting_recordings)
meeting_id = 56 # int | The meeting ID. (optional)

try:
    # List all recordings
    api_response = api_instance.recordings_list(user_id, page_size=page_size, next_page_token=next_page_token, mc=mc, trash=trash, _from=_from, to=to, trash_type=trash_type, meeting_id=meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recordings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **mc** | **str**| The query metadata of the recording if using an on-premise meeting connector for the meeting. | [optional] [default to false]
 **trash** | **bool**| The query trash. * &#x60;true&#x60; - List recordings from trash.   * &#x60;false&#x60; - Do not list recordings from the trash.    The default value is &#x60;false&#x60;. If you set it to &#x60;true&#x60;, you can use the &#x60;trash_type&#x60; property to indicate the type of Cloud recording that you need to retrieve.  | [optional] [default to false]
 **_from** | **date**| The start date in &#x27;yyyy-mm-dd&#x27; UTC format for the date range where you would like to retrieve recordings. The maximum range can be a month. If no value is provided for this field, the default will be current date.   For example, if you make the API request on June 30, 2020, without providing the &amp;ldquo;from&amp;rdquo; and &amp;ldquo;to&amp;rdquo; parameters, by default the value of &#x27;from&#x27; field will be &amp;ldquo;2020-06-30&amp;rdquo; and the value of the &#x27;to&#x27; field will be &amp;ldquo;2020-07-01&amp;rdquo;.   **Note**: The &amp;quot;trash&amp;quot; files cannot be filtered by date range and thus, the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; fields should not be used for trash files. | [optional] 
 **to** | **date**| The end date in &#x27;yyyy-mm-dd&#x27; &#x27;yyyy-mm-dd&#x27; UTC format.  | [optional] 
 **trash_type** | **str**| The type of cloud recording to retrieve from the trash.     *   &#x60;meeting_recordings&#x60;: List all meeting recordings from the trash.    *  &#x60;recording_file&#x60;: List all individual recording files from the trash.  | [optional] [default to meeting_recordings]
 **meeting_id** | **int**| The meeting ID. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

