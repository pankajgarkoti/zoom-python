# zoom.PACApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_pacs**](PACApi.md#user_pacs) | **GET** /users/{userId}/pac | List a user&#x27;s PAC accounts

# **user_pacs**
> InlineResponse20059 user_pacs(user_id)

List a user's PAC accounts

Retrieve a list of a user's [personal audio conference (PAC)](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) accounts. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.    PAC allows Pro or higher account holders to host meetings through PSTN (phone dial-in) only.    **Prerequisites**  * A Pro or higher plan with an [Audio Conferencing](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) subscription.  * The [**Personal Audio Conference**](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference#h_01F5BPM447M6QDJXX50RSFXKJ3) setting enabled in the user's profile.  **Scopes:** `pac:read:admin`,`pac:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.PACApi(zoom.ApiClient(configuration))
user_id = 'user_id_example' # str | The user's user ID or email address. For user-level apps, pass the `me` value.

try:
    # List a user's PAC accounts
    api_response = api_instance.user_pacs(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PACApi->user_pacs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#x27;s user ID or email address. For user-level apps, pass the &#x60;me&#x60; value. | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

