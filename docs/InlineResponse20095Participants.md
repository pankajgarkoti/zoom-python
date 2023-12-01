# InlineResponse20095Participants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The participant&#x27;s unique identifier. | [optional] 
**name** | **str** | The participant&#x27;s name. | [optional] 
**user_id** | **str** | The participant&#x27;s ID. This ID is assigned to the participant upon joining the webinar and is only valid for that webinar. | [optional] 
**registrant_id** | **str** | The participant&#x27;s unique registrant ID. This field only returns if you pass the &#x60;registrant_id&#x60; value for the &#x60;include_fields&#x60; query parameter.   This field does not return if the &#x60;type&#x60; query parameter is the &#x60;live&#x60; value. | [optional] 
**user_email** | **str** | Email address of the participant. If the participant is **not** part of the host&#x27;s account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details. | [optional] 
**join_time** | **datetime** | The participant&#x27;s join time. | [optional] 
**leave_time** | **datetime** | The participant&#x27;s leave time. | [optional] 
**duration** | **int** | The participant&#x27;s attendance duration. | [optional] 
**failover** | **bool** | Whether failover occurred during the webinar. | [optional] 
**status** | **str** | The participant&#x27;s status.  * &#x60;in_meeting&#x60; - In a meeting.  * &#x60;in_waiting_room&#x60; - In a waiting room. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

