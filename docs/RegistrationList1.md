# RegistrationList1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_number** | **int** | **Deprecated.** This field is deprecated. We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
**page_size** | **int** | The number of records returned with a single API call. | [optional] [default to 30]
**total_records** | **int** | The total number of all the records available across pages. | [optional] 
**registrants** | [**list[RegistrationList1Registrants]**](RegistrationList1Registrants.md) | List of registrant objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

