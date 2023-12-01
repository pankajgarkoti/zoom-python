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

class InlineResponse2002MeetingSecurityMeetingPasswordRequirement(object):
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
        'have_letter': 'bool',
        'have_number': 'bool',
        'have_special_character': 'bool',
        'have_upper_and_lower_characters': 'bool',
        'length': 'int',
        'only_allow_numeric': 'bool',
        'weak_enhance_detection': 'bool'
    }

    attribute_map = {
        'consecutive_characters_length': 'consecutive_characters_length',
        'have_letter': 'have_letter',
        'have_number': 'have_number',
        'have_special_character': 'have_special_character',
        'have_upper_and_lower_characters': 'have_upper_and_lower_characters',
        'length': 'length',
        'only_allow_numeric': 'only_allow_numeric',
        'weak_enhance_detection': 'weak_enhance_detection'
    }

    def __init__(self, consecutive_characters_length=None, have_letter=None, have_number=None, have_special_character=None, have_upper_and_lower_characters=None, length=None, only_allow_numeric=None, weak_enhance_detection=None):  # noqa: E501
        """InlineResponse2002MeetingSecurityMeetingPasswordRequirement - a model defined in Swagger"""  # noqa: E501
        self._consecutive_characters_length = None
        self._have_letter = None
        self._have_number = None
        self._have_special_character = None
        self._have_upper_and_lower_characters = None
        self._length = None
        self._only_allow_numeric = None
        self._weak_enhance_detection = None
        self.discriminator = None
        if consecutive_characters_length is not None:
            self.consecutive_characters_length = consecutive_characters_length
        if have_letter is not None:
            self.have_letter = have_letter
        if have_number is not None:
            self.have_number = have_number
        if have_special_character is not None:
            self.have_special_character = have_special_character
        if have_upper_and_lower_characters is not None:
            self.have_upper_and_lower_characters = have_upper_and_lower_characters
        if length is not None:
            self.length = length
        if only_allow_numeric is not None:
            self.only_allow_numeric = only_allow_numeric
        if weak_enhance_detection is not None:
            self.weak_enhance_detection = weak_enhance_detection

    @property
    def consecutive_characters_length(self):
        """Gets the consecutive_characters_length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        The maximum length of consecutive characters (for example, `abcdef`) allowed in a passcode.  * `4` through `8` - The maximum consecutive characters length. The length is `n` minus `1`, where `n` is the value. For example, if the value is `4`, there can only be a maximum of `3` consecutive characters in a passcode, such as `abc1x@8fdh`.  * `0` - No consecutive character restriction.  # noqa: E501

        :return: The consecutive_characters_length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: int
        """
        return self._consecutive_characters_length

    @consecutive_characters_length.setter
    def consecutive_characters_length(self, consecutive_characters_length):
        """Sets the consecutive_characters_length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        The maximum length of consecutive characters (for example, `abcdef`) allowed in a passcode.  * `4` through `8` - The maximum consecutive characters length. The length is `n` minus `1`, where `n` is the value. For example, if the value is `4`, there can only be a maximum of `3` consecutive characters in a passcode, such as `abc1x@8fdh`.  * `0` - No consecutive character restriction.  # noqa: E501

        :param consecutive_characters_length: The consecutive_characters_length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 4, 5, 6, 7, 8]  # noqa: E501
        if consecutive_characters_length not in allowed_values:
            raise ValueError(
                "Invalid value for `consecutive_characters_length` ({0}), must be one of {1}"  # noqa: E501
                .format(consecutive_characters_length, allowed_values)
            )

        self._consecutive_characters_length = consecutive_characters_length

    @property
    def have_letter(self):
        """Gets the have_letter of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether passcodes must contain at least one letter character.  # noqa: E501

        :return: The have_letter of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._have_letter

    @have_letter.setter
    def have_letter(self, have_letter):
        """Sets the have_letter of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether passcodes must contain at least one letter character.  # noqa: E501

        :param have_letter: The have_letter of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._have_letter = have_letter

    @property
    def have_number(self):
        """Gets the have_number of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether passcodes must contain at least one numeric character.  # noqa: E501

        :return: The have_number of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._have_number

    @have_number.setter
    def have_number(self, have_number):
        """Sets the have_number of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether passcodes must contain at least one numeric character.  # noqa: E501

        :param have_number: The have_number of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._have_number = have_number

    @property
    def have_special_character(self):
        """Gets the have_special_character of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether passcodes must contain at least one special character. For example, `!`, `@`, and/or `#` characters.  # noqa: E501

        :return: The have_special_character of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._have_special_character

    @have_special_character.setter
    def have_special_character(self, have_special_character):
        """Sets the have_special_character of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether passcodes must contain at least one special character. For example, `!`, `@`, and/or `#` characters.  # noqa: E501

        :param have_special_character: The have_special_character of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._have_special_character = have_special_character

    @property
    def have_upper_and_lower_characters(self):
        """Gets the have_upper_and_lower_characters of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether passcodes must include uppercase and lowercase characters.  # noqa: E501

        :return: The have_upper_and_lower_characters of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._have_upper_and_lower_characters

    @have_upper_and_lower_characters.setter
    def have_upper_and_lower_characters(self, have_upper_and_lower_characters):
        """Sets the have_upper_and_lower_characters of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether passcodes must include uppercase and lowercase characters.  # noqa: E501

        :param have_upper_and_lower_characters: The have_upper_and_lower_characters of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._have_upper_and_lower_characters = have_upper_and_lower_characters

    @property
    def length(self):
        """Gets the length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        The minimum passcode length.  # noqa: E501

        :return: The length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        The minimum passcode length.  # noqa: E501

        :param length: The length of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def only_allow_numeric(self):
        """Gets the only_allow_numeric of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether passcodes must contain **only** numeric characters.  # noqa: E501

        :return: The only_allow_numeric of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._only_allow_numeric

    @only_allow_numeric.setter
    def only_allow_numeric(self, only_allow_numeric):
        """Sets the only_allow_numeric of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether passcodes must contain **only** numeric characters.  # noqa: E501

        :param only_allow_numeric: The only_allow_numeric of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :type: bool
        """

        self._only_allow_numeric = only_allow_numeric

    @property
    def weak_enhance_detection(self):
        """Gets the weak_enhance_detection of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501

        Whether users are informed when the provided passcode is weak.  # noqa: E501

        :return: The weak_enhance_detection of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
        :rtype: bool
        """
        return self._weak_enhance_detection

    @weak_enhance_detection.setter
    def weak_enhance_detection(self, weak_enhance_detection):
        """Sets the weak_enhance_detection of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.

        Whether users are informed when the provided passcode is weak.  # noqa: E501

        :param weak_enhance_detection: The weak_enhance_detection of this InlineResponse2002MeetingSecurityMeetingPasswordRequirement.  # noqa: E501
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
        if issubclass(InlineResponse2002MeetingSecurityMeetingPasswordRequirement, dict):
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
        if not isinstance(other, InlineResponse2002MeetingSecurityMeetingPasswordRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
