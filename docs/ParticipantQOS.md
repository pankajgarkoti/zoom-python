# ParticipantQOS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The participant&#x27;s universally unique ID. This value is the same as the participant&#x27;s user ID if the participant joins the webinar by logging into Zoom. If the participant joins the webinar without logging into Zoom, this returns an empty value. | [optional] 
**device** | **str** | The type of device the participant used to join the meeting.  * &#x60;Phone&#x60; - The participant joined via PSTN.  * &#x60;H.323/SIP&#x60; - The participant joined via an H.323 or SIP device.  * &#x60;Windows&#x60; - The participant joined via VoIP using a Windows device.  * &#x60;Mac&#x60; - The participant joined via VoIP using a Mac device.  * &#x60;iOS&#x60; - The participant joined via VoIP using an iOS device.  * &#x60;Android&#x60; - The participant joined via VoIP using an Android device.   **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**domain** | **str** | The participant&#x27;s PC domain.   **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**harddisk_id** | **str** | The participant&#x27;s hard disk ID.   **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**internal_ip_addresses** | **list[str]** | The participant&#x27;s internal IP addresses. This field will not return under these conditions:  * The account calling this API is a **legacy** [business associate agreement (BAA) under HIPAA](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp&#x3D;1&amp;amp;n&#x3D;se45.1.160_1103&amp;amp;r&#x3D;SECTION&amp;amp;ty&#x3D;HTML).  * The account calling this API is a BAA under HIPAA **without** a signed BAA data processing addendum. | [optional] 
**ip_address** | **str** | The participant&#x27;s IP address. | [optional] 
**join_time** | **datetime** | The time when the participant joined the meeting. | [optional] 
**leave_time** | **datetime** | The time when the participant left the meeting. | [optional] 
**location** | **str** | The participant&#x27;s location. | [optional] 
**mac_addr** | **str** | The participant&#x27;s MAC address.   **Note:** This response returns an empty string (&#x60;&amp;ldquo;&amp;ldquo;&#x60;) value for any users who are **not** a part of the host&#x27;s account (external users). | [optional] 
**pc_name** | **str** | The participant&#x27;s PC name. | [optional] 
**user_id** | **str** | The participant&#x27;s ID. This value is assigned to a participant upon joining a meeting and is only valid for the meeting&#x27;s duration. | [optional] 
**user_name** | **str** | The participant&#x27;s display name. | [optional] 
**user_qos** | [**list[ParticipantQOSUserQos]**](ParticipantQOSUserQos.md) | The participant&#x27;s quality of service information. | [optional] 
**version** | **str** | The participant&#x27;s Zoom client version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

