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

class GroupsgroupIdsettingsInMeetingWebinarChat(object):
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
        'allow_attendees_chat_with': 'int',
        'allow_auto_save_local_chat_file': 'bool',
        'allow_panelists_chat_with': 'int',
        'allow_panelists_send_direct_message': 'bool',
        'allow_users_save_chats': 'int',
        'default_attendees_chat_with': 'int',
        'enable': 'bool'
    }

    attribute_map = {
        'allow_attendees_chat_with': 'allow_attendees_chat_with',
        'allow_auto_save_local_chat_file': 'allow_auto_save_local_chat_file',
        'allow_panelists_chat_with': 'allow_panelists_chat_with',
        'allow_panelists_send_direct_message': 'allow_panelists_send_direct_message',
        'allow_users_save_chats': 'allow_users_save_chats',
        'default_attendees_chat_with': 'default_attendees_chat_with',
        'enable': 'enable'
    }

    def __init__(self, allow_attendees_chat_with=None, allow_auto_save_local_chat_file=None, allow_panelists_chat_with=None, allow_panelists_send_direct_message=None, allow_users_save_chats=None, default_attendees_chat_with=None, enable=None):  # noqa: E501
        """GroupsgroupIdsettingsInMeetingWebinarChat - a model defined in Swagger"""  # noqa: E501
        self._allow_attendees_chat_with = None
        self._allow_auto_save_local_chat_file = None
        self._allow_panelists_chat_with = None
        self._allow_panelists_send_direct_message = None
        self._allow_users_save_chats = None
        self._default_attendees_chat_with = None
        self._enable = None
        self.discriminator = None
        if allow_attendees_chat_with is not None:
            self.allow_attendees_chat_with = allow_attendees_chat_with
        if allow_auto_save_local_chat_file is not None:
            self.allow_auto_save_local_chat_file = allow_auto_save_local_chat_file
        if allow_panelists_chat_with is not None:
            self.allow_panelists_chat_with = allow_panelists_chat_with
        if allow_panelists_send_direct_message is not None:
            self.allow_panelists_send_direct_message = allow_panelists_send_direct_message
        if allow_users_save_chats is not None:
            self.allow_users_save_chats = allow_users_save_chats
        if default_attendees_chat_with is not None:
            self.default_attendees_chat_with = default_attendees_chat_with
        if enable is not None:
            self.enable = enable

    @property
    def allow_attendees_chat_with(self):
        """Gets the allow_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Allow webinar attendees to chat with: * `1` - No one. * `2` - Host and all panelists. * `3` - Everyone.  # noqa: E501

        :return: The allow_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: int
        """
        return self._allow_attendees_chat_with

    @allow_attendees_chat_with.setter
    def allow_attendees_chat_with(self, allow_attendees_chat_with):
        """Sets the allow_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Allow webinar attendees to chat with: * `1` - No one. * `2` - Host and all panelists. * `3` - Everyone.  # noqa: E501

        :param allow_attendees_chat_with: The allow_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if allow_attendees_chat_with not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_attendees_chat_with` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_attendees_chat_with, allowed_values)
            )

        self._allow_attendees_chat_with = allow_attendees_chat_with

    @property
    def allow_auto_save_local_chat_file(self):
        """Gets the allow_auto_save_local_chat_file of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Whether to automatically save chat messages to a local file on the host's computer when the webinar ends.  # noqa: E501

        :return: The allow_auto_save_local_chat_file of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: bool
        """
        return self._allow_auto_save_local_chat_file

    @allow_auto_save_local_chat_file.setter
    def allow_auto_save_local_chat_file(self, allow_auto_save_local_chat_file):
        """Sets the allow_auto_save_local_chat_file of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Whether to automatically save chat messages to a local file on the host's computer when the webinar ends.  # noqa: E501

        :param allow_auto_save_local_chat_file: The allow_auto_save_local_chat_file of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: bool
        """

        self._allow_auto_save_local_chat_file = allow_auto_save_local_chat_file

    @property
    def allow_panelists_chat_with(self):
        """Gets the allow_panelists_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Allow webinar panelists to chat with: * `1` - Host and all panelists. * `2` - Everyone.  # noqa: E501

        :return: The allow_panelists_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: int
        """
        return self._allow_panelists_chat_with

    @allow_panelists_chat_with.setter
    def allow_panelists_chat_with(self, allow_panelists_chat_with):
        """Sets the allow_panelists_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Allow webinar panelists to chat with: * `1` - Host and all panelists. * `2` - Everyone.  # noqa: E501

        :param allow_panelists_chat_with: The allow_panelists_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if allow_panelists_chat_with not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_panelists_chat_with` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_panelists_chat_with, allowed_values)
            )

        self._allow_panelists_chat_with = allow_panelists_chat_with

    @property
    def allow_panelists_send_direct_message(self):
        """Gets the allow_panelists_send_direct_message of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Whether to allow webinar panelists to send direct messages to other panelists.  # noqa: E501

        :return: The allow_panelists_send_direct_message of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: bool
        """
        return self._allow_panelists_send_direct_message

    @allow_panelists_send_direct_message.setter
    def allow_panelists_send_direct_message(self, allow_panelists_send_direct_message):
        """Sets the allow_panelists_send_direct_message of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Whether to allow webinar panelists to send direct messages to other panelists.  # noqa: E501

        :param allow_panelists_send_direct_message: The allow_panelists_send_direct_message of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: bool
        """

        self._allow_panelists_send_direct_message = allow_panelists_send_direct_message

    @property
    def allow_users_save_chats(self):
        """Gets the allow_users_save_chats of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Whether webinar attendees can save chats. * `0` - Attendees cannot save chats. * `1` - Attendees can only save host and panelist chats. * `2` - Attendees can save all chats.  # noqa: E501

        :return: The allow_users_save_chats of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: int
        """
        return self._allow_users_save_chats

    @allow_users_save_chats.setter
    def allow_users_save_chats(self, allow_users_save_chats):
        """Sets the allow_users_save_chats of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Whether webinar attendees can save chats. * `0` - Attendees cannot save chats. * `1` - Attendees can only save host and panelist chats. * `2` - Attendees can save all chats.  # noqa: E501

        :param allow_users_save_chats: The allow_users_save_chats of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if allow_users_save_chats not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_users_save_chats` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_users_save_chats, allowed_values)
            )

        self._allow_users_save_chats = allow_users_save_chats

    @property
    def default_attendees_chat_with(self):
        """Gets the default_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        By default, who to allow webinar attendees to chat with. * `1` - Host and all panelists. * `2` - Everyone.  # noqa: E501

        :return: The default_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: int
        """
        return self._default_attendees_chat_with

    @default_attendees_chat_with.setter
    def default_attendees_chat_with(self, default_attendees_chat_with):
        """Sets the default_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.

        By default, who to allow webinar attendees to chat with. * `1` - Host and all panelists. * `2` - Everyone.  # noqa: E501

        :param default_attendees_chat_with: The default_attendees_chat_with of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if default_attendees_chat_with not in allowed_values:
            raise ValueError(
                "Invalid value for `default_attendees_chat_with` ({0}), must be one of {1}"  # noqa: E501
                .format(default_attendees_chat_with, allowed_values)
            )

        self._default_attendees_chat_with = default_attendees_chat_with

    @property
    def enable(self):
        """Gets the enable of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501

        Whether to allow webinar participants to send chat messages.  # noqa: E501

        :return: The enable of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GroupsgroupIdsettingsInMeetingWebinarChat.

        Whether to allow webinar participants to send chat messages.  # noqa: E501

        :param enable: The enable of this GroupsgroupIdsettingsInMeetingWebinarChat.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if issubclass(GroupsgroupIdsettingsInMeetingWebinarChat, dict):
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
        if not isinstance(other, GroupsgroupIdsettingsInMeetingWebinarChat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other