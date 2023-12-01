# InlineResponse20073Meetings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_keys** | [**list[InlineResponse20073CustomKeys]**](InlineResponse20073CustomKeys.md) | Information about the meeting&#x27;s assigned custom keys and values. This returns a maximum of 10 items. | [optional] 
**duration** | **int** | The meeting&#x27;s duration. | [optional] 
**end_time** | **datetime** | The meeting&#x27;s end date and time. | [optional] 
**id** | **int** | The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID). | [optional] 
**participants_count** | **int** | The number of meeting participants. | [optional] 
**session_key** | **str** | The Video SDK custom session ID. | [optional] 
**source** | **str** | Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app&#x27;s name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the &#x60;Zoom&#x60; value. | [optional] 
**start_time** | **datetime** | The meeting&#x27;s start date and time. | [optional] 
**topic** | **str** | The meeting&#x27;s topic. | [optional] 
**total_minutes** | **int** | The sum of meeting minutes from all meeting participants in the meeting. | [optional] 
**type** | **int** | The type of meeting or webinar.   meeting:  * &#x60;1&#x60; &amp;mdash; Instant meeting.  * &#x60;2&#x60; &amp;mdash; Scheduled meeting.  * &#x60;3&#x60; &amp;mdash; A recurring meeting with no fixed time.  * &#x60;4&#x60; &amp;mdash; A meeting created via PMI (Personal Meeting ID).  * &#x60;7&#x60; &amp;mdash; A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * &#x60;8&#x60; - Recurring meeting with a fixed time.   webinar:  * &#x60;5&#x60; &amp;mdash; A webinar.  * &#x60;6&#x60; &amp;mdash; A recurring webinar without a fixed time  * &#x60;9&#x60; &amp;mdash; A recurring webinar with a fixed time.  | [optional] 
**user_email** | **str** | The user&#x27;s email address. | [optional] 
**user_name** | **str** | The user&#x27;s display name. | [optional] 
**uuid** | **str** | The meeting&#x27;s universally unique identifier (UUID). Each meeting instance generates a meeting UUID. | [optional] 
**schedule_time** | **str** | The meeting&#x27;s scheduled date and time. | [optional] 
**join_waiting_room_time** | **str** | The date and time at which the attendee joined the waiting room. | [optional] 
**join_time** | **str** | The date and time at which the attendee joined the meeting. | [optional] 
**leave_time** | **str** | The date and time at which the attendee left the meeting. | [optional] 
**host_organization** | **str** | Host Account Name of Hosting Organization. | [optional] 
**host_name** | **str** | Host&#x27;s name. | [optional] 
**has_screen_share** | **bool** | Indicates whether or not the screenshare feature was used in the meeting. | [optional] 
**has_recording** | **bool** | Indicates whether or not the recording feature was used in the meeting. | [optional] 
**has_chat** | **bool** | Indicates whether or not the chat feature was used in the meeting. | [optional] 
**meeting_encryption_status** | **int** | The meeting&#x27;s encryption status.  * &#x60;1&#x60; &amp;mdash; E2E encryption.  * &#x60;2&#x60; &amp;mdash; Enhanced encryption. | [optional] 
**participants_count_my_account** | **int** | The number of meeting participants from my account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

