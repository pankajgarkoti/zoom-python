# InlineResponse2009ParticipantAudioFiles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | The URL to download the recording. If a user has authorized and installed your OAuth app that contains recording scopes, use the user&#x27;s [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file, and set the &#x60;access_token&#x60; as a Bearer token in the Authorization header.  &#x60;curl -H &#x27;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&#x27; https://{{base-domain}}/rec/archive/download/xyz&#x60;   **Note:** This field does **not** return for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API will return the &#x60;file_path&#x60; field. | [optional] 
**file_name** | **str** | The recording file&#x27;s name. | [optional] 
**file_path** | **str** | The file path to the on-premise account recording.   **Note:** This API only returns this field for [Zoom on-premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the &#x60;download_url&#x60; field. | [optional] 
**file_size** | **float** | The recording file&#x27;s size, in bytes. | [optional] 
**file_type** | **str** | The recording file&#x27;s format.   * &#x60;MP4&#x60; - Video file. * &#x60;M4A&#x60; - Audio-only file. * &#x60;TIMELINE&#x60; - Timestamp file of the recording, in JSON file format. To get a timeline file, the **Add a timestamp to the recording** setting **must** be enabled in the [recording settings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-recording#h_3f14c3a4-d16b-4a3c-bbe5-ef7d24500048). The time will display in the host&#x27;s timezone. * &#x60;TRANSCRIPT&#x60; - A transcript of the recording, in VTT format. * &#x60;CHAT&#x60; - A text file containing chat messages sent during the meeting. * &#x60;CC&#x60; - A file containing the closed captions of the recording, in VTT file format. * &#x60;CSV&#x60; - A file containing polling data, in CSV format.  A recording file object with file the &#x60;CC&#x60; or &#x60;TIMELINE&#x60; value **does not** have the &#x60;id&#x60;, &#x60;status&#x60;, &#x60;file_size&#x60;, &#x60;recording_type&#x60;, and &#x60;play_url&#x60; properties. | [optional] 
**id** | **str** | The recording file&#x27;s unique ID. This is included in the general query response. | [optional] 
**play_url** | **str** | The URL where the recording file can be opened and played. | [optional] 
**recording_end** | **datetime** | The recording file&#x27;s end time. This is included in the general query response. | [optional] 
**recording_start** | **datetime** | The recording file&#x27;s start time. | [optional] 
**status** | **str** | The recording file&#x27;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

