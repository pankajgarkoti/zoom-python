# InlineResponse20122Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_devices** | **bool** | Allow attendees to join from multiple devices. | [optional] 
**alternative_hosts** | **str** | Alternative host emails or IDs. Multiple values separated by comma. | [optional] 
**alternative_host_update_polls** | **bool** | Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher. | [optional] 
**approval_type** | **int** | &#x60;0&#x60; - Automatically approve.    &#x60;1&#x60; - Manually approve.    &#x60;2&#x60; - No registration required. | [optional] [default to Approval_typeEnum._2]
**attendees_and_panelists_reminder_email_notification** | [**WebinarswebinarIdSettingsAttendeesAndPanelistsReminderEmailNotification**](WebinarswebinarIdSettingsAttendeesAndPanelistsReminderEmailNotification.md) |  | [optional] 
**audio** | **str** | Determine how participants can join the audio portion of the webinar. | [optional] [default to 'both']
**audio_conference_info** | **str** | Third party audio conference info. | [optional] 
**authentication_domains** | **str** | If user has configured [**Sign Into Zoom with Specified Domains**](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated. | [optional] 
**authentication_name** | **str** | Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f). | [optional] 
**authentication_option** | **str** | Webinar authentication option ID. | [optional] 
**auto_recording** | **str** | Automatic recording.   &#x60;local&#x60; - Record on local.    &#x60;cloud&#x60; -  Record on cloud.    &#x60;none&#x60; - Disabled. | [optional] [default to 'none']
**close_registration** | **bool** | Close registration after event date. | [optional] 
**contact_email** | **str** | Contact email for registration | [optional] 
**contact_name** | **str** | Contact name for registration | [optional] 
**email_language** | **str** | Set the email language to one of the following: &#x60;en-US&#x60;,&#x60;de-DE&#x60;,&#x60;es-ES&#x60;,&#x60;fr-FR&#x60;,&#x60;jp-JP&#x60;,&#x60;pt-PT&#x60;,&#x60;ru-RU&#x60;,&#x60;zh-CN&#x60;, &#x60;zh-TW&#x60;, &#x60;ko-KO&#x60;, &#x60;it-IT&#x60;, &#x60;vi-VN&#x60;. | [optional] 
**enforce_login** | **bool** | Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**   As an alternative, use the &#x60;meeting_authentication&#x60;, &#x60;authentication_option&#x60; and &#x60;authentication_domains&#x60; fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar. | [optional] 
**enforce_login_domains** | **str** | Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**   As an alternative, use the &#x60;meeting_authentication&#x60;, &#x60;authentication_option&#x60; and &#x60;authentication_domains&#x60; fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar. | [optional] 
**follow_up_absentees_email_notification** | [**InlineResponse20122SettingsFollowUpAbsenteesEmailNotification**](InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.md) |  | [optional] 
**follow_up_attendees_email_notification** | [**UsersuserIdwebinarsSettingsFollowUpAttendeesEmailNotification**](UsersuserIdwebinarsSettingsFollowUpAttendeesEmailNotification.md) |  | [optional] 
**global_dial_in_countries** | **list[str]** | List of global dial-in countries | [optional] 
**hd_video** | **bool** | Default to HD video. | [optional] [default to False]
**hd_video_for_attendees** | **bool** | Whether HD video for attendees is enabled. | [optional] [default to False]
**host_video** | **bool** | Start video when host joins webinar. | [optional] 
**language_interpretation** | [**InlineResponse20122SettingsLanguageInterpretation**](InlineResponse20122SettingsLanguageInterpretation.md) |  | [optional] 
**sign_language_interpretation** | [**UsersuserIdwebinarsSettingsSignLanguageInterpretation**](UsersuserIdwebinarsSettingsSignLanguageInterpretation.md) |  | [optional] 
**panelist_authentication** | **bool** | Require panelists to authenticate to join | [optional] 
**meeting_authentication** | **bool** | Only authenticated users can join Webinar. | [optional] 
**add_watermark** | **bool** | Add watermark that identifies the viewing participant. | [optional] 
**add_audio_watermark** | **bool** | Add audio watermark that identifies the participants. | [optional] 
**notify_registrants** | **bool** | Send notification email to registrants when the host updates a webinar. | [optional] 
**on_demand** | **bool** | Make the webinar on-demand | [optional] [default to False]
**panelists_invitation_email_notification** | **bool** | Send invitation email to panelists (If &#x60;false&#x60;, do not send invitation email to panelists). | [optional] 
**panelists_video** | **bool** | Start video when panelists join webinar. | [optional] 
**post_webinar_survey** | **bool** | Zoom will open a survey page in attendees&#x27; browsers after leaving the webinar | [optional] 
**practice_session** | **bool** | Enable practice session. | [optional] [default to False]
**question_and_answer** | [**InlineResponse20122SettingsQuestionAndAnswer**](InlineResponse20122SettingsQuestionAndAnswer.md) |  | [optional] 
**registrants_confirmation_email** | **bool** | Send confirmation email to registrants | [optional] 
**registrants_email_notification** | **bool** | Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the &#x60;registrants_confirmation_email&#x60; field. | [optional] 
**registrants_restrict_number** | **int** | Restrict number of registrants for a webinar. By default, it is set to &#x60;0&#x60;. A &#x60;0&#x60; value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number. | [optional] [default to 0]
**registration_type** | **int** | Registration types. Only used for recurring webinars with a fixed time.    &#x60;1&#x60; - Attendees register once and can attend any of the webinar sessions.    &#x60;2&#x60; - Attendees need to register for each session in order to attend.    &#x60;3&#x60; - Attendees register once and can choose one or more sessions to attend. | [optional] [default to Registration_typeEnum._1]
**send_1080p_video_to_attendees** | **bool** | Always send 1080p video to attendees. | [optional] [default to False]
**show_share_button** | **bool** | Show social share buttons on the registration page. | [optional] 
**survey_url** | **str** | Survey url for post webinar survey | [optional] 
**enable_session_branding** | **bool** | Whether the **Webinar Session Branding** setting is enabled. This setting lets hosts visually customize a webinar by setting a session background. This also lets hosts use [Webinar Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) to set the Virtual Background for and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

