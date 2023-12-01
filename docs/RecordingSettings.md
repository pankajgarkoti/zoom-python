# RecordingSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_type** | **int** | The approval type for the registration.     &#x60;0&#x60;- Automatically approve the registration when a user registers.     &#x60;1&#x60; - Manually approve or deny the registration of a user.     &#x60;2&#x60; - No registration required to view the recording. | [optional] 
**authentication_domains** | **str** | The domains for authentication. | [optional] 
**authentication_option** | **str** | The options for authentication . | [optional] 
**on_demand** | **bool** | This field determines whether registration is required to view the recording. | [optional] 
**password** | **str** | This field enables passcode protection for the recording by setting a passcode. The passcode must have a minimum of **eight** characters with a mix of numbers, letters and special characters.         **Note:** If the account owner or the admin has set minimum passcode strength requirements for recordings through Account Settings, the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/api-reference/zoom-api/ma#operation/accountSettings) API. | [optional] 
**recording_authentication** | **bool** | THis field only authenticated users can view. | [optional] 
**send_email_to_host** | **bool** | This field enables you to send an email to the host when someone registers to view the recording. This applies for On-demand recordings only. | [optional] 
**share_recording** | **str** | This field determines how the meeting recording is shared. | [optional] 
**show_social_share_buttons** | **bool** | This field shows social share buttons on registration page. This applies for On-demand recordings only. | [optional] 
**topic** | **str** | The name of the recording. | [optional] 
**viewer_download** | **bool** | This field determines whether a viewer can download the recording file or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

