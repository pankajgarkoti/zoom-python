# swagger_client.ArchivingApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_archived_files**](ArchivingApi.md#delete_archived_files) | **DELETE** /past_meetings/{meetingUUID}/archive_files | Delete a meeting&#x27;s archived files
[**get_archived_file_statistics**](ArchivingApi.md#get_archived_file_statistics) | **GET** /archive_files/statistics | Get archived file statistics
[**get_archived_files**](ArchivingApi.md#get_archived_files) | **GET** /past_meetings/{meetingUUID}/archive_files | Get a meeting&#x27;s archived files
[**list_archived_files**](ArchivingApi.md#list_archived_files) | **GET** /archive_files | List archived files
[**update_archived_file**](ArchivingApi.md#update_archived_file) | **PATCH** /archive_files/{fileId} | Update an archived file&#x27;s auto-delete status

# **delete_archived_files**
> delete_archived_files(meeting_uuid)

Delete a meeting's archived files

Use this API to delete all of a meeting's archived files.    **Prerequisites:**  * The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).  **Scopes:** `recording:write:admin`,`recording:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.ArchivingApi(swagger_client.ApiClient(configuration))
meeting_uuid = 'meeting_uuid_example' # str | The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.

try:
    # Delete a meeting's archived files
    api_instance.delete_archived_files(meeting_uuid)
except ApiException as e:
    print("Exception when calling ArchivingApi->delete_archived_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_uuid** | **str**| The meeting&#x27;s universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a &#x60;/&#x60; character or contains a &#x60;//&#x60; character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archived_file_statistics**
> InlineResponse2007 get_archived_file_statistics(_from=_from, to=to)

Get archived file statistics

Get statistics about an account's archived meeting or webinar files.    Zoom's [archiving solution](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators) lets account administrators set up an automated mechanism to record, collect, and archive meeting data to a third-party platform of their choice to satisfy FINRA and other compliance requirements.    **Prerequisites:**  * The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).  **Scopes:** `recording:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.ArchivingApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | The query start date, `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `to` query parameter value cannot exceed seven days. (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The query end date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `from` query parameter value cannot exceed seven days. (optional)

try:
    # Get archived file statistics
    api_response = api_instance.get_archived_file_statistics(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivingApi->get_archived_file_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| The query start date, &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x60; format. This value and the &#x60;to&#x60; query parameter value cannot exceed seven days. | [optional] 
 **to** | **datetime**| The query end date, in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x60; format. This value and the &#x60;from&#x60; query parameter value cannot exceed seven days. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archived_files**
> InlineResponse2008 get_archived_files(meeting_uuid)

Get a meeting's archived files

Return a specific meeting instance's [archived files](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators).    **Prerequisites:**  * The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).  **Scopes:** `recording:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.ArchivingApi(swagger_client.ApiClient(configuration))
meeting_uuid = 'meeting_uuid_example' # str | The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. After a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.

try:
    # Get a meeting's archived files
    api_response = api_instance.get_archived_files(meeting_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivingApi->get_archived_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_uuid** | **str**| The meeting&#x27;s universally unique identifier (UUID). Each meeting instance generates a UUID. After a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a &#x60;/&#x60; character or contains a &#x60;//&#x60; character, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archived_files**
> InlineResponse2006 list_archived_files(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, query_date_type=query_date_type)

List archived files

Get an account's archived meeting or webinar files.    Zoom's [archiving solution](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators) lets account administrators set up an automated mechanism to record, collect, and archive meeting data to a third-party platform of their choice to satisfy FINRA or other compliance requirements.    **Prerequisites:**  * The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).  **Scopes:** `recording:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.ArchivingApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The query start date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `to` query parameter value cannot exceed seven days. (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The query end date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `from` query parameter value cannot exceed seven days. (optional)
query_date_type = 'meeting_start_time' # str | The type of query date. * `meeting_start_time`  * `archive_complete_time`    This value defaults to `meeting_start_time`. (optional) (default to meeting_start_time)

try:
    # List archived files
    api_response = api_instance.list_archived_files(page_size=page_size, next_page_token=next_page_token, _from=_from, to=to, query_date_type=query_date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivingApi->list_archived_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **_from** | **datetime**| The query start date, in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x60; format. This value and the &#x60;to&#x60; query parameter value cannot exceed seven days. | [optional] 
 **to** | **datetime**| The query end date, in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ssZ&#x60; format. This value and the &#x60;from&#x60; query parameter value cannot exceed seven days. | [optional] 
 **query_date_type** | **str**| The type of query date. * &#x60;meeting_start_time&#x60;  * &#x60;archive_complete_time&#x60;    This value defaults to &#x60;meeting_start_time&#x60;. | [optional] [default to meeting_start_time]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_archived_file**
> update_archived_file(file_id, body=body)

Update an archived file's auto-delete status

Update an archived file's auto-delete status.    **Prerequisites:**  * [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) must enable the [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) for your account. * Open the disabling auto-delete feature in OP. Contact [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to open.  **Scopes:** `recording:write`,`recording:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.ArchivingApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | 
body = swagger_client.ArchiveFilesFileIdBody() # ArchiveFilesFileIdBody |  (optional)

try:
    # Update an archived file's auto-delete status
    api_instance.update_archived_file(file_id, body=body)
except ApiException as e:
    print("Exception when calling ArchivingApi->update_archived_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **body** | [**ArchiveFilesFileIdBody**](ArchiveFilesFileIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

