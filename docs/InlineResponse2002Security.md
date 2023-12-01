# InlineResponse2002Security

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_change_name_pic** | **bool** | Whether to only allow account administrators to change a user&#x27;s picture. | [optional] 
**admin_change_user_info** | **bool** | Whether to only allow account administrators to change a user&#x27;s information. | [optional] 
**user_modifiable_info_by_admin** | **list[str]** | If the &#x60;admin_change_user_info&#x60; value is &#x60;true&#x60;, the list of the types of user information that only the account administrators can modify.  * &#x60;name&#x60;  * &#x60;profile_picture&#x60;  * &#x60;sign_in_email&#x60;  * &#x60;host_key&#x60; | [optional] 
**signin_with_sso** | [**InlineResponse2002SecuritySigninWithSso**](InlineResponse2002SecuritySigninWithSso.md) |  | [optional] 
**hide_billing_info** | **bool** | Hide billing information. | [optional] 
**import_photos_from_devices** | **bool** | Allow users to import photos from a photo library on a  device. | [optional] 
**password_requirement** | [**InlineResponse2002SecurityPasswordRequirement**](InlineResponse2002SecurityPasswordRequirement.md) |  | [optional] 
**sign_again_period_for_inactivity_on_client** | **int** | Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Client app after a set amount of time.       If this setting is disabled, the value of this field will be &#x60;0&#x60;. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom client.     &#x60;5&#x60; - 5 minutes.     &#x60;10&#x60; - 10 minutes.     &#x60;15&#x60; - 15 minutes.     &#x60;30&#x60; - 30 minutes.     &#x60;45&#x60; - 45 minutes.     &#x60;60&#x60; - 60 .     &#x60;90&#x60; - 90 minutes.     &#x60;120&#x60; - 120 minutes.  | [optional] 
**sign_again_period_for_inactivity_on_web** | **int** | Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Web Portal after a set amount of time.       If this setting is disabled, the value of this field will be &#x60;0&#x60;. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom Web Portal.     &#x60;5&#x60; - 5 minutes.     &#x60;10&#x60; - 10 minutes.     &#x60;15&#x60; - 15 minutes.     &#x60;30&#x60; - 30 minutes.     &#x60;60&#x60; - 60 minutes.     &#x60;120&#x60; - 120 minutes.     | [optional] 
**sign_in_with_two_factor_auth** | **str** | Settings for 2FA( [two factor authentication](https://support.zoom.us/hc/en-us/articles/360038247071) ). &#x60;all&#x60; - Two factor authentication will be enabled for all users in the account.     &#x60;none&#x60; - Two factor authentication is disabled.     &#x60;group&#x60; - Two factor authentication will be enabled for users belonging to specific groups. If 2FA is enabled for certain groups, the group IDs of the group(s) will be provided in the &#x60;sign_in_with_two_factor_auth_groups&#x60; field.     &#x60;role&#x60; - Two factor authentication will be enabled only for users assigned with specific roles in the account. If 2FA is enabled for specific roles, the role IDs will be provided in the &#x60;sign_in_with_two_factor_auth_roles&#x60; field.  | [optional] 
**sign_in_with_two_factor_auth_groups** | **list[str]** | This field contains group IDs of groups that have 2FA enabled. This field is only returned if the value of &#x60;sign_in_with_two_factor_auth&#x60; is &#x60;group&#x60; | [optional] 
**sign_in_with_two_factor_auth_roles** | **list[str]** | This field contains role IDs of roles that have 2FA enabled. This field is only returned if the value of &#x60;sign_in_with_two_factor_auth&#x60; is &#x60;role&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
