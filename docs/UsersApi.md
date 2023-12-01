# zoom.UsersApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_feature**](UsersApi.md#bulk_update_feature) | **POST** /users/features | Bulk update feature
[**del_user_vb**](UsersApi.md#del_user_vb) | **DELETE** /users/{userId}/settings/virtual_backgrounds | Delete Virtual Background files
[**get_collaboration_device**](UsersApi.md#get_collaboration_device) | **GET** /users/{userId}/collaboration_devices/{collaborationDeviceId} | Get collaboration device detail
[**get_user_meeting_templates**](UsersApi.md#get_user_meeting_templates) | **GET** /users/{userId}/meeting_templates/{meetingTemplateId} | Get meeting template detail
[**list_collaboration_devices**](UsersApi.md#list_collaboration_devices) | **GET** /users/{userId}/collaboration_devices | List a user&#x27;s collaboration devices
[**update_presence_status**](UsersApi.md#update_presence_status) | **PUT** /users/{userId}/presence_status | Update a user&#x27;s presence status
[**upload_v_buser**](UsersApi.md#upload_v_buser) | **POST** /users/{userId}/settings/virtual_backgrounds | Upload Virtual Background files
[**user**](UsersApi.md#user) | **GET** /users/{userId} | Get a user
[**user_assistant_create**](UsersApi.md#user_assistant_create) | **POST** /users/{userId}/assistants | Add assistants
[**user_assistant_delete**](UsersApi.md#user_assistant_delete) | **DELETE** /users/{userId}/assistants/{assistantId} | Delete a user assistant
[**user_assistants**](UsersApi.md#user_assistants) | **GET** /users/{userId}/assistants | List user assistants
[**user_assistants_delete**](UsersApi.md#user_assistants_delete) | **DELETE** /users/{userId}/assistants | Delete user assistants
[**user_create**](UsersApi.md#user_create) | **POST** /users | Create users
[**user_delete**](UsersApi.md#user_delete) | **DELETE** /users/{userId} | Delete a user
[**user_email**](UsersApi.md#user_email) | **GET** /users/email | Check a user email
[**user_email_update**](UsersApi.md#user_email_update) | **PUT** /users/{userId}/email | Update a user&#x27;s email
[**user_password**](UsersApi.md#user_password) | **PUT** /users/{userId}/password | Update a user&#x27;s password
[**user_permission**](UsersApi.md#user_permission) | **GET** /users/{userId}/permissions | Get user permissions
[**user_picture**](UsersApi.md#user_picture) | **POST** /users/{userId}/picture | Upload a user&#x27;s profile picture
[**user_picture_delete**](UsersApi.md#user_picture_delete) | **DELETE** /users/{userId}/picture | Delete a user&#x27;s profile picture
[**user_scheduler_delete**](UsersApi.md#user_scheduler_delete) | **DELETE** /users/{userId}/schedulers/{schedulerId} | Delete a scheduler
[**user_schedulers**](UsersApi.md#user_schedulers) | **GET** /users/{userId}/schedulers | List user schedulers
[**user_schedulers_delete**](UsersApi.md#user_schedulers_delete) | **DELETE** /users/{userId}/schedulers | Delete user schedulers
[**user_settings**](UsersApi.md#user_settings) | **GET** /users/{userId}/settings | Get user settings
[**user_settings_update**](UsersApi.md#user_settings_update) | **PATCH** /users/{userId}/settings | Update user settings
[**user_sso_token_delete**](UsersApi.md#user_sso_token_delete) | **DELETE** /users/{userId}/token | Revoke a user&#x27;s SSO token
[**user_status**](UsersApi.md#user_status) | **PUT** /users/{userId}/status | Update user status
[**user_summary**](UsersApi.md#user_summary) | **GET** /users/summary | Get user summary
[**user_token**](UsersApi.md#user_token) | **GET** /users/{userId}/token | Get a user&#x27;s token
[**user_update**](UsersApi.md#user_update) | **PATCH** /users/{userId} | Update a user
[**user_vanity_name**](UsersApi.md#user_vanity_name) | **GET** /users/vanity_name | Check a user&#x27;s PM room
[**user_zak**](UsersApi.md#user_zak) | **GET** /users/me/zak | Get the user&#x27;s ZAK
[**users**](UsersApi.md#users) | **GET** /users | List users

# **bulk_update_feature**
> InlineResponse20118 bulk_update_feature(body=body)

Bulk update feature

Bulk update features.     **Scopes:** `user:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
body = zoom.UsersFeaturesBody() # UsersFeaturesBody | User feature (optional)

try:
    # Bulk update feature
    api_response = api_instance.bulk_update_feature(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->bulk_update_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersFeaturesBody**](UsersFeaturesBody.md)| User feature | [optional] 

### Return type

[**InlineResponse20118**](InlineResponse20118.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_user_vb**
> del_user_vb(user_id, file_ids=file_ids)

Delete Virtual Background files

Use this API to delete a user's Virtual Background files. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's ID. To get a user's ID, use the [**List users**](/docs/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the `me` value instead of the user ID value.
file_ids = 'file_ids_example' # str | A comma-separated list of the Virtual Background file IDs to delete. (optional)

try:
    # Delete Virtual Background files
    api_instance.del_user_vb(user_id, file_ids=file_ids)
except ApiException as e:
    print("Exception when calling UsersApi->del_user_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s ID. To get a user&#x27;s ID, use the [**List users**](/docs/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the &#x60;me&#x60; value instead of the user ID value. | 
 **file_ids** | **str**| A comma-separated list of the Virtual Background file IDs to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collaboration_device**
> InlineResponse20090 get_collaboration_device(user_id, collaboration_device_id)

Get collaboration device detail

Get collaboration device detail. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = zoom.UserId8() # UserId8 | The user ID or email address of the user. For user-level apps, pass the `me` value.
collaboration_device_id = 'collaboration_device_id_example' # str | The collaboration deviceId.

try:
    # Get collaboration device detail
    api_response = api_instance.get_collaboration_device(user_id, collaboration_device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_collaboration_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId8**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **collaboration_device_id** | **str**| The collaboration deviceId. | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_meeting_templates**
> InlineResponse20091 get_user_meeting_templates(user_id, meeting_template_id)

Get meeting template detail

Retrieve a user's [meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates). For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
meeting_template_id = 'meeting_template_id_example' # str | The meeting template ID.

try:
    # Get meeting template detail
    api_response = api_instance.get_user_meeting_templates(user_id, meeting_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_meeting_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **meeting_template_id** | **str**| The meeting template ID. | 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collaboration_devices**
> InlineResponse20089 list_collaboration_devices(user_id)

List a user's collaboration devices

List a user's collaboration devices. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = zoom.UserId7() # UserId7 | The user ID or email address of the user. For user-level apps, pass the `me` value.

try:
    # List a user's collaboration devices
    api_response = api_instance.list_collaboration_devices(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_collaboration_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId7**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_presence_status**
> update_presence_status(user_id, body=body)

Update a user's presence status

Update a user's presence status. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  A user's status **cannot** be updated more than once per minute. For example, you can only submit a maximum of one update request per minute for a single user.  Users in the Zoom desktop client and mobile apps are assigned with a [presence status](https://support.zoom.us/hc/en-us/articles/360032554051-Status-Icons). The presence status informs users of their contact's availability. Users can also change their own presence status to one the following: * **Away** * **Do not disturb** * **Available** * **In a calendar event** * **Presenting** * **In a Zoom meeting** * **On a call** * **Out of Office** * **Busy**  Note that a user's presence status **cannot** be updated via this API if the user is not logged in to the Zoom client.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = zoom.UserIdPresenceStatusBody() # UserIdPresenceStatusBody |  (optional)

try:
    # Update a user's presence status
    api_instance.update_presence_status(user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->update_presence_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserIdPresenceStatusBody**](UserIdPresenceStatusBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_v_buser**
> InlineResponse20120 upload_v_buser(user_id, file=file)

Upload Virtual Background files

Use this API to [upload a Virtual Background files](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background) to a user's profile. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.    **Note:**  * A user profile cannot exceed more than 10 Virtual Background files.  * You can only upload image files that are in JPG/JPEG, GIF or PNG format.  * Video files must be in MP4 or MOV file format with a minimum resolution of 480 by 360 pixels (360p) and a maximum resolution of 1920 by 1080 pixels (1080p).  * The Virtual Background file size cannot exceed 15 megabytes (MB).    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's ID. To get a user's ID, use the [**List users**](/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the `me` value instead of the user ID value.
file = 'file_example' # str |  (optional)

try:
    # Upload Virtual Background files
    api_response = api_instance.upload_v_buser(user_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->upload_v_buser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s ID. To get a user&#x27;s ID, use the [**List users**](/api-reference/zoom-api/ma#operation/users) API. For user-level apps, pass the &#x60;me&#x60; value instead of the user ID value. | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse20120**](InlineResponse20120.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> InlineResponse20088 user(user_id, login_type=login_type, encrypted_email=encrypted_email, search_by_unique_id=search_by_unique_id)

Get a user

View a user's information on a Zoom account. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.   **Note** Users who have not activated their account will have a `pending` status. These users' `created_at` timestamp will also display the time at which the API call was made, **not** the account's creation date.   **Note:** The `user_info:read` scope is only available when you pass the `me` value for the `$userId` value.   **Scopes:** `user:read:admin`,`user:read`,`user_info:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
login_type = 56 # int | The user's login method.  * `0` - Facebook OAuth  * `1` - Google OAuth.  * `24` - Apple OAuth.  * `27` - Microsoft OAuth.  * `97` - Mobile device.  * `98` - RingCentral OAuth.  * `99` - API user.  * `100` - Zoom Work email.  * `101` - Single Sign-On (SSO).   These login methods are only available in China.  * `11` - Phone number.  * `21` - WeChat.  * `23` - Alipay. (optional)
encrypted_email = false # bool | Whether the email address passed for the `userId` value is an encrypted email address.    * `true` - The email address is encrypted.   * `false` - The email address is not encrypted.    If you do not query this parameter, this value defaults to null (`false`). (optional) (default to false)
search_by_unique_id = true # bool | Whether the queried `userId` value is an employee unique ID.  * `true` - The queried ID is an employee's unique ID.  * `false` - The queried ID is not an employee's unique ID.   This value defaults to `false` (null). (optional)

try:
    # Get a user
    api_response = api_instance.user(user_id, login_type=login_type, encrypted_email=encrypted_email, search_by_unique_id=search_by_unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **login_type** | **int**| The user&#x27;s login method.  * &#x60;0&#x60; - Facebook OAuth  * &#x60;1&#x60; - Google OAuth.  * &#x60;24&#x60; - Apple OAuth.  * &#x60;27&#x60; - Microsoft OAuth.  * &#x60;97&#x60; - Mobile device.  * &#x60;98&#x60; - RingCentral OAuth.  * &#x60;99&#x60; - API user.  * &#x60;100&#x60; - Zoom Work email.  * &#x60;101&#x60; - Single Sign-On (SSO).   These login methods are only available in China.  * &#x60;11&#x60; - Phone number.  * &#x60;21&#x60; - WeChat.  * &#x60;23&#x60; - Alipay. | [optional] 
 **encrypted_email** | **bool**| Whether the email address passed for the &#x60;userId&#x60; value is an encrypted email address.    * &#x60;true&#x60; - The email address is encrypted.   * &#x60;false&#x60; - The email address is not encrypted.    If you do not query this parameter, this value defaults to null (&#x60;false&#x60;). | [optional] [default to false]
 **search_by_unique_id** | **bool**| Whether the queried &#x60;userId&#x60; value is an employee unique ID.  * &#x60;true&#x60; - The queried ID is an employee&#x27;s unique ID.  * &#x60;false&#x60; - The queried ID is not an employee&#x27;s unique ID.   This value defaults to &#x60;false&#x60; (null). | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistant_create**
> InlineResponse20119 user_assistant_create(user_id, body=body)

Add assistants

Assign assistants to a user. In the request body, provide either the user's ID or the user's email address. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Assistants are the users to whom the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). Assistants can schedule meetings on behalf of the current user, and can also manage and act as an alternative host for all meetings if the admin has enabled the [co-host option](https://zoom.us/account/setting) on the account.  **Prerequisites:**  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account, or the assistants' account must be in the same organization as the current user's account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserAssistantsList() # UserAssistantsList | User assistant. (optional)

try:
    # Add assistants
    api_response = api_instance.user_assistant_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserAssistantsList**](UserAssistantsList.md)| User assistant. | [optional] 

### Return type

[**InlineResponse20119**](InlineResponse20119.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistant_delete**
> user_assistant_delete(user_id, assistant_id)

Delete a user assistant

Delete a specific assistant of a user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Assistants are the users who the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user as well as manage and act as an alternative host for all meetings if the admin has enabled [co-host option](https://zoom.us/account/setting) on the account.  **Prerequisites:**  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
assistant_id = 'assistant_id_example' # str | Assistant ID.

try:
    # Delete a user assistant
    api_instance.user_assistant_delete(user_id, assistant_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistant_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **assistant_id** | **str**| Assistant ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistants**
> UserAssistantsList_ user_assistants(user_id)

List user assistants

List a user's assistants. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Assistants are users who the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meetings on behalf of the current user, as well as manage and act as an alternative host for all meetings if the admin has enabled the [co-host option](https://zoom.us/account/setting) on the account.  **Prerequisites:**  * Current user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.  **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # List user assistants
    api_response = api_instance.user_assistants(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**UserAssistantsList_**](UserAssistantsList_.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistants_delete**
> user_assistants_delete(user_id)

Delete user assistants

Delete all of the current user's assistants. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Assistants are the users who the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user, and manage and act as an alternative host for all meetings if the admin has enabled [co-host option](https://zoom.us/account/setting) on the account.  **Prerequisites:**  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # Delete user assistants
    api_instance.user_assistants_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistants_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> InlineResponse20117 user_create(body=body)

Create users

Add a new user to your Zoom account.   **Note** These rate limits apply when you use the `create` value for the `action` field:  * 50 requests per day for **Free** accounts.  * 1,500 requests per day for **Pro** accounts.  * 10,000 requests per day for **Business+** accounts.   **Prerequisites:**  * A Pro or higher plan.  **Scopes:** `user:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
body = zoom.UsersBody() # UsersBody | User (optional)

try:
    # Create users
    api_response = api_instance.user_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBody**](UsersBody.md)| User | [optional] 

### Return type

[**InlineResponse20117**](InlineResponse20117.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(user_id, encrypted_email=encrypted_email, action=action, transfer_email=transfer_email, transfer_meeting=transfer_meeting, transfer_webinar=transfer_webinar, transfer_recording=transfer_recording, transfer_whiteboard=transfer_whiteboard)

Delete a user

**Disassociate** (unlink) a user or permanently **delete** a user.    **Disassociating** a user unlinks the user from the associated Zoom account and provides the user their own basic free Zoom account. The disassociated user can then purchase their own Zoom licenses. An account owner or account admin can transfer the user's meetings, webinars, and cloud recordings to another user before disassociation.   **Deleting** a user permanently removes the user and their data from Zoom. Users can create a new Zoom account using the same email address. An account owner or an account admin can transfer meetings, webinars, and cloud recordings to another Zoom user account before deleting.   For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  **Note:** This API does not support the deletion requirements of a [Data Subject Access Request (DSAR)](https://dataprivacymanager.net/what-is-data-subject-access-request-dsar/). For a DSAR request, contact Zoom Support.      **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
encrypted_email = false # bool | Whether the email address passed for the `userId` value is an encrypted email address.    * `true` - The email address is encrypted.   * `false` - The email address is not encrypted.    If you do not query this parameter, this value defaults to null (`false`). (optional) (default to false)
action = 'disassociate' # str | Delete action options.   `disassociate` - Disassociate a user.    `delete`-  Permanently delete a user.    Note: To delete pending user in the account, use `disassociate` (optional) (default to disassociate)
transfer_email = 'transfer_email_example' # str | Transfer email. This field is **required** if the user has Zoom Events/Sessions feature. After you delete or disassociate the user, the user's hub assets on Zoom Events site will be transferred to the target user. (optional)
transfer_meeting = true # bool | Transfer meeting. (optional)
transfer_webinar = true # bool | Transfer webinar. (optional)
transfer_recording = true # bool | Transfer recording. (optional)
transfer_whiteboard = true # bool | When deleting a user, whether to transfer all their [Zoom Whiteboard](https://support.zoom.us/hc/en-us/articles/4410916881421) data to another user. (optional)

try:
    # Delete a user
    api_instance.user_delete(user_id, encrypted_email=encrypted_email, action=action, transfer_email=transfer_email, transfer_meeting=transfer_meeting, transfer_webinar=transfer_webinar, transfer_recording=transfer_recording, transfer_whiteboard=transfer_whiteboard)
except ApiException as e:
    print("Exception when calling UsersApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **encrypted_email** | **bool**| Whether the email address passed for the &#x60;userId&#x60; value is an encrypted email address.    * &#x60;true&#x60; - The email address is encrypted.   * &#x60;false&#x60; - The email address is not encrypted.    If you do not query this parameter, this value defaults to null (&#x60;false&#x60;). | [optional] [default to false]
 **action** | **str**| Delete action options.   &#x60;disassociate&#x60; - Disassociate a user.    &#x60;delete&#x60;-  Permanently delete a user.    Note: To delete pending user in the account, use &#x60;disassociate&#x60; | [optional] [default to disassociate]
 **transfer_email** | **str**| Transfer email. This field is **required** if the user has Zoom Events/Sessions feature. After you delete or disassociate the user, the user&#x27;s hub assets on Zoom Events site will be transferred to the target user. | [optional] 
 **transfer_meeting** | **bool**| Transfer meeting. | [optional] 
 **transfer_webinar** | **bool**| Transfer webinar. | [optional] 
 **transfer_recording** | **bool**| Transfer recording. | [optional] 
 **transfer_whiteboard** | **bool**| When deleting a user, whether to transfer all their [Zoom Whiteboard](https://support.zoom.us/hc/en-us/articles/4410916881421) data to another user. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_email**
> InlineResponse20084 user_email(email)

Check a user email

Verify if a user's email is registered with Zoom.          &lt;b&gt;Note: &lt;/b&gt;You can successfully check if a user is a registered Zoom user only if the user **signed up for Zoom via email and is within your account.** If you provide an email address of a user who is not in your account, the value of &quot;existed_email&quot; parameter will be &quot;false&quot; irrespective of whether or not the user is registered with Zoom. The response of this API call will not include users who joined Zoom using options such as &quot;Sign in with SSO&quot;, &quot;Sign in with Google&quot; or &quot;Sign in with Facebook&quot; even if they are in the same account as yours.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
email = 'email_example' # str | The email address to be verified.

try:
    # Check a user email
    api_response = api_instance.user_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to be verified. | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_email_update**
> user_email_update(user_id, body=body)

Update a user's email

Change a user's [email address](https://support.zoom.us/hc/en-us/articles/201362563-How-Do-I-Change-the-Email-on-My-Account-) on a Zoom account that has managed domain set up. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  * If the Zoom account in which the user belongs has multiple [managed domains](https://support.zoom.us/hc/en-us/articles/203395207-What-is-Managed-Domain-), then the email to be updated **must** match one of the managed domains. * A user's email address can be changed up to 3 times in any 24 hour period.  **Prerequisites:**  * Managed domain must be enabled in the account.  * The new email address should not already exist in Zoom.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The users's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserIdEmailBody() # UserIdEmailBody | User email. (optional)

try:
    # Update a user's email
    api_instance.user_email_update(user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->user_email_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The users&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdEmailBody**](UserIdEmailBody.md)| User email. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_password**
> user_password(user_id, body=body)

Update a user's password

Update the [password](https://support.zoom.us/hc/en-us/articles/206344385-Change-a-User-s-Password) of a user using which the user can login to Zoom. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  After this request is processed successfully, an email notification is sent to the user saying that the password was changed.     **Prerequisites:**     * Owner or admin of the Zoom account.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserIdPasswordBody() # UserIdPasswordBody | User password. (optional)

try:
    # Update a user's password
    api_instance.user_password(user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdPasswordBody**](UserIdPasswordBody.md)| User password. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_permission**
> InlineResponse20092 user_permission(user_id)

Get user permissions

Get permissions that have been granted to the user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Users can be assigned a set of permissions that allows them to access only the pages or information that a user needs to view or edit.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # Get user permissions
    api_response = api_instance.user_permission(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_picture**
> object user_picture(user_id, pic_file=pic_file)

Upload a user's profile picture

Upload a user's profile picture. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Provide `multipart/form-data` as the value of the `content-type` header for this request. This API supports `.jpeg` and `.png` file formats.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
pic_file = 'pic_file_example' # str |  (optional)

try:
    # Upload a user's profile picture
    api_response = api_instance.user_picture(user_id, pic_file=pic_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **pic_file** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_picture_delete**
> user_picture_delete(user_id)

Delete a user's profile picture

Delete a user's profile picture. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.     **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # Delete a user's profile picture
    api_instance.user_picture_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_picture_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_scheduler_delete**
> user_scheduler_delete(user_id, scheduler_id)

Delete a scheduler

Delete a scheduler. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Schedulers are users who the current user (assistant) can schedule meetings on their behalf. By calling this API, the current user will no longer be a scheduling assistant of this scheduler.  **Prerequisites:**  * Current user must be under the same account as the scheduler.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
scheduler_id = 'scheduler_id_example' # str | Scheduler's ID.

try:
    # Delete a scheduler
    api_instance.user_scheduler_delete(user_id, scheduler_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_scheduler_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **scheduler_id** | **str**| Scheduler&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_schedulers**
> UserSchedulersList user_schedulers(user_id)

List user schedulers

List all of a user's schedulers. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Schedulers in this context are users who can schedule meetings for the current user. For example, if the current user, the user whose `userId` was passed in the `path` parameter, is **User A**, this API's response will list all users for whom **User A** can schedule and manage meetings. **User A** is the assistant of these users, and thus has scheduling privilege for these users.  **Prerequisites**  * Current user must be under the same account as the scheduler.  **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # List user schedulers
    api_response = api_instance.user_schedulers(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**UserSchedulersList**](UserSchedulersList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_schedulers_delete**
> user_schedulers_delete(user_id)

Delete user schedulers

Delete all of a user's schedulers. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  Schedulers are users on whose behalf the current user (assistant) can schedule meetings for. By calling this API, the current user will no longer be a scheduling assistant of any user.   **Prerequisites:**  * Current user (assistant) must be under the same account as the scheduler.  **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # Delete user schedulers
    api_instance.user_schedulers_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_schedulers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings**
> InlineResponse20093 user_settings(user_id, login_type=login_type, option=option, custom_query_fields=custom_query_fields)

Get user settings

Retrieve a user's settings. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass the `me` value.
login_type = 56 # int | The user's login method.  * `0` - Facebook OAuth  * `1` - Google OAuth  * `24` - Apple OAuth  * `27` - Microsoft OAuth  * `97` - Mobile device  * `98` - RingCentral OAuth  * `99` - API user  * `100` - Zoom Work email  * `101` - Single Sign-On (SSO)   These login methods are only available in China:  * `11` - Phone number  * `21` - WeChat  * `23` - Alipay (optional)
option = 'option_example' # str | Optional query parameters:  * `meeting_authentication` - Use this query parameter to view the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user's account.  * `recording_authentication` - Use this query parameter to view the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user's account.  * `meeting_security` - Use this query parameter to view the meeting security settings applied to the user's account. (optional)
custom_query_fields = 'custom_query_fields_example' # str | Provide the name of the field to filter the response. For example, if you provide `host_video` as the value of this field, you will get a response similar to this.     {    schedule_meeting: {         host_video: false     } }     You can provide multiple values by separating them with commas(example: `host_video,participant_video`). (optional)

try:
    # Get user settings
    api_response = api_instance.user_settings(user_id, login_type=login_type, option=option, custom_query_fields=custom_query_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **login_type** | **int**| The user&#x27;s login method.  * &#x60;0&#x60; - Facebook OAuth  * &#x60;1&#x60; - Google OAuth  * &#x60;24&#x60; - Apple OAuth  * &#x60;27&#x60; - Microsoft OAuth  * &#x60;97&#x60; - Mobile device  * &#x60;98&#x60; - RingCentral OAuth  * &#x60;99&#x60; - API user  * &#x60;100&#x60; - Zoom Work email  * &#x60;101&#x60; - Single Sign-On (SSO)   These login methods are only available in China:  * &#x60;11&#x60; - Phone number  * &#x60;21&#x60; - WeChat  * &#x60;23&#x60; - Alipay | [optional] 
 **option** | **str**| Optional query parameters:  * &#x60;meeting_authentication&#x60; - Use this query parameter to view the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user&#x27;s account.  * &#x60;recording_authentication&#x60; - Use this query parameter to view the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user&#x27;s account.  * &#x60;meeting_security&#x60; - Use this query parameter to view the meeting security settings applied to the user&#x27;s account. | [optional] 
 **custom_query_fields** | **str**| Provide the name of the field to filter the response. For example, if you provide &#x60;host_video&#x60; as the value of this field, you will get a response similar to this.     {    schedule_meeting: {         host_video: false     } }     You can provide multiple values by separating them with commas(example: &#x60;host_video,participant_video&#x60;). | [optional] 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_update**
> user_settings_update(user_id, body=body, option=option)

Update user settings

Update a user's settings. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserIdSettingsBody() # UserIdSettingsBody | User Settings (optional)
option = 'option_example' # str | Optional query parameters:  * `meeting_authentication` &mdash; Use this query parameter to view the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user's account.  * `recording_authentication` &mdash; Use this query parameter to view the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user's account.  * `meeting_security` &mdash; Use this query parameter to view the meeting security settings applied to the user's account. (optional)

try:
    # Update user settings
    api_instance.user_settings_update(user_id, body=body, option=option)
except ApiException as e:
    print("Exception when calling UsersApi->user_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdSettingsBody**](UserIdSettingsBody.md)| User Settings | [optional] 
 **option** | **str**| Optional query parameters:  * &#x60;meeting_authentication&#x60; &amp;mdash; Use this query parameter to view the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user&#x27;s account.  * &#x60;recording_authentication&#x60; &amp;mdash; Use this query parameter to view the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user&#x27;s account.  * &#x60;meeting_security&#x60; &amp;mdash; Use this query parameter to view the meeting security settings applied to the user&#x27;s account. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_sso_token_delete**
> user_sso_token_delete(user_id)

Revoke a user's SSO token

Revoke a user's SSO token. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  After calling this API, the SSO user will be logged out of their current Zoom session.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # Revoke a user's SSO token
    api_instance.user_sso_token_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_sso_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_status**
> object user_status(user_id, body=body)

Update user status

[Deactivate](https://support.zoom.us/hc/en-us/articles/115005269946-Remove-User-from-your-Account#h_6a9bc1c3-d739-4945-b1f2-00b3b88fb5cc) an active user or to [reactivate](https://support.zoom.us/hc/en-us/articles/115005269946-Remove-User-from-your-Account#h_16319724-d120-4be6-af5d-31582d134ea0) a deactivated user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  An account owner or admins can deactivate as well as activate a user in a Zoom account. Deactivating a user removes all licenses associated with a user, and prevents the deactivated user from logging into their Zoom account. A deactivated user can be reactivated. Reactivating a user grants the user access to log in to their Zoom account.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UserIdStatusBody() # UserIdStatusBody | User status. (optional)

try:
    # Update user status
    api_response = api_instance.user_status(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UserIdStatusBody**](UserIdStatusBody.md)| User status. | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_summary**
> InlineResponse20086 user_summary()

Get user summary

Use this API to get a summary of users, including the number and types of users in the account.     **Scopes:** `user:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))

try:
    # Get user summary
    api_response = api_instance.user_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token**
> InlineResponse20094 user_token(user_id, type=type, ttl=ttl)

Get a user's token

Get a user's Zoom token or Zoom Access Key (ZAK). For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.      **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
type = 'token' # str | The user token type.  * `zak` - A Zoom Access Key (ZAK) is used to generate a URL to start meetings. See [Getting a Zoom Access Key (ZAK)](https://developers.zoom.us/docs/meeting-sdk/auth/#start-meetings-and-webinars-with-a-zoom-users-zak-token) for details. The ZAK's expiration time is two hours. For API users, the expiration time is 90 days. An API user is a user created via the `custCreate` action in the **[Create users](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/userCreate)** API. The maximum length of this value is `512`.  * `token` - **Deprecated** A Zoom token. This token expires in 14 days. You must make the request again after expiration to receive a new token. This query parameter returns a null value if the user signed in to Zoom via Google or Facebook. The maximum length of this value is `512`.    This value defaults to `token`. (optional) (default to token)
ttl = 7200 # int | The ZAK expiration time to live (TTL), in seconds. To update the user's ZAK TTL, use this field with the `zak` value for the `type` query parameter.   Defaults to `7200` or `7776000` (90 days) for API users. The maximum value is one year. (optional) (default to 7200)

try:
    # Get a user's token
    api_response = api_instance.user_token(user_id, type=type, ttl=ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **type** | **str**| The user token type.  * &#x60;zak&#x60; - A Zoom Access Key (ZAK) is used to generate a URL to start meetings. See [Getting a Zoom Access Key (ZAK)](https://developers.zoom.us/docs/meeting-sdk/auth/#start-meetings-and-webinars-with-a-zoom-users-zak-token) for details. The ZAK&#x27;s expiration time is two hours. For API users, the expiration time is 90 days. An API user is a user created via the &#x60;custCreate&#x60; action in the **[Create users](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/userCreate)** API. The maximum length of this value is &#x60;512&#x60;.  * &#x60;token&#x60; - **Deprecated** A Zoom token. This token expires in 14 days. You must make the request again after expiration to receive a new token. This query parameter returns a null value if the user signed in to Zoom via Google or Facebook. The maximum length of this value is &#x60;512&#x60;.    This value defaults to &#x60;token&#x60;. | [optional] [default to token]
 **ttl** | **int**| The ZAK expiration time to live (TTL), in seconds. To update the user&#x27;s ZAK TTL, use this field with the &#x60;zak&#x60; value for the &#x60;type&#x60; query parameter.   Defaults to &#x60;7200&#x60; or &#x60;7776000&#x60; (90 days) for API users. The maximum value is one year. | [optional] [default to 7200]

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> user_update(user_id, body=body, login_type=login_type, remove_tsp_credentials=remove_tsp_credentials)

Update a user

Update a user's [Zoom profile](https://support.zoom.us/hc/en-us/articles/201363203-My-Profile) information. For user-level apps, pass [the `me` value](hhttps://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    **Scopes:** `user:write:admin`,`user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.
body = zoom.UpdateAUser() # UpdateAUser | The user's profile information. (optional)
login_type = 56 # int | The user's login method.  * `0` - Facebook OAuth.  * `1` - Google OAuth.  * `24` - Apple OAuth.  * `27` - Microsoft OAuth.  * `97` - Mobile device.  * `98` - RingCentral OAuth.  * `99` - API user.  * `100` - Zoom Work email.  * `101` - Single Sign-On (SSO).   These login methods are only available in China.  * `11` - Phone number.  * `21` - WeChat.  * `23` - Alipay. (optional)
remove_tsp_credentials = true # bool | Whether to remove the user's TSP credentials.  * `true` - The queried ID is an employee's unique ID.  * `false` - The queried ID is not an employee's unique ID.    This value defaults to `false` (null). (optional)

try:
    # Update a user
    api_instance.user_update(user_id, body=body, login_type=login_type, remove_tsp_credentials=remove_tsp_credentials)
except ApiException as e:
    print("Exception when calling UsersApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**UpdateAUser**](UpdateAUser.md)| The user&#x27;s profile information. | [optional] 
 **login_type** | **int**| The user&#x27;s login method.  * &#x60;0&#x60; - Facebook OAuth.  * &#x60;1&#x60; - Google OAuth.  * &#x60;24&#x60; - Apple OAuth.  * &#x60;27&#x60; - Microsoft OAuth.  * &#x60;97&#x60; - Mobile device.  * &#x60;98&#x60; - RingCentral OAuth.  * &#x60;99&#x60; - API user.  * &#x60;100&#x60; - Zoom Work email.  * &#x60;101&#x60; - Single Sign-On (SSO).   These login methods are only available in China.  * &#x60;11&#x60; - Phone number.  * &#x60;21&#x60; - WeChat.  * &#x60;23&#x60; - Alipay. | [optional] 
 **remove_tsp_credentials** | **bool**| Whether to remove the user&#x27;s TSP credentials.  * &#x60;true&#x60; - The queried ID is an employee&#x27;s unique ID.  * &#x60;false&#x60; - The queried ID is not an employee&#x27;s unique ID.    This value defaults to &#x60;false&#x60; (null). | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_vanity_name**
> InlineResponse20087 user_vanity_name(vanity_name)

Check a user's PM room

A personal meeting room is a virtual meeting room that can be permanently assigned to a user. Use this API to check if a personal meeting room with the given name exists or not.           **Scopes:** `user:read:admin`,`user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
vanity_name = 'vanity_name_example' # str | Personal meeting room name.

try:
    # Check a user's PM room
    api_response = api_instance.user_vanity_name(vanity_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_vanity_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanity_name** | **str**| Personal meeting room name. | 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_zak**
> InlineResponse20085 user_zak()

Get the user's ZAK

Get the Zoom Access Key (ZAK) for the authenticated user associated with the access token in the API request. Use a ZAK to start or join a meeting on behalf of this user.  ZAKs obtained with this endpoint expire five minutes after receipt.  To get a ZAK for a different user or with a different expiration, use the [Get a user token](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods#operation/userToken) API with the `zak` `type` query parameter.  See [Getting a Zoom Access Key (ZAK)](https://developers.zoom.us/docs/meeting-sdk/auth/#start-meetings-and-webinars-with-a-zoom-users-zak-token) for details.    **Scopes:** `user_zak:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))

try:
    # Get the user's ZAK
    api_response = api_instance.user_zak()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_zak: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users**
> InlineResponse20083 users(status=status, page_size=page_size, role_id=role_id, page_number=page_number, include_fields=include_fields, next_page_token=next_page_token, license=license)

List users

Retrieve a list your account's users.     **Scopes:** `user:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.UsersApi(zoom.ApiClient(configuration))
status = 'active' # str | The user's status.  * `active` - The user exists on the account.  * `inactive` - The user has been deactivated.  * `pending` - The user exists on the account, but has not activated their account. See [Managing users](https://support.zoom.us/hc/en-us/articles/201363183) for details.  This value defaults to `active`. (optional) (default to active)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
role_id = 'role_id_example' # str | The role's unique ID. Use this parameter to filter the response by a specific role. You can use the [**List roles**](/api-reference/zoom-api/methods#operation/roles) API to get a role's unique ID value. (optional)
page_number = 'page_number_example' # str | The page number of the current page in the returned records. (optional)
include_fields = 'include_fields_example' # str | Use this parameter to display one of the following attributes in the API call's response:  * `custom_attributes` &mdash; Return the user's custom attributes.  * `host_key` &mdash; Return the user's [host key](https://support.zoom.us/hc/en-us/articles/205172555-Using-your-host-key). (optional)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)
license = 'license_example' # str | The user's license. Filter the response by a specific license. (optional)

try:
    # List users
    api_response = api_instance.users(status=status, page_size=page_size, role_id=role_id, page_number=page_number, include_fields=include_fields, next_page_token=next_page_token, license=license)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The user&#x27;s status.  * &#x60;active&#x60; - The user exists on the account.  * &#x60;inactive&#x60; - The user has been deactivated.  * &#x60;pending&#x60; - The user exists on the account, but has not activated their account. See [Managing users](https://support.zoom.us/hc/en-us/articles/201363183) for details.  This value defaults to &#x60;active&#x60;. | [optional] [default to active]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **role_id** | **str**| The role&#x27;s unique ID. Use this parameter to filter the response by a specific role. You can use the [**List roles**](/api-reference/zoom-api/methods#operation/roles) API to get a role&#x27;s unique ID value. | [optional] 
 **page_number** | **str**| The page number of the current page in the returned records. | [optional] 
 **include_fields** | **str**| Use this parameter to display one of the following attributes in the API call&#x27;s response:  * &#x60;custom_attributes&#x60; &amp;mdash; Return the user&#x27;s custom attributes.  * &#x60;host_key&#x60; &amp;mdash; Return the user&#x27;s [host key](https://support.zoom.us/hc/en-us/articles/205172555-Using-your-host-key). | [optional] 
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
 **license** | **str**| The user&#x27;s license. Filter the response by a specific license. | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

