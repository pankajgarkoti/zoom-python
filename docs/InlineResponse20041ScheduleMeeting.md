# InlineResponse20041ScheduleMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_type** | **str** | Determine how participants can join the audio portion of the meeting. | [optional] 
**embed_password_in_join_link** | **bool** | If the value is set to &#x60;true&#x60;, the meeting passcode will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the passcode.   | [optional] 
**force_pmi_jbh_password** | **bool** | If join before host option is enabled for a personal meeting, then enforce passcode requirement.   **This field will be deprecated in near future.** If you would like to enable this setting, we highly encourage you to use the &#x60;require_password_for_pmi_meetings&#x60; field.   | [optional] 
**host_video** | **bool** | Start meetings with host video on. | [optional] 
**join_before_host** | **bool** | Allow participants to join the meeting before the host arrives. | [optional] 
**mute_upon_entry** | **bool** | Automatically mute all participants when they join the meeting. | [optional] 
**participant_video** | **bool** | Start meetings with participant video on. | [optional] 
**personal_meeting** | **bool** | Personal meeting setting.    n  &#x60;true&#x60; - Indicates that the **Enable Personal Meeting ID** setting is turned on. Users can choose to use personal meeting ID for their meetings.          &#x60;false&#x60; - Indicates that the **Enable Personal Meeting ID** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **Elevate to Zoom Meeting** on desk phone will be disabled.    | [optional] 
**pstn_password_protected** | **bool** | Generate and send new passcodes for newly scheduled or edited meetings. | [optional] 
**require_password_for_instant_meetings** | **bool** | If enabled, a random passcode will be generated on the user&#x27;s end who starts the instant meeting. Other participants will have to enter the password to join the meeting. If you use PMI for your instant meetings, this option will be disabled. | [optional] 
**require_password_for_pmi_meetings** | **str** | Indicates whether a passcode is required for [PMI](https://support.zoom.us/hc/en-us/articles/203276937-Using-Personal-Meeting-ID-PMI-) meetings or not.    &#x60;none&#x60; - Do not require password for PMI meetings.      &#x60;all&#x60; - Require participants to enter password for all PMI enabled meetings.     &#x60;jbh_only&#x60; - Require password only for meetings where the **join before host** setting is enabled. | [optional] 
**require_password_for_scheduled_meetings** | **bool** | Require a passcode for meetings which have already been scheduled  | [optional] 
**require_password_for_scheduling_new_meetings** | **bool** | This setting applies for regular meetings that do not use PMI. If enabled, a password will be generated while a host schedules a new meeting and participants will be required to enter the password before they can join the meeting. | [optional] 
**upcoming_meeting_reminder** | **bool** | Receive desktop notification for upcoming meetings. | [optional] 
**use_pmi_for_instant_meetings** | **bool** | Indicates whether PMI is enabled for all instant meetings or not. | [optional] 
**use_pmi_for_schedule_meetings** | **bool** | Indicates whether PMI is enabled for all scheduled meetings or not. | [optional] 
**always_display_zoom_meeting_as_topic** | [**InlineResponse20041ScheduleMeetingAlwaysDisplayZoomMeetingAsTopic**](InlineResponse20041ScheduleMeetingAlwaysDisplayZoomMeetingAsTopic.md) |  | [optional] 
**always_display_zoom_webinar_as_topic** | [**InlineResponse20041ScheduleMeetingAlwaysDisplayZoomWebinarAsTopic**](InlineResponse20041ScheduleMeetingAlwaysDisplayZoomWebinarAsTopic.md) |  | [optional] 
**continuous_meeting_chat** | [**AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat**](AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

