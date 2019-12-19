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


class UpdatePaymentInstrumentRequest(object):
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
        'bank_account': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount',
        'card': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard',
        'buyer_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation',
        'bill_to': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo',
        'processing_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation',
        'merchant_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation',
        'meta_data': 'TmsV1InstrumentIdentifiersPost200ResponseMetadata',
        'instrument_identifier': 'Tmsv1paymentinstrumentsInstrumentIdentifier'
    }

    attribute_map = {
        'bank_account': 'bankAccount',
        'card': 'card',
        'buyer_information': 'buyerInformation',
        'bill_to': 'billTo',
        'processing_information': 'processingInformation',
        'merchant_information': 'merchantInformation',
        'meta_data': 'metaData',
        'instrument_identifier': 'instrumentIdentifier'
    }

    def __init__(self, bank_account=None, card=None, buyer_information=None, bill_to=None, processing_information=None, merchant_information=None, meta_data=None, instrument_identifier=None):
        """
        UpdatePaymentInstrumentRequest - a model defined in Swagger
        """

        self._bank_account = None
        self._card = None
        self._buyer_information = None
        self._bill_to = None
        self._processing_information = None
        self._merchant_information = None
        self._meta_data = None
        self._instrument_identifier = None

        if bank_account is not None:
          self.bank_account = bank_account
        if card is not None:
          self.card = card
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if bill_to is not None:
          self.bill_to = bill_to
        if processing_information is not None:
          self.processing_information = processing_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if meta_data is not None:
          self.meta_data = meta_data
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier

    @property
    def bank_account(self):
        """
        Gets the bank_account of this UpdatePaymentInstrumentRequest.

        :return: The bank_account of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this UpdatePaymentInstrumentRequest.

        :param bank_account: The bank_account of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount
        """

        self._bank_account = bank_account

    @property
    def card(self):
        """
        Gets the card of this UpdatePaymentInstrumentRequest.

        :return: The card of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this UpdatePaymentInstrumentRequest.

        :param card: The card of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard
        """

        self._card = card

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this UpdatePaymentInstrumentRequest.

        :return: The buyer_information of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this UpdatePaymentInstrumentRequest.

        :param buyer_information: The buyer_information of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def bill_to(self):
        """
        Gets the bill_to of this UpdatePaymentInstrumentRequest.

        :return: The bill_to of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this UpdatePaymentInstrumentRequest.

        :param bill_to: The bill_to of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo
        """

        self._bill_to = bill_to

    @property
    def processing_information(self):
        """
        Gets the processing_information of this UpdatePaymentInstrumentRequest.

        :return: The processing_information of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this UpdatePaymentInstrumentRequest.

        :param processing_information: The processing_information of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this UpdatePaymentInstrumentRequest.

        :return: The merchant_information of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this UpdatePaymentInstrumentRequest.

        :param merchant_information: The merchant_information of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def meta_data(self):
        """
        Gets the meta_data of this UpdatePaymentInstrumentRequest.

        :return: The meta_data of this UpdatePaymentInstrumentRequest.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """
        Sets the meta_data of this UpdatePaymentInstrumentRequest.

        :param meta_data: The meta_data of this UpdatePaymentInstrumentRequest.
        :type: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """

        self._meta_data = meta_data

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this UpdatePaymentInstrumentRequest.

        :return: The instrument_identifier of this UpdatePaymentInstrumentRequest.
        :rtype: Tmsv1paymentinstrumentsInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this UpdatePaymentInstrumentRequest.

        :param instrument_identifier: The instrument_identifier of this UpdatePaymentInstrumentRequest.
        :type: Tmsv1paymentinstrumentsInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

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
        if not isinstance(other, UpdatePaymentInstrumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
