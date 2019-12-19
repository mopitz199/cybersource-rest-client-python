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


class Ptsv2paymentsProcessingInformation(object):
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
        'capture': 'bool',
        'processor_id': 'str',
        'business_application_id': 'str',
        'commerce_indicator': 'str',
        'payment_solution': 'str',
        'reconciliation_id': 'str',
        'link_id': 'str',
        'purchase_level': 'str',
        'report_group': 'str',
        'visa_checkout_id': 'str',
        'industry_data_type': 'str',
        'authorization_options': 'Ptsv2paymentsProcessingInformationAuthorizationOptions',
        'capture_options': 'Ptsv2paymentsProcessingInformationCaptureOptions',
        'recurring_options': 'Ptsv2paymentsProcessingInformationRecurringOptions',
        'bank_transfer_options': 'Ptsv2paymentsProcessingInformationBankTransferOptions',
        'purchase_options': 'Ptsv2paymentsProcessingInformationPurchaseOptions',
        'electronic_benefits_transfer': 'Ptsv2paymentsProcessingInformationElectronicBenefitsTransfer'
    }

    attribute_map = {
        'capture': 'capture',
        'processor_id': 'processorId',
        'business_application_id': 'businessApplicationId',
        'commerce_indicator': 'commerceIndicator',
        'payment_solution': 'paymentSolution',
        'reconciliation_id': 'reconciliationId',
        'link_id': 'linkId',
        'purchase_level': 'purchaseLevel',
        'report_group': 'reportGroup',
        'visa_checkout_id': 'visaCheckoutId',
        'industry_data_type': 'industryDataType',
        'authorization_options': 'authorizationOptions',
        'capture_options': 'captureOptions',
        'recurring_options': 'recurringOptions',
        'bank_transfer_options': 'bankTransferOptions',
        'purchase_options': 'purchaseOptions',
        'electronic_benefits_transfer': 'electronicBenefitsTransfer'
    }

    def __init__(self, capture=False, processor_id=None, business_application_id=None, commerce_indicator=None, payment_solution=None, reconciliation_id=None, link_id=None, purchase_level=None, report_group=None, visa_checkout_id=None, industry_data_type=None, authorization_options=None, capture_options=None, recurring_options=None, bank_transfer_options=None, purchase_options=None, electronic_benefits_transfer=None):
        """
        Ptsv2paymentsProcessingInformation - a model defined in Swagger
        """

        self._capture = None
        self._processor_id = None
        self._business_application_id = None
        self._commerce_indicator = None
        self._payment_solution = None
        self._reconciliation_id = None
        self._link_id = None
        self._purchase_level = None
        self._report_group = None
        self._visa_checkout_id = None
        self._industry_data_type = None
        self._authorization_options = None
        self._capture_options = None
        self._recurring_options = None
        self._bank_transfer_options = None
        self._purchase_options = None
        self._electronic_benefits_transfer = None

        if capture is not None:
          self.capture = capture
        if processor_id is not None:
          self.processor_id = processor_id
        if business_application_id is not None:
          self.business_application_id = business_application_id
        if commerce_indicator is not None:
          self.commerce_indicator = commerce_indicator
        if payment_solution is not None:
          self.payment_solution = payment_solution
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if link_id is not None:
          self.link_id = link_id
        if purchase_level is not None:
          self.purchase_level = purchase_level
        if report_group is not None:
          self.report_group = report_group
        if visa_checkout_id is not None:
          self.visa_checkout_id = visa_checkout_id
        if industry_data_type is not None:
          self.industry_data_type = industry_data_type
        if authorization_options is not None:
          self.authorization_options = authorization_options
        if capture_options is not None:
          self.capture_options = capture_options
        if recurring_options is not None:
          self.recurring_options = recurring_options
        if bank_transfer_options is not None:
          self.bank_transfer_options = bank_transfer_options
        if purchase_options is not None:
          self.purchase_options = purchase_options
        if electronic_benefits_transfer is not None:
          self.electronic_benefits_transfer = electronic_benefits_transfer

    @property
    def capture(self):
        """
        Gets the capture of this Ptsv2paymentsProcessingInformation.
        Flag that specifies whether to also include capture service in the submitted request or not.  Possible values: - **true** - **false** (default). 

        :return: The capture of this Ptsv2paymentsProcessingInformation.
        :rtype: bool
        """
        return self._capture

    @capture.setter
    def capture(self, capture):
        """
        Sets the capture of this Ptsv2paymentsProcessingInformation.
        Flag that specifies whether to also include capture service in the submitted request or not.  Possible values: - **true** - **false** (default). 

        :param capture: The capture of this Ptsv2paymentsProcessingInformation.
        :type: bool
        """

        self._capture = capture

    @property
    def processor_id(self):
        """
        Gets the processor_id of this Ptsv2paymentsProcessingInformation.
        Value that identifies the processor/acquirer to use for the transaction. This value is supported only for **CyberSource through VisaNet**.  Contact CyberSource Customer Support to get the value for this field. 

        :return: The processor_id of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._processor_id

    @processor_id.setter
    def processor_id(self, processor_id):
        """
        Sets the processor_id of this Ptsv2paymentsProcessingInformation.
        Value that identifies the processor/acquirer to use for the transaction. This value is supported only for **CyberSource through VisaNet**.  Contact CyberSource Customer Support to get the value for this field. 

        :param processor_id: The processor_id of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if processor_id is not None and len(processor_id) > 3:
            raise ValueError("Invalid value for `processor_id`, length must be less than or equal to `3`")

        self._processor_id = processor_id

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this Ptsv2paymentsProcessingInformation.
        Payouts transaction type. Required for OCT transactions. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. **Note** When the request includes this field, this value overrides the information in your CyberSource account.  For valid values, see the `invoiceHeader_businessApplicationID` field description in [Payouts Using the Simple Order API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SO/Payouts_SO_API.pdf) 

        :return: The business_application_id of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this Ptsv2paymentsProcessingInformation.
        Payouts transaction type. Required for OCT transactions. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. **Note** When the request includes this field, this value overrides the information in your CyberSource account.  For valid values, see the `invoiceHeader_businessApplicationID` field description in [Payouts Using the Simple Order API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SO/Payouts_SO_API.pdf) 

        :param business_application_id: The business_application_id of this Ptsv2paymentsProcessingInformation.
        :type: str
        """

        self._business_application_id = business_application_id

    @property
    def commerce_indicator(self):
        """
        Gets the commerce_indicator of this Ptsv2paymentsProcessingInformation.
        Type of transaction. Some payment card companies use this information when determining discount rates.  #### Ingenico ePayments Ingenico ePayments was previously called _Global Collect_. When you omit this field for Ingenico ePayments, the processor uses the default transaction type they have on file for you instead of the default value listed in \"Commerce Indicators\" section of [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Payer Authentication Transactions For the possible values and requirements, see \"Payer Authentication\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Payouts OCT (Original Credit Transaction) Value for an OCT transaction: - `internet` For details, see the `e_commerce_indicator` field description in [Payouts Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SCMP/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Other Types of Transactions For details, see \"Commerce Indicators\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The commerce_indicator of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._commerce_indicator

    @commerce_indicator.setter
    def commerce_indicator(self, commerce_indicator):
        """
        Sets the commerce_indicator of this Ptsv2paymentsProcessingInformation.
        Type of transaction. Some payment card companies use this information when determining discount rates.  #### Ingenico ePayments Ingenico ePayments was previously called _Global Collect_. When you omit this field for Ingenico ePayments, the processor uses the default transaction type they have on file for you instead of the default value listed in \"Commerce Indicators\" section of [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Payer Authentication Transactions For the possible values and requirements, see \"Payer Authentication\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Payouts OCT (Original Credit Transaction) Value for an OCT transaction: - `internet` For details, see the `e_commerce_indicator` field description in [Payouts Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SCMP/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  #### Other Types of Transactions For details, see \"Commerce Indicators\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param commerce_indicator: The commerce_indicator of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if commerce_indicator is not None and len(commerce_indicator) > 20:
            raise ValueError("Invalid value for `commerce_indicator`, length must be less than or equal to `20`")

        self._commerce_indicator = commerce_indicator

    @property
    def payment_solution(self):
        """
        Gets the payment_solution of this Ptsv2paymentsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :return: The payment_solution of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._payment_solution

    @payment_solution.setter
    def payment_solution(self, payment_solution):
        """
        Sets the payment_solution of this Ptsv2paymentsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay. 

        :param payment_solution: The payment_solution of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if payment_solution is not None and len(payment_solution) > 12:
            raise ValueError("Invalid value for `payment_solution`, length must be less than or equal to `12`")

        self._payment_solution = payment_solution

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2paymentsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2paymentsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def link_id(self):
        """
        Gets the link_id of this Ptsv2paymentsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The link_id of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """
        Sets the link_id of this Ptsv2paymentsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param link_id: The link_id of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if link_id is not None and len(link_id) > 26:
            raise ValueError("Invalid value for `link_id`, length must be less than or equal to `26`")

        self._link_id = link_id

    @property
    def purchase_level(self):
        """
        Gets the purchase_level of this Ptsv2paymentsProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :return: The purchase_level of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._purchase_level

    @purchase_level.setter
    def purchase_level(self, purchase_level):
        """
        Sets the purchase_level of this Ptsv2paymentsProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :param purchase_level: The purchase_level of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if purchase_level is not None and len(purchase_level) > 1:
            raise ValueError("Invalid value for `purchase_level`, length must be less than or equal to `1`")

        self._purchase_level = purchase_level

    @property
    def report_group(self):
        """
        Gets the report_group of this Ptsv2paymentsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The report_group of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._report_group

    @report_group.setter
    def report_group(self, report_group):
        """
        Sets the report_group of this Ptsv2paymentsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param report_group: The report_group of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if report_group is not None and len(report_group) > 25:
            raise ValueError("Invalid value for `report_group`, length must be less than or equal to `25`")

        self._report_group = report_group

    @property
    def visa_checkout_id(self):
        """
        Gets the visa_checkout_id of this Ptsv2paymentsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  For details, see the `vc_order_id` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The visa_checkout_id of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._visa_checkout_id

    @visa_checkout_id.setter
    def visa_checkout_id(self, visa_checkout_id):
        """
        Sets the visa_checkout_id of this Ptsv2paymentsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field.  For details, see the `vc_order_id` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param visa_checkout_id: The visa_checkout_id of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if visa_checkout_id is not None and len(visa_checkout_id) > 48:
            raise ValueError("Invalid value for `visa_checkout_id`, length must be less than or equal to `48`")

        self._visa_checkout_id = visa_checkout_id

    @property
    def industry_data_type(self):
        """
        Gets the industry_data_type of this Ptsv2paymentsProcessingInformation.
        Flag that indicates whether the transaction includes airline or restaurant data.  To send the data in a transaction request to the processor, you must set this field to `airline` or `restaurant`.  **Note** If you do not set this field to one of the possible values, CyberSource does not send any data to the processor.  Possible Values: - `airline` - `restaurant` 

        :return: The industry_data_type of this Ptsv2paymentsProcessingInformation.
        :rtype: str
        """
        return self._industry_data_type

    @industry_data_type.setter
    def industry_data_type(self, industry_data_type):
        """
        Sets the industry_data_type of this Ptsv2paymentsProcessingInformation.
        Flag that indicates whether the transaction includes airline or restaurant data.  To send the data in a transaction request to the processor, you must set this field to `airline` or `restaurant`.  **Note** If you do not set this field to one of the possible values, CyberSource does not send any data to the processor.  Possible Values: - `airline` - `restaurant` 

        :param industry_data_type: The industry_data_type of this Ptsv2paymentsProcessingInformation.
        :type: str
        """
        if industry_data_type is not None and len(industry_data_type) > 10:
            raise ValueError("Invalid value for `industry_data_type`, length must be less than or equal to `10`")

        self._industry_data_type = industry_data_type

    @property
    def authorization_options(self):
        """
        Gets the authorization_options of this Ptsv2paymentsProcessingInformation.

        :return: The authorization_options of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationAuthorizationOptions
        """
        return self._authorization_options

    @authorization_options.setter
    def authorization_options(self, authorization_options):
        """
        Sets the authorization_options of this Ptsv2paymentsProcessingInformation.

        :param authorization_options: The authorization_options of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationAuthorizationOptions
        """

        self._authorization_options = authorization_options

    @property
    def capture_options(self):
        """
        Gets the capture_options of this Ptsv2paymentsProcessingInformation.

        :return: The capture_options of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationCaptureOptions
        """
        return self._capture_options

    @capture_options.setter
    def capture_options(self, capture_options):
        """
        Sets the capture_options of this Ptsv2paymentsProcessingInformation.

        :param capture_options: The capture_options of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationCaptureOptions
        """

        self._capture_options = capture_options

    @property
    def recurring_options(self):
        """
        Gets the recurring_options of this Ptsv2paymentsProcessingInformation.

        :return: The recurring_options of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationRecurringOptions
        """
        return self._recurring_options

    @recurring_options.setter
    def recurring_options(self, recurring_options):
        """
        Sets the recurring_options of this Ptsv2paymentsProcessingInformation.

        :param recurring_options: The recurring_options of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationRecurringOptions
        """

        self._recurring_options = recurring_options

    @property
    def bank_transfer_options(self):
        """
        Gets the bank_transfer_options of this Ptsv2paymentsProcessingInformation.

        :return: The bank_transfer_options of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationBankTransferOptions
        """
        return self._bank_transfer_options

    @bank_transfer_options.setter
    def bank_transfer_options(self, bank_transfer_options):
        """
        Sets the bank_transfer_options of this Ptsv2paymentsProcessingInformation.

        :param bank_transfer_options: The bank_transfer_options of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationBankTransferOptions
        """

        self._bank_transfer_options = bank_transfer_options

    @property
    def purchase_options(self):
        """
        Gets the purchase_options of this Ptsv2paymentsProcessingInformation.

        :return: The purchase_options of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationPurchaseOptions
        """
        return self._purchase_options

    @purchase_options.setter
    def purchase_options(self, purchase_options):
        """
        Sets the purchase_options of this Ptsv2paymentsProcessingInformation.

        :param purchase_options: The purchase_options of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationPurchaseOptions
        """

        self._purchase_options = purchase_options

    @property
    def electronic_benefits_transfer(self):
        """
        Gets the electronic_benefits_transfer of this Ptsv2paymentsProcessingInformation.

        :return: The electronic_benefits_transfer of this Ptsv2paymentsProcessingInformation.
        :rtype: Ptsv2paymentsProcessingInformationElectronicBenefitsTransfer
        """
        return self._electronic_benefits_transfer

    @electronic_benefits_transfer.setter
    def electronic_benefits_transfer(self, electronic_benefits_transfer):
        """
        Sets the electronic_benefits_transfer of this Ptsv2paymentsProcessingInformation.

        :param electronic_benefits_transfer: The electronic_benefits_transfer of this Ptsv2paymentsProcessingInformation.
        :type: Ptsv2paymentsProcessingInformationElectronicBenefitsTransfer
        """

        self._electronic_benefits_transfer = electronic_benefits_transfer

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
        if not isinstance(other, Ptsv2paymentsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
