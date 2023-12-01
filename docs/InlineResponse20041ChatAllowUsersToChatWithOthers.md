# InlineResponse20041ChatAllowUsersToChatWithOthers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | If you select &#x27;In the same organization&#x27;, users may still be able to chat with external users if they are added to channels or group chats with external users. | [optional] 
**selected_option** | **int** | The type of allowing users to add contacts.  * 1 - Anyone (internal and external contacts).  * 2 - In the same organization.  * 3 - In the same organization and specified domains.  * 4 - In the same organization and specified users. | [optional] 
**user_email_addresses** | **str** | The domains or emails, either internal or external.  * When the &#x60;selected_option&#x60; field value is &#x60;3&#x60;, the value is internal or external domains. Use a comma to separate multiple domains. * When the &#x60;selected_option&#x60; field value is &#x60;4&#x60;, the value is internal or external email addresses. Use a comma to separate multiple emails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

