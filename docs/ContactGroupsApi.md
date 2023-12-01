# zoom.ContactGroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_group**](ContactGroupsApi.md#contact_group) | **GET** /contacts/groups/{groupId} | Get a contact group
[**contact_group_create**](ContactGroupsApi.md#contact_group_create) | **POST** /contacts/groups | Create a contact group
[**contact_group_delete**](ContactGroupsApi.md#contact_group_delete) | **DELETE** /contacts/groups/{groupId} | Delete a contact group
[**contact_group_member_add**](ContactGroupsApi.md#contact_group_member_add) | **POST** /contacts/groups/{groupId}/members | Add contact group members
[**contact_group_member_remove**](ContactGroupsApi.md#contact_group_member_remove) | **DELETE** /contacts/groups/{groupId}/members | Remove members in a contact group
[**contact_group_members**](ContactGroupsApi.md#contact_group_members) | **GET** /contacts/groups/{groupId}/members | List contact group members
[**contact_group_update**](ContactGroupsApi.md#contact_group_update) | **PATCH** /contacts/groups/{groupId} | Update a contact group
[**contact_groups**](ContactGroupsApi.md#contact_groups) | **GET** /contacts/groups | List contact groups

# **contact_group**
> InlineResponse20014 contact_group(group_id)

Get a contact group

Get a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
group_id = 'group_id_example' # str | The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API.

try:
    # Get a contact group
    api_response = api_instance.contact_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_create**
> InlineResponse2012 contact_group_create(body=body)

Create a contact group

Use this API to create a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
body = zoom.ContactsGroupsBody() # ContactsGroupsBody |  (optional)

try:
    # Create a contact group
    api_response = api_instance.contact_group_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactsGroupsBody**](ContactsGroupsBody.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_delete**
> contact_group_delete(group_id)

Delete a contact group

Use this API to delete a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
group_id = 'group_id_example' # str | The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API.

try:
    # Delete a contact group
    api_instance.contact_group_delete(group_id)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_member_add**
> InlineResponse2013 contact_group_member_add(body=body)

Add contact group members

Use this API to add members to a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
body = zoom.GroupIdMembersBody() # GroupIdMembersBody |  (optional)

try:
    # Add contact group members
    api_response = api_instance.contact_group_member_add(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_member_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupIdMembersBody**](GroupIdMembersBody.md)|  | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_member_remove**
> contact_group_member_remove(member_ids)

Remove members in a contact group

Use this API to remove members in a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
member_ids = 'member_ids_example' # str | The member's ID in a contact group. Use commas (,) to separate a maximum of 20 ids.      Can be retrieved by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroupMembers) API.

try:
    # Remove members in a contact group
    api_instance.contact_group_member_remove(member_ids)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_member_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_ids** | **str**| The member&#x27;s ID in a contact group. Use commas (,) to separate a maximum of 20 ids.      Can be retrieved by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroupMembers) API. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_members**
> InlineResponse20015 contact_group_members(page_size=page_size, next_page_token=next_page_token)

List contact group members

List members in [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
page_size = 10 # int | The number of records returned with a single API call.  (optional) (default to 10)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List contact group members
    api_response = api_instance.contact_group_members(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned with a single API call.  | [optional] [default to 10]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_group_update**
> contact_group_update(group_id, body=body)

Update a contact group

Update a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
group_id = 'group_id_example' # str | The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API.
body = zoom.GroupsGroupIdBody() # GroupsGroupIdBody |  (optional)

try:
    # Update a contact group
    api_instance.contact_group_update(group_id, body=body)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. | 
 **body** | [**GroupsGroupIdBody**](GroupsGroupIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_groups**
> InlineResponse20013 contact_groups(page_size=page_size, next_page_token=next_page_token)

List contact groups

List [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.ContactGroupsApi(zoom.ApiClient(configuration))
page_size = 10 # int | The number of records returned with a single API call.  (optional) (default to 10)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List contact groups
    api_response = api_instance.contact_groups(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactGroupsApi->contact_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned with a single API call.  | [optional] [default to 10]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

