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


class Ptsv2payoutsMerchantInformationMerchantDescriptor(object):
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
        'locality': 'str',
        'country': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'contact': 'str'
    }

    attribute_map = {
        'name': 'name',
        'locality': 'locality',
        'country': 'country',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'contact': 'contact'
    }

    def __init__(self, name=None, locality=None, country=None, administrative_area=None, postal_code=None, contact=None):
        """
        Ptsv2payoutsMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._name = None
        self._locality = None
        self._country = None
        self._administrative_area = None
        self._postal_code = None
        self._contact = None

        if name is not None:
          self.name = name
        if locality is not None:
          self.locality = locality
        if country is not None:
          self.country = country
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if contact is not None:
          self.contact = contact

    @property
    def name(self):
        """
        Gets the name of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's name.  For more details about the merchant-related fields, see the `merchant_descriptor` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22. 

        :return: The name of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's name.  For more details about the merchant-related fields, see the `merchant_descriptor` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22. 

        :param name: The name of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._name = name

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's City.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_city` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The locality of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's City.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_city` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param locality: The locality of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """
        if locality is not None and len(locality) > 13:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `13`")

        self._locality = locality

    @property
    def country(self):
        """
        Gets the country of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's country.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_country` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The country of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's country.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_country` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param country: The country of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._country = country

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_state` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  Merchant State. For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The administrative_area of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_state` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  Merchant State. For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param administrative_area: The administrative_area of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's postal code.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_postal_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The postal_code of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        Merchant's postal code.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_postal_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param postal_code: The postal_code of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 14:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `14`")

        self._postal_code = postal_code

    @property
    def contact(self):
        """
        Gets the contact of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_contact` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> Contact information for the merchant.  **Note** These are the maximum data lengths for the following payment processors: - FDCCompass (13) - Paymentech (13) 

        :return: The contact of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_contact` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> Contact information for the merchant.  **Note** These are the maximum data lengths for the following payment processors: - FDCCompass (13) - Paymentech (13) 

        :param contact: The contact of this Ptsv2payoutsMerchantInformationMerchantDescriptor.
        :type: str
        """
        if contact is not None and len(contact) > 14:
            raise ValueError("Invalid value for `contact`, length must be less than or equal to `14`")

        self._contact = contact

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
        if not isinstance(other, Ptsv2payoutsMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
