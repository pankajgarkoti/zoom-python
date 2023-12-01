# InlineResponse2008ArchiveFiles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | The URL to download the the archive file.    **OAuth apps**    If a user has authorized and installed your OAuth app that contains recording scopes, use the user&#x27;s [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file. For example:    &#x60;https://{{base-domain}}/rec/archive/download/xxx--header &#x27;Authorization: Bearer {{OAuth-access-token}}&#x27;&#x60;    **Note:** This field does **not** return for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API will return the &#x60;file_path&#x60; field. | 
**file_extension** | **str** | The archived file&#x27;s extension. | 
**file_path** | **str** | The file path to the on-premise account archive file.    **Note:** The API only returns this field for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the &#x60;download_url&#x60; field. | [optional] 
**file_size** | **int** | The archived file&#x27;s size, in bytes. | 
**file_type** | **str** | The archive file&#x27;s type.  * &#x60;MP4&#x60; - Video file.  * &#x60;M4A&#x60; - Audio-only file.  * &#x60;CHAT&#x60; - A TXT file containing in-meeting chat messages.  * &#x60;CC&#x60; - A file containing the closed captions of the recording, in VTT file format.  * &#x60;CHAT_MESSAGE&#x60; - A JSON file encoded in base64 format containing chat messages. The file also includes waiting room chats, deleted messages, meeting emojis and non-verbal feedback. | 
**id** | **str** | The archive file&#x27;s unique ID. | 
**individual** | **bool** | Whether the archive file is an individual recording file.  * &#x60;true&#x60; - An individual recording file.   * &#x60;false&#x60; - An entire meeting file. | 
**participant_email** | **str** | The individual recording file&#x27;s participant email address. This value is returned when the &#x60;individual&#x60; value is &#x60;true&#x60;. If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details. | [optional] 
**participant_join_time** | **datetime** | The join time for the generated recording file. If this value is returned when the individual value is true, then it is the recording file&#x27;s participant join time. When the individual value is false, it returns the join time for the archiving gateway. | 
**participant_leave_time** | **datetime** | The leave time for the generated recording file. If this value is returned when the individual value is true, then it is the recording file&#x27;s participant leave time. When the individual value is false, it returns the leave time for the archiving gateway. | 
**recording_type** | **str** | The archive file&#x27;s recording type.  * &#x60;shared_screen_with_speaker_view&#x60;  * &#x60;audio_only&#x60;  * &#x60;chat_file&#x60;  * &#x60;closed_caption&#x60;  * &#x60;chat_message&#x60;    For more information, read our [Managing and sharing cloud recordings](https://support.zoom.us/hc/en-us/articles/205347605-Managing-and-sharing-cloud-recordings#h_9898497b-e736-4980-a749-d55608f10773) documentation. | 
**status** | **str** | The archived file&#x27;s processing status.  * &#x60;completed&#x60; - The processing of the file is complete.  * &#x60;processing&#x60; - The file is processing.  * &#x60;failed&#x60; - The processing of the file failed. | 
**encryption_fingerprint** | **str** | The archived file&#x27;s encryption fingerprint, using the SHA256 hash algorithm. | 
**number_of_messages** | **int** | The number of &#x60;TXT&#x60; or &#x60;JSON&#x60; file messages. This field returns only when the &#x60;file_extension&#x60; is &#x60;JSON&#x60; or &#x60;TXT&#x60; | [optional] 
**storage_location** | **str** | The region where the file is stored. This field returns only &#x60;Enable Distributed Compliance Archiving&#x60; op feature is enabled. | [optional] 
**auto_delete** | **bool** | Whether to auto delete the archived file.   **Prerequisites:**   * The \&quot;Tag Archiving Files for Deletion\&quot; feature must be enabled in OP. Contact [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to open.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

