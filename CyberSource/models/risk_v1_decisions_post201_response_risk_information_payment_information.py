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


class RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation(object):
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
        'bin_country': 'str',
        'account_type': 'str',
        'issuer': 'str',
        'scheme': 'str',
        'bin': 'str'
    }

    attribute_map = {
        'bin_country': 'binCountry',
        'account_type': 'accountType',
        'issuer': 'issuer',
        'scheme': 'scheme',
        'bin': 'bin'
    }

    def __init__(self, bin_country=None, account_type=None, issuer=None, scheme=None, bin=None):
        """
        RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation - a model defined in Swagger
        """

        self._bin_country = None
        self._account_type = None
        self._issuer = None
        self._scheme = None
        self._bin = None

        if bin_country is not None:
          self.bin_country = bin_country
        if account_type is not None:
          self.account_type = account_type
        if issuer is not None:
          self.issuer = issuer
        if scheme is not None:
          self.scheme = scheme
        if bin is not None:
          self.bin = bin

    @property
    def bin_country(self):
        """
        Gets the bin_country of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer’s card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the Business Center. 

        :return: The bin_country of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :rtype: str
        """
        return self._bin_country

    @bin_country.setter
    def bin_country(self, bin_country):
        """
        Sets the bin_country of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer’s card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the Business Center. 

        :param bin_country: The bin_country of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :type: str
        """
        if bin_country is not None and len(bin_country) > 255:
            raise ValueError("Invalid value for `bin_country`, length must be less than or equal to `255`")

        self._bin_country = bin_country

    @property
    def account_type(self):
        """
        Gets the account_type of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type. 

        :return: The account_type of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type. 

        :param account_type: The account_type of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :type: str
        """
        if account_type is not None and len(account_type) > 255:
            raise ValueError("Invalid value for `account_type`, length must be less than or equal to `255`")

        self._account_type = account_type

    @property
    def issuer(self):
        """
        Gets the issuer of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Name of the bank or entity that issued the card account.

        :return: The issuer of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Name of the bank or entity that issued the card account.

        :param issuer: The issuer of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :type: str
        """
        if issuer is not None and len(issuer) > 255:
            raise ValueError("Invalid value for `issuer`, length must be less than or equal to `255`")

        self._issuer = issuer

    @property
    def scheme(self):
        """
        Gets the scheme of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron *Note:* Additional values may be present. 

        :return: The scheme of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """
        Sets the scheme of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron *Note:* Additional values may be present. 

        :param scheme: The scheme of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :type: str
        """
        if scheme is not None and len(scheme) > 255:
            raise ValueError("Invalid value for `scheme`, length must be less than or equal to `255`")

        self._scheme = scheme

    @property
    def bin(self):
        """
        Gets the bin of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `bin` request field or from the first six characters of the `number` field. 

        :return: The bin of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `bin` request field or from the first six characters of the `number` field. 

        :param bin: The bin of this RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation.
        :type: str
        """
        if bin is not None and len(bin) > 255:
            raise ValueError("Invalid value for `bin`, length must be less than or equal to `255`")

        self._bin = bin

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
        if not isinstance(other, RiskV1DecisionsPost201ResponseRiskInformationPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
