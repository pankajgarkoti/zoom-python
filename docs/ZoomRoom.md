# ZoomRoom

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | Zoom room email type. | [optional] 
**calender_name** | **str** | Zoom calendar name. | [optional] 
**camera** | **str** | Zoom Room camera.  **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**device_ip** | **str** | Zoom room device IP. | [optional] 
**email** | **str** | Zoom room email. | [optional] 
**health** | **str** | Health of the Zoom Room. | [optional] 
**id** | **str** | Zoom room ID. | [optional] 
**issues** | **list[str]** | Issues encountered by the Zoom Room. | [optional] 
**last_start_time** | **str** | Zoom room last start time. | [optional] 
**location** | **str** | Zoom room location. | [optional] 
**microphone** | **str** | Zoom Room microphone.  **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**room_name** | **str** | Zoom room name. | [optional] 
**speaker** | **str** | Zoom Room speaker.  **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**status** | **str** | Zoom room status. | [optional] 
**live_meeting** | [**MeetingMetrics1**](MeetingMetrics1.md) |  | [optional] 
**past_meetings** | [**ZoomRoomPastMeetings**](ZoomRoomPastMeetings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

