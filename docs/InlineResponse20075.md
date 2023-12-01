# InlineResponse20075

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token&#x27;s expiration period is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_size** | **int** | The number of records returned within a single API call. | [optional] [default to 30]
**total_records** | **int** | The number of all records available across pages. | [optional] 
**participants** | [**list[InlineResponse20075Participants]**](InlineResponse20075Participants.md) | Information about the webinar participant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

