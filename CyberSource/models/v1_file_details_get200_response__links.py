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


class V1FileDetailsGet200ResponseLinks(object):
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
        '_self': 'V1FileDetailsGet200ResponseLinksSelf',
        'files': 'list[V1FileDetailsGet200ResponseLinksFiles]'
    }

    attribute_map = {
        '_self': 'self',
        'files': 'files'
    }

    def __init__(self, _self=None, files=None):
        """
        V1FileDetailsGet200ResponseLinks - a model defined in Swagger
        """

        self.__self = None
        self._files = None

        if _self is not None:
          self._self = _self
        if files is not None:
          self.files = files

    @property
    def _self(self):
        """
        Gets the _self of this V1FileDetailsGet200ResponseLinks.

        :return: The _self of this V1FileDetailsGet200ResponseLinks.
        :rtype: V1FileDetailsGet200ResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this V1FileDetailsGet200ResponseLinks.

        :param _self: The _self of this V1FileDetailsGet200ResponseLinks.
        :type: V1FileDetailsGet200ResponseLinksSelf
        """

        self.__self = _self

    @property
    def files(self):
        """
        Gets the files of this V1FileDetailsGet200ResponseLinks.

        :return: The files of this V1FileDetailsGet200ResponseLinks.
        :rtype: list[V1FileDetailsGet200ResponseLinksFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this V1FileDetailsGet200ResponseLinks.

        :param files: The files of this V1FileDetailsGet200ResponseLinks.
        :type: list[V1FileDetailsGet200ResponseLinksFiles]
        """

        self._files = files

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
        if not isinstance(other, V1FileDetailsGet200ResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
