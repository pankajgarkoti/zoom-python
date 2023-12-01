# InlineResponse20034Devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Unique identifier of the device. | [optional] 
**device_name** | **str** | The name of the device. | [optional] 
**mac_address** | **str** | The mac address of the device. | [optional] 
**serial_number** | **str** | The device&#x27;s serial number. | [optional] 
**vendor** | **str** | The device&#x27;s manufacturer. | [optional] 
**model** | **str** | The device&#x27;s model. | [optional] 
**platform_os** | **str** | The device&#x27;s platform. | [optional] 
**app_version** | **str** | App version of Zoom Rooms. | [optional] 
**tag** | **str** | The name of the tag. | [optional] 
**enrolled_in_zdm** | **bool** | Whether the device enrolled in ZDM (Zoom Device Management). | [optional] 
**connected_to_zdm** | **bool** | Whether the device connected to ZDM (Zoom Device Management). | [optional] 
**room_id** | **str** | id of the Zoom Room. | [optional] 
**room_name** | **str** | Name of the Zoom Room. | [optional] 
**device_type** | **int** | Filter devices by device type.     Device Type:    &#x60;-1&#x60; - All Zoom Room device(0,1,2,3,4,6).    &#x60;0&#x60; - Zoom Rooms Computer.    &#x60;1&#x60; - Zoom Rooms Controller.    &#x60;2&#x60; - Zoom Rooms Scheduling Display.    &#x60;3&#x60; - Zoom Rooms Control System.    &#x60;4&#x60; -  Zoom Rooms Whiteboard.    &#x60;5&#x60; - Zoom Phone Appliance.    &#x60;6&#x60; - Zoom Rooms Computer (with Controller). | [optional] 
**skd_version** | **str** | The version of the SDK. | [optional] 
**device_status** | **int** | Filter devices by status.      Device Status:    &#x60;0&#x60; - offline.    &#x60;1&#x60; - online.    &#x60;-1&#x60; - unlink | [optional] 
**last_online** | **str** | The time when device was online last time. | [optional] 
**user_email** | **str** | The owner of the phone device | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

