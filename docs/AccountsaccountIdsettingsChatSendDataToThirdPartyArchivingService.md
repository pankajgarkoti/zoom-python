# AccountsaccountIdsettingsChatSendDataToThirdPartyArchivingService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Allow users to send data to third-party archiving service. | [optional] 
**type** | **str** | The type of global relay.  * &#x60;global_relay&#x60; - The participant cannot use chat. * &#x60;smarsh&#x60; - Host and co-hosts only. | [optional] 
**smtp_delivery_address** | **str** | SMTP delivery address. It is used when the field &#x60;type&#x60; value is &#x60;global_relay&#x60;, and it is required. | [optional] 
**user_name** | **str** | User name. It is used when the field &#x60;type&#x60; value is &#x60;global_relay&#x60;, and it is required. | [optional] 
**passcode** | **str** | passcode. It is used when the field &#x60;type&#x60; value is &#x60;global_relay&#x60;, and it is required. | [optional] 
**authorized_channel_token** | **str** | Authorized channel token. It is used when the field &#x60;type&#x60; value is &#x60;smarsh&#x60;, and it is required. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

