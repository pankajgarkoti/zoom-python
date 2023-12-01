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

class AccountsaccountIdsettingsInMeetingLanguageInterpretation(object):
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
        'custom_languages': 'list[str]',
        'enable_language_interpretation_by_default': 'bool',
        'allow_participants_to_speak_in_listening_channel': 'bool',
        'allow_up_to_25_custom_languages_when_scheduling_meetings': 'bool',
        'enable': 'bool'
    }

    attribute_map = {
        'custom_languages': 'custom_languages',
        'enable_language_interpretation_by_default': 'enable_language_interpretation_by_default',
        'allow_participants_to_speak_in_listening_channel': 'allow_participants_to_speak_in_listening_channel',
        'allow_up_to_25_custom_languages_when_scheduling_meetings': 'allow_up_to_25_custom_languages_when_scheduling_meetings',
        'enable': 'enable'
    }

    def __init__(self, custom_languages=None, enable_language_interpretation_by_default=None, allow_participants_to_speak_in_listening_channel=None, allow_up_to_25_custom_languages_when_scheduling_meetings=None, enable=None):  # noqa: E501
        """AccountsaccountIdsettingsInMeetingLanguageInterpretation - a model defined in Swagger"""  # noqa: E501
        self._custom_languages = None
        self._enable_language_interpretation_by_default = None
        self._allow_participants_to_speak_in_listening_channel = None
        self._allow_up_to_25_custom_languages_when_scheduling_meetings = None
        self._enable = None
        self.discriminator = None
        if custom_languages is not None:
            self.custom_languages = custom_languages
        if enable_language_interpretation_by_default is not None:
            self.enable_language_interpretation_by_default = enable_language_interpretation_by_default
        if allow_participants_to_speak_in_listening_channel is not None:
            self.allow_participants_to_speak_in_listening_channel = allow_participants_to_speak_in_listening_channel
        if allow_up_to_25_custom_languages_when_scheduling_meetings is not None:
            self.allow_up_to_25_custom_languages_when_scheduling_meetings = allow_up_to_25_custom_languages_when_scheduling_meetings
        if enable is not None:
            self.enable = enable

    @property
    def custom_languages(self):
        """Gets the custom_languages of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501

        A list of user-defined supported languages.  # noqa: E501

        :return: The custom_languages of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_languages

    @custom_languages.setter
    def custom_languages(self, custom_languages):
        """Sets the custom_languages of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.

        A list of user-defined supported languages.  # noqa: E501

        :param custom_languages: The custom_languages of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :type: list[str]
        """

        self._custom_languages = custom_languages

    @property
    def enable_language_interpretation_by_default(self):
        """Gets the enable_language_interpretation_by_default of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501

        Whether to enable language interpretation by default.  # noqa: E501

        :return: The enable_language_interpretation_by_default of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :rtype: bool
        """
        return self._enable_language_interpretation_by_default

    @enable_language_interpretation_by_default.setter
    def enable_language_interpretation_by_default(self, enable_language_interpretation_by_default):
        """Sets the enable_language_interpretation_by_default of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.

        Whether to enable language interpretation by default.  # noqa: E501

        :param enable_language_interpretation_by_default: The enable_language_interpretation_by_default of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :type: bool
        """

        self._enable_language_interpretation_by_default = enable_language_interpretation_by_default

    @property
    def allow_participants_to_speak_in_listening_channel(self):
        """Gets the allow_participants_to_speak_in_listening_channel of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501

        Whether to allow participants to speak in the listening channel.  # noqa: E501

        :return: The allow_participants_to_speak_in_listening_channel of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :rtype: bool
        """
        return self._allow_participants_to_speak_in_listening_channel

    @allow_participants_to_speak_in_listening_channel.setter
    def allow_participants_to_speak_in_listening_channel(self, allow_participants_to_speak_in_listening_channel):
        """Sets the allow_participants_to_speak_in_listening_channel of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.

        Whether to allow participants to speak in the listening channel.  # noqa: E501

        :param allow_participants_to_speak_in_listening_channel: The allow_participants_to_speak_in_listening_channel of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :type: bool
        """

        self._allow_participants_to_speak_in_listening_channel = allow_participants_to_speak_in_listening_channel

    @property
    def allow_up_to_25_custom_languages_when_scheduling_meetings(self):
        """Gets the allow_up_to_25_custom_languages_when_scheduling_meetings of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501

        Whether to allow up to 25 custom languages when scheduling meetings.  # noqa: E501

        :return: The allow_up_to_25_custom_languages_when_scheduling_meetings of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :rtype: bool
        """
        return self._allow_up_to_25_custom_languages_when_scheduling_meetings

    @allow_up_to_25_custom_languages_when_scheduling_meetings.setter
    def allow_up_to_25_custom_languages_when_scheduling_meetings(self, allow_up_to_25_custom_languages_when_scheduling_meetings):
        """Sets the allow_up_to_25_custom_languages_when_scheduling_meetings of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.

        Whether to allow up to 25 custom languages when scheduling meetings.  # noqa: E501

        :param allow_up_to_25_custom_languages_when_scheduling_meetings: The allow_up_to_25_custom_languages_when_scheduling_meetings of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :type: bool
        """

        self._allow_up_to_25_custom_languages_when_scheduling_meetings = allow_up_to_25_custom_languages_when_scheduling_meetings

    @property
    def enable(self):
        """Gets the enable of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501

        Whether to allow hosts to assign participants as interpreters who can interpret one language into another in real-time.  # noqa: E501

        :return: The enable of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.

        Whether to allow hosts to assign participants as interpreters who can interpret one language into another in real-time.  # noqa: E501

        :param enable: The enable of this AccountsaccountIdsettingsInMeetingLanguageInterpretation.  # noqa: E501
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
        if issubclass(AccountsaccountIdsettingsInMeetingLanguageInterpretation, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsInMeetingLanguageInterpretation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
