# MembersMemberIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to perform:  * &#x60;move&#x60; &amp;mdash; Remove the group member from one group and move them to a different group.  * &#x60;set_primary&#x60; &amp;mdash; Set the user&#x27;s primary group. | 
**target_group_id** | **str** | The target group&#x27;s ID. To get this value, use the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.  * To set a user&#x27;s primary group, use the designated primary group&#x27;s &#x60;groupId&#x60; value.  * To move a group member from one group to another, use the &#x60;groupId&#x60; of the designated group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

