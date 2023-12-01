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

class AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat(object):
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
        'can_add_external_users': 'bool',
        'auto_add_invited_external_users': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'can_add_external_users': 'can_add_external_users',
        'auto_add_invited_external_users': 'auto_add_invited_external_users'
    }

    def __init__(self, enable=None, can_add_external_users=None, auto_add_invited_external_users=None):  # noqa: E501
        """AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._can_add_external_users = None
        self._auto_add_invited_external_users = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if can_add_external_users is not None:
            self.can_add_external_users = can_add_external_users
        if auto_add_invited_external_users is not None:
            self.auto_add_invited_external_users = auto_add_invited_external_users

    @property
    def enable(self):
        """Gets the enable of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501

        Whether to enable the **Enable continuous meeting chat** setting.  # noqa: E501

        :return: The enable of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.

        Whether to enable the **Enable continuous meeting chat** setting.  # noqa: E501

        :param enable: The enable of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def can_add_external_users(self):
        """Gets the can_add_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501

        Whether to enable the **External users can be added** setting.  # noqa: E501

        :return: The can_add_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_external_users

    @can_add_external_users.setter
    def can_add_external_users(self, can_add_external_users):
        """Sets the can_add_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.

        Whether to enable the **External users can be added** setting.  # noqa: E501

        :param can_add_external_users: The can_add_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :type: bool
        """

        self._can_add_external_users = can_add_external_users

    @property
    def auto_add_invited_external_users(self):
        """Gets the auto_add_invited_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501

        Whether to enable the **Automatically add invited external users** setting.  # noqa: E501

        :return: The auto_add_invited_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :rtype: bool
        """
        return self._auto_add_invited_external_users

    @auto_add_invited_external_users.setter
    def auto_add_invited_external_users(self, auto_add_invited_external_users):
        """Sets the auto_add_invited_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.

        Whether to enable the **Automatically add invited external users** setting.  # noqa: E501

        :param auto_add_invited_external_users: The auto_add_invited_external_users of this AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat.  # noqa: E501
        :type: bool
        """

        self._auto_add_invited_external_users = auto_add_invited_external_users

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
        if issubclass(AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other