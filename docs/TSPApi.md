# zoom.TSPApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tsp**](TSPApi.md#tsp) | **GET** /tsp | Get account&#x27;s TSP information
[**tsp_update**](TSPApi.md#tsp_update) | **PATCH** /tsp | Update account&#x27;s TSP information
[**tsp_url_update**](TSPApi.md#tsp_url_update) | **PATCH** /users/{userId}/tsp/settings | Set global dial-in URL for a TSP user
[**user_tsp**](TSPApi.md#user_tsp) | **GET** /users/{userId}/tsp/{tspId} | Get a user&#x27;s TSP account
[**user_tsp_create**](TSPApi.md#user_tsp_create) | **POST** /users/{userId}/tsp | Add a user&#x27;s TSP account
[**user_tsp_delete**](TSPApi.md#user_tsp_delete) | **DELETE** /users/{userId}/tsp/{tspId} | Delete a user&#x27;s TSP account
[**user_tsp_update**](TSPApi.md#user_tsp_update) | **PATCH** /users/{userId}/tsp/{tspId} | Update a TSP account
[**user_tsps**](TSPApi.md#user_tsps) | **GET** /users/{userId}/tsp | List user&#x27;s TSP accounts

# **tsp**
> InlineResponse20080 tsp()

Get account's TSP information

Get information on Telephony Service Provider on an account level.         **Prerequisites:**     * A Pro or a higher plan.  **Scopes:** `tsp:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))

try:
    # Get account's TSP information
    api_response = api_instance.tsp()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->tsp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tsp_update**
> tsp_update(body=body)

Update account's TSP information

Update information of the Telephony Service Provider set up on an account.     **Prerequisites**:     TSP account option should be enabled.       **Scopes:** `tsp:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
body = zoom.TspBody() # TspBody | TSP Account (optional)

try:
    # Update account's TSP information
    api_instance.tsp_update(body=body)
except ApiException as e:
    print("Exception when calling TSPApi->tsp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TspBody**](TspBody.md)| TSP Account | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tsp_url_update**
> tsp_url_update(user_id, body=body)

Set global dial-in URL for a TSP user

A global dial-in page can provide a list of global access numbers using which audio conferencing can be conducted. By calling this API, you can set the url for the global dial-in page of a user whose Zoom account has TSP and special TSP with third-party audio conferencing options enabled. &lt;p&gt;&lt;/p&gt;   **Scopes:** `tsp:write:admin`,`tsp:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The userId or email address of the user.
body = zoom.TSPGlobalDialInURLSetting() # TSPGlobalDialInURLSetting | Global dial-in URL of the user. (optional)

try:
    # Set global dial-in URL for a TSP user
    api_instance.tsp_url_update(user_id, body=body)
except ApiException as e:
    print("Exception when calling TSPApi->tsp_url_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The userId or email address of the user. | 
 **body** | [**TSPGlobalDialInURLSetting**](TSPGlobalDialInURLSetting.md)| Global dial-in URL of the user. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp**
> TSPAccount user_tsp(user_id, tsp_id)

Get a user's TSP account

Each user can have a maximum of two TSP accounts. Use this API to retrieve details of a specific TSP account enabled for a specific user.           **Scopes:** `tsp:read:admin`,`tsp:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = zoom.UserId4() # UserId4 | The user ID or email address of the user. For user-level apps, pass the `me` value.
tsp_id = 'tsp_id_example' # str | TSP account ID.

try:
    # Get a user's TSP account
    api_response = api_instance.user_tsp(user_id, tsp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId4**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **tsp_id** | **str**| TSP account ID. | 

### Return type

[**TSPAccount**](TSPAccount.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_create**
> TSPAccountsList1 user_tsp_create(user_id, body=body)

Add a user's TSP account

Add a user's TSP account.           **Scopes:** `tsp:write:admin`,`tsp:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = zoom.UserId3() # UserId3 | The user ID or email address of the user. For user-level apps, pass the `me` value.
body = zoom.TSPAccountsList() # TSPAccountsList | TSP account. (optional)

try:
    # Add a user's TSP account
    api_response = api_instance.user_tsp_create(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId3**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **body** | [**TSPAccountsList**](TSPAccountsList.md)| TSP account. | [optional] 

### Return type

[**TSPAccountsList1**](TSPAccountsList1.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_delete**
> user_tsp_delete(user_id, tsp_id)

Delete a user's TSP account

Delete a user's TSP account.           **Scopes:** `tsp:write:admin`,`tsp:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = zoom.UserId5() # UserId5 | The user ID or email address of the user. For user-level apps, pass the `me` value.
tsp_id = 'tsp_id_example' # str | TSP account ID.

try:
    # Delete a user's TSP account
    api_instance.user_tsp_delete(user_id, tsp_id)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId5**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **tsp_id** | **str**| TSP account ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_update**
> user_tsp_update(user_id, tsp_id, body=body)

Update a TSP account

Update a user's TSP account.           **Scopes:** `tsp:write:admin`,`tsp:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = zoom.UserId6() # UserId6 | The user ID or email address of the user. For user-level apps, pass the `me` value.
tsp_id = 'tsp_id_example' # str | TSP account ID.
body = zoom.TSPAccount1() # TSPAccount1 | TSP account. (optional)

try:
    # Update a TSP account
    api_instance.user_tsp_update(user_id, tsp_id, body=body)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId6**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 
 **tsp_id** | **str**| TSP account ID. | 
 **body** | [**TSPAccount1**](TSPAccount1.md)| TSP account. | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsps**
> InlineResponse20081 user_tsps(user_id)

List user's TSP accounts

A user can have a maximum of two TSP accounts. Use this API to list all TSP accounts of a user.           **Scopes:** `tsp:read:admin`,`tsp:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.TSPApi(zoom.ApiClient(configuration))
user_id = zoom.UserId2() # UserId2 | The user ID or email address of the user. For user-level apps, pass the `me` value.

try:
    # List user's TSP accounts
    api_response = api_instance.user_tsps(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserId2**](.md)| The user ID or email address of the user. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

