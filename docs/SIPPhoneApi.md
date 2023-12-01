# zoom.SIPPhoneApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sip_phone**](SIPPhoneApi.md#create_sip_phone) | **POST** /sip_phones | Enable SIP phone
[**delete_sip_phone**](SIPPhoneApi.md#delete_sip_phone) | **DELETE** /sip_phones/{phoneId} | Delete SIP phone
[**list_sip_phones**](SIPPhoneApi.md#list_sip_phones) | **GET** /sip_phones | List SIP phones
[**update_sip_phone**](SIPPhoneApi.md#update_sip_phone) | **PATCH** /sip_phones/{phoneId} | Update SIP phone

# **create_sip_phone**
> InlineResponse20116 create_sip_phone(body=body)

Enable SIP phone

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to enable a user to use SIP phone.         **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.       **Scopes:** `sip_phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.SIPPhoneApi(zoom.ApiClient(configuration))
body = zoom.SipPhonesBody() # SipPhonesBody |  (optional)

try:
    # Enable SIP phone
    api_response = api_instance.create_sip_phone(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->create_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SipPhonesBody**](SipPhonesBody.md)|  | [optional] 

### Return type

[**InlineResponse20116**](InlineResponse20116.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_phone**
> delete_sip_phone(phone_id)

Delete SIP phone

Use this API to delete a Zoom account's SIP phone.    **Prerequisites**:  * Currently only supported on Cisco and Avaya PBX systems.  * The user must enable **SIP Phone Integration** by contacting the [Zoom Sales](https://zoom.us/contactsales) team.  **Scopes:** `sip_phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.SIPPhoneApi(zoom.ApiClient(configuration))
phone_id = 'phone_id_example' # str | The SIP phone ID. It can be retrieved from the List SIP Phones API.

try:
    # Delete SIP phone
    api_instance.delete_sip_phone(phone_id)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->delete_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**| The SIP phone ID. It can be retrieved from the List SIP Phones API. | 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_phones**
> InlineResponse20079 list_sip_phones(page_number=page_number, search_key=search_key, page_size=page_size, next_page_token=next_page_token)

List SIP phones

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to list SIP phones on an account.         **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * User must enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.       **Scopes:** `sip_phone:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = zoom.SIPPhoneApi(zoom.ApiClient(configuration))
page_number = 1 # int | **Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination. (optional) (default to 1)
search_key = 'search_key_example' # str | User name or email address of a user. If this parameter is provided, only the SIP phone system integration enabled for that specific user will be returned. Otherwise, all SIP phones on an account will be returned. (optional)
page_size = 56 # int | The number of records returned within a single API call. (optional)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List SIP phones
    api_response = api_instance.list_sip_phones(page_number=page_number, search_key=search_key, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->list_sip_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
 **search_key** | **str**| User name or email address of a user. If this parameter is provided, only the SIP phone system integration enabled for that specific user will be returned. Otherwise, all SIP phones on an account will be returned. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] 
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_phone**
> update_sip_phone(phone_id, body=body)

Update SIP phone

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to update information of a specific SIP Phone on a Zoom account.         **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.       **Scopes:** `sip_phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = zoom.SIPPhoneApi(zoom.ApiClient(configuration))
phone_id = 'phone_id_example' # str | The SIP phone ID. This can be retrieved from the List SIP Phones API.
body = zoom.SipPhonesPhoneIdBody() # SipPhonesPhoneIdBody |  (optional)

try:
    # Update SIP phone
    api_instance.update_sip_phone(phone_id, body=body)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->update_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**| The SIP phone ID. This can be retrieved from the List SIP Phones API. | 
 **body** | [**SipPhonesPhoneIdBody**](SipPhonesPhoneIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[openapi_authorization](../README.md#openapi_authorization), [openapi_oauth](../README.md#openapi_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

