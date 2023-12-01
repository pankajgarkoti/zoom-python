# zoom.InformationBarriersApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**information_barriers_create**](InformationBarriersApi.md#information_barriers_create) | **POST** /information_barriers/policies | Create an Information Barrier policy
[**information_barriers_delete**](InformationBarriersApi.md#information_barriers_delete) | **DELETE** /information_barriers/policies/{policyId} | Remove an Information Barrier policy
[**information_barriers_get**](InformationBarriersApi.md#information_barriers_get) | **GET** /information_barriers/policies/{policyId} | Get an Information Barrier policy by ID
[**information_barriers_list**](InformationBarriersApi.md#information_barriers_list) | **GET** /information_barriers/policies | List information Barrier policies
[**information_barriers_update**](InformationBarriersApi.md#information_barriers_update) | **PATCH** /information_barriers/policies/{policyId} | Update an Information Barriers policy

# **information_barriers_create**
> InlineResponse2019 information_barriers_create(body=body)

Create an Information Barrier policy

Create a new Information Barrier policy. [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) help customers control communication policies and meet regulatory requirements at scale. Use information barriers to prevent specific groups of users who possess sensitive information from communicating with others who should not know this information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.InformationBarriersApi(zoom.ApiClient(configuration))
body = zoom.InformationBarriersPoliciesBody() # InformationBarriersPoliciesBody | Information Barriers object (optional)

try:
    # Create an Information Barrier policy
    api_response = api_instance.information_barriers_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationBarriersApi->information_barriers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InformationBarriersPoliciesBody**](InformationBarriersPoliciesBody.md)| Information Barriers object | [optional] 

### Return type

[**InlineResponse2019**](InlineResponse2019.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **information_barriers_delete**
> information_barriers_delete(policy_id)

Remove an Information Barrier policy

Remove an [Information Barrier](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.InformationBarriersApi(zoom.ApiClient(configuration))
policy_id = 'policy_id_example' # str | The Information Barriers policy's ID.

try:
    # Remove an Information Barrier policy
    api_instance.information_barriers_delete(policy_id)
except ApiException as e:
    print("Exception when calling InformationBarriersApi->information_barriers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| The Information Barriers policy&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **information_barriers_get**
> InlineResponse2019 information_barriers_get(policy_id)

Get an Information Barrier policy by ID

Return an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy by its ID.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.InformationBarriersApi(zoom.ApiClient(configuration))
policy_id = 'policy_id_example' # str | The Information Barrier policy's ID.

try:
    # Get an Information Barrier policy by ID
    api_response = api_instance.information_barriers_get(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationBarriersApi->information_barriers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| The Information Barrier policy&#x27;s ID. | 

### Return type

[**InlineResponse2019**](InlineResponse2019.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **information_barriers_list**
> InlineResponse20043 information_barriers_list()

List information Barrier policies

Return a list of all [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policies and their information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.InformationBarriersApi(zoom.ApiClient(configuration))

try:
    # List information Barrier policies
    api_response = api_instance.information_barriers_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationBarriersApi->information_barriers_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **information_barriers_update**
> object information_barriers_update(policy_id, body=body)

Update an Information Barriers policy

Update an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

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
api_instance = zoom.InformationBarriersApi(zoom.ApiClient(configuration))
policy_id = 'policy_id_example' # str | The Information Barriers policy's ID.
body = zoom.PoliciesPolicyIdBody() # PoliciesPolicyIdBody | Information about the updated Information Barriers policy. (optional)

try:
    # Update an Information Barriers policy
    api_response = api_instance.information_barriers_update(policy_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InformationBarriersApi->information_barriers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| The Information Barriers policy&#x27;s ID. | 
 **body** | [**PoliciesPolicyIdBody**](PoliciesPolicyIdBody.md)| Information about the updated Information Barriers policy. | [optional] 

### Return type

**object**

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

