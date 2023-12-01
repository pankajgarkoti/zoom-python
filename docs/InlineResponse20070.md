# InlineResponse20070

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | Start date for this report. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. This field does **not** return if the &#x60;query_date_type&#x60; parameter is the &#x60;meeting_start_time&#x60; or &#x60;meeting_end_time&#x60; value. | [optional] 
**page_size** | **int** | The number of records returned with a single API call. | [optional] 
**to** | **date** | End date for this report. | [optional] 
**total_records** | **int** | The total number of all the records available across pages. This field does **not** return if the &#x60;query_date_type&#x60; parameter is the &#x60;meeting_start_time&#x60; or &#x60;meeting_end_time&#x60; value. | [optional] 
**telephony_usage** | [**list[InlineResponse20070TelephonyUsage]**](InlineResponse20070TelephonyUsage.md) | Array of telephony objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

