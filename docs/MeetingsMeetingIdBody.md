# MeetingsMeetingIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agenda** | **str** | Meeting description. | [optional] 
**duration** | **int** | Meeting duration in minutes. Used for scheduled meetings only. | [optional] 
**password** | **str** | Meeting passcode. Passcodes may only contain these characters [a-z A-Z 0-9 @ - _ *] and can have a maximum of 10 characters.  **Note** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, view those requirements by calling either the [**Get user settings**](/docs/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/docs/api-reference/zoom-api/ma#operation/accountSettings) API. | [optional] 
**pre_schedule** | **bool** | Whether to create a prescheduled meeting through the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting &#x60;type&#x60; value of &#x60;2&#x60; - scheduled meetings- and &#x60;3&#x60; - recurring meetings with no fixed time.  * &#x60;true&#x60; - Create a prescheduled meeting.  * &#x60;false&#x60; - Create a regular meeting. | [optional] [default to False]
**schedule_for** | **str** | The email address or &#x60;userId&#x60; of the user to schedule a meeting for. | [optional] 
**recurrence** | [**MeetingsmeetingIdRecurrence**](MeetingsmeetingIdRecurrence.md) |  | [optional] 
**settings** | [**MeetingsmeetingIdSettings**](MeetingsmeetingIdSettings.md) |  | [optional] 
**start_time** | **datetime** | Meeting start time. When using a format like &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;&#x60;, always use GMT time. When using a format like &#x60;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x60;, use local time and specify the time zone. Only used for scheduled meetings and recurring meetings with a fixed time. | [optional] 
**template_id** | **str** | Unique identifier of the meeting template.   [Schedule the meeting from a meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates#h_86f06cff-0852-4998-81c5-c83663c176fb). Retrieve this field&#x27;s value by calling the [List meeting templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listMeetingTemplates) API. | [optional] 
**timezone** | **str** | The timezone to assign to the &#x60;start_time&#x60; value. Only use this field ifor scheduled or recurring meetings with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones). | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**tracking_fields** | [**list[MeetingsmeetingIdTrackingFields]**](MeetingsmeetingIdTrackingFields.md) | Tracking fields. | [optional] 
**type** | **int** | Meeting types.  &#x60;1&#x60; - Instant meeting.    &#x60;2&#x60; - Scheduled meeting.    &#x60;3&#x60; - Recurring meeting with no fixed time.    &#x60;8&#x60; - Recurring meeting with a fixed time. | [optional] [default to TypeEnum._2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

