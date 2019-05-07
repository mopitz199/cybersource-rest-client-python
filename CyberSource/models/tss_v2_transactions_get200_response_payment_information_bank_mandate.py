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


class TssV2TransactionsGet200ResponsePaymentInformationBankMandate(object):
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
        'reference_number': 'str',
        'recurring_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'reference_number': 'referenceNumber',
        'recurring_type': 'recurringType',
        'id': 'id'
    }

    def __init__(self, reference_number=None, recurring_type=None, id=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformationBankMandate - a model defined in Swagger
        """

        self._reference_number = None
        self._recurring_type = None
        self._id = None

        if reference_number is not None:
          self.reference_number = reference_number
        if recurring_type is not None:
          self.recurring_type = recurring_type
        if id is not None:
          self.id = id

    @property
    def reference_number(self):
        """
        Gets the reference_number of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :return: The reference_number of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """
        Sets the reference_number of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :param reference_number: The reference_number of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :type: str
        """

        self._reference_number = reference_number

    @property
    def recurring_type(self):
        """
        Gets the recurring_type of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :return: The recurring_type of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :rtype: str
        """
        return self._recurring_type

    @recurring_type.setter
    def recurring_type(self, recurring_type):
        """
        Sets the recurring_type of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :param recurring_type: The recurring_type of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :type: str
        """

        self._recurring_type = recurring_type

    @property
    def id(self):
        """
        Gets the id of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :return: The id of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        The description for this field is not available.

        :param id: The id of this TssV2TransactionsGet200ResponsePaymentInformationBankMandate.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformationBankMandate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
