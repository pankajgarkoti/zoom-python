# InlineResponse20110Polls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous** | **bool** | Whether to allow meeting participants to answer poll questions anonymously:  * &#x60;true&#x60; &amp;mdash; Anonymous polls enabled.  * &#x60;false&#x60; &amp;mdash; Participants cannot answer poll questions anonymously. | [optional] 
**id** | **str** | Meeting Poll ID | [optional] 
**poll_type** | **int** | The type of poll:  * &#x60;1&#x60; &amp;mdash; Poll.  * &#x60;2&#x60; &amp;mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * &#x60;3&#x60; &amp;mdash; Quiz. This feature must be enabled in your Zoom account. | [optional] 
**questions** | [**list[InlineResponse20110Questions]**](InlineResponse20110Questions.md) | Information about the poll&#x27;s questions. | [optional] 
**status** | **str** | Status of the Meeting Poll:    &#x60;notstart&#x60; - Poll not started    &#x60;started&#x60; - Poll started    &#x60;ended&#x60; - Poll ended    &#x60;sharing&#x60; - Sharing poll results | [optional] 
**title** | **str** | Title for the Poll | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

