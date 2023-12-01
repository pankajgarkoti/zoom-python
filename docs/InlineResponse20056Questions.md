# InlineResponse20056Questions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#x27;s email address. If the user is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details. | [optional] 
**name** | **str** | The user&#x27;s name. If &#x60;anonymous&#x60; option is enabled for the Q&amp;amp;A, the participant&#x27;s information is be kept anonymous and the value of &#x60;name&#x60; field is &#x60;Anonymous Attendee&#x60;. | [optional] 
**question_details** | [**list[InlineResponse20056QuestionDetails]**](InlineResponse20056QuestionDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

