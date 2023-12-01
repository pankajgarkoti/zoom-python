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

class AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel(object):
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
        'retention_period': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'retention_period': 'retention_period'
    }

    def __init__(self, enable=None, retention_period=None):  # noqa: E501
        """AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._retention_period = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if retention_period is not None:
            self.retention_period = retention_period

    @property
    def enable(self):
        """Gets the enable of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501

        Specify how long your messages sent in your personal channel are saved on local devices. If this setting is disabled, messages are never deleted locally.  # noqa: E501

        :return: The enable of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.

        Specify how long your messages sent in your personal channel are saved on local devices. If this setting is disabled, messages are never deleted locally.  # noqa: E501

        :param enable: The enable of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def retention_period(self):
        """Gets the retention_period of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501

        Delete data after retention period. 'y' - year, 'm' - month, 'd' - day.   # noqa: E501

        :return: The retention_period of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501
        :rtype: str
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        """Sets the retention_period of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.

        Delete data after retention period. 'y' - year, 'm' - month, 'd' - day.   # noqa: E501

        :param retention_period: The retention_period of this AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel.  # noqa: E501
        :type: str
        """

        self._retention_period = retention_period

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
        if issubclass(AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
