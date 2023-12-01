# InlineResponse20083Users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_created_at** | **datetime** | The date and time when this user was created. | [optional] 
**created_at** | **datetime** | The date and time when this user&#x27;s latest login type was created. | [optional] 
**custom_attributes** | [**list[InlineResponse20083CustomAttributes]**](InlineResponse20083CustomAttributes.md) | Information about the user&#x27;s custom attributes.  This field is **only** returned if users are assigned custom attributes and you provided the &#x60;custom_attributes&#x60; value for the &#x60;include_fields&#x60; query parameter in the API request. | [optional] 
**dept** | **str** | The user&#x27;s department. | [optional] 
**email** | **str** | The user&#x27;s email address. | 
**employee_unique_id** | **str** | The employee&#x27;s unique ID. The this field only returns when:  * SAML single sign-on (SSO) is enabled.  * The &#x60;login_type&#x60; value is &#x60;101&#x60; (SSO). | [optional] 
**first_name** | **str** | The user&#x27;s first name. | [optional] 
**group_ids** | **list[str]** | The IDs of groups where the user is a member. | [optional] 
**host_key** | **str** | The user&#x27;s [host key](https://support.zoom.us/hc/en-us/articles/205172555-Using-your-host-key).  This field is **only** returned if users are assigned a host key and you provided the &#x60;host_key&#x60; value for the &#x60;include_fields&#x60; query parameter in the API request. | [optional] 
**id** | **str** | The user&#x27;s ID.   The API does **not** return this value for users with the &#x60;pending&#x60; status. | [optional] 
**im_group_ids** | **list[str]** | The IDs of IM directory groups where the user is a member. | [optional] 
**last_client_version** | **str** | The last client version that user used to log in. | [optional] 
**last_login_time** | **datetime** | The user&#x27;s last login time. This field has a three-day buffer period.  For example, if user first logged in on &#x60;2020-01-01&#x60; and then logged out and logged in on &#x60;2020-01-02&#x60;, this value will still reflect the login time of &#x60;2020-01-01&#x60;. However, if the user logs in on &#x60;2020-01-04&#x60;, the value of this field will reflect the corresponding login time since it exceeds the three-day buffer period. | [optional] 
**last_name** | **str** | The user&#x27;s last name. | [optional] 
**plan_united_type** | **str** | This field is returned if the user is enrolled in the [Zoom United](https://zoom.us/pricing/zoom-bundles) plan. The license option:  * &#x60;1&#x60; &amp;mdash; Zoom United Pro-United with US/CA Unlimited.  * &#x60;2&#x60; &amp;mdash; Zoom United Pro-United with UK/IR Unlimited.  * &#x60;4&#x60; &amp;mdash; Zoom United Pro-United with AU/NZ Unlimited.  * &#x60;8&#x60; &amp;mdash; Zoom United Pro-United with Global Select.  * &#x60;16&#x60; &amp;mdash; Zoom United Pro-United with Zoom Phone Pro.  * &#x60;32&#x60; &amp;mdash; Zoom United Biz-United with US/CA Unlimited.  * &#x60;64&#x60; &amp;mdash; Zoom United Biz-United with UK/IR Unlimited.  * &#x60;128&#x60; &amp;mdash; Zoom United Biz-United with AU/NZ Unlimited.  * &#x60;256&#x60; &amp;mdash; Zoom United Biz-United with Global Select.  * &#x60;512&#x60; &amp;mdash; Zoom United Biz-United with Zoom Phone Pro.  * &#x60;1024&#x60; &amp;mdash; Zoom United Ent-United with US/CA Unlimited.  * &#x60;2048&#x60; &amp;mdash; Zoom United Ent-United with UK/IR Unlimited.  * &#x60;4096&#x60; &amp;mdash; Zoom United Ent-United with AU/NZ Unlimited.  * &#x60;8192&#x60; &amp;mdash; Zoom United Ent-United with Global Select.  * &#x60;16384&#x60; &amp;mdash; Zoom United Ent-United with Zoom Phone Pro.  * &#x60;32768&#x60; &amp;mdash; Zoom United Pro-United with JP Unlimited.  * &#x60;65536&#x60; &amp;mdash; Zoom United Biz-United with JP Unlimited.  * &#x60;131072&#x60; &amp;mdash; Zoom United Ent-United with JP Unlimited. | [optional] 
**pmi** | **int** | The user&#x27;s [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) | [optional] 
**role_id** | **str** | The unique ID of the user&#x27;s assigned [role](/api-reference/zoom-api/methods#operation/roles). | [optional] 
**status** | **str** | The user&#x27;s status.  * &#x60;active&#x60; - An active user.  * &#x60;inactive&#x60; - A deactivated user.  * &#x60;pending&#x60; - A pending user. | [optional] 
**timezone** | **str** | The user&#x27;s timezone. | [optional] 
**type** | **int** | The user&#x27;s assigned plan type.  * &#x60;1&#x60; - Basic.  * &#x60;2&#x60; - Licensed.  * &#x60;4&#x60; - No Meeting License.  * &#x60;99&#x60; - None (this can only be set with &#x60;ssoCreate&#x60;). | 
**verified** | **int** | Display whether the user&#x27;s email address for the Zoom account is verified.  * &#x60;1&#x60; - A verified user email.  * &#x60;0&#x60; - The user&#x27;s email **not** verified. | [optional] 
**display_name** | **str** | The user&#x27;s display name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

