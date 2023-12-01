# InlineResponse2002InSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data_center_regions** | **bool** | Whether custom [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-meetings-webinars) are in use.  * &#x60;true&#x60; - Users can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting real-time meeting traffic. The data center regions can be provided in the &#x60;data_center_regions&#x60; field.  * &#x60;false&#x60; - Only the default data center regions. | [optional] 
**data_center_regions** | **list[str]** | If the value of &#x60;custom_data_center_regions&#x60; is &#x60;true&#x60;, a comma-separated list of the selected custom [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list).  * &#x60;AU&#x60; - Australia. * &#x60;LA&#x60; - Latin America.  * &#x60;CA&#x60; - Canada.  * &#x60;CN&#x60; - China.  * &#x60;DE&#x60; - Germany.  * &#x60;HK&#x60; - Hong Kong SAR.  * &#x60;IN&#x60; - India.  * &#x60;IE&#x60; - Ireland.  * &#x60;TY&#x60; - Japan.  * &#x60;MX&#x60; - Mexico.  * &#x60;NL&#x60; - Netherlands.  * &#x60;SG&#x60; - Singapore.  * &#x60;US&#x60; - United States. | [optional] 
**unchecked_data_center_regions** | **list[str]** | If the value of &#x60;custom_data_center_regions&#x60; is &#x60;true&#x60;, a comma-separated list the [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list) that are **not** selected.  * &#x60;EU&#x60; - Europe.  * &#x60;HK&#x60; - Hong Kong.  * &#x60;AU&#x60; - Australia.  * &#x60;IN&#x60; - India.  * &#x60;LA&#x60; - Latin America.  * &#x60;TY&#x60; - Tokyo.  * &#x60;CN&#x60; - China.  * &#x60;US&#x60; - United States.  * &#x60;CA&#x60; - Canada. | [optional] 
**p2p_connetion** | **bool** | Whether to enable the [**Peer to Peer connection while only 2 people are in a meeting**](https://support.zoom.us/hc/en-us/articles/360061410851-Enabling-Peer-to-Peer-connection-for-2-people-in-a-meeting) setting. | [optional] 
**p2p_ports** | **bool** | Whether to enable the **Listening ports range** setting. | [optional] 
**ports_range** | **str** | When the &#x60;p2p_ports&#x60; value is &#x60;true&#x60;, the value is a semi-colon list of the peer to peer listening ports range, between &#x60;1&#x60; to &#x60;65535&#x60;. This value defaults to an empty string. | [optional] [default to '']
**dscp_audio** | **int** | The DSCP audio marking value. This value defaults to &#x60;56&#x60;. | [optional] [default to 56]
**dscp_marking** | **bool** | Whether to enable [differentiated services code point (DSCP)](https://en.wikipedia.org/wiki/Differentiated_services) marking. | [optional] 
**dscp_video** | **int** | The DSCP video marking value. This value defaults to &#x60;40&#x60;. | [optional] [default to 40]
**dscp_dual** | **bool** | Whether to use the differentiated services code point classifiers (&#x27;dscp_video&#x27;, &#x27;dscp_audio&#x27;) in the dual way (incoming and outgoing). | [optional] 
**subsession** | **bool** | Allow host to split meeting participants into separate, smaller rooms. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

