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

class InlineResponse20122SettingsFollowUpAbsenteesEmailNotification(object):
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
        'enable': 'bool',
        'type': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'type': 'type'
    }

    def __init__(self, enable=None, type=None):  # noqa: E501
        """InlineResponse20122SettingsFollowUpAbsenteesEmailNotification - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._type = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if type is not None:
            self.type = type

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501

        * `true`: Send follow-up email to absentees.  * `false`: Do not send follow-up email to absentees.  # noqa: E501

        :return: The enable of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.

        * `true`: Send follow-up email to absentees.  * `false`: Do not send follow-up email to absentees.  # noqa: E501

        :param enable: The enable of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def type(self):
        """Gets the type of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501

        `0` - No plan.    `1` - Send 1 days after the scheduled end date.    `2` - Send 2 days after the scheduled end date.    `3` - Send 3 days after the scheduled end date.    `4` - Send 4 days after the scheduled end date.    `5` - Send 5 days after the scheduled end date.    `6` - Send 6 days after the scheduled end date.    `7` - Send 7 days after the scheduled end date.  # noqa: E501

        :return: The type of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.

        `0` - No plan.    `1` - Send 1 days after the scheduled end date.    `2` - Send 2 days after the scheduled end date.    `3` - Send 3 days after the scheduled end date.    `4` - Send 4 days after the scheduled end date.    `5` - Send 5 days after the scheduled end date.    `6` - Send 6 days after the scheduled end date.    `7` - Send 7 days after the scheduled end date.  # noqa: E501

        :param type: The type of this InlineResponse20122SettingsFollowUpAbsenteesEmailNotification.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(InlineResponse20122SettingsFollowUpAbsenteesEmailNotification, dict):
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
        if not isinstance(other, InlineResponse20122SettingsFollowUpAbsenteesEmailNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
