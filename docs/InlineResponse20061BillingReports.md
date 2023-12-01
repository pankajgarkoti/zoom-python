# InlineResponse20061BillingReports

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | End date of the billing period. | [optional] 
**id** | **str** | Unique Identifier of the report. Use this ID to retrieve billing invoice via the &amp;quot;Get Billing Invoices API&amp;quot;.   You can also use this ID to export a CSV file of the billing report from this URL: &#x60;https://zoom.us/account/report/billing/export?id&#x3D;{id}&#x60;. | [optional] 
**start_date** | **date** | Start date of the billing period. | [optional] 
**tax_amount** | **str** | Total tax amount for this billing period. | [optional] 
**total_amount** | **str** | Total billing amount for this billing period. | [optional] 
**type** | **int** | Type of the billing report. The value should be either of the following:     &#x60;0&#x60; - Detailed Billing Reports &#x60;1&#x60; - Custom Billing Reports | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

