# InlineResponse20068Questions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Participant email. If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details. | [optional] 
**name** | **str** | Participant display name.       If the anonymous [Q&amp;amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) option is enabled and if a participant submits the Q&amp;amp;A without providing their name, the value of the &#x60;name&#x60; field is &amp;quot;Anonymous Attendee&amp;quot;. | [optional] 
**question_details** | [**list[InlineResponse20068QuestionDetails]**](InlineResponse20068QuestionDetails.md) | Array of questions from user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

