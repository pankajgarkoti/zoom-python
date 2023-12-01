# InlineResponse20080

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dial_in_number_unrestricted** | **bool** | Control restriction on account users adding a TSP number outside of account&#x27;s dial in numbers. | [optional] 
**dial_in_numbers** | [**list[InlineResponse20080DialInNumbers]**](InlineResponse20080DialInNumbers.md) |  | [optional] 
**enable** | **bool** | Enable Telephony Service Provider for account users. | [optional] 
**master_account_setting_extended** | **bool** | For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account. | [optional] 
**modify_credential_forbidden** | **bool** | Control restriction on account users being able to modify their TSP credentials. | [optional] 
**tsp_bridge** | **str** | Telephony bridge zone | [optional] 
**tsp_enabled** | **bool** | Enable TSP feature for account. This has to be enabled to use any other tsp settings/features. | [optional] 
**tsp_provider** | **str** | Telephony Service Provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

