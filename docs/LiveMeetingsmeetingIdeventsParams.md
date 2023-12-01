# LiveMeetingsmeetingIdeventsParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**list[LiveMeetingsmeetingIdeventsParamsContacts]**](LiveMeetingsmeetingIdeventsParamsContacts.md) | The user&#x27;s email address or the user ID, up to a maximum of 10 contacts. The account must be a part of the meeting host&#x27;s account. | [optional] 
**invitee_name** | **str** | The user&#x27;s name to display in the meeting. Use this field if you pass the &#x60;participant.invite.callout&#x60; value for the &#x60;method&#x60; field. | [optional] 
**phone_number** | **str** | The user&#x27;s phone number. Use this field if you pass the &#x60;participant.invite.callout&#x60; value for the &#x60;method&#x60; field. As a best practice, ensure this includes a country code and area code. | [optional] 
**invite_options** | [**LiveMeetingsmeetingIdeventsParamsInviteOptions**](LiveMeetingsmeetingIdeventsParamsInviteOptions.md) |  | [optional] 
**call_type** | **str** | The type of call out. Use a value of &#x60;h323&#x60; or &#x60;sip&#x60;. Use this field if you pass the &#x60;participant.invite.room_system_callout&#x60; value for the &#x60;method&#x60; field. | [optional] 
**device_ip** | **str** | The user&#x27;s device IP address or URI. Use this field if you pass the &#x60;participant.invite.room_system_callout&#x60; value for the &#x60;method&#x60; field. | [optional] 
**h323_headers** | [**LiveMeetingsmeetingIdeventsParamsH323Headers**](LiveMeetingsmeetingIdeventsParamsH323Headers.md) |  | [optional] 
**sip_headers** | [**LiveMeetingsmeetingIdeventsParamsSipHeaders**](LiveMeetingsmeetingIdeventsParamsSipHeaders.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

