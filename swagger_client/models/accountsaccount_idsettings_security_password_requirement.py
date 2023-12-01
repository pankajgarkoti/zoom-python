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

class AccountsaccountIdsettingsSecurityPasswordRequirement(object):
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
        'consecutive_characters_length': 'int',
        'have_special_character': 'bool',
        'minimum_password_length': 'int',
        'weak_enhance_detection': 'bool'
    }

    attribute_map = {
        'consecutive_characters_length': 'consecutive_characters_length',
        'have_special_character': 'have_special_character',
        'minimum_password_length': 'minimum_password_length',
        'weak_enhance_detection': 'weak_enhance_detection'
    }

    def __init__(self, consecutive_characters_length=None, have_special_character=None, minimum_password_length=None, weak_enhance_detection=None):  # noqa: E501
        """AccountsaccountIdsettingsSecurityPasswordRequirement - a model defined in Swagger"""  # noqa: E501
        self._consecutive_characters_length = None
        self._have_special_character = None
        self._minimum_password_length = None
        self._weak_enhance_detection = None
        self.discriminator = None
        if consecutive_characters_length is not None:
            self.consecutive_characters_length = consecutive_characters_length
        if have_special_character is not None:
            self.have_special_character = have_special_character
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if weak_enhance_detection is not None:
            self.weak_enhance_detection = weak_enhance_detection

    @property
    def consecutive_characters_length(self):
        """Gets the consecutive_characters_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501

         Specify the max length of consecutive characters(abcde...) that can be used in a passcode. If you set the value of this field to `0`, no restriction will be applied on consecutive characters.   If you would like to set this restriction, you can specify a number between 4 and 8 that define the maximum allowed length for consecutive characters in a passcode.  The max allowed length will be `n-1` where `n` refers to the value you provide for this field.  For instance, if you provide `4` as the value, there can only be a maximum of `3` consecutive characters in a passcode(example: abc1x@8fdh).  # noqa: E501

        :return: The consecutive_characters_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :rtype: int
        """
        return self._consecutive_characters_length

    @consecutive_characters_length.setter
    def consecutive_characters_length(self, consecutive_characters_length):
        """Sets the consecutive_characters_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.

         Specify the max length of consecutive characters(abcde...) that can be used in a passcode. If you set the value of this field to `0`, no restriction will be applied on consecutive characters.   If you would like to set this restriction, you can specify a number between 4 and 8 that define the maximum allowed length for consecutive characters in a passcode.  The max allowed length will be `n-1` where `n` refers to the value you provide for this field.  For instance, if you provide `4` as the value, there can only be a maximum of `3` consecutive characters in a passcode(example: abc1x@8fdh).  # noqa: E501

        :param consecutive_characters_length: The consecutive_characters_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :type: int
        """

        self._consecutive_characters_length = consecutive_characters_length

    @property
    def have_special_character(self):
        """Gets the have_special_character of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501

        If the value of this field is set to `true`, the passcode must have at least one special character(!, @, #...).  # noqa: E501

        :return: The have_special_character of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._have_special_character

    @have_special_character.setter
    def have_special_character(self, have_special_character):
        """Sets the have_special_character of this AccountsaccountIdsettingsSecurityPasswordRequirement.

        If the value of this field is set to `true`, the passcode must have at least one special character(!, @, #...).  # noqa: E501

        :param have_special_character: The have_special_character of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._have_special_character = have_special_character

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501

        Specify a minimum length for the passcode. The passcode length can be between 9 and 14 characters. If the value of this field is `0`, this field is disabled and the basic passcode length (minimum of 8 characters) is required.  # noqa: E501

        :return: The minimum_password_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.

        Specify a minimum length for the passcode. The passcode length can be between 9 and 14 characters. If the value of this field is `0`, this field is disabled and the basic passcode length (minimum of 8 characters) is required.  # noqa: E501

        :param minimum_password_length: The minimum_password_length of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :type: int
        """

        self._minimum_password_length = minimum_password_length

    @property
    def weak_enhance_detection(self):
        """Gets the weak_enhance_detection of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501

        If the value of this field is set to `true`, user passcodes will have to pass detection through a weak passcode dictionary in case hackers use simple passcodes to sign in to your users' accounts.  # noqa: E501

        :return: The weak_enhance_detection of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._weak_enhance_detection

    @weak_enhance_detection.setter
    def weak_enhance_detection(self, weak_enhance_detection):
        """Sets the weak_enhance_detection of this AccountsaccountIdsettingsSecurityPasswordRequirement.

        If the value of this field is set to `true`, user passcodes will have to pass detection through a weak passcode dictionary in case hackers use simple passcodes to sign in to your users' accounts.  # noqa: E501

        :param weak_enhance_detection: The weak_enhance_detection of this AccountsaccountIdsettingsSecurityPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._weak_enhance_detection = weak_enhance_detection

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
        if issubclass(AccountsaccountIdsettingsSecurityPasswordRequirement, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsSecurityPasswordRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
