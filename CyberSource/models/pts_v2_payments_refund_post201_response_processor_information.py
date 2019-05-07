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


class PtsV2PaymentsRefundPost201ResponseProcessorInformation(object):
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
        'transaction_id': 'str',
        'forwarded_acquirer_code': 'str',
        'merchant_number': 'str',
        'response_code': 'str',
        'ach_verification': 'PtsV2PaymentsPost201ResponseProcessorInformationAchVerification'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'forwarded_acquirer_code': 'forwardedAcquirerCode',
        'merchant_number': 'merchantNumber',
        'response_code': 'responseCode',
        'ach_verification': 'achVerification'
    }

    def __init__(self, transaction_id=None, forwarded_acquirer_code=None, merchant_number=None, response_code=None, ach_verification=None):
        """
        PtsV2PaymentsRefundPost201ResponseProcessorInformation - a model defined in Swagger
        """

        self._transaction_id = None
        self._forwarded_acquirer_code = None
        self._merchant_number = None
        self._response_code = None
        self._ach_verification = None

        if transaction_id is not None:
          self.transaction_id = transaction_id
        if forwarded_acquirer_code is not None:
          self.forwarded_acquirer_code = forwarded_acquirer_code
        if merchant_number is not None:
          self.merchant_number = merchant_number
        if response_code is not None:
          self.response_code = response_code
        if ach_verification is not None:
          self.ach_verification = ach_verification

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Processor transaction ID.  This value identifies the transaction on a host system. This value is supported only for Moneris. It contains this information:   - Terminal used to process the transaction  - Shift during which the transaction took place  - Batch number  - Transaction number within the batch  You must store this value. If you give the customer a receipt, display this value on the receipt.  Example For the value 66012345001069003:   - Terminal ID = 66012345  - Shift number = 001  - Batch number = 069  - Transaction number = 003 

        :return: The transaction_id of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Processor transaction ID.  This value identifies the transaction on a host system. This value is supported only for Moneris. It contains this information:   - Terminal used to process the transaction  - Shift during which the transaction took place  - Batch number  - Transaction number within the batch  You must store this value. If you give the customer a receipt, display this value on the receipt.  Example For the value 66012345001069003:   - Terminal ID = 66012345  - Shift number = 001  - Batch number = 069  - Transaction number = 003 

        :param transaction_id: The transaction_id of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :type: str
        """
        if transaction_id is not None and len(transaction_id) > 18:
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `18`")

        self._transaction_id = transaction_id

    @property
    def forwarded_acquirer_code(self):
        """
        Gets the forwarded_acquirer_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Name of the Japanese acquirer that processed the transaction. Returned only for CCS (CAFIS) and JCN Gateway. Please contact the CyberSource Japan Support Group for more information. 

        :return: The forwarded_acquirer_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._forwarded_acquirer_code

    @forwarded_acquirer_code.setter
    def forwarded_acquirer_code(self, forwarded_acquirer_code):
        """
        Sets the forwarded_acquirer_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Name of the Japanese acquirer that processed the transaction. Returned only for CCS (CAFIS) and JCN Gateway. Please contact the CyberSource Japan Support Group for more information. 

        :param forwarded_acquirer_code: The forwarded_acquirer_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :type: str
        """
        if forwarded_acquirer_code is not None and len(forwarded_acquirer_code) > 32:
            raise ValueError("Invalid value for `forwarded_acquirer_code`, length must be less than or equal to `32`")

        self._forwarded_acquirer_code = forwarded_acquirer_code

    @property
    def merchant_number(self):
        """
        Gets the merchant_number of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Identifier that was assigned to you by your acquirer.  This value must be printed on the receipt.  This field is supported only on **American Express Direct**, **FDC Nashville Global**, and **SIX**. 

        :return: The merchant_number of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """
        Sets the merchant_number of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        Identifier that was assigned to you by your acquirer.  This value must be printed on the receipt.  This field is supported only on **American Express Direct**, **FDC Nashville Global**, and **SIX**. 

        :param merchant_number: The merchant_number of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :type: str
        """
        if merchant_number is not None and len(merchant_number) > 15:
            raise ValueError("Invalid value for `merchant_number`, length must be less than or equal to `15`")

        self._merchant_number = merchant_number

    @property
    def response_code(self):
        """
        Gets the response_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  Important Do not use this field to evaluate the result of the authorization. 

        :return: The response_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  Important Do not use this field to evaluate the result of the authorization. 

        :param response_code: The response_code of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :type: str
        """
        if response_code is not None and len(response_code) > 10:
            raise ValueError("Invalid value for `response_code`, length must be less than or equal to `10`")

        self._response_code = response_code

    @property
    def ach_verification(self):
        """
        Gets the ach_verification of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.

        :return: The ach_verification of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :rtype: PtsV2PaymentsPost201ResponseProcessorInformationAchVerification
        """
        return self._ach_verification

    @ach_verification.setter
    def ach_verification(self, ach_verification):
        """
        Sets the ach_verification of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.

        :param ach_verification: The ach_verification of this PtsV2PaymentsRefundPost201ResponseProcessorInformation.
        :type: PtsV2PaymentsPost201ResponseProcessorInformationAchVerification
        """

        self._ach_verification = ach_verification

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
        if not isinstance(other, PtsV2PaymentsRefundPost201ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
