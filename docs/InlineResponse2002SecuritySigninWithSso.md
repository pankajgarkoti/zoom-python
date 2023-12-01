# InlineResponse2002SecuritySigninWithSso

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to allow users to sign in with single sign-on (SSO). If enabling this, configure your account&#x27;s SSO settings. This lets users sign in with SSO through your company&#x27;s vanity URL. | [optional] 
**require_sso_for_domains** | **bool** | Whether to require users to sign in with single sign-on (SSO) if their e-mail address belongs to one of the &#x60;domains&#x60;. | [optional] 
**domains** | **list[str]** | Users on these domains must sign in with single sign-on (SSO).  | [optional] 
**sso_bypass_users** | [**list[InlineResponse2002SecuritySigninWithSsoSsoBypassUsers]**](InlineResponse2002SecuritySigninWithSsoSsoBypassUsers.md) | The users can bypass SSO sign-in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

