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

class GroupsgroupIdsettingsChatShareFiles(object):
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
        'share_option': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'share_option': 'share_option'
    }

    def __init__(self, enable=None, share_option=None):  # noqa: E501
        """GroupsgroupIdsettingsChatShareFiles - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._share_option = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if share_option is not None:
            self.share_option = share_option

    @property
    def enable(self):
        """Gets the enable of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501

        Allow users of this account to send and receive files in chats and channels. When disabled, users can still take and share screenshots.  # noqa: E501

        :return: The enable of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GroupsgroupIdsettingsChatShareFiles.

        Allow users of this account to send and receive files in chats and channels. When disabled, users can still take and share screenshots.  # noqa: E501

        :param enable: The enable of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def share_option(self):
        """Gets the share_option of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501

        Allow users of this account to send and receive files in chats and channels. When disabled, users can still take and share screenshots.  # noqa: E501

        :return: The share_option of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501
        :rtype: str
        """
        return self._share_option

    @share_option.setter
    def share_option(self, share_option):
        """Sets the share_option of this GroupsgroupIdsettingsChatShareFiles.

        Allow users of this account to send and receive files in chats and channels. When disabled, users can still take and share screenshots.  # noqa: E501

        :param share_option: The share_option of this GroupsgroupIdsettingsChatShareFiles.  # noqa: E501
        :type: str
        """
        allowed_values = ["anyone", "account", "organization"]  # noqa: E501
        if share_option not in allowed_values:
            raise ValueError(
                "Invalid value for `share_option` ({0}), must be one of {1}"  # noqa: E501
                .format(share_option, allowed_values)
            )

        self._share_option = share_option

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
        if issubclass(GroupsgroupIdsettingsChatShareFiles, dict):
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
        if not isinstance(other, GroupsgroupIdsettingsChatShareFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
