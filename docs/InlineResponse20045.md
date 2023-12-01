# InlineResponse20045

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant_id** | **str** | The ID of the user who scheduled this meeting on behalf of the host. | [optional] 
**host_email** | **str** | The meeting host&#x27;s email address. | [optional] 
**host_id** | **str** | The ID of the user who is set as the meeting host. | [optional] 
**id** | **int** | [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format, represented as int64 data type in JSON, also known as the meeting number. | [optional] 
**uuid** | **str** | Unique meeting ID. Each meeting instance generates its own meeting UUID - after a meeting ends, a new UUID is generated for the next instance of the meeting. Retrieve a list of UUIDs from past meeting instances using the [**List past meeting instances**](/docs/api-reference/zoom-api/methods#operation/pastMeetings) API. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a &#x60;/&#x60; or contains &#x60;//&#x60; in it.  | [optional] 
**agenda** | **str** | The meeting description. | [optional] 
**created_at** | **datetime** | The creation time.  | [optional] 
**duration** | **int** | The meeting duration. | [optional] 
**encrypted_password** | **str** | Encrypted passcode for third party endpoints (H323/SIP). | [optional] 
**h323_password** | **str** | H.323/SIP room system passcode. | [optional] 
**join_url** | **str** | The URL for participants to join the meeting. This URL should only be shared with users invited to the meeting. | [optional] 
**chat_join_url** | **str** | The URL to join the chat. | [optional] 
**occurrences** | [**list[InlineResponse20045Occurrences]**](InlineResponse20045Occurrences.md) | Array of occurrence objects. | [optional] 
**password** | **str** | Meeting passcode. | [optional] 
**pmi** | **str** | [Personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time. | [optional] 
**pre_schedule** | **bool** | Whether the prescheduled meeting was created via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting &#x60;type&#x60; value of &#x60;2&#x60; (scheduled meetings) and &#x60;3&#x60; (recurring meetings with no fixed time):  * &#x60;true&#x60; - A GSuite prescheduled meeting.  * &#x60;false&#x60; - A regular meeting. | [optional] [default to False]
**recurrence** | [**InlineResponse20045Recurrence**](InlineResponse20045Recurrence.md) |  | [optional] 
**settings** | [**InlineResponse20045Settings**](InlineResponse20045Settings.md) |  | [optional] 
**start_time** | **datetime** | Meeting start time in GMT or UTC. Start time will not be returned if the meeting is an **instant** meeting.   | [optional] 
**start_url** | **str** | The &#x60;start_url&#x60; of a meeting is a URL that a host or an alternative host can start the meeting.   The expiration time for the &#x60;start_url&#x60; field listed in the response of the [**Create a meeting**](/docs/api-reference/zoom-api/methods#operation/meetingCreate) API is two hours for all regular users.    For users created using the &#x60;custCreate&#x60; option via the [**Create users**](/docs/api-reference/zoom-api/methods#operation/userCreate) API, the expiration time of the &#x60;start_url&#x60; field is 90 days.   For security reasons, to retrieve the updated value for the &#x60;start_url&#x60; field programmatically after the expiry time, you must call the [**Get a meeting](/docs/api-reference/zoom-api/methods#operation/meeting) API and refer to the value of the &#x60;start_url&#x60; field in the response.    This URL should only be used by the host of the meeting and **should not be shared with anyone other than the host** of the meeting as anyone with this URL will be able to login to the Zoom Client as the host of the meeting. | [optional] 
**status** | **str** | Meeting status | [optional] 
**timezone** | **str** | The timezone to format the meeting start time. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**tracking_fields** | [**list[InlineResponse20045TrackingFields]**](InlineResponse20045TrackingFields.md) | Tracking fields. | [optional] 
**type** | **int** | Meeting types.   &#x60;1&#x60; - Instant meeting.    &#x60;2&#x60; - Scheduled meeting.    &#x60;3&#x60; - Recurring meeting with no fixed time.    &#x60;4&#x60; - PMI Meeting     &#x60;8&#x60; - Recurring meeting with a fixed time. | [optional] [default to TypeEnum._2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

