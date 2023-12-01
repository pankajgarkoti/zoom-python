# InlineResponse20075Participants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_key** | **str** | The participant&#x27;s SDK identifier. This value can be alphanumeric, up to a maximum length of 35 characters. | [optional] 
**duration** | **int** | The participant&#x27;s attendance duration. | [optional] 
**failover** | **bool** | Whether failover occurred during the webinar. | [optional] 
**id** | **str** | The participant&#x27;s universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the &#x60;id&#x60; value in the [**Get a user**](/docs/api-reference/zoom-api/methods#operation/user) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.   **Note:** Use the &#x60;participant_user_id&#x60; value instead of this value. We will remove this response in a future release. | [optional] 
**join_time** | **datetime** | The participant&#x27;s join time. | [optional] 
**leave_time** | **datetime** | The participant&#x27;s leave time. | [optional] 
**name** | **str** | The participant&#x27;s display name. This returns an empty string value if the account calling the API is a BAA account. | [optional] 
**registrant_id** | **str** | The registrant&#x27;s ID. This field only returns if you provide the &#x60;registrant_id&#x60; value for the &#x60;include_fields&#x60; query parameter. | [optional] 
**status** | **str** | The participant&#x27;s status.  * &#x60;in_meeting&#x60; - In a meeting.  * &#x60;in_waiting_room&#x60; - In a waiting room. | [optional] 
**user_email** | **str** | The participant&#x27;s email address. If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](/docs/api-reference/using-zoom-apis#email-address) for details. This returns an empty string value if the account calling the API is a BAA account. | [optional] 
**user_id** | **str** | The participant&#x27;s ID. This ID is assigned to the participant upon joining the webinar and is only valid for that webinar. | [optional] 
**participant_user_id** | **str** | The participant&#x27;s universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the &#x60;id&#x60; value in the [**Get a user**](/docs/api-reference/zoom-api/methods#operation/user) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

