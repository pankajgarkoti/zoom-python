# InlineResponse20012Meetings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique Identifier of the user account. | [optional] 
**duration** | **int** | Meeting duration. | [optional] 
**host_id** | **str** | ID of the user set as host of meeting. | [optional] 
**id** | **int** | Meeting ID - also known as the meeting number. | [optional] 
**recording_count** | **int** | Number of recording files returned in the response of this API call. This includes the &#x60;recording_files&#x60; and  &#x60;participant_audio_files&#x60; files. | [optional] 
**start_time** | **datetime** | The time when the meeting started. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**total_size** | **int** | The total file size of the recording. This includes the &#x60;recording_files&#x60; and &#x60;participant_audio_files&#x60; files. | [optional] 
**type** | **str** | The recording&#x27;s associated type of meeting or webinar:   If the recording is of a meeting:  * &#x60;1&#x60; &amp;mdash; Instant meeting.  * &#x60;2&#x60; &amp;mdash; Scheduled meeting.  * &#x60;3&#x60; &amp;mdash; A recurring meeting with no fixed time.  * &#x60;4&#x60; &amp;mdash; A meeting created via PMI (Personal Meeting ID).  * &#x60;7&#x60; &amp;mdash; A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * &#x60;8&#x60; - Recurring meeting with a fixed time.   If the recording is of a webinar:  * &#x60;5&#x60; &amp;mdash; A webinar.  * &#x60;6&#x60; &amp;mdash; A recurring webinar without a fixed time  * &#x60;9&#x60; &amp;mdash; A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * &#x60;99&#x60; &amp;mdash; A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal. | [optional] 
**uuid** | **str** | Unique Meeting Identifier. Each instance of the meeting will have its own UUID. | [optional] 
**recording_play_passcode** | **str** | The cloud recording&#x27;s passcode to be used in the URL. This recording&#x27;s passcode can be directly spliced in &#x60;play_url&#x60; or &#x60;share_url&#x60; with &#x60;?pwd&#x3D;&#x60; to access and play. For example, &#x27;https://zoom.us/rec/share/**************?pwd&#x3D;yNYIS408EJygs7rE5vVsJwXIz4-VW7MH&#x27;. If you want to use this field, please contact Zoom support. | [optional] 
**recording_files** | [**list[InlineResponse20012RecordingFiles]**](InlineResponse20012RecordingFiles.md) | List of recording file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

