# PtsV2PaymentsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2PaymentsPost201ResponseLinks**](PtsV2PaymentsPost201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; Example &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  | [optional] 
**status** | **str** | The status of the submitted transaction.  Possible values:  - AUTHORIZED  - PARTIAL_AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - AUTHORIZED_RISK_DECLINED  - PENDING_AUTHENTICATION  - PENDING_REVIEW  - DECLINED  - INVALID_REQUEST  | [optional] 
**reconciliation_id** | **str** | Reference number for the transaction. This value is not returned for all processors.  Returned by authorization service.  #### Atos Positive string (6)  #### All other processors String (60)  | [optional] 
**error_information** | [**PtsV2PaymentsPost201ResponseErrorInformation**](PtsV2PaymentsPost201ResponseErrorInformation.md) |  | [optional] 
**client_reference_information** | [**PtsV2PaymentsPost201ResponseClientReferenceInformation**](PtsV2PaymentsPost201ResponseClientReferenceInformation.md) |  | [optional] 
**processing_information** | [**PtsV2PaymentsPost201ResponseProcessingInformation**](PtsV2PaymentsPost201ResponseProcessingInformation.md) |  | [optional] 
**processor_information** | [**PtsV2PaymentsPost201ResponseProcessorInformation**](PtsV2PaymentsPost201ResponseProcessorInformation.md) |  | [optional] 
**issuer_information** | [**PtsV2PaymentsPost201ResponseIssuerInformation**](PtsV2PaymentsPost201ResponseIssuerInformation.md) |  | [optional] 
**payment_information** | [**PtsV2PaymentsPost201ResponsePaymentInformation**](PtsV2PaymentsPost201ResponsePaymentInformation.md) |  | [optional] 
**order_information** | [**PtsV2PaymentsPost201ResponseOrderInformation**](PtsV2PaymentsPost201ResponseOrderInformation.md) |  | [optional] 
**point_of_sale_information** | [**PtsV2PaymentsPost201ResponsePointOfSaleInformation**](PtsV2PaymentsPost201ResponsePointOfSaleInformation.md) |  | [optional] 
**installment_information** | [**PtsV2PaymentsPost201ResponseInstallmentInformation**](PtsV2PaymentsPost201ResponseInstallmentInformation.md) |  | [optional] 
**risk_information** | [**PtsV2PaymentsPost201ResponseRiskInformation**](PtsV2PaymentsPost201ResponseRiskInformation.md) |  | [optional] 
**consumer_authentication_information** | [**PtsV2PaymentsPost201ResponseConsumerAuthenticationInformation**](PtsV2PaymentsPost201ResponseConsumerAuthenticationInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


