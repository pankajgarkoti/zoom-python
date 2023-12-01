# InlineResponse20054Participants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier of the Participant. It is the same as the User ID of the participant if the participant joins the meeting by logging into Zoom. If the participant joins the meeting without logging in, the value of this field will be blank. | [optional] 
**name** | **str** | Participant display name. | [optional] 
**user_id** | **str** | Participant ID. This is a unique ID assigned to the participant joining a meeting and is valid for that meeting only. | [optional] 
**registrant_id** | **str** | The participant&#x27;s unique registrant ID. This field only returns if you pass the &#x60;registrant_id&#x60; value for the &#x60;include_fields&#x60; query parameter.   This field does not return if the &#x60;type&#x60; query parameter is the &#x60;live&#x60; value. | [optional] 
**user_email** | **str** | Email address of the user. If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details. | [optional] 
**join_time** | **datetime** | Participant join time. | [optional] 
**leave_time** | **datetime** | Participant leave time. | [optional] 
**duration** | **int** | Participant duration. | [optional] 
**failover** | **bool** | Indicates if failover happened during the meeting. | [optional] 
**status** | **str** | The participant&#x27;s status.  * &#x60;in_meeting&#x60; - In a meeting.  * &#x60;in_waiting_room&#x60; - In a waiting room. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

