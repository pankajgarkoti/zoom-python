# zoom.AccountsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_managed_domain**](AccountsApi.md#account_managed_domain) | **GET** /accounts/{accountId}/managed_domains | Get account&#x27;s managed domains
[**account_settings**](AccountsApi.md#account_settings) | **GET** /accounts/{accountId}/settings | Get account settings
[**account_settings_registration**](AccountsApi.md#account_settings_registration) | **GET** /accounts/{accountId}/settings/registration | Get an account&#x27;s webinar registration settings
[**account_settings_registration_update**](AccountsApi.md#account_settings_registration_update) | **PATCH** /accounts/{accountId}/settings/registration | Update an account&#x27;s webinar registration settings
[**account_settings_update**](AccountsApi.md#account_settings_update) | **PATCH** /accounts/{accountId}/settings | Update account settings
[**account_trusted_domain**](AccountsApi.md#account_trusted_domain) | **GET** /accounts/{accountId}/trusted_domains | Get account&#x27;s trusted domains
[**del_vb**](AccountsApi.md#del_vb) | **DELETE** /accounts/{accountId}/settings/virtual_backgrounds | Delete virtual background files
[**get_account_lock_settings**](AccountsApi.md#get_account_lock_settings) | **GET** /accounts/{accountId}/lock_settings | Get locked settings
[**update_locked_settings**](AccountsApi.md#update_locked_settings) | **PATCH** /accounts/{accountId}/lock_settings | Update locked settings
[**update_the_account_owner**](AccountsApi.md#update_the_account_owner) | **PUT** /accounts/{accountId}/owner | Update the account owner
[**upload_vb**](AccountsApi.md#upload_vb) | **POST** /accounts/{accountId}/settings/virtual_backgrounds | Upload virtual background files

# **account_managed_domain**
> InlineResponse2001 account_managed_domain(account_id)

Get account's managed domains

Retrieve a list of an account's [managed domains](https://support.zoom.us/hc/en-us/articles/203395207). To get the master account's managed domains, pass the `me` value for the `accountId` path parameter.    **Prerequisites:**  * A Pro or a higher paid account with the Master account option enabled.  **Scopes:** `account:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | The account's ID. For master accounts, pass the `me` value for this parameter.

try:
    # Get account's managed domains
    api_response = api_instance.account_managed_domain(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_managed_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#x27;s ID. For master accounts, pass the &#x60;me&#x60; value for this parameter. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings**
> InlineResponse2002 account_settings(account_id, option=option, custom_query_fields=custom_query_fields)

Get account settings

Get an account's settings.   To get settings for a master account, use the `me` value for the `accountId` path parameter.    **Prerequisites:**  * The account must be a paid account.  **Scopes:** `account:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
option = 'option_example' # str | Optional query parameters.  * `meeting_authentication` - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user's account.  * `recording_authentication` - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user's account.  * `security` - View the account's security settings. For example, passcode requirements for user login or two-factor authentication.  * `meeting_security` - View the meeting security settings applied to the user's account. (optional)
custom_query_fields = 'custom_query_fields_example' # str | The name of the field to use to filter the response. For example, if you provide the `host_video` value for this field, you will get a response similar to.    `{ schedule_meeting: { host_video: false } }`    To use multiple values, comma-separate each value, like `host_video,participant_video`. (optional)

try:
    # Get account settings
    api_response = api_instance.account_settings(account_id, option=option, custom_query_fields=custom_query_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **option** | **str**| Optional query parameters.  * &#x60;meeting_authentication&#x60; - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user&#x27;s account.  * &#x60;recording_authentication&#x60; - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user&#x27;s account.  * &#x60;security&#x60; - View the account&#x27;s security settings. For example, passcode requirements for user login or two-factor authentication.  * &#x60;meeting_security&#x60; - View the meeting security settings applied to the user&#x27;s account. | [optional] 
 **custom_query_fields** | **str**| The name of the field to use to filter the response. For example, if you provide the &#x60;host_video&#x60; value for this field, you will get a response similar to.    &#x60;{ schedule_meeting: { host_video: false } }&#x60;    To use multiple values, comma-separate each value, like &#x60;host_video,participant_video&#x60;. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings_registration**
> InlineResponse2003 account_settings_registration(account_id, type=type)

Get an account's webinar registration settings

Get an account's webinar registration settings. To get the master account's webinar registration settings, use the `me` value for the `accountId` path parameter.   **Prerequisites:**  * The account must be a paid account.  **Scopes:** `account:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | The account's ID. For master accounts, pass the `me` value for this parameter.
type = 'type_example' # str | The registration's type. * `webinar` &mdash; webinar. (optional)

try:
    # Get an account's webinar registration settings
    api_response = api_instance.account_settings_registration(account_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#x27;s ID. For master accounts, pass the &#x60;me&#x60; value for this parameter. | 
 **type** | **str**| The registration&#x27;s type. * &#x60;webinar&#x60; &amp;mdash; webinar. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings_registration_update**
> account_settings_registration_update(account_id, body=body, type=type)

Update an account's webinar registration settings

Update an account's webinar registration settings. To update the master account's webinar registration settings, pass the `me` value for the `accountId` path parameter.    **Prerequisites:**  * The account must be a paid account.  **Scopes:** `account:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | The account's ID. For master accounts, pass the `me` value for this parameter.
body = zoom.SettingsRegistrationBody() # SettingsRegistrationBody |  (optional)
type = 'type_example' # str | The registration's type. * `webinar` &mdash; webinar. (optional)

try:
    # Update an account's webinar registration settings
    api_instance.account_settings_registration_update(account_id, body=body, type=type)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings_registration_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#x27;s ID. For master accounts, pass the &#x60;me&#x60; value for this parameter. | 
 **body** | [**SettingsRegistrationBody**](SettingsRegistrationBody.md)|  | [optional] 
 **type** | **str**| The registration&#x27;s type. * &#x60;webinar&#x60; &amp;mdash; webinar. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings_update**
> account_settings_update(account_id, body=body, option=option)

Update account settings

Update an account's settings.  To update the settings for a master account, pass the `me` value for the `accountId` path parameter.    **Prerequisites:**  * The account must be a paid account.  **Scopes:** `account:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = zoom.AccountIdSettingsBody() # AccountIdSettingsBody |  (optional)
option = 'option_example' # str | Optional query parameters.  * `meeting_authentication` - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user's account.  * `recording_authentication` - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user's account.  * `security` - View the account's security settings. For example, passcode requirements for user login or two-factor authentication.  * `meeting_security` - View the meeting security settings applied to the user's account. (optional)

try:
    # Update account settings
    api_instance.account_settings_update(account_id, body=body, option=option)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**AccountIdSettingsBody**](AccountIdSettingsBody.md)|  | [optional] 
 **option** | **str**| Optional query parameters.  * &#x60;meeting_authentication&#x60; - View the [meeting authentication settings](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied to the user&#x27;s account.  * &#x60;recording_authentication&#x60; - View the [recording authentication settings](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied to the user&#x27;s account.  * &#x60;security&#x60; - View the account&#x27;s security settings. For example, passcode requirements for user login or two-factor authentication.  * &#x60;meeting_security&#x60; - View the meeting security settings applied to the user&#x27;s account. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_trusted_domain**
> InlineResponse2004 account_trusted_domain(account_id)

Get account's trusted domains

Retrieve an account's [trusted domains](https://support.zoom.us/hc/en-us/articles/203395207). To get the master account's trusted domains, use the `me` value for the `accountId` path parameter.    **Prerequisites:**  * The account must be a paid account.  **Scopes:** `account:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | The account's ID. For master accounts, pass the `me` value for this parameter.

try:
    # Get account's trusted domains
    api_response = api_instance.account_trusted_domain(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_trusted_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account&#x27;s ID. For master accounts, pass the &#x60;me&#x60; value for this parameter. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_vb**
> del_vb(account_id, file_ids=file_ids)

Delete virtual background files

Delete an account's existing virtual background files.    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `account:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
file_ids = 'file_ids_example' # str | A comma-separated list of file IDs to delete. (optional)

try:
    # Delete virtual background files
    api_instance.del_vb(account_id, file_ids=file_ids)
except ApiException as e:
    print("Exception when calling AccountsApi->del_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **file_ids** | **str**| A comma-separated list of file IDs to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_lock_settings**
> InlineResponse200 get_account_lock_settings(account_id, option=option, custom_query_fields=custom_query_fields)

Get locked settings

Retrieve an account's locked settings.    Account admins and account owners can use [Account Locked Settings](https://support.zoom.us/hc/en-us/articles/115005269866) to toggle settings on or off for all users in their account.    **Note:** You can use Account Locked Settings with accounts that have master and sub accounts enabled.          **Prerequisites:** * Pro or a higher paid account.         **Scopes:** `account:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
option = 'option_example' # str | Optional query parameters:  * `meeting_security` &mdash; Use this query parameter to view the meeting security settings applied to the user's account. (optional)
custom_query_fields = 'custom_query_fields_example' # str | Provide the name of the field by which you would like to filter the response. For example, if you provide &quot;host_video&quot; as the value of this field, you will get a response similar to the following:     {     &quot;schedule_meeting&quot;: {         &quot;host_video&quot;: false     } }     You can provide multiple values by separating them with commas(example: &quot;host_video,participant_video&rdquo;). (optional)

try:
    # Get locked settings
    api_response = api_instance.get_account_lock_settings(account_id, option=option, custom_query_fields=custom_query_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_lock_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **option** | **str**| Optional query parameters:  * &#x60;meeting_security&#x60; &amp;mdash; Use this query parameter to view the meeting security settings applied to the user&#x27;s account. | [optional] 
 **custom_query_fields** | **str**| Provide the name of the field by which you would like to filter the response. For example, if you provide &amp;quot;host_video&amp;quot; as the value of this field, you will get a response similar to the following:     {     &amp;quot;schedule_meeting&amp;quot;: {         &amp;quot;host_video&amp;quot;: false     } }     You can provide multiple values by separating them with commas(example: &amp;quot;host_video,participant_video&amp;rdquo;). | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_locked_settings**
> object update_locked_settings(account_id, body=body)

Update locked settings

Update an account's locked settings.  [Account Locked Settings](https://support.zoom.us/hc/en-us/articles/115005269866) allows account admins and account owners to toggle settings on or off for all users in your account.    **Note:** Yout must have a Pro or a higher plan and enabled master and sub accounts options.         **Prerequisites:**     * Pro or a higher paid account.         **Scopes:** `account:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = zoom.AccountIdLockSettingsBody() # AccountIdLockSettingsBody |  (optional)

try:
    # Update locked settings
    api_response = api_instance.update_locked_settings(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_locked_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**AccountIdLockSettingsBody**](AccountIdLockSettingsBody.md)|  | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_the_account_owner**
> update_the_account_owner(account_id, body=body)

Update the account owner

Change an account's owner.  An account's current owner can [change the account's owner](https://support.zoom.us/hc/en-us/articles/115005686983-Change-Account-Owner) to another user on the same account.  **Prerequisites:**  * An account owner or admin permissions of an account  * The account making this API request must be on a Pro or a higher account plan with [Master account](https://developers.zoom.us/docs/api/rest/master-account-apis/) privileges  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = zoom.AccountIdOwnerBody() # AccountIdOwnerBody |  (optional)

try:
    # Update the account owner
    api_instance.update_the_account_owner(account_id, body=body)
except ApiException as e:
    print("Exception when calling AccountsApi->update_the_account_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**AccountIdOwnerBody**](AccountIdOwnerBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_vb**
> InlineResponse201 upload_vb(account_id, file=file)

Upload virtual background files

[Upload virtual background files](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_01EJF3YFEWGT8YA0ZJ079JEDQE) for all users on the account to use.    **Prerequisites:**  * The [Virtual Background feature](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background#h_2ef28080-fce9-4ac2-b567-dc958afab1b7) must be enabled on the account.  **Scopes:** `account:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.AccountsApi(zoom.ApiClient(configuration))
account_id = 'account_id_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # Upload virtual background files
    api_response = api_instance.upload_vb(account_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->upload_vb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

