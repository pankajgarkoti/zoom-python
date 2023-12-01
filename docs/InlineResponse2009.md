# InlineResponse2009

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The user account&#x27;s unique identifier. | [optional] 
**duration** | **int** | The meeting duration. | [optional] 
**host_id** | **str** | The ID of the user set as host of meeting. | [optional] 
**id** | **int** | The meeting ID, also known as the meeting number. | [optional] 
**recording_count** | **int** |  The number of recording files returned in the response of this API call. This includes the &#x60;recording_files&#x60; and  &#x60;participant_audio_files&#x60; files. | [optional] 
**start_time** | **datetime** | The time when the meeting started. | [optional] 
**topic** | **str** | The meeting topic. | [optional] 
**total_size** | **int** | The recording&#x27;s total file size. This includes the &#x60;recording_files&#x60; and &#x60;participant_audio_files&#x60; files. | [optional] 
**type** | **str** | The recording&#x27;s associated type of meeting or webinar.   If the recording is of a meeting:  * &#x60;1&#x60; - Instant meeting.  * &#x60;2&#x60; - Scheduled meeting.  * &#x60;3&#x60; - A recurring meeting with no fixed time.  * &#x60;4&#x60; - A meeting created via PMI (Personal Meeting ID).  * &#x60;7&#x60; - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * &#x60;8&#x60; - Recurring meeting with a fixed time.   If the recording is of a webinar:  * &#x60;5&#x60; - A webinar.  * &#x60;6&#x60; - A recurring webinar without a fixed time  * &#x60;9&#x60; - A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * &#x60;99&#x60; - A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal. | [optional] 
**uuid** | **str** | The unique meeting identifier. Each instance of the meeting has its own UUID. | [optional] 
**recording_play_passcode** | **str** | The cloud recording&#x27;s passcode to be used in the URL. Directly splice this recording&#x27;s passcode in &#x60;play_url&#x60; or &#x60;share_url&#x60; with &#x60;?pwd&#x3D;&#x60; to access and play. Example: &#x27;https://zoom.us/rec/share/**************?pwd&#x3D;yNYIS408EJygs7rE5vVsJwXIz4-VW7MH&#x27;. | [optional] 
**recording_files** | [**list[InlineResponse2009RecordingFiles]**](InlineResponse2009RecordingFiles.md) | The list of recording file. | [optional] 
**download_access_token** | **str** | The JWT token to download the meeting&#x27;s recording. This response only returns if the &#x60;download_access_token&#x60; is included in the &#x60;include_fields&#x60; query parameter. | [optional] 
**password** | **str** | The cloud recording&#x27;s passcode. | [optional] 
**participant_audio_files** | [**list[InlineResponse2009ParticipantAudioFiles]**](InlineResponse2009ParticipantAudioFiles.md) | A list of recording files. The API only returns this response when the **Record a separate audio file of each participant** setting is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

