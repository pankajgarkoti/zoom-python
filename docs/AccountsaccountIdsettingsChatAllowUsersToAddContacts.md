# AccountsaccountIdsettingsChatAllowUsersToAddContacts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | By disabling this setting, users will not be able to add contacts. | [optional] 
**selected_option** | **int** | The type of allowing users to add contacts.  * 1 - Anyone (internal and external contacts).  * 2 - In the same organization.  * 3 - In the same organization and specified domains.  * 4 - In the same organization and specified users. | [optional] 
**user_email_addresses** | **str** | The internal or external domains or emails.  * When the &#x60;selected_option&#x60; field value is &#x60;3&#x60;, the value is internal or external domains. Use a comma to separate multiple domains. Example: company.com.  * When the &#x60;selected_option&#x60; field value is &#x60;4&#x60;, the value is internal or external email addresses. Use a comma to separate multiple emails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

