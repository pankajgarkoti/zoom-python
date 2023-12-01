# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20114SettingsAuthenticationException(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'email': 'str',
        'name': 'str',
        'join_url': 'str'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'join_url': 'join_url'
    }

    def __init__(self, email=None, name=None, join_url=None):  # noqa: E501
        """InlineResponse20114SettingsAuthenticationException - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._name = None
        self._join_url = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if join_url is not None:
            self.join_url = join_url

    @property
    def email(self):
        """Gets the email of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501

        The participant's email address.  # noqa: E501

        :return: The email of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20114SettingsAuthenticationException.

        The participant's email address.  # noqa: E501

        :param email: The email of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501

        The participant's name.  # noqa: E501

        :return: The name of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20114SettingsAuthenticationException.

        The participant's name.  # noqa: E501

        :param name: The name of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def join_url(self):
        """Gets the join_url of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501

        URL for participants to join the meeting.  # noqa: E501

        :return: The join_url of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :rtype: str
        """
        return self._join_url

    @join_url.setter
    def join_url(self, join_url):
        """Sets the join_url of this InlineResponse20114SettingsAuthenticationException.

        URL for participants to join the meeting.  # noqa: E501

        :param join_url: The join_url of this InlineResponse20114SettingsAuthenticationException.  # noqa: E501
        :type: str
        """

        self._join_url = join_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse20114SettingsAuthenticationException, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20114SettingsAuthenticationException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
