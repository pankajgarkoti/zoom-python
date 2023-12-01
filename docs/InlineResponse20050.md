# InlineResponse20050

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meeting_host_id** | **str** | The ID of the user who is set as the meeting host. | [optional] 
**meeting_host_email** | **str** | The meeting host&#x27;s email address. | [optional] 
**meeting_uuid** | **str** | The unique meeting ID.   Each meeting instance generates its own meeting UUID. After a meeting ends, a new UUID is generated for the next instance of the meeting.   Use the [**List past meeting instances**](/docs/api-reference/zoom-api/methods#operation/pastMeetings) API to retrieve a list of UUIDs from past meeting instances. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a &#x60;/&#x60; or contains &#x60;//&#x60; in it.  | [optional] 
**meeting_id** | **int** | [ The meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-)  The meeting&#x27;s unique identifier in **long** format, represented as int64 data type in JSON. Also known as the meeting number. | [optional] 
**meeting_topic** | **str** | The meeting topic. | [optional] 
**meeting_start_time** | **datetime** | The meeting&#x27;s start date and time. | [optional] 
**meeting_end_time** | **datetime** | The meeting&#x27;s end date and time. | [optional] 
**summary_start_time** | **datetime** | The summary&#x27;s start date and time. | [optional] 
**summary_end_time** | **datetime** | The summary&#x27;s end date and time. | [optional] 
**summary_created_time** | **datetime** | The date and time when the meeting summary was created. | [optional] 
**summary_last_modified_time** | **datetime** | The date and time when the meeting summary was last modified. | [optional] 
**summary_title** | **str** | The summary title. | [optional] 
**summary_overview** | **str** | The summary overview. | [optional] 
**summary_details** | [**list[InlineResponse20050SummaryDetails]**](InlineResponse20050SummaryDetails.md) | The summary content details. | [optional] 
**next_steps** | **list[str]** | The next steps. | [optional] 
**edited_summary** | [**InlineResponse20050EditedSummary**](InlineResponse20050EditedSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

