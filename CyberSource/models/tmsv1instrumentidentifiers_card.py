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


class Tmsv1instrumentidentifiersCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'security_code': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'security_code': 'securityCode'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, security_code=None):
        """
        Tmsv1instrumentidentifiersCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._security_code = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if security_code is not None:
          self.security_code = security_code

    @property
    def number(self):
        """
        Gets the number of this Tmsv1instrumentidentifiersCard.
        Credit card number (PAN).

        :return: The number of this Tmsv1instrumentidentifiersCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Tmsv1instrumentidentifiersCard.
        Credit card number (PAN).

        :param number: The number of this Tmsv1instrumentidentifiersCard.
        :type: str
        """
        if number is not None and len(number) > 19:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `19`")
        if number is not None and len(number) < 12:
            raise ValueError("Invalid value for `number`, length must be greater than or equal to `12`")

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Tmsv1instrumentidentifiersCard.
        Card expiration month.  Format: `MM`. Possible values: `01` through `12`. 

        :return: The expiration_month of this Tmsv1instrumentidentifiersCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Tmsv1instrumentidentifiersCard.
        Card expiration month.  Format: `MM`. Possible values: `01` through `12`. 

        :param expiration_month: The expiration_month of this Tmsv1instrumentidentifiersCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")
        if expiration_month is not None and len(expiration_month) < 2:
            raise ValueError("Invalid value for `expiration_month`, length must be greater than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Tmsv1instrumentidentifiersCard.
        Card expiration year. Format: `YYYY`. Possible values: `1900` through `2099`. 

        :return: The expiration_year of this Tmsv1instrumentidentifiersCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Tmsv1instrumentidentifiersCard.
        Card expiration year. Format: `YYYY`. Possible values: `1900` through `2099`. 

        :param expiration_year: The expiration_year of this Tmsv1instrumentidentifiersCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")
        if expiration_year is not None and len(expiration_year) < 4:
            raise ValueError("Invalid value for `expiration_year`, length must be greater than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def security_code(self):
        """
        Gets the security_code of this Tmsv1instrumentidentifiersCard.
        Card security code.

        :return: The security_code of this Tmsv1instrumentidentifiersCard.
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """
        Sets the security_code of this Tmsv1instrumentidentifiersCard.
        Card security code.

        :param security_code: The security_code of this Tmsv1instrumentidentifiersCard.
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")
        if security_code is not None and len(security_code) < 3:
            raise ValueError("Invalid value for `security_code`, length must be greater than or equal to `3`")

        self._security_code = security_code

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
        if not isinstance(other, Tmsv1instrumentidentifiersCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
