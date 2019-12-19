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


class Ptsv2paymentsidcapturesProcessingInformation(object):
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
        'payment_solution': 'str',
        'reconciliation_id': 'str',
        'link_id': 'str',
        'report_group': 'str',
        'visa_checkout_id': 'str',
        'purchase_level': 'str',
        'industry_data_type': 'str',
        'issuer': 'Ptsv2paymentsIssuerInformation',
        'authorization_options': 'Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions',
        'capture_options': 'Ptsv2paymentsidcapturesProcessingInformationCaptureOptions'
    }

    attribute_map = {
        'payment_solution': 'paymentSolution',
        'reconciliation_id': 'reconciliationId',
        'link_id': 'linkId',
        'report_group': 'reportGroup',
        'visa_checkout_id': 'visaCheckoutId',
        'purchase_level': 'purchaseLevel',
        'industry_data_type': 'industryDataType',
        'issuer': 'issuer',
        'authorization_options': 'authorizationOptions',
        'capture_options': 'captureOptions'
    }

    def __init__(self, payment_solution=None, reconciliation_id=None, link_id=None, report_group=None, visa_checkout_id=None, purchase_level=None, industry_data_type=None, issuer=None, authorization_options=None, capture_options=None):
        """
        Ptsv2paymentsidcapturesProcessingInformation - a model defined in Swagger
        """

        self._payment_solution = None
        self._reconciliation_id = None
        self._link_id = None
        self._report_group = None
        self._visa_checkout_id = None
        self._purchase_level = None
        self._industry_data_type = None
        self._issuer = None
        self._authorization_options = None
        self._capture_options = None

        if payment_solution is not None:
          self.payment_solution = payment_solution
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if link_id is not None:
          self.link_id = link_id
        if report_group is not None:
          self.report_group = report_group
        if visa_checkout_id is not None:
          self.visa_checkout_id = visa_checkout_id
        if purchase_level is not None:
          self.purchase_level = purchase_level
        if industry_data_type is not None:
          self.industry_data_type = industry_data_type
        if issuer is not None:
          self.issuer = issuer
        if authorization_options is not None:
          self.authorization_options = authorization_options
        if capture_options is not None:
          self.capture_options = capture_options

    @property
    def payment_solution(self):
        """
        Gets the payment_solution of this Ptsv2paymentsidcapturesProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :return: The payment_solution of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._payment_solution

    @payment_solution.setter
    def payment_solution(self, payment_solution):
        """
        Sets the payment_solution of this Ptsv2paymentsidcapturesProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :param payment_solution: The payment_solution of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if payment_solution is not None and len(payment_solution) > 12:
            raise ValueError("Invalid value for `payment_solution`, length must be less than or equal to `12`")

        self._payment_solution = payment_solution

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def link_id(self):
        """
        Gets the link_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The link_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """
        Sets the link_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param link_id: The link_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if link_id is not None and len(link_id) > 26:
            raise ValueError("Invalid value for `link_id`, length must be less than or equal to `26`")

        self._link_id = link_id

    @property
    def report_group(self):
        """
        Gets the report_group of this Ptsv2paymentsidcapturesProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The report_group of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._report_group

    @report_group.setter
    def report_group(self, report_group):
        """
        Sets the report_group of this Ptsv2paymentsidcapturesProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param report_group: The report_group of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if report_group is not None and len(report_group) > 25:
            raise ValueError("Invalid value for `report_group`, length must be less than or equal to `25`")

        self._report_group = report_group

    @property
    def visa_checkout_id(self):
        """
        Gets the visa_checkout_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  For details, see the `vc_order_id` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The visa_checkout_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._visa_checkout_id

    @visa_checkout_id.setter
    def visa_checkout_id(self, visa_checkout_id):
        """
        Sets the visa_checkout_id of this Ptsv2paymentsidcapturesProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  For details, see the `vc_order_id` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param visa_checkout_id: The visa_checkout_id of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if visa_checkout_id is not None and len(visa_checkout_id) > 48:
            raise ValueError("Invalid value for `visa_checkout_id`, length must be less than or equal to `48`")

        self._visa_checkout_id = visa_checkout_id

    @property
    def purchase_level(self):
        """
        Gets the purchase_level of this Ptsv2paymentsidcapturesProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :return: The purchase_level of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._purchase_level

    @purchase_level.setter
    def purchase_level(self, purchase_level):
        """
        Sets the purchase_level of this Ptsv2paymentsidcapturesProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :param purchase_level: The purchase_level of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if purchase_level is not None and len(purchase_level) > 1:
            raise ValueError("Invalid value for `purchase_level`, length must be less than or equal to `1`")

        self._purchase_level = purchase_level

    @property
    def industry_data_type(self):
        """
        Gets the industry_data_type of this Ptsv2paymentsidcapturesProcessingInformation.
        Flag that indicates whether the transaction includes airline or restaurant data.  To send the data in a transaction request to the processor, you must set this field to `airline` or `restaurant`.  **Note** If you do not set this field to one of the possible values, CyberSource does not send any data to the processor.  Possible Values: - `airline` - `restaurant` 

        :return: The industry_data_type of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: str
        """
        return self._industry_data_type

    @industry_data_type.setter
    def industry_data_type(self, industry_data_type):
        """
        Sets the industry_data_type of this Ptsv2paymentsidcapturesProcessingInformation.
        Flag that indicates whether the transaction includes airline or restaurant data.  To send the data in a transaction request to the processor, you must set this field to `airline` or `restaurant`.  **Note** If you do not set this field to one of the possible values, CyberSource does not send any data to the processor.  Possible Values: - `airline` - `restaurant` 

        :param industry_data_type: The industry_data_type of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: str
        """
        if industry_data_type is not None and len(industry_data_type) > 10:
            raise ValueError("Invalid value for `industry_data_type`, length must be less than or equal to `10`")

        self._industry_data_type = industry_data_type

    @property
    def issuer(self):
        """
        Gets the issuer of this Ptsv2paymentsidcapturesProcessingInformation.

        :return: The issuer of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: Ptsv2paymentsIssuerInformation
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this Ptsv2paymentsidcapturesProcessingInformation.

        :param issuer: The issuer of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: Ptsv2paymentsIssuerInformation
        """

        self._issuer = issuer

    @property
    def authorization_options(self):
        """
        Gets the authorization_options of this Ptsv2paymentsidcapturesProcessingInformation.

        :return: The authorization_options of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions
        """
        return self._authorization_options

    @authorization_options.setter
    def authorization_options(self, authorization_options):
        """
        Sets the authorization_options of this Ptsv2paymentsidcapturesProcessingInformation.

        :param authorization_options: The authorization_options of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: Ptsv2paymentsidcapturesProcessingInformationAuthorizationOptions
        """

        self._authorization_options = authorization_options

    @property
    def capture_options(self):
        """
        Gets the capture_options of this Ptsv2paymentsidcapturesProcessingInformation.

        :return: The capture_options of this Ptsv2paymentsidcapturesProcessingInformation.
        :rtype: Ptsv2paymentsidcapturesProcessingInformationCaptureOptions
        """
        return self._capture_options

    @capture_options.setter
    def capture_options(self, capture_options):
        """
        Sets the capture_options of this Ptsv2paymentsidcapturesProcessingInformation.

        :param capture_options: The capture_options of this Ptsv2paymentsidcapturesProcessingInformation.
        :type: Ptsv2paymentsidcapturesProcessingInformationCaptureOptions
        """

        self._capture_options = capture_options

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
        if not isinstance(other, Ptsv2paymentsidcapturesProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
