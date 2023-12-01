# WebinarSurveyObjectCustomSurveyQuestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The survey question, up to 420 characters. | [optional] 
**type** | **str** | The survey&#x27;s question and answer type.  * &#x60;single&#x60; - Single choice.  * &#x60;multiple&#x60; - Multiple choice.  * &#x60;matching&#x60; - Matching.  * &#x60;rank_order&#x60; - Rank order  * &#x60;short_answer&#x60; - Short answer  * &#x60;long_answer&#x60; - Long answer.  * &#x60;fill_in_the_blank&#x60; - Fill in the blank  * &#x60;rating_scale&#x60; - Rating scale. | [optional] 
**answer_required** | **bool** | Whether participants must answer the question.  * &#x60;true&#x60; - The participant must answer the question.  * &#x60;false&#x60; - The participant does not need to answer the question.    This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**show_as_dropdown** | **bool** | Whether to display the radio selection as a drop-down box.  * &#x60;true&#x60; - Show as a drop-down box.  * &#x60;false&#x60; - Do not show as a drop-down box.    This value defaults to &#x60;false&#x60;. | [optional] [default to False]
**answers** | **list[str]** | The survey question&#x27;s available answers. This field requires a **minimum** of two answers.   * For &#x60;single&#x60; and &#x60;multiple&#x60; questions, you can only provide a maximum of 50 answers.  * For &#x60;matching&#x60; polls, you can only provide a maximum of 16 answers.  * For &#x60;rank_order&#x60; polls, you can only provide a maximum of seven answers. | [optional] 
**prompts** | [**list[MeetingsmeetingIdsurveyCustomSurveyPrompts]**](MeetingsmeetingIdsurveyCustomSurveyPrompts.md) | Information about the prompt questions. This field only applies to &#x60;matching&#x60; and &#x60;rank_order&#x60; questions. You **must** provide a minimum of two prompts, up to a maximum of 10 prompts. | [optional] 
**answer_min_character** | **int** | The allowed minimum number of characters. This field only applies to &#x60;short_answer&#x60; and &#x60;long_answer&#x60; questions. You must provide at least a **one** character minimum value. | [optional] 
**answer_max_character** | **int** | The allowed maximum number of characters. This field only applies to &#x60;short_answer&#x60; and &#x60;long_answer&#x60; questions.  * For &#x60;short_answer&#x60; question, a maximum of 500 characters.  * For &#x60;long_answer&#x60; question, a maximum of 2,000 characters. | [optional] 
**rating_min_value** | **int** | The rating scale&#x27;s minimum value. This value cannot be less than zero.    This field only applies to the &#x60;rating_scale&#x60; survey. | [optional] 
**rating_max_value** | **int** | The rating scale&#x27;s maximum value, up to a maximum value of 10.    This field only applies to the &#x60;rating_scale&#x60; survey. | [optional] 
**rating_min_label** | **str** | The low score label used for the &#x60;rating_min_value&#x60; field, up to 50 characters.    This field only applies to the &#x60;rating_scale&#x60; survey. | [optional] 
**rating_max_label** | **str** | The high score label used for the &#x60;rating_max_value&#x60; field, up to 50 characters.    This field only applies to the &#x60;rating_scale&#x60; survey. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

