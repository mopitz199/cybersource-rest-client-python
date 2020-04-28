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


class TssV2TransactionsGet200ResponseOrderInformation(object):
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
        'bill_to': 'TssV2TransactionsGet200ResponseOrderInformationBillTo',
        'ship_to': 'TssV2TransactionsGet200ResponseOrderInformationShipTo',
        'line_items': 'list[TssV2TransactionsGet200ResponseOrderInformationLineItems]',
        'amount_details': 'TssV2TransactionsGet200ResponseOrderInformationAmountDetails',
        'shipping_details': 'TssV2TransactionsGet200ResponseOrderInformationShippingDetails',
        'invoice_details': 'TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails'
    }

    attribute_map = {
        'bill_to': 'billTo',
        'ship_to': 'shipTo',
        'line_items': 'lineItems',
        'amount_details': 'amountDetails',
        'shipping_details': 'shippingDetails',
        'invoice_details': 'invoiceDetails'
    }

    def __init__(self, bill_to=None, ship_to=None, line_items=None, amount_details=None, shipping_details=None, invoice_details=None):
        """
        TssV2TransactionsGet200ResponseOrderInformation - a model defined in Swagger
        """

        self._bill_to = None
        self._ship_to = None
        self._line_items = None
        self._amount_details = None
        self._shipping_details = None
        self._invoice_details = None

        if bill_to is not None:
          self.bill_to = bill_to
        if ship_to is not None:
          self.ship_to = ship_to
        if line_items is not None:
          self.line_items = line_items
        if amount_details is not None:
          self.amount_details = amount_details
        if shipping_details is not None:
          self.shipping_details = shipping_details
        if invoice_details is not None:
          self.invoice_details = invoice_details

    @property
    def bill_to(self):
        """
        Gets the bill_to of this TssV2TransactionsGet200ResponseOrderInformation.

        :return: The bill_to of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: TssV2TransactionsGet200ResponseOrderInformationBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this TssV2TransactionsGet200ResponseOrderInformation.

        :param bill_to: The bill_to of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: TssV2TransactionsGet200ResponseOrderInformationBillTo
        """

        self._bill_to = bill_to

    @property
    def ship_to(self):
        """
        Gets the ship_to of this TssV2TransactionsGet200ResponseOrderInformation.

        :return: The ship_to of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: TssV2TransactionsGet200ResponseOrderInformationShipTo
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """
        Sets the ship_to of this TssV2TransactionsGet200ResponseOrderInformation.

        :param ship_to: The ship_to of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: TssV2TransactionsGet200ResponseOrderInformationShipTo
        """

        self._ship_to = ship_to

    @property
    def line_items(self):
        """
        Gets the line_items of this TssV2TransactionsGet200ResponseOrderInformation.
        Transaction Line Item data.

        :return: The line_items of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: list[TssV2TransactionsGet200ResponseOrderInformationLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """
        Sets the line_items of this TssV2TransactionsGet200ResponseOrderInformation.
        Transaction Line Item data.

        :param line_items: The line_items of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: list[TssV2TransactionsGet200ResponseOrderInformationLineItems]
        """

        self._line_items = line_items

    @property
    def amount_details(self):
        """
        Gets the amount_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :return: The amount_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: TssV2TransactionsGet200ResponseOrderInformationAmountDetails
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """
        Sets the amount_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :param amount_details: The amount_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: TssV2TransactionsGet200ResponseOrderInformationAmountDetails
        """

        self._amount_details = amount_details

    @property
    def shipping_details(self):
        """
        Gets the shipping_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :return: The shipping_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: TssV2TransactionsGet200ResponseOrderInformationShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """
        Sets the shipping_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :param shipping_details: The shipping_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: TssV2TransactionsGet200ResponseOrderInformationShippingDetails
        """

        self._shipping_details = shipping_details

    @property
    def invoice_details(self):
        """
        Gets the invoice_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :return: The invoice_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :rtype: TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails
        """
        return self._invoice_details

    @invoice_details.setter
    def invoice_details(self, invoice_details):
        """
        Sets the invoice_details of this TssV2TransactionsGet200ResponseOrderInformation.

        :param invoice_details: The invoice_details of this TssV2TransactionsGet200ResponseOrderInformation.
        :type: TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails
        """

        self._invoice_details = invoice_details

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
        if not isinstance(other, TssV2TransactionsGet200ResponseOrderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
