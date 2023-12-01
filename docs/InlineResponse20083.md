# InlineResponse20083

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_number** | **int** | The page number of the current results. | [optional] [default to 1]
**page_size** | **int** | The number of records returned within a single API call. | [optional] [default to 30]
**total_records** | **int** | The total number of all the records available across pages. | [optional] 
**users** | [**list[InlineResponse20083Users]**](InlineResponse20083Users.md) | Information about the users. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

