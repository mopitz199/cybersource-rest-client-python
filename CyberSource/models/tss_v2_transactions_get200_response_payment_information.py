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


class TssV2TransactionsGet200ResponsePaymentInformation(object):
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
        'payment_type': 'TssV2TransactionsGet200ResponsePaymentInformationPaymentType',
        'customer': 'Ptsv2paymentsPaymentInformationCustomer',
        'card': 'TssV2TransactionsGet200ResponsePaymentInformationCard',
        'invoice': 'TssV2TransactionsGet200ResponsePaymentInformationInvoice',
        'bank': 'TssV2TransactionsGet200ResponsePaymentInformationBank',
        'account_features': 'TssV2TransactionsGet200ResponsePaymentInformationAccountFeatures'
    }

    attribute_map = {
        'payment_type': 'paymentType',
        'customer': 'customer',
        'card': 'card',
        'invoice': 'invoice',
        'bank': 'bank',
        'account_features': 'accountFeatures'
    }

    def __init__(self, payment_type=None, customer=None, card=None, invoice=None, bank=None, account_features=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformation - a model defined in Swagger
        """

        self._payment_type = None
        self._customer = None
        self._card = None
        self._invoice = None
        self._bank = None
        self._account_features = None

        if payment_type is not None:
          self.payment_type = payment_type
        if customer is not None:
          self.customer = customer
        if card is not None:
          self.card = card
        if invoice is not None:
          self.invoice = invoice
        if bank is not None:
          self.bank = bank
        if account_features is not None:
          self.account_features = account_features

    @property
    def payment_type(self):
        """
        Gets the payment_type of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The payment_type of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param payment_type: The payment_type of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationPaymentType
        """

        self._payment_type = payment_type

    @property
    def customer(self):
        """
        Gets the customer of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The customer of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param customer: The customer of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCustomer
        """

        self._customer = customer

    @property
    def card(self):
        """
        Gets the card of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The card of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param card: The card of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationCard
        """

        self._card = card

    @property
    def invoice(self):
        """
        Gets the invoice of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The invoice of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """
        Sets the invoice of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param invoice: The invoice of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationInvoice
        """

        self._invoice = invoice

    @property
    def bank(self):
        """
        Gets the bank of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The bank of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param bank: The bank of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationBank
        """

        self._bank = bank

    @property
    def account_features(self):
        """
        Gets the account_features of this TssV2TransactionsGet200ResponsePaymentInformation.

        :return: The account_features of this TssV2TransactionsGet200ResponsePaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationAccountFeatures
        """
        return self._account_features

    @account_features.setter
    def account_features(self, account_features):
        """
        Sets the account_features of this TssV2TransactionsGet200ResponsePaymentInformation.

        :param account_features: The account_features of this TssV2TransactionsGet200ResponsePaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationAccountFeatures
        """

        self._account_features = account_features

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
