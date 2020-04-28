# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PtsV2PaymentsPost201Response(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'PtsV2PaymentsPost201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'reconciliation_id': 'str',
        'error_information': 'PtsV2PaymentsPost201ResponseErrorInformation',
        'client_reference_information': 'PtsV2PaymentsPost201ResponseClientReferenceInformation',
        'processing_information': 'PtsV2PaymentsPost201ResponseProcessingInformation',
        'processor_information': 'PtsV2PaymentsPost201ResponseProcessorInformation',
        'issuer_information': 'PtsV2PaymentsPost201ResponseIssuerInformation',
        'payment_information': 'PtsV2PaymentsPost201ResponsePaymentInformation',
        'order_information': 'PtsV2PaymentsPost201ResponseOrderInformation',
        'point_of_sale_information': 'PtsV2PaymentsPost201ResponsePointOfSaleInformation',
        'installment_information': 'PtsV2PaymentsPost201ResponseInstallmentInformation',
        'risk_information': 'PtsV2PaymentsPost201ResponseRiskInformation',
        'consumer_authentication_information': 'PtsV2PaymentsPost201ResponseConsumerAuthenticationInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'reconciliation_id': 'reconciliationId',
        'error_information': 'errorInformation',
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'processor_information': 'processorInformation',
        'issuer_information': 'issuerInformation',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'installment_information': 'installmentInformation',
        'risk_information': 'riskInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, reconciliation_id=None, error_information=None, client_reference_information=None, processing_information=None, processor_information=None, issuer_information=None, payment_information=None, order_information=None, point_of_sale_information=None, installment_information=None, risk_information=None, consumer_authentication_information=None):
        """
        PtsV2PaymentsPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._reconciliation_id = None
        self._error_information = None
        self._client_reference_information = None
        self._processing_information = None
        self._processor_information = None
        self._issuer_information = None
        self._payment_information = None
        self._order_information = None
        self._point_of_sale_information = None
        self._installment_information = None
        self._risk_information = None
        self._consumer_authentication_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if error_information is not None:
          self.error_information = error_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if processor_information is not None:
          self.processor_information = processor_information
        if issuer_information is not None:
          self.issuer_information = issuer_information
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if installment_information is not None:
          self.installment_information = installment_information
        if risk_information is not None:
          self.risk_information = risk_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information

    @property
    def links(self):
        """
        Gets the links of this PtsV2PaymentsPost201Response.

        :return: The links of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PtsV2PaymentsPost201Response.

        :param links: The links of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PtsV2PaymentsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this PtsV2PaymentsPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2PaymentsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this PtsV2PaymentsPost201Response.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV2PaymentsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this PtsV2PaymentsPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV2PaymentsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this PtsV2PaymentsPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this PtsV2PaymentsPost201Response.
        The status of the submitted transaction.  Possible values:  - AUTHORIZED  - PARTIAL_AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - DECLINED  - INVALID_REQUEST 

        :return: The status of this PtsV2PaymentsPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2PaymentsPost201Response.
        The status of the submitted transaction.  Possible values:  - AUTHORIZED  - PARTIAL_AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - DECLINED  - INVALID_REQUEST 

        :param status: The status of this PtsV2PaymentsPost201Response.
        :type: str
        """

        self._status = status

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this PtsV2PaymentsPost201Response.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :return: The reconciliation_id of this PtsV2PaymentsPost201Response.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this PtsV2PaymentsPost201Response.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :param reconciliation_id: The reconciliation_id of this PtsV2PaymentsPost201Response.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def error_information(self):
        """
        Gets the error_information of this PtsV2PaymentsPost201Response.

        :return: The error_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this PtsV2PaymentsPost201Response.

        :param error_information: The error_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseErrorInformation
        """

        self._error_information = error_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PtsV2PaymentsPost201Response.

        :return: The client_reference_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PtsV2PaymentsPost201Response.

        :param client_reference_information: The client_reference_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this PtsV2PaymentsPost201Response.

        :return: The processing_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this PtsV2PaymentsPost201Response.

        :param processing_information: The processing_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this PtsV2PaymentsPost201Response.

        :return: The processor_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this PtsV2PaymentsPost201Response.

        :param processor_information: The processor_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def issuer_information(self):
        """
        Gets the issuer_information of this PtsV2PaymentsPost201Response.

        :return: The issuer_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseIssuerInformation
        """
        return self._issuer_information

    @issuer_information.setter
    def issuer_information(self, issuer_information):
        """
        Sets the issuer_information of this PtsV2PaymentsPost201Response.

        :param issuer_information: The issuer_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseIssuerInformation
        """

        self._issuer_information = issuer_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this PtsV2PaymentsPost201Response.

        :return: The payment_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this PtsV2PaymentsPost201Response.

        :param payment_information: The payment_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponsePaymentInformation
        """

        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this PtsV2PaymentsPost201Response.

        :return: The order_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this PtsV2PaymentsPost201Response.

        :param order_information: The order_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseOrderInformation
        """

        self._order_information = order_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this PtsV2PaymentsPost201Response.

        :return: The point_of_sale_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponsePointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this PtsV2PaymentsPost201Response.

        :param point_of_sale_information: The point_of_sale_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponsePointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this PtsV2PaymentsPost201Response.

        :return: The installment_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this PtsV2PaymentsPost201Response.

        :param installment_information: The installment_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseInstallmentInformation
        """

        self._installment_information = installment_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this PtsV2PaymentsPost201Response.

        :return: The risk_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this PtsV2PaymentsPost201Response.

        :param risk_information: The risk_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseRiskInformation
        """

        self._risk_information = risk_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this PtsV2PaymentsPost201Response.

        :return: The consumer_authentication_information of this PtsV2PaymentsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this PtsV2PaymentsPost201Response.

        :param consumer_authentication_information: The consumer_authentication_information of this PtsV2PaymentsPost201Response.
        :type: PtsV2PaymentsPost201ResponseConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PtsV2PaymentsPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
