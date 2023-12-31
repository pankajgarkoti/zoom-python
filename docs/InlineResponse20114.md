# InlineResponse20114

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant_id** | **str** | The ID of the user who scheduled this meeting on behalf of the host. | [optional] 
**host_email** | **str** | The meeting host&#x27;s email address. | [optional] 
**id** | **int** | The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**registration_url** | **str** | The URL that registrants can use to register for a meeting. This field is only returned for meetings that have enabled registration. | [optional] 
**agenda** | **str** | Agenda | [optional] 
**created_at** | **datetime** | The date and time when this meeting was created. | [optional] 
**duration** | **int** | The meeting duration. | [optional] 
**h323_password** | **str** | H.323/SIP room system passcode | [optional] 
**join_url** | **str** | URL for participants to join the meeting. This URL should only be shared with users that you would like to invite for the meeting. | [optional] 
**chat_join_url** | **str** | The URL to join the chat. | [optional] 
**occurrences** | [**list[InlineResponse20122Occurrences]**](InlineResponse20122Occurrences.md) | Array of occurrence objects. | [optional] 
**password** | **str** | The meeting passcode. This passcode may only contain these characters: &#x60;[a-z A-Z 0-9 @ - _ * !]&#x60;  If **Require a passcode when scheduling new meetings** setting has been enabled and [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated in the response even if it is not provided in the API request.     | [optional] 
**pmi** | **str** | [Personal meeting ID (PMI)](/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time. | [optional] 
**pre_schedule** | **bool** | Whether the prescheduled meeting was created via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This only supports the meeting &#x60;type&#x60; value of &#x60;2&#x60; (scheduled meetings) and &#x60;3&#x60; (recurring meetings with no fixed time).  * &#x60;true&#x60; - A GSuite prescheduled meeting.  * &#x60;false&#x60; - A regular meeting. | [optional] [default to False]
**recurrence** | [**InlineResponse20114Recurrence**](InlineResponse20114Recurrence.md) |  | [optional] 
**settings** | [**InlineResponse20114Settings**](InlineResponse20114Settings.md) |  | [optional] 
**start_time** | **datetime** | Meeting start date-time in UTC/GMT, such as &#x60;2020-03-31T12:02:00Z&#x60;. | [optional] 
**start_url** | **str** | URL to start the meeting. This URL should only be used by the host of the meeting and **should not be shared with anyone other than the host** of the meeting, since anyone with this URL will be able to log in to the Zoom Client as the host of the meeting. | [optional] 
**timezone** | **str** | Timezone to format &#x60;start_time&#x60;. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**tracking_fields** | [**list[InlineResponse20114TrackingFields]**](InlineResponse20114TrackingFields.md) | Tracking fields. | [optional] 
**type** | **int** | Meeting type. | [optional] [default to TypeEnum._2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

