# InlineResponse20071

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | The report&#x27;s start date. This value must be within the past six months. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token returns when the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_size** | **int** | The number of records returned in a single API call. | [optional] [default to 30]
**to** | **date** | The report&#x27;s end date. This value must be within the past six months and cannot exceed a month from the &#x60;from&#x60; value. | [optional] 
**upcoming_events** | [**list[InlineResponse20071UpcomingEvents]**](InlineResponse20071UpcomingEvents.md) | Information about the upcoming event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

