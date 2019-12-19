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


class Riskv1authenticationsMerchantInformationMerchantDescriptor(object):
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
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, name=None, url=None):
        """
        Riskv1authenticationsMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._name = None
        self._url = None

        if name is not None:
          self.name = name
        if url is not None:
          self.url = url

    @property
    def name(self):
        """
        Gets the name of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        Merchant's name.  For more details about the merchant-related fields, see the `merchant_descriptor` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22. 

        :return: The name of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        Merchant's name.  For more details about the merchant-related fields, see the `merchant_descriptor` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22. 

        :param name: The name of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """
        Gets the url of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        Address of company's website provided by merchant 

        :return: The url of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        Address of company's website provided by merchant 

        :param url: The url of this Riskv1authenticationsMerchantInformationMerchantDescriptor.
        :type: str
        """
        if url is not None and len(url) > 255:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `255`")

        self._url = url

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
        if not isinstance(other, Riskv1authenticationsMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
