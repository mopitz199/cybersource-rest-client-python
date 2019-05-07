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


class PtsV2PaymentsPost201ResponseProcessingInformation(object):
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
        'bank_transfer_options': 'PtsV2PaymentsPost201ResponseProcessingInformationBankTransferOptions'
    }

    attribute_map = {
        'bank_transfer_options': 'bankTransferOptions'
    }

    def __init__(self, bank_transfer_options=None):
        """
        PtsV2PaymentsPost201ResponseProcessingInformation - a model defined in Swagger
        """

        self._bank_transfer_options = None

        if bank_transfer_options is not None:
          self.bank_transfer_options = bank_transfer_options

    @property
    def bank_transfer_options(self):
        """
        Gets the bank_transfer_options of this PtsV2PaymentsPost201ResponseProcessingInformation.

        :return: The bank_transfer_options of this PtsV2PaymentsPost201ResponseProcessingInformation.
        :rtype: PtsV2PaymentsPost201ResponseProcessingInformationBankTransferOptions
        """
        return self._bank_transfer_options

    @bank_transfer_options.setter
    def bank_transfer_options(self, bank_transfer_options):
        """
        Sets the bank_transfer_options of this PtsV2PaymentsPost201ResponseProcessingInformation.

        :param bank_transfer_options: The bank_transfer_options of this PtsV2PaymentsPost201ResponseProcessingInformation.
        :type: PtsV2PaymentsPost201ResponseProcessingInformationBankTransferOptions
        """

        self._bank_transfer_options = bank_transfer_options

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
