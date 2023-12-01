# GroupsgroupIdsettingsMeetingSecurity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_security** | **bool** | Whether to require that all meetings are secured with at least one security option.    This setting can only be disabled by Enterprise, ISV, Business (with more than 100 licenses), and Education accounts. | [optional] 
**block_user_domain** | **bool** | Whether to block users in specific domains from joining meetings and webinars. | [optional] 
**block_user_domain_list** | **list[str]** | The domain to block, up to 20 domains. For example, the &#x60;*.example.com&#x60; domain. | [optional] 
**chat_etiquette_tool** | [**GroupsgroupIdsettingsChatChatEtiquetteTool**](GroupsgroupIdsettingsChatChatEtiquetteTool.md) |  | [optional] 
**embed_password_in_join_link** | **bool** | Whether the meeting passcode will be encrypted and included in the invitation link. The provided link will allow participants to join the meeting without having to enter the passcode. | [optional] 
**encryption_type** | **str** | The type of encryption to use when starting a meeting:  * &#x60;enhanced_encryption&#x60; - Use enhanced encryption. Encryption data is stored in the cloud.  * &#x60;e2ee&#x60; - End-to-end encryption. The encryption key is stored on the local device and cannot be obtained by anyone else. Enabling E2EE also [**disables** certain features](https://support.zoom.us/hc/en-us/articles/360048660871), such as cloud recording, live streaming, and allowing participants to join before the host. | [optional] 
**end_to_end_encrypted_meetings** | **bool** | Whether to enable end-to-end encryption for meetings. If enabled, you can specify the type of encryption in the &#x60;encryption_type&#x60; field. | [optional] 
**meeting_password** | **bool** | Whether all instant and scheduled meetings that users can join via client or Zoom Rooms systems are passcode-protected. [Personal Meeting ID (PMI)](https://support.zoom.us/hc/en-us/articles/203276937) meetings are **not** included in this setting. | [optional] 
**meeting_password_requirement** | [**GroupsgroupIdsettingsMeetingSecurityMeetingPasswordRequirement**](GroupsgroupIdsettingsMeetingSecurityMeetingPasswordRequirement.md) |  | [optional] 
**only_authenticated_can_join_from_webclient** | **bool** | Whether to specify that only authenticated users can join the meeting from the web client. | [optional] 
**phone_password** | **bool** | Whether to require a passcode for participants joining by phone.    If enabled and the meeting is passcode-protected, a numeric passcode is required for participants to join by phone. For meetings with alphanumeric passcodes, a numeric passcode will be generated. | [optional] 
**pmi_password** | **bool** | Whether all Personal Meeting ID (PMI) meetings that users can join via client or Zoom Rooms systems are passcode-protected. | [optional] 
**require_password_for_scheduled_meeting** | **bool** | Whether to require a passcode for meetings that have already been scheduled. | [optional] 
**require_password_for_scheduled_webinar** | **bool** | Whether to require a passcode for webinars that have already been scheduled. | [optional] 
**waiting_room** | **bool** | Whether participants are placed in the [**Waiting Room**](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room) when they join a meeting.    If the **Waiting Room** feature is enabled, the [**Allow participants to join before host**](https://support.zoom.us/hc/en-us/articles/202828525-Allow-participants-to-join-before-host) setting is automatically disabled. | [optional] 
**waiting_room_settings** | [**GroupsgroupIdsettingsMeetingSecurityWaitingRoomSettings**](GroupsgroupIdsettingsMeetingSecurityWaitingRoomSettings.md) |  | [optional] 
**webinar_password** | **bool** | Whether to generate a passcode when scheduling webinars. Participants must use the generated passcode to join the scheduled webinar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

