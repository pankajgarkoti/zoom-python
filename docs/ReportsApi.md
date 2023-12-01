# zoom.ReportsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_invoices_reports**](ReportsApi.md#get_billing_invoices_reports) | **GET** /report/billing/invoices | Get billing invoice reports
[**get_billing_report**](ReportsApi.md#get_billing_report) | **GET** /report/billing | Get billing reports
[**report_cloud_recording**](ReportsApi.md#report_cloud_recording) | **GET** /report/cloud_recording | Get cloud recording usage report
[**report_daily**](ReportsApi.md#report_daily) | **GET** /report/daily | Get daily usage report
[**report_meeting_details**](ReportsApi.md#report_meeting_details) | **GET** /report/meetings/{meetingId} | Get meeting detail reports
[**report_meeting_participants**](ReportsApi.md#report_meeting_participants) | **GET** /report/meetings/{meetingId}/participants | Get meeting participant reports
[**report_meeting_polls**](ReportsApi.md#report_meeting_polls) | **GET** /report/meetings/{meetingId}/polls | Get meeting poll reports
[**report_meeting_qa**](ReportsApi.md#report_meeting_qa) | **GET** /report/meetings/{meetingId}/qa | Get meeting Q&amp;A report
[**report_meetings**](ReportsApi.md#report_meetings) | **GET** /report/users/{userId}/meetings | Get meeting reports
[**report_operation_logs**](ReportsApi.md#report_operation_logs) | **GET** /report/operationlogs | Get operation logs report
[**report_sign_in_sign_out_activities**](ReportsApi.md#report_sign_in_sign_out_activities) | **GET** /report/activities | Get sign In / sign out activity report
[**report_telephone**](ReportsApi.md#report_telephone) | **GET** /report/telephone | Get telephone reports
[**report_upcoming_events**](ReportsApi.md#report_upcoming_events) | **GET** /report/upcoming_events | Get upcoming events report
[**report_users**](ReportsApi.md#report_users) | **GET** /report/users | Get active/inactive host reports
[**report_webinar_details**](ReportsApi.md#report_webinar_details) | **GET** /report/webinars/{webinarId} | Get webinar detail reports
[**report_webinar_participants**](ReportsApi.md#report_webinar_participants) | **GET** /report/webinars/{webinarId}/participants | Get webinar participant reports
[**report_webinar_polls**](ReportsApi.md#report_webinar_polls) | **GET** /report/webinars/{webinarId}/polls | Get webinar poll reports
[**report_webinar_qa**](ReportsApi.md#report_webinar_qa) | **GET** /report/webinars/{webinarId}/qa | Get webinar Q&amp;A report

# **get_billing_invoices_reports**
> InlineResponse20062 get_billing_invoices_reports(billing_id)

Get billing invoice reports

Get department billing invoices reports for a specific billing period. Provide the `billing_id` of the billing period for which you would like to retrieve the invoices for. This ID can be retrieved from **Get Billing Reports** API.   **Prerequisites:**     * Pro or a higher account with Department Billing option enabled. Contact the Zoom Support team to enable this feature.    **Scopes:** `report:read:admin`,`report:master`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
billing_id = 'billing_id_example' # str | Unique Identifier of the Billing Report. Retrieve this ID from the response of **Get Billing Reports** API request.   

try:
    # Get billing invoice reports
    api_response = api_instance.get_billing_invoices_reports(billing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_billing_invoices_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_id** | **str**| Unique Identifier of the Billing Report. Retrieve this ID from the response of **Get Billing Reports** API request.    | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_report**
> InlineResponse20061 get_billing_report()

Get billing reports

Get department billing reports of a Zoom account.  **Prerequisites:**     * Pro or a higher account with Department Billing option enabled. Contact Zoom Support team for details.    **Scopes:** `report:read:admin`,`report:master`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))

try:
    # Get billing reports
    api_response = api_instance.get_billing_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_billing_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_cloud_recording**
> InlineResponse20063 report_cloud_recording(_from, to, group_id=group_id)

Get cloud recording usage report

Retrieve cloud recording usage report for a specified period. You can only get cloud recording reports that is one day earlier than the current date and for the most recent period of 6 months. The date gap between from and to dates should be smaller or equal to 30 days.      **Prerequisites**     * Pro or higher plan.       **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. (optional)

try:
    # Get cloud recording usage report
    api_response = api_instance.report_cloud_recording(_from, to, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_cloud_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_daily**
> InlineResponse20064 report_daily(year=year, month=month, group_id=group_id)

Get daily usage report

Retrieve daily report to access the account-wide usage of Zoom services for each day in a given month. It lists the number of new users, meetings, participants, and meeting minutes.     **Prerequisites**     * Pro or higher plan.       **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
year = 56 # int | Year for this report (optional)
month = 56 # int | Month for this report (optional)
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. (optional)

try:
    # Get daily usage report
    api_response = api_instance.report_daily(year=year, month=month, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year for this report | [optional] 
 **month** | **int**| Month for this report | [optional] 
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_meeting_details**
> InlineResponse20065 report_meeting_details(meeting_id)

Get meeting detail reports

Get a detailed report for a past meeting.      **Prerequisites:**     * Pro or a higher plan.        **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId4() # MeetingId4 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

try:
    # Get meeting detail reports
    api_response = api_instance.report_meeting_details(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_meeting_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId4**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_meeting_participants**
> InlineResponse20066 report_meeting_participants(meeting_id, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)

Get meeting participant reports

Return a report of a past meeting with two or more participants, including the host. To return a report for past meeting with only **one** participant, use the [**List meeting participants**](/docs/api-reference/zoom-api/ma#operation/dashboardMeetingParticipants) API.   **Note:**   This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API:  * Does **not** have a signed HIPAA business associate agreement (BAA).  * Is a [**legacy** HIPAA BAA account](/docs/api-reference/other-references/legacy-business-associate-agreements).   **Prerequisites:**  * A Pro or a higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
include_fields = 'include_fields_example' # str | Provide `registrant_id` as the value for this field if you would like to see the registrant ID attribute in the response of this API call. A registrant ID is a unique identifier of a [meeting registrant](/docs/api-reference/zoom-api/methods#operation/meetingRegistrants). (optional)

try:
    # Get meeting participant reports
    api_response = api_instance.report_meeting_participants(meeting_id, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_meeting_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the meeting UUID before making an API request. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **include_fields** | **str**| Provide &#x60;registrant_id&#x60; as the value for this field if you would like to see the registrant ID attribute in the response of this API call. A registrant ID is a unique identifier of a [meeting registrant](/docs/api-reference/zoom-api/methods#operation/meetingRegistrants). | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_meeting_polls**
> InlineResponse20067 report_meeting_polls(meeting_id)

Get meeting poll reports

Use this API to get a report of [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) results for a past meeting.    **Prerequisites:**  * A Pro or a higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId5() # MeetingId5 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

try:
    # Get meeting poll reports
    api_response = api_instance.report_meeting_polls(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_meeting_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId5**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_meeting_qa**
> InlineResponse20068 report_meeting_qa(meeting_id)

Get meeting Q&A report

The question &amp; answer (Q&amp;A) feature for meetings lets attendees ask questions during the meeting and lets the other attendees answer their questions.  Use this API to retrieve a report on question and answers from past meetings.          **Prerequisites:**     * Pro or a higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
meeting_id = zoom.MeetingId6() # MeetingId6 | The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

try:
    # Get meeting Q&A report
    api_response = api_instance.report_meeting_qa(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_meeting_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | [**MeetingId6**](.md)| The meeting&#x27;s ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request. | 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_meetings**
> InlineResponse20073 report_meetings(user_id, _from, to, page_size=page_size, next_page_token=next_page_token, type=type)

Get meeting reports

Retrieve [report](https://support.zoom.us/hc/en-us/articles/216378603-Meeting-Reporting) on past meetings and webinars for a specified time period. The time range for the report is limited to a month and the month must fall within the past six months.  Meetings and webinars are returned only if they have two or more unique participants.           **Prerequisites:**     * Pro or higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
user_id = zoom.UserId1() # UserId1 | The user ID or email address of the user. For user-level apps, pass the `me` value.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
type = 'past' # str | The meeting type to query for:  * `past` &mdash; All past meetings.  * `pastOne` &mdash; A single past user meeting.  * `pastJoined` &mdash; All past meetings the account's users hosted or joined. (optional) (default to past)

try:
    # Get meeting reports
    api_response = api_instance.report_meetings(user_id, _from, to, page_size=page_size, next_page_token=next_page_token, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId1**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **type** | **str**| The meeting type to query for:  * &#x60;past&#x60; &amp;mdash; All past meetings.  * &#x60;pastOne&#x60; &amp;mdash; A single past user meeting.  * &#x60;pastJoined&#x60; &amp;mdash; All past meetings the account&#x27;s users hosted or joined. | [optional] [default to past]

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_operation_logs**
> InlineResponse20069 report_operation_logs(_from, to, page_size=page_size, next_page_token=next_page_token, category_type=category_type)

Get operation logs report

The [Operations Logs](https://support.zoom.us/hc/en-us/articles/360032748331-Operation-Logs) report allows you to audit admin and user activity, such as adding a new user, changing account settings, and deleting recordings.     Use this API to retrieve operation logs report for a specified period of time.     **Prerequisites:**     * Pro or higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
category_type = 'category_type_example' # str | **Optional**     Filter your response by a category type to see reports for a specific category. The value for this field can be one of the following:     `all`    `user`    `user_settings`    `account`    `billing`    `im`    `recording`    `phone_contacts`    `webinar`    `sub_account`    `role`    `zoom_rooms` (optional)

try:
    # Get operation logs report
    api_response = api_instance.report_operation_logs(_from, to, page_size=page_size, next_page_token=next_page_token, category_type=category_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_operation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **category_type** | **str**| **Optional**     Filter your response by a category type to see reports for a specific category. The value for this field can be one of the following:     &#x60;all&#x60;    &#x60;user&#x60;    &#x60;user_settings&#x60;    &#x60;account&#x60;    &#x60;billing&#x60;    &#x60;im&#x60;    &#x60;recording&#x60;    &#x60;phone_contacts&#x60;    &#x60;webinar&#x60;    &#x60;sub_account&#x60;    &#x60;role&#x60;    &#x60;zoom_rooms&#x60; | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_sign_in_sign_out_activities**
> InlineResponse20060 report_sign_in_sign_out_activities(_from=_from, to=to, page_size=page_size, next_page_token=next_page_token)

Get sign In / sign out activity report

Retrieve a list of sign in / sign out activity logs [report](https://support.zoom.us/hc/en-us/articles/201363213-Getting-Started-with-Reports) of users under a Zoom account.     **Prerequisites**     * Pro or higher plan.       **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date for which you would like to view the activity logs report. Using the `from` and `to` parameters, specify a monthly date range for the report as the API only provides one month worth of data in one request. The specified date range should fall within the last six months. (optional)
to = '2013-10-20' # date | End date up to which you would like to view the activity logs report. (optional)
page_size = 56 # int | The number of records to be returned within a single API call (optional)
next_page_token = 'next_page_token_example' # str | Next page token is used to paginate through large result sets (optional)

try:
    # Get sign In / sign out activity report
    api_response = api_instance.report_sign_in_sign_out_activities(_from=_from, to=to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_sign_in_sign_out_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date for which you would like to view the activity logs report. Using the &#x60;from&#x60; and &#x60;to&#x60; parameters, specify a monthly date range for the report as the API only provides one month worth of data in one request. The specified date range should fall within the last six months. | [optional] 
 **to** | **date**| End date up to which you would like to view the activity logs report. | [optional] 
 **page_size** | **int**| The number of records to be returned within a single API call | [optional] 
 **next_page_token** | **str**| Next page token is used to paginate through large result sets | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_telephone**
> InlineResponse20070 report_telephone(_from, to, type=type, query_date_type=query_date_type, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

Get telephone reports

The [telephone report](https://support.zoom.us/hc/en-us/articles/206514816-Telephone-reports) allows you to view who dialed into meetings via phone (Audio Conferencing or SIP Connected Audio) and which number they dialed into and other details. Use this API to get telephone report for a specified period of time.  **Prerequisites:**     * Pro or higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = '1' # str | Audio types:    `1` - Toll-free Call-in &amp; Call-out.    `2` - Toll      `3` - SIP Connected Audio (optional) (default to 1)
query_date_type = 'start_time' # str | The type of date to query.  * `start_time` &mdash; Query by call start time.  * `end_time` &mdash; Query by call end time.  * `meeting_start_time` &mdash; Query by meeting start time.  * `meeting_end_time` &mdash; Query by meeting end time.   This value defaults to `start_time`. (optional) (default to start_time)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The page number of the current page in the returned records. This field is **not** available if the `query_date_type` parameter is the `meeting_start_time` or `meeting_end_time` value.   This field is deprecated. Use the `next_page_token` query parameter for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get telephone reports
    api_response = api_instance.report_telephone(_from, to, type=type, query_date_type=query_date_type, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_telephone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| Audio types:    &#x60;1&#x60; - Toll-free Call-in &amp;amp; Call-out.    &#x60;2&#x60; - Toll      &#x60;3&#x60; - SIP Connected Audio | [optional] [default to 1]
 **query_date_type** | **str**| The type of date to query.  * &#x60;start_time&#x60; &amp;mdash; Query by call start time.  * &#x60;end_time&#x60; &amp;mdash; Query by call end time.  * &#x60;meeting_start_time&#x60; &amp;mdash; Query by meeting start time.  * &#x60;meeting_end_time&#x60; &amp;mdash; Query by meeting end time.   This value defaults to &#x60;start_time&#x60;. | [optional] [default to start_time]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The page number of the current page in the returned records. This field is **not** available if the &#x60;query_date_type&#x60; parameter is the &#x60;meeting_start_time&#x60; or &#x60;meeting_end_time&#x60; value.   This field is deprecated. Use the &#x60;next_page_token&#x60; query parameter for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_upcoming_events**
> InlineResponse20071 report_upcoming_events(_from, to, page_size=page_size, next_page_token=next_page_token, type=type, group_id=group_id)

Get upcoming events report

Use this API to list upcoming meeting and/or webinar events within a specified period of time. The report's time range is limited to one month.  **Prerequisites:**  * A Pro or higher plan  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
type = 'all' # str | The type of event to query.  * `meeting` &mdash; A meeting event.  * `webinar` &mdash; A webinar event.  * `all` &mdash; Both meeting and webinar events.  This value defaults to `all`. (optional) (default to all)
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. (optional)

try:
    # Get upcoming events report
    api_response = api_instance.report_upcoming_events(_from, to, page_size=page_size, next_page_token=next_page_token, type=type, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_upcoming_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **type** | **str**| The type of event to query.  * &#x60;meeting&#x60; &amp;mdash; A meeting event.  * &#x60;webinar&#x60; &amp;mdash; A webinar event.  * &#x60;all&#x60; &amp;mdash; Both meeting and webinar events.  This value defaults to &#x60;all&#x60;. | [optional] [default to all]
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID. | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_users**
> InlineResponse20072 report_users(_from, to, type=type, page_size=page_size, page_number=page_number, next_page_token=next_page_token, group_id=group_id)

Get active/inactive host reports

A user is considered to be an active host during the month specified in the &quot;from&quot; and &quot;to&quot; range, if the user has hosted at least one meeting during this period. If the user didn't host any meetings during this period, the user is considered to be inactive.    The Active Hosts report displays a list of meetings, participants, and meeting minutes for a specific time range, up to one month. The month should fall within the last six months.    The Inactive Hosts report pulls a list of users who were not active during a specific period of time.  Use this API to retrieve an active or inactive host report for a specified period of time. The time range for the report is limited to a month and the month should fall under the past six months.     Specify the type of report and date range using the query parameters.     **Prerequisites:**     * Pro or higher plan.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = 'type_example' # str | Active or inactive hosts.    `active` - Active hosts.     `inactive` - Inactive hosts. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The page number of the current page in the returned records. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
group_id = 'group_id_example' # str | The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. (optional)

try:
    # Get active/inactive host reports
    api_response = api_instance.report_users(_from, to, type=type, page_size=page_size, page_number=page_number, next_page_token=next_page_token, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the &amp;quot;from&amp;quot; and &amp;quot;to&amp;quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| Active or inactive hosts.    &#x60;active&#x60; - Active hosts.     &#x60;inactive&#x60; - Inactive hosts. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The page number of the current page in the returned records. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **group_id** | **str**| The group ID. To get a group ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.    **Note:** The API response will only contain users who are members of the queried group ID. | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_webinar_details**
> InlineResponse20074 report_webinar_details(webinar_id)

Get webinar detail reports

Retrieve a [report](https://support.zoom.us/hc/en-us/articles/201393719-Webinar-Reporting) containing past webinar details.           **Prerequisites:**     * Pro or higher plan with Webinar add-on.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

try:
    # Get webinar detail reports
    api_response = api_instance.report_webinar_details(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_webinar_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_webinar_participants**
> InlineResponse20075 report_webinar_participants(webinar_id, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)

Get webinar participant reports

Get a detailed report on each webinar attendee. You can get webinar participant reports for the last 6 months.    **Prerequisites:**  * A Pro or a higher plan with Webinar add-on enabled.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
include_fields = 'include_fields_example' # str | The additional query parameters to include.  * `registrant_id` - Include the registrant's ID in the API response. The registrant ID is the webinar participant's unique ID. (optional)

try:
    # Get webinar participant reports
    api_response = api_instance.report_webinar_participants(webinar_id, page_size=page_size, next_page_token=next_page_token, include_fields=include_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_webinar_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the webinar UUID before making an API request. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **include_fields** | **str**| The additional query parameters to include.  * &#x60;registrant_id&#x60; - Include the registrant&#x27;s ID in the API response. The registrant ID is the webinar participant&#x27;s unique ID. | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_webinar_polls**
> InlineResponse20076 report_webinar_polls(webinar_id)

Get webinar poll reports

Retrieve a report on past [webinar polls](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).         **Prerequisites:**     * Pro or a higher plan with Webinar add-on enabled.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.

try:
    # Get webinar poll reports
    api_response = api_instance.report_webinar_polls(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_webinar_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** double-encode the webinar UUID before making an API request. | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_webinar_qa**
> InlineResponse20077 report_webinar_qa(webinar_id)

Get webinar Q&A report

The Question &amp; Answer (Q&amp;A) feature for webinars allows attendees to ask questions during the webinar and for the panelists, co-hosts and host to answer their questions.  Use this API to retrieve a report on question and answers from past webinars.          **Prerequisites:**     * Pro or a higher plan with Webinar add-on enabled.  **Scopes:** `report:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ReportsApi(zoom.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

try:
    # Get webinar Q&A report
    api_response = api_instance.report_webinar_qa(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->report_webinar_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar&#x27;s ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a &#x60;/&#x60; character or contains the &#x60;//&#x60; characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request. | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

