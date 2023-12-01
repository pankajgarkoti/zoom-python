# InlineResponse20055Questions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user who submitted answers to the poll. If the user is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details. | [optional] 
**name** | **str** | Name of the user who submitted answers to the poll. If &#x60;anonymous&#x60; option is enabled for a poll, the participant&#x27;s polling information will be kept anonymous and the value of &#x60;name&#x60; field will be &#x60;Anonymous Attendee&#x60;. | [optional] 
**question_details** | [**list[InlineResponse20055QuestionDetails]**](InlineResponse20055QuestionDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

