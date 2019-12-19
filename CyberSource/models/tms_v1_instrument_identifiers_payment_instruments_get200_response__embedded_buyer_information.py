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


class TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation(object):
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
        'company_tax_id': 'str',
        'currency': 'str',
        'date_of_birth': 'str',
        'personal_identification': 'list[TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformationPersonalIdentification]'
    }

    attribute_map = {
        'company_tax_id': 'companyTaxID',
        'currency': 'currency',
        'date_of_birth': 'dateOfBirth',
        'personal_identification': 'personalIdentification'
    }

    def __init__(self, company_tax_id=None, currency=None, date_of_birth=None, personal_identification=None):
        """
        TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation - a model defined in Swagger
        """

        self._company_tax_id = None
        self._currency = None
        self._date_of_birth = None
        self._personal_identification = None

        if company_tax_id is not None:
          self.company_tax_id = company_tax_id
        if currency is not None:
          self.currency = currency
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if personal_identification is not None:
          self.personal_identification = personal_identification

    @property
    def company_tax_id(self):
        """
        Gets the company_tax_id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Tax identifier for the customer’s company.  **Important**: Contact your TeleCheck representative to find out whether this field is required or optional. 

        :return: The company_tax_id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :rtype: str
        """
        return self._company_tax_id

    @company_tax_id.setter
    def company_tax_id(self, company_tax_id):
        """
        Sets the company_tax_id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Tax identifier for the customer’s company.  **Important**: Contact your TeleCheck representative to find out whether this field is required or optional. 

        :param company_tax_id: The company_tax_id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :type: str
        """
        if company_tax_id is not None and len(company_tax_id) > 9:
            raise ValueError("Invalid value for `company_tax_id`, length must be less than or equal to `9`")

        self._company_tax_id = company_tax_id

    @property
    def currency(self):
        """
        Gets the currency of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Currency used by the customer. Accepts input in the ISO 4217 standard, stores as ISO 4217 Alpha.

        :return: The currency of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Currency used by the customer. Accepts input in the ISO 4217 standard, stores as ISO 4217 Alpha.

        :param currency: The currency of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")

        self._currency = currency

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Date of birth of the customer.  Format: `YYYY-MM-DD` or `YYYYMMDD` 

        :return: The date_of_birth of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        Date of birth of the customer.  Format: `YYYY-MM-DD` or `YYYYMMDD` 

        :param date_of_birth: The date_of_birth of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :type: str
        """
        if date_of_birth is not None and len(date_of_birth) > 10:
            raise ValueError("Invalid value for `date_of_birth`, length must be less than or equal to `10`")
        if date_of_birth is not None and len(date_of_birth) < 8:
            raise ValueError("Invalid value for `date_of_birth`, length must be greater than or equal to `8`")

        self._date_of_birth = date_of_birth

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.

        :return: The personal_identification of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :rtype: list[TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.

        :param personal_identification: The personal_identification of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation.
        :type: list[TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

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
        if not isinstance(other, TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
