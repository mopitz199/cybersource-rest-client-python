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


class RiskV1DecisionsPost201ResponseRiskInformationScore(object):
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
        'factor_codes': 'list[str]',
        'model_used': 'str',
        'result': 'str'
    }

    attribute_map = {
        'factor_codes': 'factorCodes',
        'model_used': 'modelUsed',
        'result': 'result'
    }

    def __init__(self, factor_codes=None, model_used=None, result=None):
        """
        RiskV1DecisionsPost201ResponseRiskInformationScore - a model defined in Swagger
        """

        self._factor_codes = None
        self._model_used = None
        self._result = None

        if factor_codes is not None:
          self.factor_codes = factor_codes
        if model_used is not None:
          self.model_used = model_used
        if result is not None:
          self.result = result

    @property
    def factor_codes(self):
        """
        Gets the factor_codes of this RiskV1DecisionsPost201ResponseRiskInformationScore.

        :return: The factor_codes of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :rtype: list[str]
        """
        return self._factor_codes

    @factor_codes.setter
    def factor_codes(self, factor_codes):
        """
        Sets the factor_codes of this RiskV1DecisionsPost201ResponseRiskInformationScore.

        :param factor_codes: The factor_codes of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :type: list[str]
        """

        self._factor_codes = factor_codes

    @property
    def model_used(self):
        """
        Gets the model_used of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        Name of the score model used for the transaction. If you did not include a custom model in your request, this field contains the name of CyberSource’s default model. 

        :return: The model_used of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :rtype: str
        """
        return self._model_used

    @model_used.setter
    def model_used(self, model_used):
        """
        Sets the model_used of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        Name of the score model used for the transaction. If you did not include a custom model in your request, this field contains the name of CyberSource’s default model. 

        :param model_used: The model_used of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :type: str
        """
        if model_used is not None and len(model_used) > 255:
            raise ValueError("Invalid value for `model_used`, length must be less than or equal to `255`")

        self._model_used = model_used

    @property
    def result(self):
        """
        Gets the result of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        Total score calculated for this order. The value cannot be negative. 

        :return: The result of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        Total score calculated for this order. The value cannot be negative. 

        :param result: The result of this RiskV1DecisionsPost201ResponseRiskInformationScore.
        :type: str
        """
        if result is not None and len(result) > 255:
            raise ValueError("Invalid value for `result`, length must be less than or equal to `255`")

        self._result = result

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
        if not isinstance(other, RiskV1DecisionsPost201ResponseRiskInformationScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
