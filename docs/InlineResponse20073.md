# InlineResponse20073

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_number** | **int** | **Deprecated.** We will no longer support this field in a future release. Instead, use the &#x60;next_page_token&#x60; for pagination. | [optional] [default to 1]
**page_size** | **int** | The number of records returned with a single API call. | [optional] [default to 30]
**total_records** | **int** | The total number of all the records available across pages. | [optional] 
**_from** | **date** | The report&#x27;s start date. | [optional] 
**meetings** | [**list[InlineResponse20073Meetings]**](InlineResponse20073Meetings.md) | Information about the meeting. | [optional] 
**to** | **date** | The report&#x27;s end date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

