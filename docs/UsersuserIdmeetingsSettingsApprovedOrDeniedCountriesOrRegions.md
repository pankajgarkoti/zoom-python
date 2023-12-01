# UsersuserIdmeetingsSettingsApprovedOrDeniedCountriesOrRegions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_list** | **list[str]** | The list of approved countries or regions. | [optional] 
**denied_list** | **list[str]** | The list of blocked countries or regions. | [optional] 
**enable** | **bool** | Whether to enable the [**Approve or block entry for users from specific countries/regions**](https://support.zoom.us/hc/en-us/articles/360060086231-Approve-or-block-entry-for-users-from-specific-countries-regions) setting. | [optional] 
**method** | **str** | Whether to allow or block users from specific countries or regions. * &#x60;approve&#x60; - Allow users from specific countries or regions to join the meeting. If you select this setting, include the approved countries or regions in the &#x60;approved_list&#x60; field.  * &#x60;deny&#x60; - Block users from specific countries or regions from joining the meeting. If you select this setting, include the blocked countries or regions in the &#x60;denied_list&#x60; field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

