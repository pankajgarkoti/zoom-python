# LiveMeetingsmeetingIdeventsParamsSipHeaders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_display_name** | **str** | Custom name that will be used within the SIP Header. | [optional] 
**to_display_name** | **str** | Custom remote name that will be used within the meeting. | [optional] 
**from_uri** | **str** | Custom URI that will be used within the SIP Header. The URI must start with &#x27;sip:&#x27; or &#x27;sips:&#x27; as a valid URI based on parameters defined by the platform. | [optional] 
**additional_headers** | [**list[LiveMeetingsmeetingIdeventsParamsSipHeadersAdditionalHeaders]**](LiveMeetingsmeetingIdeventsParamsSipHeadersAdditionalHeaders.md) | Ability to add 1 to 10 custom headers, each of which has a maximum length of 256 bytes to comply with SIP standards.  Custom headers would leverage header names starting with &#x27;X-&#x27; per SIP guidelines. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

