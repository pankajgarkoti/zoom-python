# InlineResponse20044

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | The number of records returned with a single API call. | [optional] [default to 30]
**next_page_token** | **str** | The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**_from** | **datetime** | The start date in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;&#x60; UTC format used to retrieve the creation date range of the meeting summaries. | [optional] 
**to** | **datetime** | The end date in &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;&#x60; UTC format used to retrieve the creation date range of the meeting summaries. | [optional] 
**summaries** | [**list[InlineResponse20044Summaries]**](InlineResponse20044Summaries.md) | List of meeting summary objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

