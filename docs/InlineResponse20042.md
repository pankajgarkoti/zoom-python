# InlineResponse20042

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | [optional] 
**name** | **str** | Group name. | [optional] 
**total_members** | **int** | Total number of members in this group. | [optional] 
**search_by_account** | **bool** | Members can search for others under same account. | [optional] 
**search_by_domain** | **bool** | Members can search for others in the same email domain. | [optional] 
**search_by_ma_account** | **bool** | Members can search for others under same master account - including all sub accounts. | [optional] 
**type** | **str** | IM Group types:    &#x60;normal&#x60; - Only members can see the other members in the group. Other people can search for members in the group.    &#x60;shared&#x60; - Everyone in the account can see the group and members.     &#x60;restricted&#x60; - No one except group members can see the group or search for other group members.  | [optional] [default to 'normal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

