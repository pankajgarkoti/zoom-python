# UserInMeetingSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_host_to_enable_focus_mode** | **bool** | Whether the host can enable [**Focus Mode**](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) when scheduling a meeting. This value defaults to &#x60;null&#x60;. | [optional] 
**allow_users_to_delete_messages_in_meeting_chat** | **bool** | If the value of this field is set to &#x60;true&#x60;,  allow users to delete messages in the in-meeting chat.  | [optional] 
**allow_live_streaming** | **bool** | Allow livestreaming. | [optional] 
**post_meeting_feedback** | **bool** | Whether to display a thumbs up or thumbs down feedback survey at the end of each meeting. | [optional] 
**whiteboard** | **bool** | Whether to enable the [**Zoom Whiteboard**](https://support.zoom.us/hc/en-us/articles/4410916881421) feature. | [optional] 
**allow_participants_chat_with** | **int** | Who participants can chat with:  * &#x60;1&#x60; &amp;mdash; The participant cannot use chat.  * &#x60;2&#x60; &amp;mdash; The participant can chat with the host and co-hosts only.   * &#x60;3&#x60; &amp;mdash; The participant can chat with other participants publicly.  * &#x60;4&#x60; - The participant can chat with other participants publicly and privately.    **Note:** This setting is only available with client versions 5.7.3 and above. | [optional] 
**allow_users_save_chats** | **int** | How participants can save meeting chats:  * &#x60;1&#x60; &amp;mdash; Participants cannot save meeting chats.  * &#x60;2&#x60; &amp;mdash; Participants can only save host and co-host meeting chats.  * &#x60;3&#x60; &amp;mdash; Participants can save all meeting chats. | [optional] 
**annotation** | **bool** | Allow meeting participants to use the [annotation tools](https://support.zoom.us/hc/en-us/articles/115005706806). This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**attendee_on_hold** | **bool** | Allow the host to put an attendee on hold. This value defaults to &#x60;false&#x60;. **This field has been deprecated and is no longer supported.** | [optional] [default to False]
**attention_mode_focus_mode** | **bool** | Whether the [**Focus Mode**](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) feature is enabled. When enabled, this feature only displays the host and co-hosts&#x27; video and profile pictures during a meeting.    This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**auto_saving_chat** | **bool** | Automatically save all in-meeting chats. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**breakout_room** | **bool** | Allow the meeting host to split meeting participants into separate breakout rooms. | [optional] [default to False]
**breakout_room_schedule** | **bool** | Allow the host to assign participants to breakout rooms when scheduling. This feature is **only** available in version 4.5.0 or higher. | [optional] 
**chat** | **bool** | Enable chat during meeting for all participants. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**meeting_question_answer** | **bool** | Allow participants to ask questions for the host and participants to answer. | [optional] 
**closed_caption** | **bool** | Enable closed captions. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**closed_captioning** | [**UserInMeetingSettingsClosedCaptioning**](UserInMeetingSettingsClosedCaptioning.md) |  | [optional] 
**co_host** | **bool** | Allow the host to add co-hosts. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**custom_data_center_regions** | **bool** | Use custom [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-meetings-webinars):  * &#x60;true&#x60; &amp;mdash; Users can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting real-time meeting traffic. The data center regions can be provided in the &#x60;data_center_regions&#x60; field.  * &#x60;false&#x60; &amp;mdash; Only use the default data center regions. | [optional] 
**custom_live_streaming_service** | **bool** | Allow custom livestreaming. | [optional] 
**custom_service_instructions** | **str** | The custom livestreaming service instructions. | [optional] 
**data_center_regions** | **list[str]** | If the value of &#x60;custom_data_center_regions&#x60; is &#x60;true&#x60;, a comma-separated list of the following [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list) to opt in to:  * &#x60;AU&#x60; &amp;mdash; Australia. * &#x60;LA&#x60; &amp;mdash; Latin America.  * &#x60;CA&#x60; &amp;mdash; Canada.  * &#x60;CN&#x60; &amp;mdash; China.  * &#x60;DE&#x60; &amp;mdash; Germany.  * &#x60;HK&#x60; &amp;mdash; Hong Kong SAR.  * &#x60;IN&#x60; &amp;mdash; India.  * &#x60;IE&#x60; &amp;mdash; Ireland.  * &#x60;TY&#x60; &amp;mdash; Japan.  * &#x60;MX&#x60; &amp;mdash; Mexico.  * &#x60;NL&#x60; &amp;mdash; Netherlands.  * &#x60;SG&#x60; &amp;mdash; Singapore.  * &#x60;US&#x60; &amp;mdash; United States. | [optional] 
**disable_screen_sharing_for_host_meetings** | **bool** | Enable the **Disable desktop screen sharing for meetings you host** setting. | [optional] 
**disable_screen_sharing_for_in_meeting_guests** | **bool** | Enable the **Disable screen sharing when guests are in the meeting** setting. | [optional] 
**e2e_encryption** | **bool** | Require [AES encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) for meetings. | [optional] 
**entry_exit_chime** | **str** | When to play the meeting entry/exit sound notification:  * &#x60;host&#x60; &amp;mdash; Only when the host joins or leaves.  * &#x60;all&#x60; &amp;mdash; When any participant joins or leaves.  * &#x60;none&#x60; - Disable the entry/exit sound notification.   This value defaults to &#x60;all&#x60;. | [optional] [default to 'all']
**far_end_camera_control** | **bool** | Allow another user to take control of the user&#x27;s camera. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**feedback** | **bool** | Enable the [**Feedback to Zoom**](https://support.zoom.us/hc/en-us/articles/115005838023-Feedback-to-Zoom) setting. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**file_transfer** | **bool** | Indicates whether [in-meeting file transfer](https://support.zoom.us/hc/en-us/articles/209605493-In-meeting-file-transfer) setting has been enabled for the user or not. | [optional] 
**group_hd** | **bool** | Enable group HD video in Meeting. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**webinar_group_hd** | **bool** | Enable group HD video in Webinar. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**join_from_desktop** | **bool** | Allow participants to join a meeting directly from their desktop browser. Note that the meeting experience from the desktop browser is limited. | [optional] 
**join_from_mobile** | **bool** | Allow participants to join a meeting directly from their mobile browser. Note that the meeting experience from the mobile browser is limited. | [optional] 
**language_interpretation** | [**UserInMeetingSettingsLanguageInterpretation**](UserInMeetingSettingsLanguageInterpretation.md) |  | [optional] 
**sign_language_interpretation** | [**UserInMeetingSettingsSignLanguageInterpretation**](UserInMeetingSettingsSignLanguageInterpretation.md) |  | [optional] 
**live_streaming_facebook** | **bool** | Allow Facebook livestreaming. | [optional] 
**live_streaming_youtube** | **bool** | Allow YouTube livestreaming. | [optional] 
**manual_captioning** | [**UserInMeetingSettingsManualCaptioning**](UserInMeetingSettingsManualCaptioning.md) |  | [optional] 
**meeting_reactions** | **bool** | Whether meeting participants can [communicate using the emoji reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Nonverbal-feedback-and-meeting-reactions) located in the **Reactions** menu in the meeting toolbar. | [optional] 
**meeting_reactions_emojis** | **str** | Choose from the following meeting reaction options: * &#x60;all&#x60; &amp;mdash; All emojis: Allow meeting participants to use any emoji available in Zoom chat as a reaction in a meeting. * &#x60;selected&#x60; &amp;mdash; Selected emojis: Allow meeting participants to use the 6 standard meeting reaction emojis: Clapping Hands, Thumbs Up, Heart, Tears of Joy, Open Mouth, Party Popper (Tada, Celebration)  | [optional] 
**allow_host_panelists_to_use_audible_clap** | **bool** | Whether to allow host and panelist to use audible clap. | [optional] 
**webinar_reactions** | **bool** | Set this field to true to use [webinar reactions](https://support.zoom.us/hc/en-us/articles/4803536268429). | [optional] 
**meeting_survey** | **bool** | Allow the host to present a survey to participants once a meeting has ended. This feature is only available in version 5.7.3 or higher. | [optional] 
**non_verbal_feedback** | **bool** | Enable the [**Non-verbal feedback**](https://support.zoom.us/hc/en-us/articles/115001286183-Nonverbal-feedback-and-meeting-reactions-) setting.  This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**polling** | **bool** | Add polls to the meeting controls. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**private_chat** | **bool** | [Enable private chat](https://support.zoom.us/hc/en-us/articles/360060835932-Enabling-and-disabling-private-chat) between participants during meetings. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**record_play_voice** | **bool** | Let the user record and play their own voice. | [optional] 
**remote_control** | **bool** | Enable the [**Remote control**](https://support.zoom.us/hc/en-us/articles/201362673-Requesting-or-giving-remote-control) setting.  This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**remote_support** | **bool** | Enable the [**Remote support**](https://support.zoom.us/hc/en-us/articles/360060951012-Enabling-remote-support) setting. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**request_permission_to_unmute_participants** | **bool** | Indicates whether the [**Request permission to unmute participants**](https://support.zoom.us/hc/en-us/articles/203435537-Muting-and-unmuting-participants-in-a-meeting#h_01EGK4XFWS1SJGZ71MYGKF7260) option has been enabled for the user or not. | [optional] 
**screen_sharing** | **bool** | Allow host and participants to share their screen or content during meetings  | [optional] 
**share_dual_camera** | **bool** | Allow the use of shared dual cameras. This value defaults to &#x60;false&#x60;. **This field is deprecated.** | [optional] [default to False]
**show_a_join_from_your_browser_link** | **bool** | Allow participants to join a meeting directly from their browser and bypass the Zoom application download process. This is useful for participants who cannot download, install, or run applications. Note that the meeting experience from the browser is limited. | [optional] 
**show_meeting_control_toolbar** | **bool** | Always display the [in-meeting controls](https://support.zoom.us/hc/en-us/articles/360021921032-Zoom-Room-meeting-controls-and-settings#h_01EQCC03TCPRC72VKXZ7W47FDX). | [optional] 
**slide_control** | **bool** | Whether the person sharing during a presentation can allow others to control the slide presentation. This feature is only available in version 5.8.3 or higher. | [optional] 
**virtual_background** | **bool** | Enable Virtual Backgrounds. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**virtual_background_settings** | [**UserInMeetingSettingsVirtualBackgroundSettings**](UserInMeetingSettingsVirtualBackgroundSettings.md) |  | [optional] 
**waiting_room** | **bool** | Enable the [**Waiting Room**](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room) feature. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**webinar_chat** | [**UserInMeetingSettingsWebinarChat**](UserInMeetingSettingsWebinarChat.md) |  | [optional] 
**webinar_live_streaming** | [**UserInMeetingSettingsWebinarLiveStreaming**](UserInMeetingSettingsWebinarLiveStreaming.md) |  | [optional] 
**meeting_polling** | [**UserInMeetingSettingsMeetingPolling**](UserInMeetingSettingsMeetingPolling.md) |  | [optional] 
**webinar_polling** | [**UserInMeetingSettingsWebinarPolling**](UserInMeetingSettingsWebinarPolling.md) |  | [optional] 
**webinar_survey** | **bool** | Allow the host to present surveys to attendees once a webinar has ended. | [optional] 
**who_can_share_screen** | **str** | Indicates who can share their screen or content during meetings. The value can be one of the following:      &#x60;host&#x60;: Only host can share the screen.     &#x60;all&#x60;: Both hosts and attendees can share their screen during meetings. For Webinar, the hosts and panelists can start screen sharing, but not the attendees.  | [optional] 
**who_can_share_screen_when_someone_is_sharing** | **str** | Indicates who is allowed to start sharing screen when someone else in the meeting is sharing their screen. The value can be one of the following:     &#x60;host&#x60;: Only a host can share the screen when someone else is sharing.     &#x60;all&#x60;: Anyone in the meeting is allowed to start sharing their screen when someone else is sharing. For Webinar, the hosts and panelists can start screen sharing, but not the attendees.  | [optional] 
**participants_share_simultaneously** | **str** | Indicates how many participants can share at the same time. The value can be one of the following:     &#x60;one&#x60;: Only one participant can share at a time .     &#x60;multiple&#x60;: Multiple participants can share simultaneously (dual monitors recommended). | [optional] 
**workplace_by_facebook** | **bool** | Allow Workplace by Facebook livestreaming. | [optional] 
**auto_answer** | **bool** | Allow the user to view and add contacts to the [**Auto-answer group in chat**](https://support.zoom.us/hc/en-us/articles/203736135-Auto-answering-invitations-to-meetings) feature. Calls from members of the **Auto Answer Group** will be automatically answered the user. | [optional] 
**allow_show_zoom_windows** | **bool** | Enable the [**Show Zoom windows during screen share**](https://support.zoom.us/hc/en-us/articles/360061383571-Showing-Zoom-windows-during-screen-share) feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

