# InlineResponse20077

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Webinar ID in &amp;quot;**long**&amp;quot; format(represented as int64 data type in JSON), also known as the webinar number. | [optional] 
**questions** | [**list[InlineResponse20077Questions]**](InlineResponse20077Questions.md) | Array of webinar question objects. | [optional] 
**start_time** | **datetime** | Webinar start time. | [optional] 
**uuid** | **str** | Webinar UUID. Each Webinar instance will generate its own UUID(i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). [Double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27; in it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

