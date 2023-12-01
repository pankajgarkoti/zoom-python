# zoom.MeetingsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_batch_registrants**](MeetingsApi.md#add_batch_registrants) | **POST** /meetings/{meetingId}/batch_registrants | Perform batch registration
[**create_batch_polls**](MeetingsApi.md#create_batch_polls) | **POST** /meetings/{meetingId}/batch_polls | Perform batch poll creation
[**delete_meeting_chat_message_by_id**](MeetingsApi.md#delete_meeting_chat_message_by_id) | **DELETE** /live_meetings/{meetingId}/chat/messages/{messageId} | Delete a live meeting message
[**get_meeting_live_stream_details**](MeetingsApi.md#get_meeting_live_stream_details) | **GET** /meetings/{meetingId}/livestream | Get livestream details
[**get_sip_dialing_with_passcode**](MeetingsApi.md#get_sip_dialing_with_passcode) | **POST** /meetings/{meetingId}/sip_dialing | Get a meeting SIP URI with Passcode
[**getameetingsummary**](MeetingsApi.md#getameetingsummary) | **GET** /meetings/{meetingId}/meeting_summary | Get a meeting summary
[**in_meeting_control**](MeetingsApi.md#in_meeting_control) | **PATCH** /live_meetings/{meetingId}/events | Use in-meeting controls
[**list_meeting_templates**](MeetingsApi.md#list_meeting_templates) | **GET** /users/{userId}/meeting_templates | List meeting templates
[**list_past_meeting_polls**](MeetingsApi.md#list_past_meeting_polls) | **GET** /past_meetings/{meetingId}/polls | List past meeting&#x27;s poll results
[**list_past_meeting_qa**](MeetingsApi.md#list_past_meeting_qa) | **GET** /past_meetings/{meetingId}/qa | List past meetings&#x27; Q&amp;A
[**listmeetingsummaries**](MeetingsApi.md#listmeetingsummaries) | **GET** /meetings/meeting_summaries | List meeting summaries of an account
[**meeting**](MeetingsApi.md#meeting) | **GET** /meetings/{meetingId} | Get a meeting
[**meeting_create**](MeetingsApi.md#meeting_create) | **POST** /users/{userId}/meetings | Create a meeting
[**meeting_delete**](MeetingsApi.md#meeting_delete) | **DELETE** /meetings/{meetingId} | Delete a meeting
[**meeting_invitation**](MeetingsApi.md#meeting_invitation) | **GET** /meetings/{meetingId}/invitation | Get meeting invitation
[**meeting_invite_links_create**](MeetingsApi.md#meeting_invite_links_create) | **POST** /meetings/{meetingId}/invite_links | Create meeting&#x27;s invite links
[**meeting_live_stream_status_update**](MeetingsApi.md#meeting_live_stream_status_update) | **PATCH** /meetings/{meetingId}/livestream/status | Update Live Stream Status
[**meeting_live_stream_update**](MeetingsApi.md#meeting_live_stream_update) | **PATCH** /meetings/{meetingId}/livestream | Update a livestream
[**meeting_live_streaming_join_token**](MeetingsApi.md#meeting_live_streaming_join_token) | **GET** /meetings/{meetingId}/jointoken/live_streaming | Get a meeting&#x27;s join token for live streaming
[**meeting_local_archiving_archive_token**](MeetingsApi.md#meeting_local_archiving_archive_token) | **GET** /meetings/{meetingId}/jointoken/local_archiving | Get a meeting&#x27;s archive token for local archiving
[**meeting_local_recording_join_token**](MeetingsApi.md#meeting_local_recording_join_token) | **GET** /meetings/{meetingId}/jointoken/local_recording | Get a meeting&#x27;s join token for local recording
[**meeting_poll_create**](MeetingsApi.md#meeting_poll_create) | **POST** /meetings/{meetingId}/polls | Create a meeting poll
[**meeting_poll_delete**](MeetingsApi.md#meeting_poll_delete) | **DELETE** /meetings/{meetingId}/polls/{pollId} | Delete a meeting poll
[**meeting_poll_get**](MeetingsApi.md#meeting_poll_get) | **GET** /meetings/{meetingId}/polls/{pollId} | Get a meeting poll
[**meeting_poll_update**](MeetingsApi.md#meeting_poll_update) | **PUT** /meetings/{meetingId}/polls/{pollId} | Update a meeting poll
[**meeting_polls**](MeetingsApi.md#meeting_polls) | **GET** /meetings/{meetingId}/polls | List meeting polls
[**meeting_registrant_create**](MeetingsApi.md#meeting_registrant_create) | **POST** /meetings/{meetingId}/registrants | Add a meeting registrant
[**meeting_registrant_get**](MeetingsApi.md#meeting_registrant_get) | **GET** /meetings/{meetingId}/registrants/{registrantId} | Get a meeting registrant
[**meeting_registrant_question_update**](MeetingsApi.md#meeting_registrant_question_update) | **PATCH** /meetings/{meetingId}/registrants/questions | Update registration questions
[**meeting_registrant_status**](MeetingsApi.md#meeting_registrant_status) | **PUT** /meetings/{meetingId}/registrants/status | Update registrant&#x27;s status
[**meeting_registrants**](MeetingsApi.md#meeting_registrants) | **GET** /meetings/{meetingId}/registrants | List meeting registrants
[**meeting_registrants_questions_get**](MeetingsApi.md#meeting_registrants_questions_get) | **GET** /meetings/{meetingId}/registrants/questions | List registration questions 
[**meeting_status**](MeetingsApi.md#meeting_status) | **PUT** /meetings/{meetingId}/status | Update meeting status
[**meeting_survey_delete**](MeetingsApi.md#meeting_survey_delete) | **DELETE** /meetings/{meetingId}/survey | Delete a meeting survey
[**meeting_survey_get**](MeetingsApi.md#meeting_survey_get) | **GET** /meetings/{meetingId}/survey | Get a meeting survey
[**meeting_survey_update**](MeetingsApi.md#meeting_survey_update) | **PATCH** /meetings/{meetingId}/survey | Update a meeting survey
[**meeting_template_create**](MeetingsApi.md#meeting_template_create) | **POST** /users/{userId}/meeting_templates | Create a meeting template from an existing meeting
[**meeting_token**](MeetingsApi.md#meeting_token) | **GET** /meetings/{meetingId}/token | Get meeting&#x27;s token
[**meeting_update**](MeetingsApi.md#meeting_update) | **PATCH** /meetings/{meetingId} | Update a meeting
[**meetingregistrantdelete**](MeetingsApi.md#meetingregistrantdelete) | **DELETE** /meetings/{meetingId}/registrants/{registrantId} | Delete a meeting registrant
[**meetings**](MeetingsApi.md#meetings) | **GET** /users/{userId}/meetings | List meetings
[**past_meeting_details**](MeetingsApi.md#past_meeting_details) | **GET** /past_meetings/{meetingId} | Get past meeting details
[**past_meeting_participants**](MeetingsApi.md#past_meeting_participants) | **GET** /past_meetings/{meetingId}/participants | Get past meeting participants
[**past_meetings**](MeetingsApi.md#past_meetings) | **GET** /past_meetings/{meetingId}/instances | List past meeting instances

# **add_batch_registrants**
> InlineResponse20111 add_batch_registrants(meeting_id, body=body)

Perform batch registration

Register up to 30 registrants at once for a meeting that requires [registration](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).       **Prerequisites:**     * The meeting host must be a Licensed user. * The meeting must require registration and should be of type `2`, i.e., they should be scheduled meetings. Instant meetings and Recurring meetings are not supported by this API.           **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | Unique identifier of the meeting (Meeting Number).
body = zoom.MeetingIdBatchRegistrantsBody() # MeetingIdBatchRegistrantsBody |  (optional)

try:
    # Perform batch registration
    api_response = api_instance.add_batch_registrants(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->add_batch_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| Unique identifier of the meeting (Meeting Number). | 
 **body** | [**MeetingIdBatchRegistrantsBody**](MeetingIdBatchRegistrantsBody.md)|  | [optional] 

### Return type

[**InlineResponse20111**](InlineResponse20111.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_polls**
> InlineResponse20110 create_batch_polls(meeting_id, body=body)

Perform batch poll creation

Polls allow the meeting host to survey attendees. Create batch [polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) for a meeting.          **Prerequisites**:     * Host user type must be **Pro** or higher plan. * Polling feature must be enabled in the host's account. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | 
body = zoom.MeetingIdBatchPollsBody() # MeetingIdBatchPollsBody | Batch Meeting poll object (optional)

try:
    # Perform batch poll creation
    api_response = api_instance.create_batch_polls(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->create_batch_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**|  | 
 **body** | [**MeetingIdBatchPollsBody**](MeetingIdBatchPollsBody.md)| Batch Meeting poll object | [optional] 

### Return type

[**InlineResponse20110**](InlineResponse20110.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meeting_chat_message_by_id**
> delete_meeting_chat_message_by_id(meeting_id, message_id, file_ids=file_ids)

Delete a live meeting message

Delete a message in a live meeting, based on ID.   **Prerequisites:**  * Have Zoom enable the DLP for the in-meeting chat feature to use this API.  **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** an integer. Meeting IDs can exceed 10 digits.
message_id = 'message_id_example' # str | The live meeting chat message's unique identifier (UUID), in base64-encoded format.
file_ids = 'file_ids_example' # str | The live webinar chat file's universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas. (optional)

try:
    # Delete a live meeting message
    api_instance.delete_meeting_chat_message_by_id(meeting_id, message_id, file_ids=file_ids)
except ApiException as e:
    print("Exception when calling MeetingsApi->delete_meeting_chat_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, store it as a long-format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **message_id** | **str**| The live meeting chat message&#x27;s unique identifier (UUID), in base64-encoded format. | 
 **file_ids** | **str**| The live webinar chat file&#x27;s universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meeting_live_stream_details**
> InlineResponse20049 get_meeting_live_stream_details(meeting_id)

Get livestream details

Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Get a meeting's livestream configuration details such as Stream URL, Stream Key and Page URL.         **Prerequisites:**     * Meeting host must be a licensed user with a Pro or higher plan.     * Live streaming details must have been [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the meeting.           **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | Unique identifier of the meeting.

try:
    # Get livestream details
    api_response = api_instance.get_meeting_live_stream_details(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->get_meeting_live_stream_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| Unique identifier of the meeting. | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sip_dialing_with_passcode**
> InlineResponse20051 get_sip_dialing_with_passcode(meeting_id, body=body)

Get a meeting SIP URI with Passcode

Get a meeting's SIP URI.  The URI consists of the meeting ID, (optional, user-supplied) passcode and participant identifier code.  The API return data also includes additional fields to indicate whether the API caller has a valid Cloud Room Connector subscription, the participant identifier code from the URI, and the SIP URI validity period (in seconds).     **Scopes:** `meeting:write:sip_dialing`,`meeting:write:admin:sip_dialing`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingIdSipDialingBody() # MeetingIdSipDialingBody |  (optional)

try:
    # Get a meeting SIP URI with Passcode
    api_response = api_instance.get_sip_dialing_with_passcode(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->get_sip_dialing_with_passcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingIdSipDialingBody**](MeetingIdSipDialingBody.md)|  | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getameetingsummary**
> InlineResponse20050 getameetingsummary(meeting_id)

Get a meeting summary

Displays information about a meeting summary.  **Prerequisites**: * Host user type must be Pro or higher plan. * The Meeting Summary with AI Companion feature enabled in the host's account. * E2ee meetings do not have summary feature enabled.  **Scopes:** `meeting_summary:read:admin`,`meeting_summary:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's universally unique ID (UUID). When you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

try:
    # Get a meeting summary
    api_response = api_instance.getameetingsummary(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->getameetingsummary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s universally unique ID (UUID). When you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **in_meeting_control**
> in_meeting_control(meeting_id, body=body)

Use in-meeting controls

Control [in-meeting](https://support.zoom.us/hc/en-us/articles/360021921032-In-Meeting-Controls) features. In-meeting controls include starting and stopping a recording, pausing and resuming a recording, and inviting participants.   **Note:** This API's recording control only works for cloud recordings. It does **not** work for local recordings.   **Prerequisites:** * The meeting **must** be a live meeting **except** inviting participants to the meeting through [call out (phone)/(room system)].  * Recording control: [Cloud recording](https://support.zoom.us/hc/en-us/articles/360060231472-Enabling-cloud-recording) must be enabled on the account.  * The user calling this API must be the host or an alternative meeting host.     **Scopes:** `meeting:write`,`meeting:write:admin`,`meeting:master`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The live meeting's ID.
body = zoom.MeetingIdEventsBody() # MeetingIdEventsBody |  (optional)

try:
    # Use in-meeting controls
    api_instance.in_meeting_control(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->in_meeting_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The live meeting&#x27;s ID. | 
 **body** | [**MeetingIdEventsBody**](MeetingIdEventsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_meeting_templates**
> InlineResponse20057 list_meeting_templates(user_id)

List meeting templates

List available [meeting templates](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates) for a user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API.

try:
    # List meeting templates
    api_response = api_instance.list_meeting_templates(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->list_meeting_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API. | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_meeting_polls**
> InlineResponse20055 list_past_meeting_polls(meeting_id)

List past meeting's poll results

[Polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) allow the meeting host to survey attendees. List poll results of a meeting.          **Prerequisites**:     * Host user type must be **Pro**. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.  **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

try:
    # List past meeting's poll results
    api_response = api_instance.list_past_meeting_polls(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->list_past_meeting_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_meeting_qa**
> InlineResponse20056 list_past_meeting_qa(meeting_id)

List past meetings' Q&A

The question &amp; answer (Q&amp;A) feature for Zoom Meetings lets attendees ask questions during a meeting and lets the other attendees answer those questions.     List Q&amp;A of a specific meeting.  **Prerequisites:**     *   **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

try:
    # List past meetings' Q&A
    api_response = api_instance.list_past_meeting_qa(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->list_past_meeting_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listmeetingsummaries**
> InlineResponse20044 listmeetingsummaries(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)

List meeting summaries of an account

Generates a list of all meeting summaries for an account.  **Prerequisites** * Host user type must be Pro or higher plan. * The Meeting Summary with AI Companion feature enabled in the host's account. * E2ee meetings do not have summary feature enabled.  **Scopes:** `meeting_summary:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries. (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries. (optional)

try:
    # List meeting summaries of an account
    api_response = api_instance.listmeetingsummaries(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->listmeetingsummaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **datetime**| The start date in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;&#x60; UTC format used to retrieve the creation date range of the meeting summaries. | [optional] 
 **to** | **datetime**| The end date in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;&#x60; UTC format used to retrieve the creation date range of the meeting summaries. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting**
> InlineResponse20045 meeting(meeting_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)

Get a meeting

Retrieve tha given meeting's details.        **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be more than 10 digits.
occurrence_id = 'occurrence_id_example' # str | Meeting occurrence ID. Provide this field to view meeting details of a particular occurrence of the [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings). (optional)
show_previous_occurrences = true # bool | Set this field's value to `true` to view meeting details of all previous occurrences of a [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings).  (optional)

try:
    # Get a meeting
    api_response = api_instance.meeting(meeting_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be more than 10 digits. | 
 **occurrence_id** | **str**| Meeting occurrence ID. Provide this field to view meeting details of a particular occurrence of the [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings). | [optional] 
 **show_previous_occurrences** | **bool**| Set this field&#x27;s value to &#x60;true&#x60; to view meeting details of all previous occurrences of a [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings).  | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_create**
> InlineResponse20114 meeting_create(user_id, body=body)

Create a meeting

[Create a meeting](https://support.zoom.us/hc/en-us/articles/201362413-Scheduling-meetings) for a user. For user-level apps, pass [the `me` value](/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  * A meeting's `start_url` value is the URL a host or an alternative host can use to start a meeting. The expiration time for the `start_url` value is **two hours** for all regular users. * For `custCreate` meeting hosts (users created with the `custCreate` parameter via the [**Create users**](/api-reference/zoom-api/methods#operation/userCreate) API), the expiration time of the `start_url` parameter is **90 days** from the generation of the `start_url`.  **Note:**   For security reasons, the recommended way to programmatically get the updated `start_url` value after expiry is to call the [**Get a meeting**](/api-reference/zoom-api/methods#operation/meeting) API. Refer to the `start_url` value in the response.    **100 requests per day**. The rate limit is applied against the `userId` of the **meeting host** used to make the request.  **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserIdMeetingsBody() # UserIdMeetingsBody | Meeting object. (optional)

try:
    # Create a meeting
    api_response = api_instance.meeting_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdMeetingsBody**](UserIdMeetingsBody.md)| Meeting object. | [optional] 

### Return type

[**InlineResponse20114**](InlineResponse20114.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_delete**
> meeting_delete(meeting_id, occurrence_id=occurrence_id, schedule_for_reminder=schedule_for_reminder, cancel_meeting_reminder=cancel_meeting_reminder)

Delete a meeting

Delete a meeting.           **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)
schedule_for_reminder = true # bool | `true`: Notify host and alternative host about the meeting cancellation via email. `false`: Do not send any email notification. (optional)
cancel_meeting_reminder = true # bool | `true`: Notify registrants about the meeting cancellation via email.   `false`: Do not send any email notification to meeting registrants.   The default value of this field is `false`. (optional)

try:
    # Delete a meeting
    api_instance.meeting_delete(meeting_id, occurrence_id=occurrence_id, schedule_for_reminder=schedule_for_reminder, cancel_meeting_reminder=cancel_meeting_reminder)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 
 **schedule_for_reminder** | **bool**| &#x60;true&#x60;: Notify host and alternative host about the meeting cancellation via email. &#x60;false&#x60;: Do not send any email notification. | [optional] 
 **cancel_meeting_reminder** | **bool**| &#x60;true&#x60;: Notify registrants about the meeting cancellation via email.   &#x60;false&#x60;: Do not send any email notification to meeting registrants.   The default value of this field is &#x60;false&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_invitation**
> MeetingInvitation meeting_invitation(meeting_id)

Get meeting invitation

Retrieve the meeting invitation note for a specific meeting.  **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # Get meeting invitation
    api_response = api_instance.meeting_invitation(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

[**MeetingInvitation**](MeetingInvitation.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_invite_links_create**
> InviteLinks1 meeting_invite_links_create(meeting_id, body=body)

Create meeting's invite links

Create a batch of invitation links for a meeting.    **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.InviteLinks() # InviteLinks |  (optional)

try:
    # Create meeting's invite links
    api_response = api_instance.meeting_invite_links_create(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_invite_links_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**InviteLinks**](InviteLinks.md)|  | [optional] 

### Return type

[**InviteLinks1**](InviteLinks1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_live_stream_status_update**
> meeting_live_stream_status_update(meeting_id, body=body)

Update Live Stream Status

Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Update the status of a meeting's livestream.         **Prerequisites:**     * Meeting host must have a Pro license.       **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.LivestreamStatusBody() # LivestreamStatusBody | Meeting (optional)

try:
    # Update Live Stream Status
    api_instance.meeting_live_stream_status_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_live_stream_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**LivestreamStatusBody**](LivestreamStatusBody.md)| Meeting | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_live_stream_update**
> meeting_live_stream_update(meeting_id, body=body)

Update a livestream

Update a meeting's livestream information. Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform.  **Prerequisites:**  * Meeting host must have a Pro license.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingIdLivestreamBody() # MeetingIdLivestreamBody | Meeting (optional)

try:
    # Update a livestream
    api_instance.meeting_live_stream_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_live_stream_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingIdLivestreamBody**](MeetingIdLivestreamBody.md)| Meeting | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_live_streaming_join_token**
> InlineResponse20046 meeting_live_streaming_join_token(meeting_id)

Get a meeting's join token for live streaming

Get a meeting's join token to allow live streaming. The join token allows a recording bot implemented using Zoom meeting SDK to connect to a Zoom meeting &quot;hosted by the issuer of the token&quot;, and can call the streaming method automatically. It supports both regular live streaming, and raw streaming.   **Prerequisites:**  * A Pro or higher plan for the meeting host.  * The **Allow livestreaming of meetings** user setting enabled in the Zoom web portal.  **Scopes:** `meeting_token:read:admin:live_streaming`,`meeting_token:read:live_streaming`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # Get a meeting's join token for live streaming
    api_response = api_instance.meeting_live_streaming_join_token(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_live_streaming_join_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_local_archiving_archive_token**
> InlineResponse20047 meeting_local_archiving_archive_token(meeting_id)

Get a meeting's archive token for local archiving

Get a meeting's archive token to allow local archiving. The archive token allows a meeting SDK app or bot to get archive permission to access the meeting's raw audio and video media stream in real-time.   **Prerequisites:**  * A Pro or higher plan for the meeting host.  * The **Archive meetings and webinars** account setting enabled in the Zoom web portal.  **Scopes:** `meeting_token:read:admin:local_archiving`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # Get a meeting's archive token for local archiving
    api_response = api_instance.meeting_local_archiving_archive_token(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_local_archiving_archive_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_local_recording_join_token**
> InlineResponse20048 meeting_local_recording_join_token(meeting_id)

Get a meeting's join token for local recording

Get a meeting's join token to allow for local recording. The join token lets a recording bot implemented using Zoom Meeting SDK to connect to a Zoom meeting. The recording bot can then automatically start locally recording. This supports both regular and raw local recording types.   **Prerequisites:**  * The **Local recording** user setting enabled in the Zoom web portal.  **Scopes:** `meeting_token:read:admin:local_recording`,`meeting_token:read:local_recording`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # Get a meeting's join token for local recording
    api_response = api_instance.meeting_local_recording_join_token(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_local_recording_join_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_create**
> MeetingAndWebinarPollingObject1 meeting_poll_create(meeting_id, body=body)

Create a meeting poll

Polls allow the meeting host to survey attendees. Create a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) for a meeting.          **Prerequisites**:     * Host user type must be **Pro** or higher plan. * Polling feature must be enabled in the host's account. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingAndWebinarPollingObject() # MeetingAndWebinarPollingObject | Meeting poll object (optional)

try:
    # Create a meeting poll
    api_response = api_instance.meeting_poll_create(meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingAndWebinarPollingObject**](MeetingAndWebinarPollingObject.md)| Meeting poll object | [optional] 

### Return type

[**MeetingAndWebinarPollingObject1**](MeetingAndWebinarPollingObject1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_delete**
> meeting_poll_delete(meeting_id, poll_id)

Delete a meeting poll

Polls allow the meeting host to survey attendees. Delete a meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).     **Prerequisites**:     * Host user type must be **Pro**. * Polling feature should be enabled in the host's account. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Delete a meeting poll
    api_instance.meeting_poll_delete(meeting_id, poll_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_get**
> MeetingAndWebinarPollingObject1 meeting_poll_get(meeting_id, poll_id)

Get a meeting poll

Polls allow the meeting host to survey attendees. Retrieve information about a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).           **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Get a meeting poll
    api_response = api_instance.meeting_poll_get(meeting_id, poll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **poll_id** | **str**| The poll ID | 

### Return type

[**MeetingAndWebinarPollingObject1**](MeetingAndWebinarPollingObject1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_update**
> meeting_poll_update(meeting_id, poll_id, body=body)

Update a meeting poll

Polls allow the meeting host to survey attendees. Update information of a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings)           **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
poll_id = 'poll_id_example' # str | The poll ID
body = zoom.MeetingAndWebinarPollingObject2() # MeetingAndWebinarPollingObject2 | Meeting Poll (optional)

try:
    # Update a meeting poll
    api_instance.meeting_poll_update(meeting_id, poll_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **poll_id** | **str**| The poll ID | 
 **body** | [**MeetingAndWebinarPollingObject2**](MeetingAndWebinarPollingObject2.md)| Meeting Poll | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_polls**
> PollList meeting_polls(meeting_id, anonymous=anonymous)

List meeting polls

Polls allow the meeting host to survey attendees. List all [polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) of a meeting.          **Prerequisites**:     * Host user type must be **Pro** or higher plan. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.  **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
anonymous = true # bool | Whether to query for polls with the **Anonymous** option enabled:  * `true` &mdash; Query for polls with the **Anonymous** option enabled.  * `false` &mdash; Do not query for polls with the **Anonymous** option enabled. (optional)

try:
    # List meeting polls
    api_response = api_instance.meeting_polls(meeting_id, anonymous=anonymous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **anonymous** | **bool**| Whether to query for polls with the **Anonymous** option enabled:  * &#x60;true&#x60; &amp;mdash; Query for polls with the **Anonymous** option enabled.  * &#x60;false&#x60; &amp;mdash; Do not query for polls with the **Anonymous** option enabled. | [optional] 

### Return type

[**PollList**](PollList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_create**
> InlineResponse20112 meeting_registrant_create(meeting_id, body=body, occurrence_ids=occurrence_ids)

Add a meeting registrant

Create and submit a user's registration to a meeting. See [Customizing webinar registration](https://support.zoom.us/hc/en-us/articles/202835649-Customizing-webinar-registration) for details on how to set the requirements for these fields. Note that there is a maximum limit of 4,999 registrants per meeting and users will see an error if the meeting's capacity is reached.    **Prerequisites:**  * The host must be a **Licensed** user type.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingIdRegistrantsBody() # MeetingIdRegistrantsBody |  (optional)
occurrence_ids = 'occurrence_ids_example' # str | A comma-separated list of meeting occurrence IDs. You can get this value with the [Get a meeting](/docs/api-reference/zoom-api/methods#operation/meeting) API. (optional)

try:
    # Add a meeting registrant
    api_response = api_instance.meeting_registrant_create(meeting_id, body=body, occurrence_ids=occurrence_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingIdRegistrantsBody**](MeetingIdRegistrantsBody.md)|  | [optional] 
 **occurrence_ids** | **str**| A comma-separated list of meeting occurrence IDs. You can get this value with the [Get a meeting](/docs/api-reference/zoom-api/methods#operation/meeting) API. | [optional] 

### Return type

[**InlineResponse20112**](InlineResponse20112.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_get**
> MeetingRegistrant meeting_registrant_get(meeting_id, registrant_id)

Get a meeting registrant

Retrieve details on a specific user who has registered for the meeting. A host or a user with administrative permissions can require [registration for Zoom meetings](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).  **Prerequisites:**  * The account must have a Meeting plan  **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
registrant_id = 'registrant_id_example' # str | The registrant ID.

try:
    # Get a meeting registrant
    api_response = api_instance.meeting_registrant_get(meeting_id, registrant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **registrant_id** | **str**| The registrant ID. | 

### Return type

[**MeetingRegistrant**](MeetingRegistrant.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_question_update**
> meeting_registrant_question_update(meeting_id, body=body)

Update registration questions

Update registration questions that will be displayed to users while [registering for a meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).           **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingRegistrantQuestions1() # MeetingRegistrantQuestions1 | Meeting Registrant Questions (optional)

try:
    # Update registration questions
    api_instance.meeting_registrant_question_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingRegistrantQuestions1**](MeetingRegistrantQuestions1.md)| Meeting Registrant Questions | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_status**
> meeting_registrant_status(meeting_id, body=body, occurrence_id=occurrence_id)

Update registrant's status

Update a meeting registrant's status by either approving, cancelling or denying a registrant from joining the meeting.           **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.RegistrantsStatusBody1() # RegistrantsStatusBody1 |  (optional)
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)

try:
    # Update registrant's status
    api_instance.meeting_registrant_status(meeting_id, body=body, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**RegistrantsStatusBody1**](RegistrantsStatusBody1.md)|  | [optional] 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrants**
> RegistrationList meeting_registrants(meeting_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List meeting registrants

A host or a user with admin permission can require [registration for a Zoom meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings). List users that have registered for a meeting.           **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
occurrence_id = 'occurrence_id_example' # str | The meeting or webinar occurrence ID. (optional)
status = 'approved' # str | Query by the registrant's status.  * `pending` - The registration is pending.  * `approved` - The registrant is approved.  * `denied` - The registration is denied. (optional) (default to approved)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List meeting registrants
    api_response = api_instance.meeting_registrants(meeting_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **occurrence_id** | **str**| The meeting or webinar occurrence ID. | [optional] 
 **status** | **str**| Query by the registrant&#x27;s status.  * &#x60;pending&#x60; - The registration is pending.  * &#x60;approved&#x60; - The registrant is approved.  * &#x60;denied&#x60; - The registration is denied. | [optional] [default to approved]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**RegistrationList**](RegistrationList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrants_questions_get**
> MeetingRegistrantQuestions meeting_registrants_questions_get(meeting_id)

List registration questions 

List registration questions that will be displayed to users while [registering for a meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).        **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # List registration questions 
    api_response = api_instance.meeting_registrants_questions_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

[**MeetingRegistrantQuestions**](MeetingRegistrantQuestions.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_status**
> meeting_status(meeting_id, body=body)

Update meeting status

Update the status of a meeting.           **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
body = zoom.MeetingIdStatusBody() # MeetingIdStatusBody |  (optional)

try:
    # Update meeting status
    api_instance.meeting_status(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **body** | [**MeetingIdStatusBody**](MeetingIdStatusBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_survey_delete**
> meeting_survey_delete(meeting_id)

Delete a meeting survey

Delete a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting).    **Prerequisites:**  * The host must be a **Pro** user type.  * The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature enabled in the host's account.  * The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.  **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

try:
    # Delete a meeting survey
    api_instance.meeting_survey_delete(meeting_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_survey_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_survey_get**
> MeetingSurveyObject meeting_survey_get(meeting_id)

Get a meeting survey

Display information about a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting).  **Prerequisites:** * The host has a **Pro** license. * The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature is enabled on the host's account. * The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.  **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be more than 10 digits.

try:
    # Get a meeting survey
    api_response = api_instance.meeting_survey_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_survey_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be more than 10 digits. | 

### Return type

[**MeetingSurveyObject**](MeetingSurveyObject.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_survey_update**
> meeting_survey_update(meeting_id, body=body)

Update a meeting survey

Update a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting).  **Prerequisites:** * The host must be a **Pro** user type. * The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature is enabled in the host's account. * The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.  **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be over 10 digits.
body = zoom.MeetingSurveyObject1() # MeetingSurveyObject1 |  (optional)

try:
    # Update a meeting survey
    api_instance.meeting_survey_update(meeting_id, body=body)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_survey_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be over 10 digits. | 
 **body** | [**MeetingSurveyObject1**](MeetingSurveyObject1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_template_create**
> InlineResponse20113 meeting_template_create(user_id, body=body)

Create a meeting template from an existing meeting

Create a meeting template from an existing meeting.     **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API.
body = zoom.UserIdMeetingTemplatesBody() # UserIdMeetingTemplatesBody |  (optional)

try:
    # Create a meeting template from an existing meeting
    api_response = api_instance.meeting_template_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_template_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID retrievable from the [List users](/api-reference/zoom-api/methods#operation/users) API. | 
 **body** | [**UserIdMeetingTemplatesBody**](UserIdMeetingTemplatesBody.md)|  | [optional] 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_token**
> InlineResponse20052 meeting_token(meeting_id, type=type)

Get meeting's token

Get a meeting's [closed caption token (caption URL)](https://support.zoom.us/hc/en-us/articles/115002212983-Using-a-third-party-closed-captioning-service). This token lets you use a third-party service to stream text to their closed captioning software to the Zoom meeting.   **Prerequisites:**  * The **Closed captioning** setting enabled in the Zoom web portal.  * The **Allow use of caption API Token to integrate with 3rd-party Closed Captioning services** setting enabled.  **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.
type = 'closed_caption_token' # str | The meeting token type:  * `closed_caption_token` &mdash; The third-party closed caption API token.   This defaults to `closed_caption_token`. (optional) (default to closed_caption_token)

try:
    # Get meeting's token
    api_response = api_instance.meeting_token(meeting_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits. | 
 **type** | **str**| The meeting token type:  * &#x60;closed_caption_token&#x60; &amp;mdash; The third-party closed caption API token.   This defaults to &#x60;closed_caption_token&#x60;. | [optional] [default to closed_caption_token]

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_update**
> meeting_update(meeting_id, body=body, occurrence_id=occurrence_id)

Update a meeting

Update meeting details.  **Note**  * This API has a rate limit of **100 requests per day**. You can update a meeting for a maximum of **100 times within a 24-hour period**.  * The `start_time` value **must** be a future date. If the value is omitted or a date in the past, the API ignores this value and does **not** update any recurring meetings.  * The `recurrence` object is **required**.    **Scopes:** `meeting:write`,`meeting:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The meeting's ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be greater than 10 digits.
body = zoom.MeetingsMeetingIdBody() # MeetingsMeetingIdBody | Meeting (optional)
occurrence_id = 'occurrence_id_example' # str | Meeting occurrence ID. Support change of agenda, `start_time`, duration, or settings {`host_video`, `participant_video`, `join_before_host`, `mute_upon_entry`, `waiting_room`, `watermark`, `auto_recording`}. (optional)

try:
    # Update a meeting
    api_instance.meeting_update(meeting_id, body=body, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting&#x27;s ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be greater than 10 digits. | 
 **body** | [**MeetingsMeetingIdBody**](MeetingsMeetingIdBody.md)| Meeting | [optional] 
 **occurrence_id** | **str**| Meeting occurrence ID. Support change of agenda, &#x60;start_time&#x60;, duration, or settings {&#x60;host_video&#x60;, &#x60;participant_video&#x60;, &#x60;join_before_host&#x60;, &#x60;mute_upon_entry&#x60;, &#x60;waiting_room&#x60;, &#x60;watermark&#x60;, &#x60;auto_recording&#x60;}. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meetingregistrantdelete**
> meetingregistrantdelete(meeting_id, registrant_id, occurrence_id=occurrence_id)

Delete a meeting registrant

Delete a meeting registrant.           **Scopes:** `meeting:write:admin`,`meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 56 # int | The meeting ID.
registrant_id = 'registrant_id_example' # str | The meeting registrant ID.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)

try:
    # Delete a meeting registrant
    api_instance.meetingregistrantdelete(meeting_id, registrant_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meetingregistrantdelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID. | 
 **registrant_id** | **str**| The meeting registrant ID. | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meetings**
> InlineResponse20058 meetings(user_id, type=type, page_size=page_size, next_page_token=next_page_token, page_number=page_number, _from=_from, to=to)

List meetings

List a meeting host user's scheduled meetings. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.   **Note**  * This API **only** supports scheduled meetings. This API does not return information about instant meetings.  * This API only returns a user's [unexpired meetings](https://support.zoom.us/hc/en-us/articles/201362373-Meeting-ID#h_c73f9b08-c1c0-4a1a-b538-e01ebb98e844).      **Scopes:** `meeting:read`,`meeting:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
type = 'scheduled' # str | The type of meeting.  * `scheduled` - All valid previous (unexpired) meetings, live meetings, and upcoming scheduled meetings.  * `live` - All the ongoing meetings.  * `upcoming` - All upcoming meetings, including live meetings.  * `upcoming_meetings` - All upcoming meetings, including live meetings.  * `previous_meetings` - All the previous meetings. (optional) (default to scheduled)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
page_number = 56 # int | The page number of the current page in the returned records. (optional)
_from = '2013-10-20' # date | The start date. (optional)
to = '2013-10-20' # date | The end data. (optional)

try:
    # List meetings
    api_response = api_instance.meetings(user_id, type=type, page_size=page_size, next_page_token=next_page_token, page_number=page_number, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **type** | **str**| The type of meeting.  * &#x60;scheduled&#x60; - All valid previous (unexpired) meetings, live meetings, and upcoming scheduled meetings.  * &#x60;live&#x60; - All the ongoing meetings.  * &#x60;upcoming&#x60; - All upcoming meetings, including live meetings.  * &#x60;upcoming_meetings&#x60; - All upcoming meetings, including live meetings.  * &#x60;previous_meetings&#x60; - All the previous meetings. | [optional] [default to scheduled]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **page_number** | **int**| The page number of the current page in the returned records. | [optional] 
 **_from** | **date**| The start date. | [optional] 
 **to** | **date**| The end data. | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meeting_details**
> InlineResponse20053 past_meeting_details(meeting_id)

Get past meeting details

Get information about a past meeting.      **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId3() # MeetingId3 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

try:
    # Get past meeting details
    api_response = api_instance.past_meeting_details(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meeting_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId3**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meeting_participants**
> InlineResponse20054 past_meeting_participants(meeting_id, page_size=page_size, next_page_token=next_page_token)

Get past meeting participants

Retrieve information on participants from a past meeting. Note the API doesn't return results if there's only one participant in a meeting.         **Prerequisites:**     * Paid account on a Pro or higher plan.             **Note**: Please double encode your UUID when using this API if the UUID begins with a '/'or contains '//' in it.   **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get past meeting participants
    api_response = api_instance.past_meeting_participants(meeting_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meeting_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meetings**
> MeetingInstances past_meetings(meeting_id)

List past meeting instances

Return a list of past meeting instances.      **Scopes:** `meeting:read:admin`,`meeting:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.MeetingsApi(zoom.ApiClient(configuration))
meeting_id = 789 # int | The past meeting's ID.

try:
    # List past meeting instances
    api_response = api_instance.past_meetings(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The past meeting&#x27;s ID. | 

### Return type

[**MeetingInstances**](MeetingInstances.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

