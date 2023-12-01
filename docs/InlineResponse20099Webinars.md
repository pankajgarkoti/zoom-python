# InlineResponse20099Webinars

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agenda** | **str** | Webinar description. The agenda length gets truncated to 250 characters when you list all webinars for a user. To view the complete agenda, retrieve details for a single webinar, use the [**Get a webinar**](/docs/api-reference/zoom-api/methods#operation/webinar) API. | [optional] 
**created_at** | **datetime** | The webinar&#x27;s creation time. | [optional] 
**duration** | **int** | The webinar&#x27;s duration, in minutes. | [optional] 
**host_id** | **str** | The host&#x27;s ID. | [optional] 
**id** | **int** | The webinar ID. | [optional] 
**join_url** | **str** | The URL to join the webinar. | [optional] 
**start_time** | **datetime** | The webinar&#x27;s start time. | [optional] 
**timezone** | **str** | The webinar&#x27;s [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones). | [optional] 
**topic** | **str** | The webinar&#x27;s topic. | [optional] 
**type** | **int** | The webinar type.  * &#x60;5&#x60; - A webinar.  * &#x60;6&#x60; - A recurring webinar without a fixed time.  * &#x60;9&#x60; - A recurring webinar with a fixed time. | [optional] [default to TypeEnum._5]
**uuid** | **str** | The webinar&#x27;s universally unique identifier (UUID). Each webinar instance generates a webinar UUID. | [optional] 
**is_simulive** | **bool** | Whether the webinar is &#x60;simulive&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

