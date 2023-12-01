# InlineResponse20012RecordingFiles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_time** | **str** | The time when recording was deleted. Returned in the response only for trash query. | [optional] 
**download_url** | **str** | The URL to download the recording.   **OAuth apps**   If a user has authorized and installed your OAuth app that contains recording scopes, use the user&#x27;s [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file, and set the access_token as a Bearer token in the Authorization header.   &#x60;curl -H &#x27;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&#x27; https://{{base-domain}}/rec/archive/download/xyz&#x60;.   **Note:** This field does **not** return for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API will return the &#x60;file_path&#x60; field. | [optional] 
**file_path** | **str** | The file path to the On-Premise account recording.   **Note:** This API only returns this field for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the &#x60;download_url&#x60; field. | [optional] 
**file_size** | **float** | The recording file size. | [optional] 
**file_type** | **str** | The recording file type.     &#x60;MP4&#x60; - Video file of the recording.    &#x60;M4A&#x60; Audio-only file of the recording.    &#x60;TIMELINE&#x60; - Timestamp file of the recording in JSON file format. To get a timeline file, the &amp;quot;Add a timestamp to the recording&amp;quot; setting must be enabled in the [recording settings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-recording#h_3f14c3a4-d16b-4a3c-bbe5-ef7d24500048). The time will display in the host&#x27;s timezone, set on their Zoom profile.      &#x60;TRANSCRIPT&#x60; - Transcription file of the recording in VTT format.     &#x60;CHAT&#x60; - A TXT file containing in-meeting chat messages that were sent during the meeting.    &#x60;CC&#x60; - File containing closed captions of the recording in VTT file format.    &#x60;CSV&#x60; - File containing polling data in CSV format.        A recording file object with file type of either &#x60;CC&#x60; or &#x60;TIMELINE&#x60; **does not have** the following properties:      &#x60;id&#x60;, &#x60;status&#x60;, &#x60;file_size&#x60;, &#x60;recording_type&#x60;, and &#x60;play_url&#x60;.    &#x60;SUMMARY&#x60; - Summary file of the recording in JSON file format. | [optional] 
**file_extension** | **str** | The file extension type of the recording file. | [optional] 
**id** | **str** | The recording file ID. Included in the response of general query. | [optional] 
**meeting_id** | **str** | The meeting ID.  | [optional] 
**play_url** | **str** | The URL to play a recording file. | [optional] 
**recording_end** | **str** | The recording end time. Response in general query. | [optional] 
**recording_start** | **str** | The recording start time. | [optional] 
**recording_type** | **str** | The recording type.    &#x60;shared_screen_with_speaker_view(CC)&#x60;    &#x60;shared_screen_with_speaker_view&#x60;    &#x60;shared_screen_with_gallery_view&#x60;    &#x60;speaker_view&#x60;    &#x60;gallery_view&#x60;    &#x60;shared_screen&#x60;    &#x60;audio_only&#x60;    &#x60;audio_transcript&#x60;    &#x60;chat_file&#x60;    &#x60;active_speaker&#x60;    &#x60;poll&#x60;    &#x60;timeline&#x60;    &#x60;closed_caption&#x60;    &#x60;audio_interpretation&#x60;    &#x60;summary&#x60;    &#x60;summary_next_steps&#x60;    &#x60;summary_smart_chapters&#x60;    &#x60;sign_interpretation&#x60;    &#x60;production_studio&#x60; | [optional] 
**status** | **str** | The recording status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

