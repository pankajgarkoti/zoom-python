# InlineResponse20112

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The meeting ID. | [optional] 
**join_url** | **str** | The URL the registrant can use to join the meeting.   The API will not return this field if the meeting was [created](/docs/api-reference/zoom-api/methods#operation/meetingCreate) with the &#x60;approval_type&#x60; field value of &#x60;1&#x60; (manual approval). | [optional] 
**registrant_id** | **str** | The registrant&#x27;s ID. | [optional] 
**start_time** | **datetime** | The meeting&#x27;s start time. | [optional] 
**topic** | **str** | The meeting&#x27;s topic. | [optional] 
**occurrences** | [**list[InlineResponse20112Occurrences]**](InlineResponse20112Occurrences.md) | Array of occurrence objects. | [optional] 
**participant_pin_code** | **int** | The participant PIN code is used to authenticate audio participants before they join the meeting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

