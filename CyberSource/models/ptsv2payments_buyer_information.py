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


class Ptsv2paymentsBuyerInformation(object):
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
        'merchant_customer_id': 'str',
        'date_of_birth': 'str',
        'vat_registration_number': 'str',
        'company_tax_id': 'str',
        'personal_identification': 'list[Ptsv2paymentsBuyerInformationPersonalIdentification]',
        'hashed_password': 'str',
        'mobile_phone': 'int'
    }

    attribute_map = {
        'merchant_customer_id': 'merchantCustomerId',
        'date_of_birth': 'dateOfBirth',
        'vat_registration_number': 'vatRegistrationNumber',
        'company_tax_id': 'companyTaxId',
        'personal_identification': 'personalIdentification',
        'hashed_password': 'hashedPassword',
        'mobile_phone': 'mobilePhone'
    }

    def __init__(self, merchant_customer_id=None, date_of_birth=None, vat_registration_number=None, company_tax_id=None, personal_identification=None, hashed_password=None, mobile_phone=None):
        """
        Ptsv2paymentsBuyerInformation - a model defined in Swagger
        """

        self._merchant_customer_id = None
        self._date_of_birth = None
        self._vat_registration_number = None
        self._company_tax_id = None
        self._personal_identification = None
        self._hashed_password = None
        self._mobile_phone = None

        if merchant_customer_id is not None:
          self.merchant_customer_id = merchant_customer_id
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if company_tax_id is not None:
          self.company_tax_id = company_tax_id
        if personal_identification is not None:
          self.personal_identification = personal_identification
        if hashed_password is not None:
          self.hashed_password = hashed_password
        if mobile_phone is not None:
          self.mobile_phone = mobile_phone

    @property
    def merchant_customer_id(self):
        """
        Gets the merchant_customer_id of this Ptsv2paymentsBuyerInformation.
        Your identifier for the customer.  When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.  #### Comercio Latino For recurring payments in Mexico, the value is the customer’s contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.  #### Worldpay VAP For a follow-on credit with Worldpay VAP, CyberSource checks the following locations, in the order given, for a customer account ID value and uses the first value it finds: 1. `customer_account_id` value in the follow-on credit request 2. Customer account ID value that was used for the capture that is being credited 3. Customer account ID value that was used for the original authorization If a customer account ID value cannot be found in any of these locations, then no value is used.  For processor-specific information, see the `customer_account_id` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The merchant_customer_id of this Ptsv2paymentsBuyerInformation.
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """
        Sets the merchant_customer_id of this Ptsv2paymentsBuyerInformation.
        Your identifier for the customer.  When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.  #### Comercio Latino For recurring payments in Mexico, the value is the customer’s contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.  #### Worldpay VAP For a follow-on credit with Worldpay VAP, CyberSource checks the following locations, in the order given, for a customer account ID value and uses the first value it finds: 1. `customer_account_id` value in the follow-on credit request 2. Customer account ID value that was used for the capture that is being credited 3. Customer account ID value that was used for the original authorization If a customer account ID value cannot be found in any of these locations, then no value is used.  For processor-specific information, see the `customer_account_id` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param merchant_customer_id: The merchant_customer_id of this Ptsv2paymentsBuyerInformation.
        :type: str
        """
        if merchant_customer_id is not None and len(merchant_customer_id) > 100:
            raise ValueError("Invalid value for `merchant_customer_id`, length must be less than or equal to `100`")

        self._merchant_customer_id = merchant_customer_id

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this Ptsv2paymentsBuyerInformation.
        Recipient’s date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The date_of_birth of this Ptsv2paymentsBuyerInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this Ptsv2paymentsBuyerInformation.
        Recipient’s date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param date_of_birth: The date_of_birth of this Ptsv2paymentsBuyerInformation.
        :type: str
        """
        if date_of_birth is not None and len(date_of_birth) > 8:
            raise ValueError("Invalid value for `date_of_birth`, length must be less than or equal to `8`")

        self._date_of_birth = date_of_birth

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this Ptsv2paymentsBuyerInformation.
        Customer’s government-assigned tax identification number.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this Ptsv2paymentsBuyerInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this Ptsv2paymentsBuyerInformation.
        Customer’s government-assigned tax identification number.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this Ptsv2paymentsBuyerInformation.
        :type: str
        """
        if vat_registration_number is not None and len(vat_registration_number) > 20:
            raise ValueError("Invalid value for `vat_registration_number`, length must be less than or equal to `20`")

        self._vat_registration_number = vat_registration_number

    @property
    def company_tax_id(self):
        """
        Gets the company_tax_id of this Ptsv2paymentsBuyerInformation.
        Company’s tax identifier. This is only used for eCheck service.  ** TeleCheck ** Contact your TeleCheck representative to find out whether this field is required or optional.  ** All Other Processors ** Not used. 

        :return: The company_tax_id of this Ptsv2paymentsBuyerInformation.
        :rtype: str
        """
        return self._company_tax_id

    @company_tax_id.setter
    def company_tax_id(self, company_tax_id):
        """
        Sets the company_tax_id of this Ptsv2paymentsBuyerInformation.
        Company’s tax identifier. This is only used for eCheck service.  ** TeleCheck ** Contact your TeleCheck representative to find out whether this field is required or optional.  ** All Other Processors ** Not used. 

        :param company_tax_id: The company_tax_id of this Ptsv2paymentsBuyerInformation.
        :type: str
        """
        if company_tax_id is not None and len(company_tax_id) > 9:
            raise ValueError("Invalid value for `company_tax_id`, length must be less than or equal to `9`")

        self._company_tax_id = company_tax_id

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this Ptsv2paymentsBuyerInformation.

        :return: The personal_identification of this Ptsv2paymentsBuyerInformation.
        :rtype: list[Ptsv2paymentsBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this Ptsv2paymentsBuyerInformation.

        :param personal_identification: The personal_identification of this Ptsv2paymentsBuyerInformation.
        :type: list[Ptsv2paymentsBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

    @property
    def hashed_password(self):
        """
        Gets the hashed_password of this Ptsv2paymentsBuyerInformation.
        The merchant's password that CyberSource hashes and stores as a hashed password.  For details about this field, see the `customer_password` field description in _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The hashed_password of this Ptsv2paymentsBuyerInformation.
        :rtype: str
        """
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        """
        Sets the hashed_password of this Ptsv2paymentsBuyerInformation.
        The merchant's password that CyberSource hashes and stores as a hashed password.  For details about this field, see the `customer_password` field description in _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param hashed_password: The hashed_password of this Ptsv2paymentsBuyerInformation.
        :type: str
        """
        if hashed_password is not None and len(hashed_password) > 100:
            raise ValueError("Invalid value for `hashed_password`, length must be less than or equal to `100`")

        self._hashed_password = hashed_password

    @property
    def mobile_phone(self):
        """
        Gets the mobile_phone of this Ptsv2paymentsBuyerInformation.
        Cardholder’s mobile phone number. **Important** Required for Visa Secure transactions in Brazil. Do not use this request field for any other types of transactions. 

        :return: The mobile_phone of this Ptsv2paymentsBuyerInformation.
        :rtype: int
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """
        Sets the mobile_phone of this Ptsv2paymentsBuyerInformation.
        Cardholder’s mobile phone number. **Important** Required for Visa Secure transactions in Brazil. Do not use this request field for any other types of transactions. 

        :param mobile_phone: The mobile_phone of this Ptsv2paymentsBuyerInformation.
        :type: int
        """

        self._mobile_phone = mobile_phone

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
        if not isinstance(other, Ptsv2paymentsBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
