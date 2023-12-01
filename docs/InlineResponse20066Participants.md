# InlineResponse20066Participants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_key** | **str** | The participant&#x27;s SDK identifier. This value can be alphanumeric, up to a maximum length of 35 characters. | [optional] 
**duration** | **int** | Participant duration. | [optional] 
**failover** | **bool** | Indicates if failover happened during the meeting. | [optional] 
**id** | **str** | The participant&#x27;s universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the &#x60;id&#x60; value in the [**Get a user**](/docs/api-reference/zoom-api/methods#operation/user) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.   **Note:** Use the &#x60;participant_user_id&#x60; value instead of this value. We will remove this response in a future release. | [optional] 
**join_time** | **datetime** | Participant join time. | [optional] 
**leave_time** | **datetime** | Participant leave time. | [optional] 
**name** | **str** | Participant display name.  This returns an empty string value if the account calling the API is a BAA account. | [optional] 
**registrant_id** | **str** | Unique identifier of the registrant. This field is only returned if you entered &amp;quot;registrant_id&amp;quot; as the value of &#x60;include_fields&#x60; query parameter. | [optional] 
**status** | **str** | The participant&#x27;s status.  * &#x60;in_meeting&#x60; - In a meeting.  * &#x60;in_waiting_room&#x60; - In a waiting room. | [optional] 
**user_email** | **str** | Participant email.  If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](/docs/api-reference/using-zoom-apis#email-address) for details. This returns an empty string value if the account calling the API is a BAA account. | [optional] 
**user_id** | **str** | Participant ID. This is a unique ID assigned to the participant joining a meeting and is valid for that meeting only. | [optional] 
**bo_mtg_id** | **str** | The [breakout room](https://support.zoom.us/hc/en-us/articles/206476313-Managing-breakout-rooms) ID. Each breakout room is assigned a unique ID. | [optional] 
**participant_user_id** | **str** | The participant&#x27;s universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the &#x60;id&#x60; value in the [**Get a user**](/docs/api-reference/zoom-api/methods#operation/user) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

