# WebinarMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | User display name. | [optional] 
**custom_keys** | [**list[InlineResponse20029CustomKeys]**](InlineResponse20029CustomKeys.md) | Custom keys and values assigned to the Webinar. | [optional] 
**dept** | **str** | Department of the host. | [optional] 
**duration** | **str** | Webinar duration, formatted as hh:mm:ss, for example: &#x60;10:00&#x60; for ten minutes. | [optional] 
**email** | **str** | User email. | [optional] 
**end_time** | **datetime** | Webinar end time. | [optional] 
**has_3rd_party_audio** | **bool** | Use TSP for the Webinar. | [optional] 
**has_archiving** | **bool** | Whether the archiving feature was used in the webinar. | [optional] 
**has_pstn** | **bool** | Indicates whether or not PSTN was used for the Webinar. | [optional] 
**has_recording** | **bool** | Indicates whether or not recording was used for the Webinar. | [optional] 
**has_screen_share** | **bool** | Indicates whether or not screen sharing was used for the Webinar. | [optional] 
**has_sip** | **bool** | Indicates whether or not SIP was used for the Webinar. | [optional] 
**has_video** | **bool** | Indicates whether or not video was used for the Webinar. | [optional] 
**has_voip** | **bool** | Indicates whether or not VoIP was used for the Webinar. | [optional] 
**has_manual_captions** | **bool** | Indicates whether a manual caption was enabled in the meeting. | [optional] 
**has_automated_captions** | **bool** | Indicates whether an automated caption was enabled in the meeting. | [optional] 
**id** | **int** | Webinar ID in &amp;quot;**long**&amp;quot; format(represented as int64 data type in JSON), also known as the webinar number. | [optional] 
**participants** | **int** | Webinar participant count. | [optional] 
**start_time** | **datetime** | Webinar start time. | [optional] 
**topic** | **str** | Webinar topic. | [optional] 
**user_type** | **str** | User type. | [optional] 
**uuid** | **str** | Webinar UUID. | [optional] 
**audio_quality** | **str** | The webinar&#x27;s [audio quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts):  * &#x60;good&#x60; &amp;mdash; The audio is almost flawless and the quality is excellent.  * &#x60;fair&#x60; &amp;mdash; The audio occasionally has distortion, noise, and other problems, but the content is basically continuous. Participants can communicate normally.  * &#x60;poor&#x60; &amp;mdash; The audio often has distortion, noise, and other problems, but the content is basically continuous. Participants can communicate normally.  * &#x60;bad&#x60; &amp;mdash; The sound quality is extremely poor and the audio content is almost inaudible. | [optional] 
**video_quality** | **str** | The webinar&#x27;s [video quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts):  * &#x60;good&#x60; &amp;mdash; The video is almost flawless and the quality is excellent.  * &#x60;fair&#x60; &amp;mdash; The video definition is high, occasionally gets stuck, fast or slow, or other problems, but the frequency is very low and the video quality is good.  * &#x60;poor&#x60; &amp;mdash; The video definition is not high, but not many problems exist. The video quality is mediocre.  * &#x60;bad&#x60; &amp;mdash; The picture is very blurred and often gets stuck. | [optional] 
**screen_share_quality** | **str** | The webinar&#x27;s [screen share quality score](https://support.zoom.us/hc/en-us/articles/360061244651-Using-meeting-quality-scores-and-network-alerts):  * &#x60;good&#x60; &amp;mdash; The video is almost flawless and the quality is excellent.  * &#x60;fair&#x60; &amp;mdash; The video definition is high, occasionally gets stuck, fast or slow, or other problems, but the frequency is very low and the video quality is good.  * &#x60;poor&#x60; &amp;mdash; The video definition is not high, but not many problems exist. The video quality is mediocre.  * &#x60;bad&#x60; &amp;mdash; The picture is very blurred and often gets stuck. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

