# AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The policy&#x27;s description. | [optional] 
**id** | **str** | The policy ID. | [optional] 
**is_locked** | **bool** | Whether to lock the policy. When it is locked, users cannot update the policy. This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**keywords** | **list[str]** | A list of defined rule keywords. | [optional] 
**name** | **str** | The policy name. | [optional] 
**regular_expression** | **str** | The regular expression to match to the content of chat messages. | [optional] 
**status** | **str** | The policy&#x27;s current status.  * &#x60;activated&#x60; - Activated.  * &#x60;deactivated&#x60; - Deactivated. | [optional] 
**trigger_action** | **int** | The policy&#x27;s trigger action.  * &#x60;1&#x60; - Ask the user to confirm before they send the message.  * &#x60;2&#x60; - Block the user&#x27;s message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

