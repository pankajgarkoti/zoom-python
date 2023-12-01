# UsersBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to take to create the new user.  * &#x60;create&#x60; - The user receives an email from Zoom containing a confirmation link. The user must then use the link to activate their Zoom account. The user can then set or change their password.  * &#x60;autoCreate&#x60; - This action is for Enterprise customers with a managed domain. autoCreate creates an email login type for users.  * &#x60;custCreate&#x60; - Users created with this action do not have passwords and will **not** have the ability to log into the Zoom web portal or the Zoom client. These users can still host and join meetings using the &#x60;start_url&#x60; and &#x60;join_url&#x60; respectively. To use this option, you must [contact the Integrated Software Vendor (ISV) sales team](https://explore.zoom.us/en/isv/#isv).  * &#x60;ssoCreate&#x60; - This action is provided for the enabled &amp;ldquo;Pre-provisioning SSO User&amp;rdquo; option. A user created this way has no password. If it is **not** a Basic user, a personal vanity URL with the username (no domain) of the provisioning email is generated. If the username or PMI is invalid or occupied, it uses a random number or random personal vanity URL. | 
**user_info** | [**UsersUserInfo**](UsersUserInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

