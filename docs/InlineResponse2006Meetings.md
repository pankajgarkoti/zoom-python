# InlineResponse2006Meetings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | The user&#x27;s account name. | 
**archive_files** | [**list[InlineResponse2006ArchiveFiles]**](InlineResponse2006ArchiveFiles.md) | Information about the archive files. | 
**complete_time** | **AnyOfinlineResponse2006MeetingsCompleteTime** | The meeting or webinar&#x27;s archive completion time. | 
**duration** | **int** | The meeting or webinar&#x27;s scheduled duration. | 
**duration_in_second** | **int** | The meeting or webinar&#x27;s duration, in seconds. | 
**host_id** | **str** | The ID of the user set as the host of the archived meeting or webinar. | 
**id** | **int** | The meeting or webinar ID, either &#x60;meetingId&#x60; or &#x60;webinarId&#x60;. | 
**is_breakout_room** | **bool** | Whether the room is a [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms). | 
**meeting_type** | **str** | Whether the meeting or webinar is internal or external.  * &#x60;internal&#x60; - An internal meeting or webinar.  * &#x60;external&#x60; - An external meeting or webinar.    The &#x60;id&#x60;, &#x60;host_id&#x60;, and &#x60;topic&#x60; PII (Personal Identifiable Information) values in this response are removed when this value is &#x60;external&#x60;. | 
**parent_meeting_id** | **str** | The parent meeting&#x27;s universally unique ID (UUID). Each meeting or webinar instance generates a UUID. If the &#x60;is_breakout_room&#x60; value is &#x60;true&#x60;, the API returns this value. | [optional] 
**recording_count** | **int** | The number of archived files returned in the API call response. | 
**start_time** | **datetime** | The meeting or webinar&#x27;s start time. | 
**timezone** | **str** | The meeting or webinar&#x27;s [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones). | 
**topic** | **str** | The meeting or webinar topic. | 
**total_size** | **int** | The total size of the archive file, in bytes. | 
**type** | **int** | The type of archived meeting or webinar.    Meeting recordings use these archive types.  * &#x60;1&#x60; - Instant meeting.  * &#x60;2&#x60; - Scheduled meeting.  * &#x60;3&#x60; - A recurring meeting with no fixed time.  * &#x60;4&#x60; - A meeting created via PMI (Personal Meeting ID).  * &#x60;7&#x60; - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * &#x60;8&#x60; - Recurring meeting with a fixed time.    Webinar recordings use these archive types.  * &#x60;5&#x60; - A webinar.  * &#x60;6&#x60; - A recurring webinar without a fixed time.  * &#x60;9&#x60; - A recurring webinar with a fixed time.    If the recording is **not** from a meeting or webinar:   * &#x60;100&#x60; - A [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms). | 
**uuid** | **str** | The recorded meeting or webinar instance&#x27;s universally unique identifier (UUID). Each meeting or webinar instance generates a UUID. | 
**status** | **str** | The archive&#x27;s processing status.  * &#x60;completed&#x60; - The archive&#x27;s processing is complete.  * &#x60;processing&#x60; - The archive is processing. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

