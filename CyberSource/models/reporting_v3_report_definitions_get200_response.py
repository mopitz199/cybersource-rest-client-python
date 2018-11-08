# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ReportingV3ReportDefinitionsGet200Response(object):
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
        'report_definitions': 'list[ReportingV3ReportDefinitionsGet200ResponseReportDefinitions]'
    }

    attribute_map = {
        'report_definitions': 'reportDefinitions'
    }

    def __init__(self, report_definitions=None):
        """
        ReportingV3ReportDefinitionsGet200Response - a model defined in Swagger
        """

        self._report_definitions = None

        if report_definitions is not None:
          self.report_definitions = report_definitions

    @property
    def report_definitions(self):
        """
        Gets the report_definitions of this ReportingV3ReportDefinitionsGet200Response.

        :return: The report_definitions of this ReportingV3ReportDefinitionsGet200Response.
        :rtype: list[ReportingV3ReportDefinitionsGet200ResponseReportDefinitions]
        """
        return self._report_definitions

    @report_definitions.setter
    def report_definitions(self, report_definitions):
        """
        Sets the report_definitions of this ReportingV3ReportDefinitionsGet200Response.

        :param report_definitions: The report_definitions of this ReportingV3ReportDefinitionsGet200Response.
        :type: list[ReportingV3ReportDefinitionsGet200ResponseReportDefinitions]
        """

        self._report_definitions = report_definitions

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
        if not isinstance(other, ReportingV3ReportDefinitionsGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other