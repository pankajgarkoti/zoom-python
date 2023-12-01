# PoliciesPolicyIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_group_id** | **str** | The assigner group&#x27;s (Group 1) ID. | 
**id** | **str** | The Information Barriers policy&#x27;s ID. | 
**policy_name** | **str** | The Information Barriers policy&#x27;s name. | 
**settings** | [**InformationBarrierspoliciesSettings**](InformationBarrierspoliciesSettings.md) |  | 
**status** | **int** | The Information Barriers policy&#x27;s status.  * &#x60;0&#x60; &amp;mdash; Disabled.  * &#x60;1&#x60; &amp;mdash; Enabled. | 
**to_group_id** | **str** | The assignee group&#x27;s (Group 2) ID. | 
**type** | **int** | The Information Barriers policy&#x27;s type of &#x60;settings&#x60; restrictions.  * &#x60;0&#x60; &amp;mdash; A [hard or soft block](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers#h_a603c6f7-05c8-4de5-b4b6-91982d748b34) exists, but users in Group 1 and Group 2 can chat with each other.  * &#x60;1&#x60; &amp;mdash; A [hard or soft block](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers#h_a603c6f7-05c8-4de5-b4b6-91982d748b34) exists and only users in Group 1 can chat with users in Group 2.  * &#x60;2&#x60; &amp;mdash; No blocks exist, but only users in Group 1 can chat with users in Group 2.  * &#x60;3&#x60; &amp;mdash; No blocks exist and users in Group 1 and Group 2 can chat with each other.   This field only supports &#x60;0&#x60;. | [default to TypeEnum._0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

