# InlineResponse20093MeetingSecurityMeetingPasswordRequirement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consecutive_characters_length** | **int** | The maximum length of consecutive characters (for example, &#x60;abcdef&#x60;) allowed in a passcode:  * &#x60;4&#x60; through &#x60;8&#x60; - The maximum consecutive characters length. The length is &#x60;n&#x60; minus &#x60;1&#x60;, where &#x60;n&#x60; is the value. For example, if the value is &#x60;4&#x60;, there can only be a maximum of &#x60;3&#x60; consecutive characters in a passcode (for example, &#x60;abc1x@8fdh&#x60;).  * &#x60;0&#x60; - No consecutive character restriction. | [optional] 
**have_letter** | **bool** | Whether passcodes must contain at least one letter character. | [optional] 
**have_number** | **bool** | Whether passcodes must contain at least one numeric character. | [optional] 
**have_special_character** | **bool** | Whether passcodes must contain at least one special character. For example, &#x60;!&#x60;, &#x60;@&#x60;, and/or &#x60;#&#x60; characters. | [optional] 
**have_upper_and_lower_characters** | **bool** | Whether passcodes must include uppercase and lowercase characters. | [optional] 
**length** | **int** | The minimum passcode length. | [optional] 
**only_allow_numeric** | **bool** | Whether passcodes must contain **only** numeric characters. | [optional] 
**weak_enhance_detection** | **bool** | Whether users are informed when the provided passcode is weak. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

