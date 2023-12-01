# WebinarIdBatchRegistrantsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_approve** | **bool** | If a meeting was scheduled with approval_type &#x60;1&#x60; (manual approval), but you want to automatically approve registrants added via this API, set the value of this field to &#x60;true&#x60;.   You **cannot** use this field to change approval setting for a meeting that was originally scheduled with approval_type &#x60;0&#x60; (automatic approval). | [optional] 
**registrants** | [**list[WebinarswebinarIdbatchRegistrantsRegistrants]**](WebinarswebinarIdbatchRegistrantsRegistrants.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

