# MeetingMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host display name. | [optional] 
**custom_keys** | [**list[MeetingMetricsCustomKeys]**](MeetingMetricsCustomKeys.md) | Custom keys and values assigned to the meeting. | [optional] 
**dept** | **str** | Department of the host. | [optional] 
**duration** | **str** | Meeting duration. | [optional] 
**email** | **str** | Email address of the host. | [optional] 
**end_time** | **datetime** | Meeting end time. | [optional] 
**has_3rd_party_audio** | **bool** | Indicates whether or not [third party audio](https://support.zoom.us/hc/en-us/articles/202470795-3rd-Party-Audio-Conference) was used in the meeting. | [optional] 
**has_archiving** | **bool** | Whether the archiving feature was used in the meeting. | [optional] 
**has_pstn** | **bool** | Indicates whether or not the PSTN was used in the meeting. | [optional] 
**has_recording** | **bool** | Indicates whether or not the recording feature was used in the meeting.  | [optional] 
**has_screen_share** | **bool** | Indicates whether or not screenshare feature was used in the meeting. | [optional] 
**has_sip** | **bool** | Indicates whether or not someone joined the meeting using SIP. | [optional] 
**has_video** | **bool** | Indicates whether or not video was used in the meeting. | [optional] 
**has_voip** | **bool** | Indicates whether or not VoIP was used in the meeting. | [optional] 
**has_manual_captions** | **bool** | Indicates whether a manual caption was enabled in the meeting. | [optional] 
**has_automated_captions** | **bool** | Indicates whether an automated caption was enabled in the meeting. | [optional] 
**id** | **int** | [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &amp;quot;**long**&amp;quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**in_room_participants** | **int** | The number of Zoom Room participants in the meeting. | [optional] 
**participants** | **int** | Meeting participant count. | [optional] 
**start_time** | **datetime** | Meeting start time. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**user_type** | **str** | License type of the user. | [optional] 
**uuid** | **str** | Meeting UUID. [Double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27;or contains &#x27;//&#x27; in it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

