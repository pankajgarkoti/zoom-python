# GroupsgroupIdsettingsScheduleMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_type** | **str** | Determine how participants can join the audio portion of the meeting. | [optional] 
**embed_password_in_join_link** | **bool** | If the value is set to &#x60;true&#x60;, the meeting passcode will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the passcode.   | [optional] 
**force_pmi_jbh_password** | **bool** | If join before host option is enabled for a personal meeting, then enforce passcode requirement. | [optional] 
**host_video** | **bool** | Start meetings with host video on. | [optional] 
**join_before_host** | **bool** | Allow participants to join the meeting before the host arrives | [optional] 
**mute_upon_entry** | **bool** | Automatically mute all participants when they join the meeting. | [optional] 
**participant_video** | **bool** | Start meetings with participant video on. | [optional] 
**pstn_password_protected** | **bool** | Generate and send new passcodes for newly scheduled or edited meetings. | [optional] 
**require_password_for_all_meetings** | **bool** | Require passcode from all participants before joining a meeting. | [optional] 
**require_password_for_instant_meetings** | **bool** | If enabled, a random passcode will be generated on the user&#x27;s end who starts the instant meeting. Other participants will have to enter the passcode to join the meeting. If you use PMI for your instant meetings, this option will be disabled. | [optional] 
**require_password_for_pmi_meetings** | **str** | Indicates whether a passcode is required for [PMI](https://support.zoom.us/hc/en-us/articles/203276937-Using-Personal-Meeting-ID-PMI-) meetings or not. The value can be one of the following:     &#x60;none&#x60;: Do not require passcode for PMI meetings.      &#x60;all&#x60;: Require participants to enter passcode for all PMI enabled meetings.     &#x60;jbh_only&#x60;: Require passcode only for meetings where the **join before host** setting is enabled. | [optional] 
**require_password_for_scheduled_meetings** | **bool** | Require a passcode for meetings which have already been scheduled.  | [optional] 
**require_password_for_scheduling_new_meetings** | **bool** | This setting applies for regular meetings that do not use PMI. If enabled, a passcode will be generated while a host schedules a new meeting and participants will be required to enter the passcode before they can join the meeting.  | [optional] 
**upcoming_meeting_reminder** | **bool** | Receive desktop notification for upcoming meetings. | [optional] 
**always_display_zoom_meeting_as_topic** | [**GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomMeetingAsTopic**](GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomMeetingAsTopic.md) |  | [optional] 
**always_display_zoom_webinar_as_topic** | [**GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomWebinarAsTopic**](GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomWebinarAsTopic.md) |  | [optional] 
**continuous_meeting_chat** | [**AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat**](AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

