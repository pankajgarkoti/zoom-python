# MeetingIdRegistrantsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The registrant&#x27;s first name. | 
**last_name** | **str** | The registrant&#x27;s last name. | [optional] 
**email** | **str** | The registrant&#x27;s email address. | 
**address** | **str** | The registrant&#x27;s address. | [optional] 
**city** | **str** | The registrant&#x27;s city. | [optional] 
**state** | **str** | The registrant&#x27;s state or province. | [optional] 
**zip** | **str** | The registrant&#x27;s ZIP or postal code. | [optional] 
**country** | **str** | The registrant&#x27;s two-letter [country code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries). | [optional] 
**phone** | **str** | The registrant&#x27;s phone number. | [optional] 
**comments** | **str** | The registrant&#x27;s questions and comments. | [optional] 
**custom_questions** | [**list[MeetingsmeetingIdrecordingsregistrantsCustomQuestions]**](MeetingsmeetingIdrecordingsregistrantsCustomQuestions.md) | Information about custom questions. | [optional] 
**industry** | **str** | The registrant&#x27;s industry. | [optional] 
**job_title** | **str** | The registrant&#x27;s job title. | [optional] 
**no_of_employees** | **str** | The registrant&#x27;s number of employees:  * &#x60;1-20&#x60;  * &#x60;21-50&#x60;  * &#x60;51-100&#x60;  * &#x60;101-500&#x60;  * &#x60;500-1,000&#x60;  * &#x60;1,001-5,000&#x60;  * &#x60;5,001-10,000&#x60;  * &#x60;More than 10,000&#x60; | [optional] 
**org** | **str** | The registrant&#x27;s organization. | [optional] 
**purchasing_time_frame** | **str** | The registrant&#x27;s purchasing time frame:  * &#x60;Within a month&#x60;  * &#x60;1-3 months&#x60;  * &#x60;4-6 months&#x60;  * &#x60;More than 6 months&#x60;  * &#x60;No timeframe&#x60; | [optional] 
**role_in_purchase_process** | **str** | The registrant&#x27;s role in the purchase process:  * &#x60;Decision Maker&#x60;  * &#x60;Evaluator/Recommender&#x60;  * &#x60;Influencer&#x60;  * &#x60;Not involved&#x60; | [optional] 
**language** | **str** | The registrant&#x27;s language preference for confirmation emails:  * &#x60;en-US&#x60; &amp;mdash; English (US)  * &#x60;de-DE&#x60; &amp;mdash; German (Germany)  * &#x60;es-ES&#x60; &amp;mdash; Spanish (Spain)  * &#x60;fr-FR&#x60; &amp;mdash; French (France)  * &#x60;jp-JP&#x60; &amp;mdash; Japanese  * &#x60;pt-PT&#x60; &amp;mdash; Portuguese (Portugal)  * &#x60;ru-RU&#x60; &amp;mdash; Russian  * &#x60;zh-CN&#x60; &amp;mdash; Chinese (PRC)  * &#x60;zh-TW&#x60; &amp;mdash; Chinese (Taiwan)  * &#x60;ko-KO&#x60; &amp;mdash; Korean  * &#x60;it-IT&#x60; &amp;mdash; Italian (Italy)  * &#x60;vi-VN&#x60; &amp;mdash; Vietnamese  * &#x60;pl-PL&#x60; &amp;mdash; Polish  * &#x60;Tr-TR&#x60; &amp;mdash; Turkish | [optional] 
**auto_approve** | **bool** | If a meeting was scheduled with the &#x60;approval_type&#x60; field value of &#x60;1&#x60; (manual approval) but you want to automatically approve meeting registrants, set the value of this field to &#x60;true&#x60;.   **Note:** You cannot use this field to change approval setting for a meeting originally scheduled with the &#x60;approval_type&#x60; field value of &#x60;0&#x60; (automatic approval). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

