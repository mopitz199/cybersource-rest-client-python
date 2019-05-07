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


class TssV2TransactionsGet200ResponseApplicationInformationApplications(object):
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
        'status': 'str',
        'reason_code': 'str',
        'r_code': 'str',
        'r_flag': 'str',
        'reconciliation_id': 'str',
        'r_message': 'str',
        'return_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'reason_code': 'reasonCode',
        'r_code': 'rCode',
        'r_flag': 'rFlag',
        'reconciliation_id': 'reconciliationId',
        'r_message': 'rMessage',
        'return_code': 'returnCode'
    }

    def __init__(self, name=None, status=None, reason_code=None, r_code=None, r_flag=None, reconciliation_id=None, r_message=None, return_code=None):
        """
        TssV2TransactionsGet200ResponseApplicationInformationApplications - a model defined in Swagger
        """

        self._name = None
        self._status = None
        self._reason_code = None
        self._r_code = None
        self._r_flag = None
        self._reconciliation_id = None
        self._r_message = None
        self._return_code = None

        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if reason_code is not None:
          self.reason_code = reason_code
        if r_code is not None:
          self.r_code = r_code
        if r_flag is not None:
          self.r_flag = r_flag
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if r_message is not None:
          self.r_message = r_message
        if return_code is not None:
          self.return_code = return_code

    @property
    def name(self):
        """
        Gets the name of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The name of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param name: The name of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The status of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param status: The status of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._status = status

    @property
    def reason_code(self):
        """
        Gets the reason_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The reason_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """
        Sets the reason_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param reason_code: The reason_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._reason_code = reason_code

    @property
    def r_code(self):
        """
        Gets the r_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The r_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._r_code

    @r_code.setter
    def r_code(self, r_code):
        """
        Sets the r_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param r_code: The r_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._r_code = r_code

    @property
    def r_flag(self):
        """
        Gets the r_flag of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The r_flag of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._r_flag

    @r_flag.setter
    def r_flag(self, r_flag):
        """
        Sets the r_flag of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param r_flag: The r_flag of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._r_flag = r_flag

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The reconciliation_id of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param reconciliation_id: The reconciliation_id of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def r_message(self):
        """
        Gets the r_message of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The r_message of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._r_message

    @r_message.setter
    def r_message(self, r_message):
        """
        Sets the r_message of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param r_message: The r_message of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._r_message = r_message

    @property
    def return_code(self):
        """
        Gets the return_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :return: The return_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """
        Sets the return_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        The description for this field is not available.

        :param return_code: The return_code of this TssV2TransactionsGet200ResponseApplicationInformationApplications.
        :type: str
        """

        self._return_code = return_code

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
        if not isinstance(other, TssV2TransactionsGet200ResponseApplicationInformationApplications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
