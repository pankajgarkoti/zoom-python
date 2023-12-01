# swagger_client.IMGroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**im_group**](IMGroupsApi.md#im_group) | **GET** /im/groups/{groupId} | Retrieve an IM directory group
[**im_group_create**](IMGroupsApi.md#im_group_create) | **POST** /im/groups | Create an IM directory group
[**im_group_delete**](IMGroupsApi.md#im_group_delete) | **DELETE** /im/groups/{groupId} | Delete an IM directory group
[**im_group_members**](IMGroupsApi.md#im_group_members) | **GET** /im/groups/{groupId}/members | List IM directory group members
[**im_group_members_create**](IMGroupsApi.md#im_group_members_create) | **POST** /im/groups/{groupId}/members | Add IM directory group members
[**im_group_members_delete**](IMGroupsApi.md#im_group_members_delete) | **DELETE** /im/groups/{groupId}/members/{memberId} | Delete IM directory group member
[**im_group_update**](IMGroupsApi.md#im_group_update) | **PATCH** /im/groups/{groupId} | Update an IM directory group
[**im_groups**](IMGroupsApi.md#im_groups) | **GET** /im/groups | List IM directory groups

# **im_group**
> InlineResponse20042 im_group(group_id)

Retrieve an IM directory group

Retrieve an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.         Scopes: `imgroup:read:admin`         **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.

try:
    # Retrieve an IM directory group
    api_response = api_instance.im_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_create**
> im_group_create(body=body)

Create an IM directory group

Create an IM directory group under your account.           **Scopes:** `imgroup:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImGroupsBody() # ImGroupsBody |  (optional)

try:
    # Create an IM directory group
    api_instance.im_group_create(body=body)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImGroupsBody**](ImGroupsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_delete**
> im_group_delete(group_id)

Delete an IM directory group

Delete an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.         Scopes: `imgroup:write:admin`          **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.

try:
    # Delete an IM directory group
    api_instance.im_group_delete(group_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_delete: %s\n" % e)
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

# **im_group_members**
> GroupMemberList im_group_members(group_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)

List IM directory group members

List the members of an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).           **Scopes:** `imgroup:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | **Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes. (optional)

try:
    # List IM directory group members
    api_response = api_instance.im_group_members(group_id, page_size=page_size, page_number=page_number, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **next_page_token** | **str**| Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 

### Return type

[**GroupMemberList**](GroupMemberList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_members_create**
> im_group_members_create(group_id, body=body)

Add IM directory group members

Add members to an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.           **Scopes:** `imgroup:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
body = swagger_client.GroupIdMembersBody2() # GroupIdMembersBody2 |  (optional)

try:
    # Add IM directory group members
    api_instance.im_group_members_create(group_id, body=body)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **body** | [**GroupIdMembersBody2**](GroupIdMembersBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_members_delete**
> im_group_members_delete(group_id, member_id)

Delete IM directory group member

Delete a member from an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.         Scopes: `imgroup:write:admin`          **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
member_id = 'member_id_example' # str | The member ID.

try:
    # Delete IM directory group member
    api_instance.im_group_members_delete(group_id, member_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **member_id** | **str**| The member ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_update**
> im_group_update(group_id, body=body)

Update an IM directory group

Update an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.           **Scopes:** `imgroup:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.
body = swagger_client.GroupsGroupIdBody2() # GroupsGroupIdBody2 |  (optional)

try:
    # Update an IM directory group
    api_instance.im_group_update(group_id, body=body)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.     Retrieve by calling the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API. | 
 **body** | [**GroupsGroupIdBody2**](GroupsGroupIdBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_groups**
> IMGroupList im_groups()

List IM directory groups

List [IM directory groups](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).           **Scopes:** `imgroup:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))

try:
    # List IM directory groups
    api_response = api_instance.im_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IMGroupList**](IMGroupList.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

