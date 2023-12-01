# InlineResponse20072

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | Start date for this report. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_number** | **int** | The page number of the current results. | [optional] [default to 1]
**page_size** | **int** | The number of records returned with a single API call. | [optional] [default to 30]
**to** | **date** | End date for this report. | [optional] 
**total_records** | **int** | The total number of all the records available across pages. | [optional] 
**total_meeting_minutes** | **int** | Number of meeting minutes for this range. | [optional] 
**total_meetings** | **int** | Number of meetings for this range. | [optional] 
**total_participants** | **int** | Number of participants for this range. | [optional] 
**users** | [**list[InlineResponse20072Users]**](InlineResponse20072Users.md) | Array of user objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

