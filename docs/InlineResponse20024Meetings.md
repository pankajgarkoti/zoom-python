# InlineResponse20024Meetings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The host&#x27;s display name. | [optional] 
**audio_quality** | **str** | The meeting&#x27;s [audio quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts).  * &#x60;good&#x60; &amp;mdash; The audio is almost flawless and the quality is excellent.  * &#x60;fair&#x60; - The audio occasionally has distortion, noise, and other problems, but the content is basically continuous. Participants can communicate normally.  * &#x60;poor&#x60; - The audio often has distortion, noise, and other problems, but the content is basically continuous. Participants can communicate normally.  * &#x60;bad&#x60; - The sound quality is extremely poor and the audio content is almost inaudible. | [optional] 
**custom_keys** | [**list[InlineResponse20024CustomKeys]**](InlineResponse20024CustomKeys.md) | The custom keys and values assigned to the meeting. | [optional] 
**dept** | **str** | The department of the host. | [optional] 
**duration** | **str** | The meeting duration. It&#x27;s formatted as hh:mm:ss, for example: &#x60;16:08&#x60; for 16 minutes and 8 seconds. | [optional] 
**email** | **str** | The email address of the host. | [optional] 
**end_time** | **datetime** | The meeting&#x27;s end time. | [optional] 
**has_3rd_party_audio** | **bool** | This field indicates whether or not [third party audio](https://support.zoom.us/hc/en-us/articles/202470795-3rd-Party-Audio-Conference) was used in the meeting. | [optional] 
**has_archiving** | **bool** | Whether the archiving feature was used in the meeting. | [optional] 
**has_pstn** | **bool** | This field indicates  whether or not the PSTN was used in the meeting. | [optional] 
**has_recording** | **bool** | This field indicates  whether or not the recording feature was used in the meeting.  | [optional] 
**has_screen_share** | **bool** | This field indicates  whether or not screenshare feature was used in the meeting. | [optional] 
**has_sip** | **bool** | This field indicates  whether or not someone joined the meeting using SIP. | [optional] 
**has_video** | **bool** | This field indicates  whether or not video was used in the meeting. | [optional] 
**has_voip** | **bool** | This field indicates whether or not VoIP was used in the meeting. | [optional] 
**has_manual_captions** | **bool** | This field indicates  whether a manual caption was enabled in the meeting. | [optional] 
**has_automated_captions** | **bool** | This field indicates  whether an automated caption was enabled in the meeting. | [optional] 
**id** | **int** | The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &amp;quot;**long**&amp;quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**in_room_participants** | **int** | The number of Zoom Room participants in the meeting. | [optional] 
**participants** | **int** | The meeting participant count. | [optional] 
**screen_share_quality** | **str** | The meeting&#x27;s [screen share quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts).  * &#x60;good&#x60; - The video is almost flawless and the quality is excellent.  * &#x60;fair&#x60; - The video definition is high, occasionally gets stuck, fast or slow, or other problems, but the frequency is very low and the video quality is good.  * &#x60;poor&#x60; - The video definition is not high, but not many problems exist. The video quality is mediocre.  * &#x60;bad&#x60; - The picture is very blurred and often gets stuck. | [optional] 
**session_key** | **str** | The Video SDK custom session ID. | [optional] 
**start_time** | **datetime** | The meeting start time. | [optional] 
**topic** | **str** | The meeting topic. | [optional] 
**tracking_fields** | [**list[InlineResponse20024TrackingFields]**](InlineResponse20024TrackingFields.md) | The tracking fields and values assigned to the meeting. | [optional] 
**user_type** | **str** | The license type of the user. | [optional] 
**uuid** | **str** | The meeting UUID. Please double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27;or contains &#x27;//&#x27; in it. | [optional] 
**video_quality** | **str** | The meeting&#x27;s [video quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts).  * &#x60;good&#x60; - The video is almost flawless and the quality is excellent.  * &#x60;fair&#x60; - The video definition is high, occasionally gets stuck, fast or slow, or other problems, but the frequency is very low and the video quality is good.  * &#x60;poor&#x60; - The video definition is not high, but not many problems exist. The video quality is mediocre.  * &#x60;bad&#x60; - The picture is very blurred and often gets stuck. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

