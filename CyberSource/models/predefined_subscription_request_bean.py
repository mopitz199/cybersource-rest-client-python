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


class PredefinedSubscriptionRequestBean(object):
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
        'report_definition_name': 'str',
        'subscription_type': 'str',
        'report_name': 'str',
        'report_mime_type': 'str',
        'report_frequency': 'str',
        'report_interval': 'str',
        'timezone': 'str',
        'start_time': 'str',
        'start_day': 'int',
        'subscription_status': 'str'
    }

    attribute_map = {
        'report_definition_name': 'reportDefinitionName',
        'subscription_type': 'subscriptionType',
        'report_name': 'reportName',
        'report_mime_type': 'reportMimeType',
        'report_frequency': 'reportFrequency',
        'report_interval': 'reportInterval',
        'timezone': 'timezone',
        'start_time': 'startTime',
        'start_day': 'startDay',
        'subscription_status': 'subscriptionStatus'
    }

    def __init__(self, report_definition_name=None, subscription_type=None, report_name=None, report_mime_type=None, report_frequency=None, report_interval=None, timezone=None, start_time=None, start_day=None, subscription_status=None):
        """
        PredefinedSubscriptionRequestBean - a model defined in Swagger
        """

        self._report_definition_name = None
        self._subscription_type = None
        self._report_name = None
        self._report_mime_type = None
        self._report_frequency = None
        self._report_interval = None
        self._timezone = None
        self._start_time = None
        self._start_day = None
        self._subscription_status = None

        self.report_definition_name = report_definition_name
        self.subscription_type = subscription_type
        if report_name is not None:
          self.report_name = report_name
        if report_mime_type is not None:
          self.report_mime_type = report_mime_type
        if report_frequency is not None:
          self.report_frequency = report_frequency
        if report_interval is not None:
          self.report_interval = report_interval
        if timezone is not None:
          self.timezone = timezone
        if start_time is not None:
          self.start_time = start_time
        if start_day is not None:
          self.start_day = start_day
        if subscription_status is not None:
          self.subscription_status = subscription_status

    @property
    def report_definition_name(self):
        """
        Gets the report_definition_name of this PredefinedSubscriptionRequestBean.
        Valid Report Definition Name

        :return: The report_definition_name of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._report_definition_name

    @report_definition_name.setter
    def report_definition_name(self, report_definition_name):
        """
        Sets the report_definition_name of this PredefinedSubscriptionRequestBean.
        Valid Report Definition Name

        :param report_definition_name: The report_definition_name of this PredefinedSubscriptionRequestBean.
        :type: str
        """
        if report_definition_name is None:
            raise ValueError("Invalid value for `report_definition_name`, must not be `None`")
        if report_definition_name is not None and len(report_definition_name) > 80:
            raise ValueError("Invalid value for `report_definition_name`, length must be less than or equal to `80`")
        if report_definition_name is not None and len(report_definition_name) < 1:
            raise ValueError("Invalid value for `report_definition_name`, length must be greater than or equal to `1`")
        if report_definition_name is not None and not re.search('[a-zA-Z]+', report_definition_name):
            raise ValueError("Invalid value for `report_definition_name`, must be a follow pattern or equal to `/[a-zA-Z]+/`")

        self._report_definition_name = report_definition_name

    @property
    def subscription_type(self):
        """
        Gets the subscription_type of this PredefinedSubscriptionRequestBean.
        The subscription type for which report definition is required. Valid values are CLASSIC and STANDARD. Valid Values:   - CLASSIC   - STANDARD 

        :return: The subscription_type of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """
        Sets the subscription_type of this PredefinedSubscriptionRequestBean.
        The subscription type for which report definition is required. Valid values are CLASSIC and STANDARD. Valid Values:   - CLASSIC   - STANDARD 

        :param subscription_type: The subscription_type of this PredefinedSubscriptionRequestBean.
        :type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")

        self._subscription_type = subscription_type

    @property
    def report_name(self):
        """
        Gets the report_name of this PredefinedSubscriptionRequestBean.

        :return: The report_name of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """
        Sets the report_name of this PredefinedSubscriptionRequestBean.

        :param report_name: The report_name of this PredefinedSubscriptionRequestBean.
        :type: str
        """
        if report_name is not None and len(report_name) > 128:
            raise ValueError("Invalid value for `report_name`, length must be less than or equal to `128`")
        if report_name is not None and len(report_name) < 1:
            raise ValueError("Invalid value for `report_name`, length must be greater than or equal to `1`")
        if report_name is not None and not re.search('[a-zA-Z0-9-_ ]+', report_name):
            raise ValueError("Invalid value for `report_name`, must be a follow pattern or equal to `/[a-zA-Z0-9-_ ]+/`")

        self._report_name = report_name

    @property
    def report_mime_type(self):
        """
        Gets the report_mime_type of this PredefinedSubscriptionRequestBean.
        Report Format             Valid Values:   - application/xml   - text/csv 

        :return: The report_mime_type of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._report_mime_type

    @report_mime_type.setter
    def report_mime_type(self, report_mime_type):
        """
        Sets the report_mime_type of this PredefinedSubscriptionRequestBean.
        Report Format             Valid Values:   - application/xml   - text/csv 

        :param report_mime_type: The report_mime_type of this PredefinedSubscriptionRequestBean.
        :type: str
        """

        self._report_mime_type = report_mime_type

    @property
    def report_frequency(self):
        """
        Gets the report_frequency of this PredefinedSubscriptionRequestBean.
        'The frequency for which subscription is created. For Standard we can have DAILY, WEEKLY and MONTHLY. But for Classic we will have only DAILY.'  Valid Values: - 'DAILY' - 'WEEKLY' - 'MONTHLY' - 'USER_DEFINED' 

        :return: The report_frequency of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._report_frequency

    @report_frequency.setter
    def report_frequency(self, report_frequency):
        """
        Sets the report_frequency of this PredefinedSubscriptionRequestBean.
        'The frequency for which subscription is created. For Standard we can have DAILY, WEEKLY and MONTHLY. But for Classic we will have only DAILY.'  Valid Values: - 'DAILY' - 'WEEKLY' - 'MONTHLY' - 'USER_DEFINED' 

        :param report_frequency: The report_frequency of this PredefinedSubscriptionRequestBean.
        :type: str
        """

        self._report_frequency = report_frequency

    @property
    def report_interval(self):
        """
        Gets the report_interval of this PredefinedSubscriptionRequestBean.
        If the reportFrequency is User-defined, reportInterval should be in **ISO 8601 time format** Please refer the following link to know more about ISO 8601 format.[Rfc Time Format](https://en.wikipedia.org/wiki/ISO_8601#Durations)  **Example time format for 2 hours and 30 Mins:**   - PT2H30M **NOTE: Do not document reportInterval field in developer center** 

        :return: The report_interval of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._report_interval

    @report_interval.setter
    def report_interval(self, report_interval):
        """
        Sets the report_interval of this PredefinedSubscriptionRequestBean.
        If the reportFrequency is User-defined, reportInterval should be in **ISO 8601 time format** Please refer the following link to know more about ISO 8601 format.[Rfc Time Format](https://en.wikipedia.org/wiki/ISO_8601#Durations)  **Example time format for 2 hours and 30 Mins:**   - PT2H30M **NOTE: Do not document reportInterval field in developer center** 

        :param report_interval: The report_interval of this PredefinedSubscriptionRequestBean.
        :type: str
        """
        if report_interval is not None and not re.search('^PT((([1-9]|1[0-9]|2[0-3])H(([1-9]|[1-4][0-9]|5[0-9])M)?)|((([1-9]|1[0-9]|2[0-3])H)?([1-9]|[1-4][0-9]|5[0-9])M))$', report_interval):
            raise ValueError("Invalid value for `report_interval`, must be a follow pattern or equal to `/^PT((([1-9]|1[0-9]|2[0-3])H(([1-9]|[1-4][0-9]|5[0-9])M)?)|((([1-9]|1[0-9]|2[0-3])H)?([1-9]|[1-4][0-9]|5[0-9])M))$/`")

        self._report_interval = report_interval

    @property
    def timezone(self):
        """
        Gets the timezone of this PredefinedSubscriptionRequestBean.
        By Default the timezone for Standard subscription is PST. And for Classic subscription it will be GMT. If user provides any other time zone apart from PST for Standard subscription api should error out.

        :return: The timezone of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this PredefinedSubscriptionRequestBean.
        By Default the timezone for Standard subscription is PST. And for Classic subscription it will be GMT. If user provides any other time zone apart from PST for Standard subscription api should error out.

        :param timezone: The timezone of this PredefinedSubscriptionRequestBean.
        :type: str
        """

        self._timezone = timezone

    @property
    def start_time(self):
        """
        Gets the start_time of this PredefinedSubscriptionRequestBean.
        The hour at which the report generation should start. It should be in hhmm format. By Default it will be 0000. The format is 24 hours format.

        :return: The start_time of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this PredefinedSubscriptionRequestBean.
        The hour at which the report generation should start. It should be in hhmm format. By Default it will be 0000. The format is 24 hours format.

        :param start_time: The start_time of this PredefinedSubscriptionRequestBean.
        :type: str
        """

        self._start_time = start_time

    @property
    def start_day(self):
        """
        Gets the start_day of this PredefinedSubscriptionRequestBean.
        This is the start day if the frequency is WEEKLY or MONTHLY. The value varies from 1-7 for WEEKLY and 1-31 for MONTHLY. For WEEKLY 1 means Sunday and 7 means Saturday. By default the value is 1.

        :return: The start_day of this PredefinedSubscriptionRequestBean.
        :rtype: int
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        """
        Sets the start_day of this PredefinedSubscriptionRequestBean.
        This is the start day if the frequency is WEEKLY or MONTHLY. The value varies from 1-7 for WEEKLY and 1-31 for MONTHLY. For WEEKLY 1 means Sunday and 7 means Saturday. By default the value is 1.

        :param start_day: The start_day of this PredefinedSubscriptionRequestBean.
        :type: int
        """
        if start_day is not None and start_day > 31:
            raise ValueError("Invalid value for `start_day`, must be a value less than or equal to `31`")
        if start_day is not None and start_day < 1:
            raise ValueError("Invalid value for `start_day`, must be a value greater than or equal to `1`")

        self._start_day = start_day

    @property
    def subscription_status(self):
        """
        Gets the subscription_status of this PredefinedSubscriptionRequestBean.
        The status for subscription which is either created or updated. By default it is ACTIVE. Valid Values:   - ACTIVE   - INACTIVE 

        :return: The subscription_status of this PredefinedSubscriptionRequestBean.
        :rtype: str
        """
        return self._subscription_status

    @subscription_status.setter
    def subscription_status(self, subscription_status):
        """
        Sets the subscription_status of this PredefinedSubscriptionRequestBean.
        The status for subscription which is either created or updated. By default it is ACTIVE. Valid Values:   - ACTIVE   - INACTIVE 

        :param subscription_status: The subscription_status of this PredefinedSubscriptionRequestBean.
        :type: str
        """

        self._subscription_status = subscription_status

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
        if not isinstance(other, PredefinedSubscriptionRequestBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
