# MeetingAndWebinarPollingObject5

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of Poll | [optional] 
**status** | **str** | Status of Poll:    &#x60;notstart&#x60; - Poll not started    &#x60;started&#x60; - Poll started    &#x60;ended&#x60; - Poll ended    &#x60;sharing&#x60; - Sharing poll results | [optional] 
**anonymous** | **bool** | Allow meeting participants to answer poll questions anonymously.   This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**poll_type** | **int** | The type of poll:  * &#x60;1&#x60; &amp;mdash; Poll.  * &#x60;2&#x60; &amp;mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * &#x60;3&#x60; &amp;mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to &#x60;1&#x60;. | [optional] 
**questions** | [**list[MeetingsmeetingIdpollsQuestions]**](MeetingsmeetingIdpollsQuestions.md) | Information about the poll&#x27;s questions. | [optional] 
**title** | **str** | The poll&#x27;s title, up to 64 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

