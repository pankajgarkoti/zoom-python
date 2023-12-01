# InlineResponse20012

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | The start date. | [optional] 
**to** | **date** | The end date. | [optional] 
**next_page_token** | **str** | The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_size** | **int** | The number of records returned within a single API call. | [optional] [default to 30]
**total_records** | **int** | The number of all records available across pages. | [optional] 
**meetings** | [**list[InlineResponse20012Meetings]**](InlineResponse20012Meetings.md) | List of recordings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

