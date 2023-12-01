# swagger_client.GroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_group_vb**](GroupsApi.md#del_group_vb) | **DELETE** /groups/{groupId}/settings/virtual_backgrounds | Delete Virtual Background files
[**get_group_lock_settings**](GroupsApi.md#get_group_lock_settings) | **GET** /groups/{groupId}/lock_settings | Get locked settings
[**get_group_settings**](GroupsApi.md#get_group_settings) | **GET** /groups/{groupId}/settings | Get a group&#x27;s settings
[**group**](GroupsApi.md#group) | **GET** /groups/{groupId} | Get a group
[**group_admins**](GroupsApi.md#group_admins) | **GET** /groups/{groupId}/admins | List group admins
[**group_admins_create**](GroupsApi.md#group_admins_create) | **POST** /groups/{groupId}/admins | Add group admins
[**group_admins_delete**](GroupsApi.md#group_admins_delete) | **DELETE** /groups/{groupId}/admins/{userId} | Delete a group admin
[**group_create**](GroupsApi.md#group_create) | **POST** /groups | Create a group
[**group_delete**](GroupsApi.md#group_delete) | **DELETE** /groups/{groupId} | Delete a group
[**group_locked_settings**](GroupsApi.md#group_locked_settings) | **PATCH** /groups/{groupId}/lock_settings | Update locked settings
[**group_members**](GroupsApi.md#group_members) | **GET** /groups/{groupId}/members | List group members 
[**group_members_create**](GroupsApi.md#group_members_create) | **POST** /groups/{groupId}/members | Add group members
[**group_members_delete**](GroupsApi.md#group_members_delete) | **DELETE** /groups/{groupId}/members/{memberId} | Delete a group member
[**group_settings_registration**](GroupsApi.md#group_settings_registration) | **GET** /groups/{groupId}/settings/registration | Get a group&#x27;s webinar registration settings
[**group_settings_registration_update**](GroupsApi.md#group_settings_registration_update) | **PATCH** /groups/{groupId}/settings/registration | Update a group&#x27;s webinar registration settings
[**group_update**](GroupsApi.md#group_update) | **PATCH** /groups/{groupId} | Update a group
[**groups**](GroupsApi.md#groups) | **GET** /groups | List groups
[**update_a_group_member**](GroupsApi.md#update_a_group_member) | **PATCH** /groups/{groupId}/members/{memberId} | Update a group member
[**update_group_settings**](GroupsApi.md#update_group_settings) | **PATCH** /groups/{groupId}/settings | Update a group&#x27;s settings
[**upload_group_vb**](GroupsApi.md#upload_group_vb) | **POST** /groups/{groupId}/settings/virtual_backgrounds | Upload Virtual Background files

# **del_group_vb**
> del_group_vb(group_id, file_ids=file_ids)

Delete Virtual Background files

Use this API to delete a group's [Virtual Background files](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_01EJF3YFEWGT8YA0ZJ079JEDQE).    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID. To get a group's ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.
file_ids = 'file_ids_example' # str | A comma-separated list of the file IDs to delete. (optional)

try:
    # Delete Virtual Background files
    api_instance.del_group_vb(group_id, file_ids=file_ids)
except ApiException as e:
    print("Exception when calling GroupsApi->del_group_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID. To get a group&#x27;s ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API. | 
 **file_ids** | **str**| A comma-separated list of the file IDs to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_lock_settings**
> InlineResponse20039 get_group_lock_settings(group_id, option=option)

Get locked settings

Retrieve a [group's](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) locked settings.  If you lock a setting, the group members will not be able to modify it individually.    **Note:** The `force_pmi_jbh_password` field under meeting settings is to be deprecated on September 22, 2019. This field is replaced by another field that will provide the same functionality.  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Id of the group.
option = 'option_example' # str | Optional query parameters:  * `meeting_security` &mdash; Use this query parameter to view the meeting security settings applied to the user's account. (optional)

try:
    # Get locked settings
    api_response = api_instance.get_group_lock_settings(group_id, option=option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_lock_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group. | 
 **option** | **str**| Optional query parameters:  * &#x60;meeting_security&#x60; &amp;mdash; Use this query parameter to view the meeting security settings applied to the user&#x27;s account. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_settings**
> InlineResponse20041 get_group_settings(group_id, option=option, custom_query_fields=custom_query_fields)

Get a group's settings

Get settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
option = 'option_example' # str | Optional query parameters.  * `meeting_authentication` - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user's account.  * `recording_authentication` - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user's account.  * `meeting_security` - View the meeting security settings applied to the user's account. (optional)
custom_query_fields = 'custom_query_fields_example' # str | Provide the name of the field by which you would like to filter the response. For example, if you provide `host_video` as the value of this field, you will get a response similar to the following:   {  `schedule_meeting`: {  `host_video`: false  } }   You can provide multiple values by separating them with commas(example: `host_video,participant_video`). (optional)

try:
    # Get a group's settings
    api_response = api_instance.get_group_settings(group_id, option=option, custom_query_fields=custom_query_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **option** | **str**| Optional query parameters.  * &#x60;meeting_authentication&#x60; - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user&#x27;s account.  * &#x60;recording_authentication&#x60; - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user&#x27;s account.  * &#x60;meeting_security&#x60; - View the meeting security settings applied to the user&#x27;s account. | [optional] 
 **custom_query_fields** | **str**| Provide the name of the field by which you would like to filter the response. For example, if you provide &#x60;host_video&#x60; as the value of this field, you will get a response similar to the following:   {  &#x60;schedule_meeting&#x60;: {  &#x60;host_video&#x60;: false  } }   You can provide multiple values by separating them with commas(example: &#x60;host_video,participant_video&#x60;). | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group**
> InlineResponse20037 group(group_id)

Get a group

Get a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.

try:
    # Get a group
    api_response = api_instance.group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_admins**
> InlineResponse20038 group_admins(group_id, page_size=page_size, next_page_token=next_page_token)

List group admins

Use this API to return a list of [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) administrators under your account.  **Prerequisites:**  * A Pro, Business, or Education account  **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List group admins
    api_response = api_instance.group_admins(group_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_admins_create**
> group_admins_create(group_id, body=body)

Add group admins

Use this API to add administrators to a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisites:**  * A Pro, Business, or Education account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
body = swagger_client.GroupIdAdminsBody() # GroupIdAdminsBody |  (optional)

try:
    # Add group admins
    api_instance.group_admins_create(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->group_admins_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **body** | [**GroupIdAdminsBody**](GroupIdAdminsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_admins_delete**
> group_admins_delete(group_id, user_id)

Delete a group admin

Use this API to remove a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) administrator in a Zoom account.  **Prerequisites:**  * A Pro, Business, or Education account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
user_id = swagger_client.UserId() # UserId | The user ID or email address of the user. For user-level apps, pass the `me` value.

try:
    # Delete a group admin
    api_instance.group_admins_delete(group_id, user_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_admins_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **user_id** | [**UserId**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create**
> group_create(body=body)

Create a group

Use this API to create a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management). You can add a **maximum** of 100 groups in one account per day, and a maximum of 5000 groups in one account.  If you enabled a new group via the user interface, you can also choose whether to display the group and set its privacy level.  **Prerequisites**:  * A Pro or higher account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsBody() # GroupsBody |  (optional)

try:
    # Create a group
    api_instance.group_create(body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsBody**](GroupsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete**
> group_delete(group_id)

Delete a group

Delete an entire [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-). **Prerequisites:** * A Pro, Business, or Education account.  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.

try:
    # Delete a group
    api_instance.group_delete(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_locked_settings**
> group_locked_settings(group_id, body=body, option=option)

Update locked settings

Update a [group's](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) locked settings. If you lock a setting, the group members cannot modify it individually.    **Note:** The `force_pmi_jbh_password` field under meeting settings is deprecated as of September 22, 2019. This field will be replaced by another field that will provide the same functionality.&lt;/p&gt;  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group's ID.
body = swagger_client.GroupIdLockSettingsBody() # GroupIdLockSettingsBody |  (optional)
option = 'option_example' # str | Optional query parameters. * `meeting_security` - View the meeting security settings applied to the user's account. (optional)

try:
    # Update locked settings
    api_instance.group_locked_settings(group_id, body=body, option=option)
except ApiException as e:
    print("Exception when calling GroupsApi->group_locked_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group&#x27;s ID. | 
 **body** | [**GroupIdLockSettingsBody**](GroupIdLockSettingsBody.md)|  | [optional] 
 **option** | **str**| Optional query parameters. * &#x60;meeting_security&#x60; - View the meeting security settings applied to the user&#x27;s account. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members**
> InlineResponse20040 group_members(group_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List group members 

List the members of a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List group members 
    api_response = api_instance.group_members(group_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members_create**
> group_members_create(group_id, body=body)

Add group members

Use this API to add users to a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) in your account.  **Prerequisites:**  * A Pro, Business, or Education account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
body = swagger_client.GroupIdMembersBody1() # GroupIdMembersBody1 |  (optional)

try:
    # Add group members
    api_instance.group_members_create(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **body** | [**GroupIdMembersBody1**](GroupIdMembersBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members_delete**
> group_members_delete(group_id, member_id)

Delete a group member

Use this API to remove a user from a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) in an account.  **Prerequisites:**  * A Pro, Business, or Education account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
member_id = 'member_id_example' # str | The member ID or email address.

try:
    # Delete a group member
    api_instance.group_members_delete(group_id, member_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **member_id** | **str**| The member ID or email address. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_registration**
> InlineResponse2003 group_settings_registration(group_id, type=type)

Get a group's webinar registration settings

Get webinar registration settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
type = 'type_example' # str | The registration type:  * `webinar` &mdash; webinar. (optional)

try:
    # Get a group's webinar registration settings
    api_response = api_instance.group_settings_registration(group_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_settings_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **type** | **str**| The registration type:  * &#x60;webinar&#x60; &amp;mdash; webinar. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_settings_registration_update**
> group_settings_registration_update(group_id, body=body, type=type)

Update a group's webinar registration settings

Update webinar registration settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).&lt;p style=&quot;background-color:#FEEFB3; color:#9F6000&quot;&gt;    Note:&lt;/b&gt; The `force_pmi_jbh_password` field under meeting settings is planned to be deprecated on September 22, 2019. This field will be replaced by another field that will provide the same functionality.&lt;/p&gt; **Prerequisite**: Pro, Business, or Education account        **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
body = swagger_client.SettingsRegistrationBody1() # SettingsRegistrationBody1 |  (optional)
type = 'type_example' # str | The registration type:  * `webinar` &mdash; webinar. (optional)

try:
    # Update a group's webinar registration settings
    api_instance.group_settings_registration_update(group_id, body=body, type=type)
except ApiException as e:
    print("Exception when calling GroupsApi->group_settings_registration_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**SettingsRegistrationBody1**](SettingsRegistrationBody1.md)|  | [optional] 
 **type** | **str**| The registration type:  * &#x60;webinar&#x60; &amp;mdash; webinar. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update**
> group_update(group_id, body=body)

Update a group

Update a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro, Business, or Education account       **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
body = swagger_client.GroupsGroupIdBody1() # GroupsGroupIdBody1 |  (optional)

try:
    # Update a group
    api_instance.group_update(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **body** | [**GroupsGroupIdBody1**](GroupsGroupIdBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups**
> InlineResponse20036 groups()

List groups

List [groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))

try:
    # List groups
    api_response = api_instance.groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_group_member**
> update_a_group_member(group_id, member_id, body=body)

Update a group member

Use this API to perform either of the following tasks:  * Remove a group member from one group and move them to a different group.  * Set a user's primary group. By default, the primary group is the first group that user is added to.  If a user is a member of multiple groups, you can [assign the user a primary group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-#h_d07c7dcd-4fd8-485a-b5fe-a322e8d21c09). The user will use the primary group's settings by default. However, if the user is a member of a group with locked settings, those group settings will remain locked to the user.  **Prerequisites:**  * A Pro or higher account  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group's unique ID. To get this value, use the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. * To set a user's primary group, use the `target_group_id` value for this parameter's value.  * To move a group member from one group to another, use the `groupId` of the designated group.
member_id = 'member_id_example' # str | The group member's unique ID. To get this value, use the [**List group members**](/docs/api-reference/zoom-api/methods#operation/groupMembers) API.
body = swagger_client.MembersMemberIdBody() # MembersMemberIdBody |  (optional)

try:
    # Update a group member
    api_instance.update_a_group_member(group_id, member_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->update_a_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group&#x27;s unique ID. To get this value, use the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. * To set a user&#x27;s primary group, use the &#x60;target_group_id&#x60; value for this parameter&#x27;s value.  * To move a group member from one group to another, use the &#x60;groupId&#x60; of the designated group. | 
 **member_id** | **str**| The group member&#x27;s unique ID. To get this value, use the [**List group members**](/docs/api-reference/zoom-api/methods#operation/groupMembers) API. | 
 **body** | [**MembersMemberIdBody**](MembersMemberIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_settings**
> object update_group_settings(group_id, body=body, option=option)

Update a group's settings

Update settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).   **Note:**The `force_pmi_jbh_password` field under meeting settings is planned to be deprecated on September 22, 2019. This field will be replaced by another field that will provide the same functionality **Prerequisite**: Pro, Business, or Education account        **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group's ID.
body = swagger_client.GroupIdSettingsBody() # GroupIdSettingsBody |  (optional)
option = 'option_example' # str | Optional query parameters.  * `meeting_authentication` - [Meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars).  * `recording_authentication` - [Recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings).  * `meeting_security` - Meeting security settings. (optional)

try:
    # Update a group's settings
    api_response = api_instance.update_group_settings(group_id, body=body, option=option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group&#x27;s ID. | 
 **body** | [**GroupIdSettingsBody**](GroupIdSettingsBody.md)|  | [optional] 
 **option** | **str**| Optional query parameters.  * &#x60;meeting_authentication&#x60; - [Meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars).  * &#x60;recording_authentication&#x60; - [Recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings).  * &#x60;meeting_security&#x60; - Meeting security settings. | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_group_vb**
> InlineResponse2017 upload_group_vb(group_id, file=file)

Upload Virtual Background files

Use this API to [upload Virtual Background files](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_01EJF3YFEWGT8YA0ZJ079JEDQE) for all users in a group to use.    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID. To get a group's ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API.
file = 'file_example' # str |  (optional)

try:
    # Upload Virtual Background files
    api_response = api_instance.upload_group_vb(group_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->upload_group_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID. To get a group&#x27;s ID, use the [**List groups**](/api-reference/zoom-api/methods#operation/groups) API. | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

