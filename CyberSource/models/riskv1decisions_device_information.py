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


class Riskv1decisionsDeviceInformation(object):
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
        'cookies_accepted': 'str',
        'ip_address': 'str',
        'network_ip_address': 'str',
        'host_name': 'str',
        'fingerprint_session_id': 'str',
        'http_browser_email': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'cookies_accepted': 'cookiesAccepted',
        'ip_address': 'ipAddress',
        'network_ip_address': 'networkIpAddress',
        'host_name': 'hostName',
        'fingerprint_session_id': 'fingerprintSessionId',
        'http_browser_email': 'httpBrowserEmail',
        'user_agent': 'userAgent'
    }

    def __init__(self, cookies_accepted=None, ip_address=None, network_ip_address=None, host_name=None, fingerprint_session_id=None, http_browser_email=None, user_agent=None):
        """
        Riskv1decisionsDeviceInformation - a model defined in Swagger
        """

        self._cookies_accepted = None
        self._ip_address = None
        self._network_ip_address = None
        self._host_name = None
        self._fingerprint_session_id = None
        self._http_browser_email = None
        self._user_agent = None

        if cookies_accepted is not None:
          self.cookies_accepted = cookies_accepted
        if ip_address is not None:
          self.ip_address = ip_address
        if network_ip_address is not None:
          self.network_ip_address = network_ip_address
        if host_name is not None:
          self.host_name = host_name
        if fingerprint_session_id is not None:
          self.fingerprint_session_id = fingerprint_session_id
        if http_browser_email is not None:
          self.http_browser_email = http_browser_email
        if user_agent is not None:
          self.user_agent = user_agent

    @property
    def cookies_accepted(self):
        """
        Gets the cookies_accepted of this Riskv1decisionsDeviceInformation.
        Whether the customer’s browser accepts cookies. This field can contain one of the following values: - `yes`: The customer’s browser accepts cookies. - `no`: The customer’s browser does not accept cookies. 

        :return: The cookies_accepted of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._cookies_accepted

    @cookies_accepted.setter
    def cookies_accepted(self, cookies_accepted):
        """
        Sets the cookies_accepted of this Riskv1decisionsDeviceInformation.
        Whether the customer’s browser accepts cookies. This field can contain one of the following values: - `yes`: The customer’s browser accepts cookies. - `no`: The customer’s browser does not accept cookies. 

        :param cookies_accepted: The cookies_accepted of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._cookies_accepted = cookies_accepted

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Riskv1decisionsDeviceInformation.
        IP address of the customer. 

        :return: The ip_address of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Riskv1decisionsDeviceInformation.
        IP address of the customer. 

        :param ip_address: The ip_address of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if ip_address is not None and len(ip_address) > 48:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `48`")

        self._ip_address = ip_address

    @property
    def network_ip_address(self):
        """
        Gets the network_ip_address of this Riskv1decisionsDeviceInformation.
        Network IP address of the customer (for example, 10.1.27). A network IP address includes up to 256 IP addresses. 

        :return: The network_ip_address of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._network_ip_address

    @network_ip_address.setter
    def network_ip_address(self, network_ip_address):
        """
        Sets the network_ip_address of this Riskv1decisionsDeviceInformation.
        Network IP address of the customer (for example, 10.1.27). A network IP address includes up to 256 IP addresses. 

        :param network_ip_address: The network_ip_address of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if network_ip_address is not None and len(network_ip_address) > 11:
            raise ValueError("Invalid value for `network_ip_address`, length must be less than or equal to `11`")

        self._network_ip_address = network_ip_address

    @property
    def host_name(self):
        """
        Gets the host_name of this Riskv1decisionsDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :return: The host_name of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this Riskv1decisionsDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :param host_name: The host_name of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if host_name is not None and len(host_name) > 60:
            raise ValueError("Invalid value for `host_name`, length must be less than or equal to `60`")

        self._host_name = host_name

    @property
    def fingerprint_session_id(self):
        """
        Gets the fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual’s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page. 

        :return: The fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._fingerprint_session_id

    @fingerprint_session_id.setter
    def fingerprint_session_id(self, fingerprint_session_id):
        """
        Sets the fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual’s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page. 

        :param fingerprint_session_id: The fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._fingerprint_session_id = fingerprint_session_id

    @property
    def http_browser_email(self):
        """
        Gets the http_browser_email of this Riskv1decisionsDeviceInformation.
        Email address set in the customer’s browser, which may differ from customer email. 

        :return: The http_browser_email of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_email

    @http_browser_email.setter
    def http_browser_email(self, http_browser_email):
        """
        Sets the http_browser_email of this Riskv1decisionsDeviceInformation.
        Email address set in the customer’s browser, which may differ from customer email. 

        :param http_browser_email: The http_browser_email of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._http_browser_email = http_browser_email

    @property
    def user_agent(self):
        """
        Gets the user_agent of this Riskv1decisionsDeviceInformation.
        Customer’s browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :return: The user_agent of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this Riskv1decisionsDeviceInformation.
        Customer’s browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :param user_agent: The user_agent of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if user_agent is not None and len(user_agent) > 40:
            raise ValueError("Invalid value for `user_agent`, length must be less than or equal to `40`")

        self._user_agent = user_agent

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
        if not isinstance(other, Riskv1decisionsDeviceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
