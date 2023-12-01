# zoom.DashboardsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_chat**](DashboardsApi.md#dashboard_chat) | **GET** /metrics/chat | Get chat metrics
[**dashboard_client_feedback**](DashboardsApi.md#dashboard_client_feedback) | **GET** /metrics/client/feedback | List Zoom meetings client feedback
[**dashboard_client_feedback_detail**](DashboardsApi.md#dashboard_client_feedback_detail) | **GET** /metrics/client/feedback/{feedbackId} | Get zoom meetings client feedback
[**dashboard_crc**](DashboardsApi.md#dashboard_crc) | **GET** /metrics/crc | Get CRC port usage
[**dashboard_issue_detail_zoom_room**](DashboardsApi.md#dashboard_issue_detail_zoom_room) | **GET** /metrics/issues/zoomrooms/{zoomroomId} | Get issues of Zoom Rooms
[**dashboard_issue_zoom_room**](DashboardsApi.md#dashboard_issue_zoom_room) | **GET** /metrics/issues/zoomrooms | Get top 25 Zoom Rooms with issues
[**dashboard_meeting_detail**](DashboardsApi.md#dashboard_meeting_detail) | **GET** /metrics/meetings/{meetingId} | Get meeting details
[**dashboard_meeting_participant_qos**](DashboardsApi.md#dashboard_meeting_participant_qos) | **GET** /metrics/meetings/{meetingId}/participants/{participantId}/qos | Get meeting participant QoS
[**dashboard_meeting_participant_share**](DashboardsApi.md#dashboard_meeting_participant_share) | **GET** /metrics/meetings/{meetingId}/participants/sharing | Get meeting sharing/recording details
[**dashboard_meeting_participants**](DashboardsApi.md#dashboard_meeting_participants) | **GET** /metrics/meetings/{meetingId}/participants | List meeting participants
[**dashboard_meeting_participants_qos**](DashboardsApi.md#dashboard_meeting_participants_qos) | **GET** /metrics/meetings/{meetingId}/participants/qos | List meeting participants QoS
[**dashboard_meetings**](DashboardsApi.md#dashboard_meetings) | **GET** /metrics/meetings | List meetings
[**dashboard_quality**](DashboardsApi.md#dashboard_quality) | **GET** /metrics/quality | Get meeting quality scores
[**dashboard_webinar_detail**](DashboardsApi.md#dashboard_webinar_detail) | **GET** /metrics/webinars/{webinarId} | Get webinar details
[**dashboard_webinar_participant_qos**](DashboardsApi.md#dashboard_webinar_participant_qos) | **GET** /metrics/webinars/{webinarId}/participants/{participantId}/qos | Get webinar participant QoS
[**dashboard_webinar_participant_share**](DashboardsApi.md#dashboard_webinar_participant_share) | **GET** /metrics/webinars/{webinarId}/participants/sharing | Get webinar sharing/recording details
[**dashboard_webinar_participants**](DashboardsApi.md#dashboard_webinar_participants) | **GET** /metrics/webinars/{webinarId}/participants | Get webinar participants
[**dashboard_webinar_participants_qos**](DashboardsApi.md#dashboard_webinar_participants_qos) | **GET** /metrics/webinars/{webinarId}/participants/qos | List webinar participant QoS
[**dashboard_webinars**](DashboardsApi.md#dashboard_webinars) | **GET** /metrics/webinars | List webinars
[**dashboard_zoom_room**](DashboardsApi.md#dashboard_zoom_room) | **GET** /metrics/zoomrooms/{zoomroomId} | Get Zoom Rooms details
[**dashboard_zoom_room_issue**](DashboardsApi.md#dashboard_zoom_room_issue) | **GET** /metrics/zoomrooms/issues | Get top 25 issues of Zoom Rooms
[**dashboard_zoom_rooms**](DashboardsApi.md#dashboard_zoom_rooms) | **GET** /metrics/zoomrooms | List Zoom Rooms
[**get_client_versions**](DashboardsApi.md#get_client_versions) | **GET** /metrics/client_versions | List the client versions
[**list_meeting_satisfaction**](DashboardsApi.md#list_meeting_satisfaction) | **GET** /metrics/client/satisfaction | List client meeting satisfaction
[**participant_feedback**](DashboardsApi.md#participant_feedback) | **GET** /metrics/meetings/{meetingId}/participants/satisfaction | Get post meeting feedback
[**participant_webinar_feedback**](DashboardsApi.md#participant_webinar_feedback) | **GET** /metrics/webinars/{webinarId}/participants/satisfaction | Get post webinar feedback

# **dashboard_chat**
> InlineResponse20016 dashboard_chat(_from, to, page_size=page_size, next_page_token=next_page_token)

Get chat metrics

Get [metrics](https://support.zoom.us/hc/en-us/articles/204654719-Dashboard#h_cc7e9749-1c70-4afb-a9a2-9680654821e4) for how users are utilizing Zoom Chat to send messages.  Use the `from` and `to` query parameters to specify a monthly date range for the dashboard data. The monthly date range must be within the last six months.  &gt; **Note:** To query chat metrics from July 1, 2021 and later, use this endpoint instead of the [**Get IM metrics**](/docs/api-reference/zoom-api/methods#operation/dashboardIM) API.  **Prerequisites:**  * Business or a higher plan  **Scopes:** `dashboard_im:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get chat metrics
    api_response = api_instance.dashboard_chat(_from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_client_feedback**
> InlineResponse20017 dashboard_client_feedback(_from, to)

List Zoom meetings client feedback

Use this API to return [Zoom meetings client feedback](https://support.zoom.us/hc/en-us/articles/115005855266-End-of-Meeting-Feedback-Survey#h_e30d552b-6d8e-4e0a-a588-9ca8180c4dbf) survey results. You can specify a monthly date range for the Dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.   **Prerequisites:**  * A Business or higher account.  * The &quot;[**Feedback to Zoom**](https://support.zoom.us/hc/en-us/articles/115005838023)&quot; option enabled.  **Scopes:** `dashboard_home:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # List Zoom meetings client feedback
    api_response = api_instance.dashboard_client_feedback(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_client_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_client_feedback_detail**
> InlineResponse20018 dashboard_client_feedback_detail(feedback_id, _from=_from, to=to, page_size=page_size, next_page_token=next_page_token)

Get zoom meetings client feedback

Retrieve detailed information on a [Zoom meetings client feedback](https://support.zoom.us/hc/en-us/articles/115005855266-End-of-Meeting-Feedback-Survey#h_e30d552b-6d8e-4e0a-a588-9ca8180c4dbf).      You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  **Prerequisites:** * Business or higher account * [Feedback to Zoom](https://support.zoom.us/hc/en-us/articles/115005838023) enabled.    **Scopes:** `dashboard_home:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
feedback_id = 'feedback_id_example' # str | Feedback Detail Id
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
page_size = 30 # int |  (optional) (default to 30)
next_page_token = 'next_page_token_example' # str |  (optional)

try:
    # Get zoom meetings client feedback
    api_response = api_instance.dashboard_client_feedback_detail(feedback_id, _from=_from, to=to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_client_feedback_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**| Feedback Detail Id | 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 30]
 **next_page_token** | **str**|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_crc**
> InlineResponse20021 dashboard_crc(_from, to)

Get CRC port usage

A Cloud Room Connector allows H.323/SIP endpoints to connect to a Zoom meeting.   Use this API to get the hour by hour CRC Port usage for a specified period of time. &lt;aside class='notice'&gt;We will provide the report for a maximum of one month. For example, if &quot;from&quot; is set to &quot;2017-08-05&quot; and &quot;to&quot; is set to &quot;2017-10-10&quot;, we will adjust &quot;from&quot; to &quot;2017-09-10&quot;.&lt;/aside&gt;         **Prerequisites:**     * Business, Education or API Plan. * Room Connector must be enabled on the account.           **Scopes:** `dashboard_crc:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get CRC port usage
    api_response = api_instance.dashboard_crc(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_crc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_issue_detail_zoom_room**
> InlineResponse20023 dashboard_issue_detail_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)

Get issues of Zoom Rooms

Use this API to return information about the Zoom Rooms in an account with issues, such as disconnected hardware or bandwidth issues. You can specify a monthly date range for the Dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.   **Prerequisites:**  * A Business or a higher plan.  * A Zoom Room must be enabled in the account.  **Scopes:** `dashboard_home:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
zoomroom_id = 'zoomroom_id_example' # str | The Zoom room ID.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get issues of Zoom Rooms
    api_response = api_instance.dashboard_issue_detail_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_issue_detail_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoomroom_id** | **str**| The Zoom room ID. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_issue_zoom_room**
> InlineResponse20022 dashboard_issue_zoom_room(_from, to)

Get top 25 Zoom Rooms with issues

Get information on top 25 Zoom Rooms with issues in a month. The month specified with the &quot;from&quot; and &quot;to&quot; range should fall within the last six months.     **Prerequisites:**     * Business or a higher plan. * Zoom Room must be enabled in the account.  **Scopes:** `dashboard_home:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get top 25 Zoom Rooms with issues
    api_response = api_instance.dashboard_issue_zoom_room(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_issue_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_detail**
> MeetingMetrics dashboard_meeting_detail(meeting_id, type=type)

Get meeting details

Get details on live or past meetings. This overview will show if features such as audio, video, screen sharing, and recording were being used in the meeting. You can also see the license types of each user on your account.     You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.       **Prerequisites:**      * Business or a higher plan.  **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId() # MeetingId | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.
type = 'live' # str | The type of meeting to query:  * `past` &mdash; All past meetings.  * `pastOne` &mdash; All past one-user meetings.  * `live` - All live meetings.   This value defaults to `live`. (optional) (default to live)

try:
    # Get meeting details
    api_response = api_instance.dashboard_meeting_detail(meeting_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 
 **type** | **str**| The type of meeting to query:  * &#x60;past&#x60; &amp;mdash; All past meetings.  * &#x60;pastOne&#x60; &amp;mdash; All past one-user meetings.  * &#x60;live&#x60; - All live meetings.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]

### Return type

[**MeetingMetrics**](MeetingMetrics.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participant_qos**
> ParticipantQOS dashboard_meeting_participant_qos(meeting_id, participant_id, type=type)

Get meeting participant QoS

Return the quality of service (QoS) report for participants from live or past meetings. The data returned indicates the connection quality for sending/receiving video, audio, and shared content. The API returns this data for either the API request or when the API request was last received.   When the sender sends data, a timestamp is attached to the sender's data packet. The receiver then returns this timestamp to the sender. This helps determine the upstream and downstream latency, which includes the application processing time. The latency data returned is the five second average and five second maximum.    This API will **not** return data if there is no data being sent or received at the time of request.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](https://developers.zoom.us/docs/api/rest/other-references/legacy-business-associate-agreements/).  * Displays data for any users who are **not** part of the host's account (external users) unless they meet certain conditions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.     **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.
participant_id = 'participant_id_example' # str | The participant's ID.
type = 'live' # str | The type of meeting to query.  * `past` - All past meetings.  * `live` - All live meetings.   This value defaults to `live`. (optional) (default to live)

try:
    # Get meeting participant QoS
    api_response = api_instance.dashboard_meeting_participant_qos(meeting_id, participant_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participant_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 
 **participant_id** | **str**| The participant&#x27;s ID. | 
 **type** | **str**| The type of meeting to query.  * &#x60;past&#x60; - All past meetings.  * &#x60;live&#x60; - All live meetings.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]

### Return type

[**ParticipantQOS**](ParticipantQOS.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participant_share**
> InlineResponse20027 dashboard_meeting_participant_share(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get meeting sharing/recording details

Retrieve the sharing and recording details of participants from live or past meetings.     **Prerequisites:**      * Business or a higher plan.  **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId2() # MeetingId2 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.
type = 'live' # str | The type of meeting to query:  * `past` &mdash; All past meetings.  * `live` - All live meetings.   This value defaults to `live`. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceed the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get meeting sharing/recording details
    api_response = api_instance.dashboard_meeting_participant_share(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participant_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId2**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 
 **type** | **str**| The type of meeting to query:  * &#x60;past&#x60; &amp;mdash; All past meetings.  * &#x60;live&#x60; - All live meetings.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceed the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participants**
> InlineResponse20025 dashboard_meeting_participants(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)

List meeting participants

Return a list of participants from live or past meetings.    If you do not provide the `type` query parameter, the default value will be set to the `live` value. This API will only return metrics for participants in a live meeting, if any exist. You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](/docs/api-reference/other-references/legacy-business-associate-agreements).  * Displays data for any users who are **not** part of the host's account (external users) unless they meet certain conditions. See [Email address display rules](/docs/api-reference/using-zoom-apis#email-address) for details.   **Prerequisites:**  * A Business or higher plan.  **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.
type = 'live' # str | The type of meeting to query.  * `past` - All past meetings.  * `pastOne` - All past one-user meetings.  * `live` - All live meetings.   This value defaults to `live`. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
include_fields = 'include_fields_example' # str | Provide `registrant_id` as the value for this field if you would like to see the registrant ID attribute in the response of this API call. A registrant ID is a unique identifier of a [meeting registrant](/docs/api-reference/zoom-api/methods#operation/meetingRegistrants). This is not supported for `live` meeting types. (optional)

try:
    # List meeting participants
    api_response = api_instance.dashboard_meeting_participants(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 
 **type** | **str**| The type of meeting to query.  * &#x60;past&#x60; - All past meetings.  * &#x60;pastOne&#x60; - All past one-user meetings.  * &#x60;live&#x60; - All live meetings.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **include_fields** | **str**| Provide &#x60;registrant_id&#x60; as the value for this field if you would like to see the registrant ID attribute in the response of this API call. A registrant ID is a unique identifier of a [meeting registrant](/docs/api-reference/zoom-api/methods#operation/meetingRegistrants). This is not supported for &#x60;live&#x60; meeting types. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participants_qos**
> ParticipantQOSList dashboard_meeting_participants_qos(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)

List meeting participants QoS

Show a list of meeting participants from live or past meetings, and their quality of service received during the meeting. The data returned indicates the connection quality for sending or receiving video, audio, and shared content.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API.  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](https://developers.zoom.us/docs/api/rest/other-references/legacy-business-associate-agreements/).  * Displays data for any users who are **not** part of the host's account (external users) unless they meet certain conditions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.   **Prerequisites:**  * A Business or a higher plan.  **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.
type = 'live' # str | The type of meeting to query.  * `past` - All past meetings.  * `live` - All live meetings.   This value defaults to `live`. (optional) (default to live)
page_size = 1 # int | The number of items returned per page. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List meeting participants QoS
    api_response = api_instance.dashboard_meeting_participants_qos(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participants_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 
 **type** | **str**| The type of meeting to query.  * &#x60;past&#x60; - All past meetings.  * &#x60;live&#x60; - All live meetings.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of items returned per page. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**ParticipantQOSList**](ParticipantQOSList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meetings**
> InlineResponse20024 dashboard_meetings(_from, to, type=type, page_size=page_size, next_page_token=next_page_token, group_id=group_id, include_fields=include_fields, query_date_type=query_date_type)

List meetings

Lists the total live or past meetings that occurred during a specified period of time. This overview shows if features such as audio, video, screen sharing, and recording were being used in the meeting. You can also see the license types of each user on your account. You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.   **Prerequisites:**    * Business or a higher plan.        **Scopes:** `dashboard_meetings:read:admin`,`dashboard:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `RESOURCE-INTENSIVE`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '_from_example' # str | The start date in 'yyyy-MM-dd HH:mm:ss' or 'yyyy-MM-dd'format The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = 'to_example' # str | The end date 'yyyy-MM-dd HH:mm:ss' or 'yyyy-MM-dd' format
type = 'live' # str | This field specifies a value to get the response for the corresponding meeting type.      `past` - Meeting that already occurred in the specified date range.    `pastOne` - Past meetings that were attended by only one user.     `live` - Live meetings.          If you do not provide this field, the default value will be `live` and the API will only query responses for live meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. (optional)
include_fields = 'include_fields_example' # str | This field sets the value of this field to &quot;tracking_fields&quot; if you would like to include tracking fields of each meeting in the response. (optional)
query_date_type = 'query_date_type_example' # str | The type of date to query. This field is only supported when `type` is `past`.  * `start_time` - Query by call start time.  * `end_time` - Query by call end time.   This value defaults to `start_time`. (optional)

try:
    # List meetings
    api_response = api_instance.dashboard_meetings(_from, to, type=type, page_size=page_size, next_page_token=next_page_token, group_id=group_id, include_fields=include_fields, query_date_type=query_date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The start date in &#x27;yyyy-MM-dd HH:mm:ss&#x27; or &#x27;yyyy-MM-dd&#x27;format The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **str**| The end date &#x27;yyyy-MM-dd HH:mm:ss&#x27; or &#x27;yyyy-MM-dd&#x27; format | 
 **type** | **str**| This field specifies a value to get the response for the corresponding meeting type.      &#x60;past&#x60; - Meeting that already occurred in the specified date range.    &#x60;pastOne&#x60; - Past meetings that were attended by only one user.     &#x60;live&#x60; - Live meetings.          If you do not provide this field, the default value will be &#x60;live&#x60; and the API will only query responses for live meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. | [optional] 
 **include_fields** | **str**| This field sets the value of this field to &amp;quot;tracking_fields&amp;quot; if you would like to include tracking fields of each meeting in the response. | [optional] 
 **query_date_type** | **str**| The type of date to query. This field is only supported when &#x60;type&#x60; is &#x60;past&#x60;.  * &#x60;start_time&#x60; - Query by call start time.  * &#x60;end_time&#x60; - Query by call end time.   This value defaults to &#x60;start_time&#x60;. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_quality**
> InlineResponse20028 dashboard_quality(_from, to, type=type)

Get meeting quality scores

Use this API to return [meeting quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Meeting-quality-scores-and-network-alerts-on-Dashboard) information. Meeting quality scores are based on the mean opinion score (MOS). The MOS measures a meeting's quality on a scale of &quot;Good&quot; (5-4), &quot;Fair&quot; (4-3), &quot;Poor&quot; (3-2), or &quot;Bad&quot; (2-1).   **Prerequisites:**  * A Business or a higher plan.  **Scopes:** `dashboard_home:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = 'meeting' # str | The type of meeting quality score to query:  * `meeting` &mdash; Query by meetings.  * `participants` &mdash; Query by meeting participants. (optional) (default to meeting)

try:
    # Get meeting quality scores
    api_response = api_instance.dashboard_quality(_from, to, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_quality: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| The type of meeting quality score to query:  * &#x60;meeting&#x60; &amp;mdash; Query by meetings.  * &#x60;participants&#x60; &amp;mdash; Query by meeting participants. | [optional] [default to meeting]

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_detail**
> WebinarMetrics dashboard_webinar_detail(webinar_id, type=type)

Get webinar details

Retrieve details from live or past webinars.         **Prerequisites:**     * Business, Education or API Plan with Webinar add-on.    **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.
type = 'live' # str | The type of webinar to query:  * `past` &mdash; All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)

try:
    # Get webinar details
    api_response = api_instance.dashboard_webinar_detail(webinar_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 
 **type** | **str**| The type of webinar to query:  * &#x60;past&#x60; &amp;mdash; All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]

### Return type

[**WebinarMetrics**](WebinarMetrics.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participant_qos**
> ParticipantQOS1 dashboard_webinar_participant_qos(webinar_id, participant_id, type=type)

Get webinar participant QoS

Return the quality of service (QoS) for participants during live or past webinars. This data returned indicates the connection quality for sending/receiving video, audio, and shared content. The API returns this data for either the API request or when the API request was last received.   When the sender sends its data, a timestamp is attached to the sender's data packet. The receiver then returns this timestamp to the sender. This helps determine the upstream and downstream latency, which includes the application processing time. The latency data returned is the five second average and five second maximum.   This API will **not** return data if there is no data being sent or received at the time of request.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](https://developers.zoom.us/docs/api/rest/other-references/legacy-business-associate-agreements/).  * Displays data for any users who are **not** part of the host's account, such as external users, unless they meet certain conditions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.   **Prerequisites:**  * A Business, Education, or API Plan with Zoom Rooms set up.  **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.
participant_id = 'participant_id_example' # str | The participant's ID.
type = 'live' # str | The type of webinar to query.  * `past` - All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)

try:
    # Get webinar participant QoS
    api_response = api_instance.dashboard_webinar_participant_qos(webinar_id, participant_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participant_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the webinar UUID before making an API request. | 
 **participant_id** | **str**| The participant&#x27;s ID. | 
 **type** | **str**| The type of webinar to query.  * &#x60;past&#x60; - All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]

### Return type

[**ParticipantQOS1**](ParticipantQOS1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participant_share**
> InlineResponse20032 dashboard_webinar_participant_share(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get webinar sharing/recording details

Retrieve the sharing and recording details of participants from live or past webinars.          **Prerequisites:**     * Business, Education or API Plan with Webinar add-on.    **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.
type = 'live' # str | The type of webinar to query:  * `past` &mdash; All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceed the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get webinar sharing/recording details
    api_response = api_instance.dashboard_webinar_participant_share(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participant_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 
 **type** | **str**| The type of webinar to query:  * &#x60;past&#x60; &amp;mdash; All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceed the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participants**
> InlineResponse20030 dashboard_webinar_participants(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)

Get webinar participants

Return information about participants from live or past webinars.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](/docs/api-reference/other-references/legacy-business-associate-agreements).  * Displays data for any users who are **not** part of the host's account (external users) unless they meet certain conditions. See [Email address display rules](/docs/api-reference/using-zoom-apis#email-address) for details.   **Prerequisites:**  * A Business, Education, or API Plan with Webinar add-on.  **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.
type = 'live' # str | The type of webinar to query.  * `past` - All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
include_fields = 'include_fields_example' # str | Additional fields to include in the query.  * `registrant_id` - Include the webinar registrant's ID. The registrant ID is the [webinar registrant's unique ID](/docs/api-reference/zoom-api/methods#operation/webinarRegistrants). (optional)

try:
    # Get webinar participants
    api_response = api_instance.dashboard_webinar_participants(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the webinar UUID before making an API request. | 
 **type** | **str**| The type of webinar to query.  * &#x60;past&#x60; - All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **include_fields** | **str**| Additional fields to include in the query.  * &#x60;registrant_id&#x60; - Include the webinar registrant&#x27;s ID. The registrant ID is the [webinar registrant&#x27;s unique ID](/docs/api-reference/zoom-api/methods#operation/webinarRegistrants). | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participants_qos**
> ParticipantQOSList1 dashboard_webinar_participants_qos(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

List webinar participant QoS

Show a list of webinar participants from live or past webinars and the quality of service they received during the webinar. The data returned indicates the connection quality for sending/receiving video, audio, and shared content.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](https://developers.zoom.us/docs/api/rest/other-references/legacy-business-associate-agreements/).  * Displays data for any users who are **not** part of the host's account, such as external users, unless they meet certain conditions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.   **Prerequisites:**  * A Business, Education, or API Plan with Webinar add-on.  **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.
type = 'live' # str | The type of webinar to query.  * `past` - All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)
page_size = 1 # int | The number of items returned per page. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List webinar participant QoS
    api_response = api_instance.dashboard_webinar_participants_qos(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participants_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the webinar UUID before making an API request. | 
 **type** | **str**| The type of webinar to query.  * &#x60;past&#x60; - All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of items returned per page. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**ParticipantQOSList1**](ParticipantQOSList1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinars**
> InlineResponse20029 dashboard_webinars(_from, to, type=type, page_size=page_size, next_page_token=next_page_token, group_id=group_id)

List webinars

List all the live or past webinars from a specified period of time.          **Prerequisites:**     * Business, Education or API Plan with Webinar add-on.     **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = 'live' # str | The type of webinar to query:  * `past` &mdash; All past webinars.  * `live` - All live webinars.   This value defaults to `live`. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. (optional)

try:
    # List webinars
    api_response = api_instance.dashboard_webinars(_from, to, type=type, page_size=page_size, next_page_token=next_page_token, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| The type of webinar to query:  * &#x60;past&#x60; &amp;mdash; All past webinars.  * &#x60;live&#x60; - All live webinars.   This value defaults to &#x60;live&#x60;. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_room**
> ZoomRoom dashboard_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)

Get Zoom Rooms details

The Zoom Rooms dashboard metrics lets you know the type of configuration a Zoom room has and details on the meetings held in that room.   Use this API to retrieve information on a specific room.         **Prerequisites:**     * Business, Education or API Plan with Zoom Rooms set up.   **Scopes:** `dashboard_zr:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
zoomroom_id = 'zoomroom_id_example' # str | The Zoom room ID.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get Zoom Rooms details
    api_response = api_instance.dashboard_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoomroom_id** | **str**| The Zoom room ID. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**ZoomRoom**](ZoomRoom.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_room_issue**
> InlineResponse20033 dashboard_zoom_room_issue(_from, to)

Get top 25 issues of Zoom Rooms

Get top 25 issues of Zoom Rooms.     **Prerequisites:**     * Business, Education or API Plan with Zoom Rooms set up.    **Scopes:** `dashboard_zr:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get top 25 issues of Zoom Rooms
    api_response = api_instance.dashboard_zoom_room_issue(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_room_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_rooms**
> ZoomRoomList dashboard_zoom_rooms(page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List Zoom Rooms

List information on all Zoom Rooms in an account.         **Prerequisites:**     * Business, Education or API Plan with Zoom Rooms set up.     **Scopes:** `dashboard_zr:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The page number of the current page in the returned records. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Zoom Rooms
    api_response = api_instance.dashboard_zoom_rooms(page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The page number of the current page in the returned records. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**ZoomRoomList**](ZoomRoomList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_versions**
> InlineResponse20020 get_client_versions()

List the client versions

Use this API to list all the client versions and its count.    **Prerequisites:**  * A Business or a higher plan.  **Scopes:** `dashboard:read:admin,dashboard_home:read:admin,zms:dashboard:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))

try:
    # List the client versions
    api_response = api_instance.get_client_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_client_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_meeting_satisfaction**
> InlineResponse20019 list_meeting_satisfaction(_from=_from, to=to)

List client meeting satisfaction

If the [End of Meeting Feedback Survey](https://support.zoom.us/hc/en-us/articles/115005855266) option is enabled, attendees will be prompted with a survey window where they can tap either the **Thumbs Up** or **Thumbs Down** button that indicates their Zoom meeting experience. With this API, you can get information on the attendees' meeting satisfaction. Specify a monthly date range for the query using the from and to query parameters. The month should fall within the last six months.  To get information on the survey results with negative experiences (indicated by **Thumbs Down**), use the [**Get Zoom meetings client feedback**](/docs/api-reference/zoom-api/methods#operation/dashboardClientFeedbackDetail) API.       **Scopes:** `dashboard:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | The start date for the query in &ldquo;yyyy-mm-dd&rdquo; format.  (optional)
to = '2013-10-20' # date | The end date for the query in &ldquo;yyyy-mm-dd&rdquo; format.  (optional)

try:
    # List client meeting satisfaction
    api_response = api_instance.list_meeting_satisfaction(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->list_meeting_satisfaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start date for the query in &amp;ldquo;yyyy-mm-dd&amp;rdquo; format.  | [optional] 
 **to** | **date**| The end date for the query in &amp;ldquo;yyyy-mm-dd&amp;rdquo; format.  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **participant_feedback**
> InlineResponse20026 participant_feedback(meeting_id, type=type, next_page_token=next_page_token, page_size=page_size)

Get post meeting feedback

When a meeting ends, each attendee will be prompted to share their meeting experience by clicking either thumbs up or thumbs down. Use this API to retrieve the feedback submitted for a specific meeting. Note that this API only works for meetings scheduled after December 20, 2020.  **Prerequisites:** * [Feedback to Zoom](https://support.zoom.us/hc/en-us/articles/115005838023) setting must be enabled by the participant prior to the meeting. * The user making the API request must be enrolled in a Business or a higher plan.         **Scopes:** `dashboard_meetings:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId1() # MeetingId1 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.
type = 'live' # str | Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:         `past` - Meeting that already occurred in the specified date range.    `pastOne` - Past meetings that were attended by only one user.     `live` - Live meetings.          If you do not provide this field, the default value will be `live` and thus, the API will only query responses for live meetings. (optional) (default to live)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # Get post meeting feedback
    api_response = api_instance.participant_feedback(meeting_id, type=type, next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->participant_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId1**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 
 **type** | **str**| Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:         &#x60;past&#x60; - Meeting that already occurred in the specified date range.    &#x60;pastOne&#x60; - Past meetings that were attended by only one user.     &#x60;live&#x60; - Live meetings.          If you do not provide this field, the default value will be &#x60;live&#x60; and thus, the API will only query responses for live meetings. | [optional] [default to live]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **participant_webinar_feedback**
> InlineResponse20031 participant_webinar_feedback(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get post webinar feedback

When a Webinar ends, each attendee will be prompted to share their Webinar experience by clicking either thumbs up or thumbs down. Use this API to retrieve the feedback submitted for a specific webinar. Note that this API only works for meetings scheduled after December 20, 2020.  **Prerequisites:** * [Feedback to Zoom](https://support.zoom.us/hc/en-us/articles/115005838023) setting must be enabled by the participant prior to the meeting. * The user making the API request must be enrolled in a Business or a higher plan.          **Scopes:** `dashboard_webinars:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.DashboardsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.
type = 'live' # str | Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:         `past` - Meeting that already occurred in the specified date range.    `pastOne` - Past meetings that were attended by only one user.     `live` - Live meetings.          If you do not provide this field, the default value will be `live` and thus, the API will only query responses for live meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # Get post webinar feedback
    api_response = api_instance.participant_webinar_feedback(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->participant_webinar_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 
 **type** | **str**| Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:         &#x60;past&#x60; - Meeting that already occurred in the specified date range.    &#x60;pastOne&#x60; - Past meetings that were attended by only one user.     &#x60;live&#x60; - Live meetings.          If you do not provide this field, the default value will be &#x60;live&#x60; and thus, the API will only query responses for live meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

