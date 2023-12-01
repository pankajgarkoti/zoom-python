# AccountsaccountIdsettingsMeetingSecurityWaitingRoomOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether to enable the waiting room. | [optional] 
**locked** | **bool** | Whether to enable the option to lock after selecting  &#x60;How are participants admitted from the waiting room&#x60;. | [optional] 
**admit_type** | **int** | The type of admission for participants from the waiting room.  * &#x60;1&#x60; - Everyone is automatically admitted.  * &#x60;2&#x60; - Participants are manually admitted.  * &#x60;3&#x60; - External users are manually admitted. Internal users are automatically admitted10 minutes before start time.  * &#x60;4&#x60; - External users and users without approved domains are manually admitted. Internal users are automatically admitted. | [optional] 
**internal_user_auto_admit** | **int** | If the &#x60;admit_type&#x60; in (&#x60;1&#x60;,&#x60;3&#x60;,&#x60;4&#x60;), the time when the internal user can join a meeting before the host.  * &#x60;1&#x60; - when the host joins.  * &#x60;2&#x60; - anytime.  * &#x60;3&#x60; - 5 minutes before start time.  * &#x60;4&#x60; - 10 minutes before start time.   * &#x60;5&#x60; - 15 minutes before start time.   If the &#x60;admit_type&#x60; equal &#x60;1&#x60;, this field value can not be &#x60;2&#x60;.  | [optional] 
**admit_domain_allowlist** | **str** | If the &#x60;admit_type&#x60; field is &#x60;4&#x60;, a comma-separated list of the domains that can bypass the waiting room (&#x60;example.com,example2.com&#x60;). | [optional] 
**who_can_admit_participants** | **int** | The type of who can admit participants from the waiting room.  * &#x60;0&#x60; - Host and co-hosts only.  * &#x60;1&#x60; - Host, co-hosts, and anyone who bypassed the waiting room (only if host and co-hosts are not present). | [optional] 
**sort_order_of_people** | **int** | The type of sort order of people in the waiting room in the participants panel.  * &#x60;0&#x60; - Join order.  * &#x60;1&#x60; - Alphabetical.   This feature is only available with version 5.10.3 or later. | [optional] 
**more_options** | [**AccountsaccountIdsettingsMeetingSecurityWaitingRoomOptionsMoreOptions**](AccountsaccountIdsettingsMeetingSecurityWaitingRoomOptionsMoreOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

