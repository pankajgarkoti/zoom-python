# InlineResponse20068

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The meeting ID in &amp;quot;**long**&amp;quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**questions** | [**list[InlineResponse20068Questions]**](InlineResponse20068Questions.md) | Array of meeting question objects. | [optional] 
**start_time** | **datetime** | Meeting start time. | [optional] 
**uuid** | **str** | The meeting UUID. Each meeting instance will generate its own UUID - for example, after a meeting ends, a new UUID will be generated for the next instance of the Meeting. Double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

