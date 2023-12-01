# InlineResponse200MeetingSecurity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_or_denied_countries_or_regions** | **bool** | Whether to enable the [**Approve or block entry for users from specific countries/regions**](https://support.zoom.us/hc/en-us/articles/360060086231-Joining-from-specific-countries-regions) setting. | [optional] 
**auto_security** | **bool** | Whether all meetings must be secured with at least one security option.    This setting can only be disabled by Enterprise, ISV, Business (with more than 100 licenses), and Education accounts. | [optional] 
**block_user_domain** | **bool** | Whether users in specific domains are blocked from joining meetings and webinars. | [optional] 
**chat_etiquette_tool** | **bool** | Whether to enable the **Chat Etiquette Tool**. | [optional] 
**embed_password_in_join_link** | **bool** | Whether the meeting passcode is encrypted and included in the invitation link. The provided link will allow participants to join the meeting without having to enter the passcode. | [optional] 
**encryption_type** | **bool** | Whether use encryption to start a meeting. | [optional] 
**end_to_end_encrypted_meetings** | **bool** | Whether to enable end-to-end encryption for meetings. | [optional] 
**meeting_password** | **bool** | Whether all instant and scheduled meetings that users can join via client or Zoom Rooms systems are passcode-protected. [Personal Meeting ID (PMI)](https://support.zoom.us/hc/en-us/articles/203276937) meetings are **not** included in this setting. | [optional] 
**only_authenticated_can_join_from_webclient** | **bool** | Whether to specify that only authenticated users can join the meeting from the web client. | [optional] 
**phone_password** | **bool** | Whether passcodes are required for participants joining by phone.    If enabled and the meeting is passcode-protected, a numeric passcode is required for participants to join by phone. For meetings with alphanumeric passcodes, a numeric passcode will be generated. | [optional] 
**pmi_password** | **bool** | Whether all Personal Meeting ID (PMI) meetings that users can join via client or Zoom Rooms systems are passcode-protected. | [optional] 
**waiting_room** | **bool** | Whether participants are placed in the [**Waiting Room**](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room) when they join a meeting.    If the **Waiting Room** feature is enabled, the [**Allow participants to join before host**](https://support.zoom.us/hc/en-us/articles/202828525-Allow-participants-to-join-before-host) setting is automatically disabled. | [optional] 
**webinar_password** | **bool** | Whether to generate a passcode when scheduling webinars. Participants must use the generated passcode to join the scheduled webinar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

