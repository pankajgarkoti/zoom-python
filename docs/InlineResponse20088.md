# InlineResponse20088

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID. | [optional] 
**created_at** | **datetime** | The date and time when this user&#x27;s latest login type was created. | [optional] 
**dept** | **str** | Department. | [optional] 
**email** | **str** | User&#x27;s email address. | [optional] 
**first_name** | **str** | User&#x27;s first name. | [optional] 
**last_client_version** | **str** | User last login client version. | [optional] 
**last_login_time** | **datetime** | User last login time. | [optional] 
**last_name** | **str** | User&#x27;s last name. | [optional] 
**pmi** | **int** | [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). | [optional] 
**role_name** | **str** | User&#x27;s [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) name. | [optional] 
**timezone** | **str** | The time zone of the user. | [optional] 
**type** | **int** | User&#x27;s plan type:    &#x60;1&#x60; - Basic.    &#x60;2&#x60; - Licensed.    &#x60;99&#x60; - None (this can only be set with &#x60;ssoCreate&#x60;). | 
**use_pmi** | **bool** | Displays &#x60;true&#x60; if user has enabled a [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) for instant meetings, &#x60;false&#x60; otherwise. | [optional] [default to False]
**display_name** | **str** | User&#x27;s display name. | [optional] 
**account_id** | **str** | User&#x27;s account ID. | [optional] 
**account_number** | **int** | The user&#x27;s account number. | [optional] 
**cms_user_id** | **str** | The user&#x27;s CMS ID. Only enabled for Kaltura integration. | [optional] 
**company** | **str** | The user&#x27;s company. | [optional] 
**user_created_at** | **datetime** | The date and time when this user was created. | [optional] 
**custom_attributes** | [**list[InlineResponse20088CustomAttributes]**](InlineResponse20088CustomAttributes.md) | Custom attributes that have been assigned to the user. | [optional] 
**employee_unique_id** | **str** | The employee&#x27;s unique ID. This field only returns when:  * SAML single sign-on (SSO) is enabled.  * The &#x60;login_type&#x60; value is &#x60;101&#x60; (SSO). | [optional] 
**group_ids** | **list[str]** | IDs of the web groups that the user belongs to.  | [optional] 
**im_group_ids** | **list[str]** | IM IDs of the groups that the user belongs to. | [optional] 
**jid** | **str** |  | [optional] 
**job_title** | **str** | The user&#x27;s job title. | [optional] 
**language** | **str** | Default language for the Zoom Web Portal. | [optional] 
**location** | **str** | Theser&#x27;s location. | [optional] 
**login_types** | **list[int]** | The user&#x27;s login method.  &#x60;0&#x60; - Facebook OAuth. &#x60;1&#x60; - Google OAuth. &#x60;24&#x60; - Apple OAuth. &#x60;27&#x60; - Microsoft OAuth. &#x60;97&#x60; - Mobile device. &#x60;98&#x60; - RingCentral OAuth. &#x60;99&#x60; - API user. &#x60;100&#x60; - Zoom Work email. &#x60;101&#x60; - Single Sign-On (SSO).  These login methods are only available in China.  &#x60;11&#x60; - Phone number. &#x60;21&#x60; - WeChat. &#x60;23&#x60; - Alipay. | [optional] 
**manager** | **str** | The manager for the user. | [optional] 
**personal_meeting_url** | **str** | User&#x27;s personal meeting url. | [optional] 
**phone_country** | **str** | **Note:** This field has been **deprecated** and will not be supported in the future. Use the **phone_numbers** field instead of this field.      User&#x27;s country for Company Phone Number. | [optional] 
**phone_number** | **str** | **Note:** This field has been **deprecated** and will not be supported in the future. Use the **phone_numbers** field instead of this field.  The user&#x27;s phone number. | [optional] 
**phone_numbers** | [**list[InlineResponse20088PhoneNumbers]**](InlineResponse20088PhoneNumbers.md) |  | [optional] 
**pic_url** | **str** | The URL for user&#x27;s profile picture. | [optional] 
**plan_united_type** | **str** | This field is returned if the user is enrolled in the [Zoom United](https://zoom.us/pricing/zoom-bundles) plan. The license option:  * &#x60;1&#x60; - Zoom United Pro-United with US/CA Unlimited.  * &#x60;2&#x60; - Zoom United Pro-United with UK/IR Unlimited.  * &#x60;4&#x60; - Zoom United Pro-United with AU/NZ Unlimited.  * &#x60;8&#x60; - Zoom United Pro-United with Global Select.  * &#x60;16&#x60; - Zoom United Pro-United with Zoom Phone Pro.  * &#x60;32&#x60; - Zoom United Biz-United with US/CA Unlimited.  * &#x60;64&#x60; - Zoom United Biz-United with UK/IR Unlimited.  * &#x60;128&#x60; - Zoom United Biz-United with AU/NZ Unlimited.  * &#x60;256&#x60; - Zoom United Biz-United with Global Select.  * &#x60;512&#x60; - Zoom United Biz-United with Zoom Phone Pro.  * &#x60;1024&#x60; - Zoom United Ent-United with US/CA Unlimited.  * &#x60;2048&#x60; - Zoom United Ent-United with UK/IR Unlimited.  * &#x60;4096&#x60; - Zoom United Ent-United with AU/NZ Unlimited.  * &#x60;8192&#x60; - Zoom United Ent-United with Global Select.  * &#x60;16384&#x60; - Zoom United Ent-United with Zoom Phone Pro.  * &#x60;32768&#x60; - Zoom United Pro-United with JP Unlimited.  * &#x60;65536&#x60; - Zoom United Biz-United with JP Unlimited.  * &#x60;131072&#x60; - Zoom United Ent-United with JP Unlimited. | [optional] 
**pronouns** | **str** | The user&#x27;s pronouns. | [optional] 
**pronouns_option** | **int** | The user&#x27;s display pronouns setting. * &#x60;1&#x60; - Ask the user every time they join meetings and webinars.  * &#x60;2&#x60; - Always display pronouns in meetings and webinars.  * &#x60;3&#x60; - Do not display pronouns in meetings and webinars. | [optional] 
**role_id** | **str** | Unique identifier of the user&#x27;s assigned [role](/docs/api-reference/zoom-api/methods#operation/roles). | [optional] 
**status** | **str** | Status of user&#x27;s account. | [optional] 
**vanity_url** | **str** | Personal meeting room URL, if the user has one. | [optional] 
**verified** | **int** | Displays whether user is verified or not.   &#x60;1&#x60; - Account verified.     &#x60;0&#x60; - Account not verified. | [optional] 
**cluster** | **str** | The user&#x27;s cluster. | [optional] 
**zoom_one_type** | **int** | The user&#x27;s Zoom One plan option.    &#x60;4&#x60; - Zoom One Enterprise.    &#x60;8&#x60; - Zoom One Enterprise Plus.    &#x60;16&#x60; - Zoom One Business Plus with US/CA Unlimited.    &#x60;32&#x60; - Zoom One Business Plus with UK/IR Unlimited.    &#x60;64&#x60; - Zoom One Business Plus with AU/NZ Unlimited.    &#x60;128&#x60; - Zoom One Business Plus with Japan Unlimited.    &#x60;33554432&#x60; - Zoom One Business Plus with Global Select.    &#x60;134217728&#x60; - Zoom One Enterprise Premier with US/CA Unlimited.    &#x60;1073741824&#x60; - Zoom One Enterprise Premier with AU/NZ Unlimited.    &#x60;536870912&#x60; - Zoom One Enterprise Premier with UK/IR Unlimited.    &#x60;268435456&#x60; - Zoom One Enterprise Premier with Japan Unlimited.     The Zoom One plan option for Gov accounts:    &#x60;4&#x60; - Zoom One Enterprise.    &#x60;8&#x60; - Zoom One Enterprise Plus.    &#x60;16&#x60; - Zoom One Business Plus.    The Zoom One plan option for Education accounts:    &#x60;18014398509481984&#x60; - Zoom One for Education School and Campus.    &#x60;72057594037927936&#x60; - Zoom One for Education Enterprise Essentials.    &#x60;576460752303423488&#x60; - Zoom One for Education Enterprise Student.   &#x60;144115188075855872&#x60; - Zoom One for Education Enterprise Plus.    &#x60;137438953472&#x60; - Zoom One for Education School and Campus Plus with US/CA Unlimited.    &#x60;1099511627776&#x60; -Zoom One for Education School and Campus Plus with AU/NZ Unlimited.    &#x60;549755813888&#x60; - Zoom One for Education School and Campus Plus with UK/IR Unlimited.    &#x60;274877906944&#x60; - Zoom One for Education School and Campus Plus with Japan Unlimited.    &#x60;2199023255552&#x60; - Zoom One for Education School and Campus Plus with Global Select.    &#x60;4294967296&#x60; - Zoom One for Education Enterprise Premier with US/CA Unlimited.    &#x60;34359738368&#x60; - Zoom One for Education Enterprise Premier with AU/NZ Unlimited.    &#x60;17179869184&#x60; -Zoom One for Education Enterprise Premier with UK/IR Unlimited.    &#x60;8589934592&#x60; - Zoom One for Education Enterprise Premier with with Japan Unlimited.    &#x60;68719476736&#x60; - Zoom One for Education Enterprise Premier with Global Select. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

