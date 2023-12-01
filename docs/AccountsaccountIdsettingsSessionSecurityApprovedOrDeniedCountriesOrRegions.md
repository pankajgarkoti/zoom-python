# AccountsaccountIdsettingsSessionSecurityApprovedOrDeniedCountriesOrRegions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_list** | **list[str]** | List of countries/regions from where participants can join this meeting.  | [optional] 
**denied_list** | **list[str]** | List of countries/regions from where participants can not join this meeting.  | [optional] 
**enable** | **bool** | &#x60;true&#x60;: Setting enabled to either allow or block users from specific regions from joining your meetings.       &#x60;false&#x60;: Setting disabled. | [optional] 
**method** | **str** | Specify whether to allow users from specific regions to join this meeting, or block users from specific regions from joining this meeting.          &#x60;approve&#x60;: Allow users from specific regions or countries to join this meeting. If this setting is selected, the approved regions or countries must be included in the &#x60;approved_list&#x60;.         &#x60;deny&#x60;: Block users from specific regions or countries from joining this meeting. If this setting is selected, the approved regions or countries must be included in the &#x60;denied_list&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

