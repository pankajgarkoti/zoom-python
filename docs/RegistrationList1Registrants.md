# RegistrationList1Registrants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Registrant ID. | [optional] 
**address** | **str** | The registrant&#x27;s address. | [optional] 
**city** | **str** | The registrant&#x27;s city. | [optional] 
**comments** | **str** | The registrant&#x27;s questions and comments. | [optional] 
**country** | **str** | The registrant&#x27;s two-letter ISO [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries). | [optional] 
**custom_questions** | [**list[MeetingsmeetingIdrecordingsregistrantsCustomQuestions]**](MeetingsmeetingIdrecordingsregistrantsCustomQuestions.md) | Information about custom questions. | [optional] 
**email** | **str** | The registrant&#x27;s email address. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details. | 
**first_name** | **str** | The registrant&#x27;s first name. | 
**industry** | **str** | The registrant&#x27;s industry. | [optional] 
**job_title** | **str** | The registrant&#x27;s job title. | [optional] 
**last_name** | **str** | The registrant&#x27;s last name. | [optional] 
**no_of_employees** | **str** | The registrant&#x27;s number of employees.  * &#x60;1-20&#x60;  * &#x60;21-50&#x60;  * &#x60;51-100&#x60;  * &#x60;101-250&#x60;  * &#x60;251-500&#x60;  * &#x60;501-1,000&#x60;  * &#x60;1,001-5,000&#x60;  * &#x60;5,001-10,000&#x60;  * &#x60;More than 10,000&#x60; | [optional] 
**org** | **str** | The registrant&#x27;s organization. | [optional] 
**phone** | **str** | The registrant&#x27;s phone number. | [optional] 
**purchasing_time_frame** | **str** | The registrant&#x27;s purchasing time frame.  * &#x60;Within a month&#x60;  * &#x60;1-3 months&#x60;  * &#x60;4-6 months&#x60;  * &#x60;More than 6 months&#x60;  * &#x60;No timeframe&#x60; | [optional] 
**role_in_purchase_process** | **str** | The registrant&#x27;s role in the purchase process.  * &#x60;Decision Maker&#x60;  * &#x60;Evaluator/Recommender&#x60;  * &#x60;Influencer&#x60;  * &#x60;Not involved&#x60; | [optional] 
**state** | **str** | The registrant&#x27;s state or province. | [optional] 
**status** | **str** | The status of the registrant&#x27;s registration.   &#x60;approved&#x60; - User has been successfully approved for the webinar.     &#x60;pending&#x60; -  The registration is still pending.     &#x60;denied&#x60; - User has been denied from joining the webinar. | [optional] 
**zip** | **str** | The registrant&#x27;s ZIP or postal code. | [optional] 
**create_time** | **datetime** | The time when the registrant registered. | [optional] 
**join_url** | **str** | The URL that an approved registrant can use to join the meeting or webinar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

