# InlineResponse20016

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | The report&#x27;s start date. | [optional] 
**next_page_token** | **str** | The report&#x27;s [&#x60;next_page_token&#x60; value](https://marketplace.zoom.us/docs/api-reference/pagination#next-page-token). The API returns this value when the set of available results exceeds the current page size. This token expires after 15 minutes. | [optional] 
**page_size** | **int** | The number of records to return within a single API call. | [optional] [default to 30]
**to** | **date** | The report&#x27;s end date. | [optional] 
**users** | [**list[InlineResponse20016Users]**](InlineResponse20016Users.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

