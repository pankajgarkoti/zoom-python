# InlineResponse20093MeetingSecurity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_security** | **bool** | Whether all meetings must be secured with at least one security option.    This setting can only be disabled by Enterprise, ISV, Business (with more than 100 licenses), and Education accounts. | [optional] 
**block_user_domain** | **bool** | Whether users in specific domains are blocked from joining meetings and webinars. | [optional] 
**block_user_domain_list** | **list[str]** | The blocked domains. | [optional] 
**embed_password_in_join_link** | **bool** | Whether the meeting passcode is encrypted and included in the invitation link. The provided link will allow participants to join the meeting without having to enter the passcode. | [optional] 
**encryption_type** | **str** | The type of encryption used when starting a meeting:  * &#x60;enhanced_encryption&#x60; - Enhanced encryption. Encryption data is stored in the cloud.  * &#x60;e2ee&#x60; - End-to-end encryption. The encryption key is stored on the local device and cannot be obtained by anyone else. Enabling E2EE also [**disables** certain features](https://support.zoom.us/hc/en-us/articles/360048660871), such as cloud recording, live streaming, and allowing participants to join before the host. | [optional] 
**end_to_end_encrypted_meetings** | **bool** | Whether end-to-end encryption is enabled for meetings. | [optional] 
**meeting_password** | **bool** | Whether all instant and scheduled meetings that users can join via client or Zoom Rooms systems are passcode-protected. [Personal Meeting ID (PMI)](https://support.zoom.us/hc/en-us/articles/203276937) meetings are **not** included in this setting. | [optional] 
**meeting_password_requirement** | [**InlineResponse20093MeetingSecurityMeetingPasswordRequirement**](InlineResponse20093MeetingSecurityMeetingPasswordRequirement.md) |  | [optional] 
**only_authenticated_can_join_from_webclient** | **bool** | Whether to specify that only authenticated users can join the meeting from the web client. | [optional] 
**phone_password** | **bool** | Whether passcodes are required for participants joining by phone.    If enabled and the meeting is passcode-protected, a numeric passcode is required for participants to join by phone. For meetings with alphanumeric passcodes, a numeric passcode will be generated. | [optional] 
**pmi_password** | **bool** | Whether all Personal Meeting ID (PMI) meetings that users can join via client or Zoom Rooms systems are passcode-protected. | [optional] 
**require_password_for_scheduled_meeting** | **bool** | Whether passcodes are required for meetings that have already been scheduled. | [optional] 
**require_password_for_scheduled_webinar** | **bool** | Whether passcodes are required for webinars that have already been scheduled. | [optional] 
**waiting_room** | **bool** | Whether participants are placed in the [**Waiting Room**](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room) when they join a meeting.    If the **Waiting Room** feature is enabled, the [**Allow participants to join before host**](https://support.zoom.us/hc/en-us/articles/202828525-Allow-participants-to-join-before-host) setting is automatically disabled. | [optional] 
**waiting_room_settings** | [**InlineResponse20093MeetingSecurityWaitingRoomSettings**](InlineResponse20093MeetingSecurityWaitingRoomSettings.md) |  | [optional] 
**webinar_password** | **bool** | Whether to generate a passcode when scheduling webinars. Participants must use the generated passcode to join the scheduled webinar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

