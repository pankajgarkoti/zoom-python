# InlineResponse20091SettingsInMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_exit_chime** | **str** | Play sound when participants join or leave.    &#x60;host&#x60; - Heard by host only.    &#x60;all&#x60; - Heard by host and all attendees.    &#x60;none&#x60; - Disable. | [optional] 
**feedback** | **bool** | Add a **Feedback** tab to the Windows Settings or Mac Preferences dialog. Enable users to provide feedback to Zoom at the end of the meeting. | [optional] 
**polling** | **bool** | Add &#x27;Polls&#x27; to the meeting controls. This allows the host to survey the attendees. | [optional] 
**post_meeting_feedback** | **bool** | Whether to display a thumbs up or thumbs down feedback survey at the end of each meeting. | [optional] 
**screen_sharing** | **bool** | Whether to allow hosts and participants to share their screen or content during meetings. | [optional] 
**who_can_share_screen** | **str** | The type of user who can share their screen or content during meetings.  * &#x60;host&#x60; - Only hosts can screen share.  * &#x60;all&#x60; - Both hosts and participants can screen share. | [optional] 
**who_can_share_screen_when_someone_is_sharing** | **str** | Indicates who is allowed to start sharing screen when someone else in the meeting is sharing their screen. The value can be one of the following:     &#x60;host&#x60;: Only a host can share the screen when someone else is sharing.     &#x60;all&#x60;: Anyone in the meeting is allowed to start sharing their screen when someone else is sharing. For Webinar, the hosts and panelists can start screen sharing, but not the attendees.  | [optional] 
**disable_screen_sharing_for_host_meetings** | **bool** | Whether the **Disable desktop screen sharing for meetings you host** setting is enabled. | [optional] 
**annotation** | **bool** | Allow participants to use annotation tools to add information to shared screens. | [optional] 
**whiteboard** | **bool** | Allow participants to share a whiteboard that includes annotation tools. | [optional] 
**remote_control** | **bool** | Whether to enable the [**Remote control**](https://support.zoom.us/hc/en-us/articles/201362673-Requesting-or-giving-remote-control) setting. | [optional] 
**non_verbal_feedback** | **bool** | Allow participants in a meeting to provide nonverbal feedback and express opinions by clicking on icons in the Participants panel. | [optional] 
**allow_participants_to_rename** | **bool** | If the value of this field is set to &#x60;true&#x60;, meeting participants and webinar panelists are allowed to rename themselves during a meeting or a webinar.  | [optional] 
**breakout_room** | **bool** | Allow the meeting host to split meeting participants into separate breakout rooms. | [optional] 
**remote_support** | **bool** | Allow meeting host to provide 1:1 remote support to another participant. | [optional] 
**manual_captioning** | [**InlineResponse20091SettingsInMeetingManualCaptioning**](InlineResponse20091SettingsInMeetingManualCaptioning.md) |  | [optional] 
**closed_captioning** | [**InlineResponse20091SettingsInMeetingClosedCaptioning**](InlineResponse20091SettingsInMeetingClosedCaptioning.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

