# Ptsv2paymentsClientReferenceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization**\\ Required field.  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports.  | [optional] 
**transaction_id** | **str** | Identifier that you assign to the transaction.  **Note** Use this field only if you want to support merchant-initiated reversal and void operations.  #### Used by **Authorization, Authorization Reversal, Capture, Credit, and Void**\\ Optional field.  | [optional] 
**comments** | **str** | Comments | [optional] 
**partner** | [**Ptsv2paymentsClientReferenceInformationPartner**](Ptsv2paymentsClientReferenceInformationPartner.md) |  | [optional] 
**application_name** | **str** | The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource.  | [optional] 
**application_version** | **str** | Version of the CyberSource application or integration used for a transaction.  | [optional] 
**application_user** | **str** | The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


