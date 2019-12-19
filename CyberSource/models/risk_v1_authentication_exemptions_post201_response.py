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


class RiskV1AuthenticationExemptionsPost201Response(object):
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
        'links': 'PtsV2PaymentsReversalsPost201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'risk_information': 'RiskV1AuthenticationExemptionsPost201ResponseRiskInformation',
        'consumer_authentication_information': 'RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation',
        'error_information': 'PtsV2PaymentsPost201ResponseErrorInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'risk_information': 'riskInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'error_information': 'errorInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, risk_information=None, consumer_authentication_information=None, error_information=None):
        """
        RiskV1AuthenticationExemptionsPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._risk_information = None
        self._consumer_authentication_information = None
        self._error_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if risk_information is not None:
          self.risk_information = risk_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if error_information is not None:
          self.error_information = error_information

    @property
    def links(self):
        """
        Gets the links of this RiskV1AuthenticationExemptionsPost201Response.

        :return: The links of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this RiskV1AuthenticationExemptionsPost201Response.

        :param links: The links of this RiskV1AuthenticationExemptionsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this RiskV1AuthenticationExemptionsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :return: The id of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RiskV1AuthenticationExemptionsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :param id: The id of this RiskV1AuthenticationExemptionsPost201Response.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this RiskV1AuthenticationExemptionsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this RiskV1AuthenticationExemptionsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this RiskV1AuthenticationExemptionsPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this RiskV1AuthenticationExemptionsPost201Response.
        The status for authentication-exemptions 201. Value is: - AUTHENTICATION_EXEMPTIONS_SUCCESSFUL 

        :return: The status of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RiskV1AuthenticationExemptionsPost201Response.
        The status for authentication-exemptions 201. Value is: - AUTHENTICATION_EXEMPTIONS_SUCCESSFUL 

        :param status: The status of this RiskV1AuthenticationExemptionsPost201Response.
        :type: str
        """

        self._status = status

    @property
    def risk_information(self):
        """
        Gets the risk_information of this RiskV1AuthenticationExemptionsPost201Response.

        :return: The risk_information of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: RiskV1AuthenticationExemptionsPost201ResponseRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this RiskV1AuthenticationExemptionsPost201Response.

        :param risk_information: The risk_information of this RiskV1AuthenticationExemptionsPost201Response.
        :type: RiskV1AuthenticationExemptionsPost201ResponseRiskInformation
        """

        self._risk_information = risk_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this RiskV1AuthenticationExemptionsPost201Response.

        :return: The consumer_authentication_information of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this RiskV1AuthenticationExemptionsPost201Response.

        :param consumer_authentication_information: The consumer_authentication_information of this RiskV1AuthenticationExemptionsPost201Response.
        :type: RiskV1AuthenticationExemptionsPost201ResponseConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def error_information(self):
        """
        Gets the error_information of this RiskV1AuthenticationExemptionsPost201Response.

        :return: The error_information of this RiskV1AuthenticationExemptionsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this RiskV1AuthenticationExemptionsPost201Response.

        :param error_information: The error_information of this RiskV1AuthenticationExemptionsPost201Response.
        :type: PtsV2PaymentsPost201ResponseErrorInformation
        """

        self._error_information = error_information

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
        if not isinstance(other, RiskV1AuthenticationExemptionsPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
