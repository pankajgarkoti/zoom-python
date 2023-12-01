# InlineResponse20045Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_devices** | **bool** | Allow attendees to join the meeting from multiple devices. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting). | [optional] 
**alternative_hosts** | **str** | A semicolon-separated list of the meeting&#x27;s alternative hosts&#x27; email addresses or IDs. | [optional] 
**alternative_hosts_email_notification** | **bool** | Flag to determine whether to send email notifications to alternative hosts, default value is true. | [optional] [default to True]
**alternative_host_update_polls** | **bool** | Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher. | [optional] 
**approval_type** | **int** | Enable registration and set approval for the registration. Note that this feature requires the host to be of **Licensed** user type. **Registration cannot be enabled for a basic user.**           &#x60;0&#x60; - Automatically approve.    &#x60;1&#x60; - Manually approve.    &#x60;2&#x60; - No registration required. | [optional] [default to Approval_typeEnum._2]
**approved_or_denied_countries_or_regions** | [**InlineResponse20045SettingsApprovedOrDeniedCountriesOrRegions**](InlineResponse20045SettingsApprovedOrDeniedCountriesOrRegions.md) |  | [optional] 
**audio** | **str** | Determine how participants can join the audio portion of the meeting.    &#x60;both&#x60; - Both Telephony and VoIP.    &#x60;telephony&#x60; - Telephony only.    &#x60;voip&#x60; - VoIP only.    &#x60;thirdParty&#x60; - Third party audio conference. | [optional] [default to 'both']
**audio_conference_info** | **str** | Third party audio conference info. | [optional] 
**authentication_domains** | **str** | If user has configured [Sign Into Zoom with Specified Domains](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated. | [optional] 
**authentication_exception** | [**list[InlineResponse20045SettingsAuthenticationException]**](InlineResponse20045SettingsAuthenticationException.md) | The participants added here will receive unique meeting invite links and bypass authentication. | [optional] 
**authentication_name** | **str** | Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f). | [optional] 
**authentication_option** | **str** | Meeting authentication option id. | [optional] 
**auto_recording** | **str** | Automatic recording:    &#x60;local&#x60; - Record on local.    &#x60;cloud&#x60; -  Record on cloud.    &#x60;none&#x60; - Disabled. | [optional] [default to 'none']
**breakout_room** | [**InlineResponse20045SettingsBreakoutRoom**](InlineResponse20045SettingsBreakoutRoom.md) |  | [optional] 
**calendar_type** | **int** | Indicates the type of calendar integration used to schedule the meeting.  * &#x60;1&#x60; - [Zoom Outlook add-in](https://support.zoom.us/hc/en-us/articles/360031592971-Getting-started-with-Outlook-plugin-and-add-in)  * &#x60;2&#x60; - [Zoom for Google Workspace add-on](https://support.zoom.us/hc/en-us/articles/360020187492-Using-the-Zoom-for-Google-Workspace-add-on)  Works with the &#x60;private_meeting&#x60; field to determine whether to share details of meetings or not. | [optional] 
**close_registration** | **bool** | Close registration after event date | [optional] [default to False]
**cn_meeting** | **bool** | Host meeting in China. | [optional] [default to False]
**contact_email** | **str** | Contact email for registration | [optional] 
**contact_name** | **str** | Contact name for registration | [optional] 
**custom_keys** | [**list[MeetingsmeetingIdSettingsCustomKeys]**](MeetingsmeetingIdSettingsCustomKeys.md) | Custom keys and values assigned to the meeting. | [optional] 
**email_notification** | **bool** | Whether to send email notifications to [alternative hosts](https://support.zoom.us/hc/en-us/articles/208220166) and [users with scheduling privileges](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-privilege). This value defaults to &#x60;true&#x60;. | [optional] [default to True]
**encryption_type** | **str** | Choose between enhanced encryption and [end-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871) when starting or a meeting. When using end-to-end encryption, several features (e.g. cloud recording, phone/SIP/H.323 dial-in) will be **automatically disabled**.    &#x60;enhanced_encryption&#x60; - Enhanced encryption. Encryption is stored in the cloud if you enable this option.       &#x60;e2ee&#x60; - [End-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871). The encryption key is stored in your local device and can not be obtained by anyone else. Enabling this setting also **disables** the join before host, cloud recording, streaming, live transcription, breakout rooms, polling, 1:1 private chat, and meeting reactions features. | [optional] 
**enforce_login** | **bool** | Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the &#x60;meeting_authentication&#x60;, &#x60;authentication_option&#x60;, and &#x60;authentication_domains&#x60; fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting. | [optional] 
**enforce_login_domains** | **str** | Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the &#x60;meeting_authentication&#x60;, &#x60;authentication_option&#x60;, and &#x60;authentication_domains&#x60; fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting. | [optional] 
**focus_mode** | **bool** | Whether the [**Focus Mode** feature](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) is enabled when the meeting starts. | [optional] 
**global_dial_in_countries** | **list[str]** | List of global dial-in countries | [optional] 
**global_dial_in_numbers** | [**list[InlineResponse20045SettingsGlobalDialInNumbers]**](InlineResponse20045SettingsGlobalDialInNumbers.md) | Global Dial-in Countries/Regions | [optional] 
**host_video** | **bool** | Start video when the host joins the meeting. | [optional] 
**in_meeting** | **bool** | Host meeting in India. | [optional] [default to False]
**jbh_time** | **int** | If the value of &#x60;join_before_host&#x60; field is set to true, this field can be used to indicate time limits when a participant may join a meeting before a host.  *  &#x60;0&#x60; - Allow participant to join anytime. *  &#x60;5&#x60; - Allow participant to join 5 minutes before meeting start time.  * &#x60;10&#x60; - Allow participant to join 10 minutes before meeting start time. | [optional] 
**join_before_host** | **bool** | Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings. | [optional] [default to False]
**language_interpretation** | [**MeetingsmeetingIdSettingsLanguageInterpretation**](MeetingsmeetingIdSettingsLanguageInterpretation.md) |  | [optional] 
**sign_language_interpretation** | [**MeetingsmeetingIdSettingsSignLanguageInterpretation**](MeetingsmeetingIdSettingsSignLanguageInterpretation.md) |  | [optional] 
**meeting_authentication** | **bool** | &#x60;true&#x60;- Only authenticated users can join meetings. | [optional] 
**mute_upon_entry** | **bool** | Mute participants upon entry. | [optional] [default to False]
**participant_video** | **bool** | Start video when participants join the meeting. | [optional] 
**private_meeting** | **bool** | Whether the meeting is set as private. | [optional] 
**registrants_confirmation_email** | **bool** | Whether to send registrants an email confirmation. * &#x60;true&#x60; - Send a confirmation email. * &#x60;false&#x60; - Do not send a confirmation email. | [optional] 
**registrants_email_notification** | **bool** | Whether to send registrants email notifications about their registration approval, cancellation, or rejection.  * &#x60;true&#x60; - Send an email notification. * &#x60;false&#x60; - Do not send an email notification.   Set this value to &#x60;true&#x60; to also use the &#x60;registrants_confirmation_email&#x60; parameter. | [optional] 
**registration_type** | **int** | Registration type. Used for recurring meeting with fixed time only.   &#x60;1&#x60; Attendees register once and can attend any of the occurrences.    &#x60;2&#x60; Attendees need to register for each occurrence to attend.    &#x60;3&#x60; Attendees register once and can choose one or more occurrences to attend. | [optional] [default to Registration_typeEnum._1]
**show_share_button** | **bool** | Show social share buttons on the meeting registration page. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting). | [optional] 
**use_pmi** | **bool** | Use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time. | [optional] [default to False]
**waiting_room** | **bool** | Enable waiting room | [optional] [default to False]
**watermark** | **bool** | Add watermark when viewing a shared screen. | [optional] [default to False]
**host_save_video_order** | **bool** | Whether the **Allow host to save video order** feature is enabled. | [optional] 
**internal_meeting** | **bool** | Whether to set the meeting as an internal meeting. | [optional] [default to False]
**continuous_meeting_chat** | [**MeetingsmeetingIdSettingsContinuousMeetingChat**](MeetingsmeetingIdSettingsContinuousMeetingChat.md) |  | [optional] 
**participant_focused_meeting** | **bool** | Whether to set the meeting as a participant focused meeting. | [optional] [default to False]
**push_change_to_calendar** | **bool** | Whether to push meeting changes to the calendar.    To enable this feature, configure the **Configure Calendar and Contacts Service** in the user&#x27;s profile page of the Zoom web portal and enable the **Automatically sync Zoom calendar events information bi-directionally between Zoom and integrated calendars.** setting in the **Settings** page of the Zoom web portal. * &#x60;true&#x60; - Push meeting changes to the calendar. * &#x60;false&#x60; - Do not push meeting changes to the calendar. | [optional] [default to False]
**resources** | [**list[MeetingsmeetingIdSettingsResources]**](MeetingsmeetingIdSettingsResources.md) | The meeting&#x27;s resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
