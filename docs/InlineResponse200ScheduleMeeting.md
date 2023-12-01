# InlineResponse200ScheduleMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_type** | **bool** | Determine how participants can join the audio portion of the meeting. | [optional] 
**embed_password_in_join_link** | **bool** | If the value is set to &#x60;true&#x60;, the meeting passcode will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the passcode.   | [optional] 
**enforce_login** | **bool** | Allow only signed-in users to join meetings.  | [optional] 
**enforce_login_domains** | **str** | Specify the domains from which users can join a meeting.  | [optional] 
**enforce_login_with_domains** | **bool** | Allow only signed-in users with specified domains to join meetings.  | [optional] 
**host_video** | **bool** | Start meetings with host video on. | [optional] 
**join_before_host** | **bool** | Allow participants to join the meeting before the host arrives | [optional] 
**meeting_authentication** | **bool** | Only authenticated users can join meetings | [optional] 
**not_store_meeting_topic** | **bool** | Whether to enable the [**Always display &amp;quot;Zoom Meeting&amp;quot; as the meeting topic**](https://support.zoom.us/hc/en-us/articles/201363253-Changing-account-settings#h_01EG9BJ646V2WJK1S3H2MP6YV6) setting. | [optional] 
**always_display_zoom_webinar_as_topic** | **bool** | Whether to enable the [**Always show &amp;quot;Zoom Webinar&amp;quot; as the webinar topic**](https://support.zoom.us/hc/en-us/articles/201363253-Changing-account-settings#h_01EG9BJ646V2WJK1S3H2MP6YV6) setting. | [optional] 
**participant_video** | **bool** | Start meetings with participant video on. | [optional] 
**require_password_for_instant_meetings** | **bool** | Require passcode for instant meetings. If you use a PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**require_password_for_pmi_meetings** | **bool** | Require participants to enter passcode for PMI meetings. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**require_password_for_scheduling_new_meetings** | **bool** | This setting applies for regular meetings that do not use a PMI. If enabled, a passcode will be generated while a host schedules a new meeting and participants will be required to enter the passcode before they can join the meeting. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**use_pmi_for_instant_meetings** | **bool** | Use a Personal Meeting ID (PMI) when starting an instant meeting. | [optional] 
**use_pmi_for_scheduled_meetings** | **bool** | Use a Personal Meeting ID (PMI) when scheduling a meeting. | [optional] 
**continuous_meeting_chat** | **bool** | Whether to enable the [**Enable continuous meeting chat**] setting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

