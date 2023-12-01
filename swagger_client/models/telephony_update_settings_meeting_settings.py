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

class TelephonyUpdateSettingsMeetingSettings(object):
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
        'audio_conference_info': 'str',
        'show_international_numbers_link': 'bool',
        'telephony_regions': 'TelephonyUpdateSettingsMeetingSettingsTelephonyRegions',
        'third_party_audio': 'bool'
    }

    attribute_map = {
        'audio_conference_info': 'audio_conference_info',
        'show_international_numbers_link': 'show_international_numbers_link',
        'telephony_regions': 'telephony_regions',
        'third_party_audio': 'third_party_audio'
    }

    def __init__(self, audio_conference_info='', show_international_numbers_link=None, telephony_regions=None, third_party_audio=None):  # noqa: E501
        """TelephonyUpdateSettingsMeetingSettings - a model defined in Swagger"""  # noqa: E501
        self._audio_conference_info = None
        self._show_international_numbers_link = None
        self._telephony_regions = None
        self._third_party_audio = None
        self.discriminator = None
        if audio_conference_info is not None:
            self.audio_conference_info = audio_conference_info
        if show_international_numbers_link is not None:
            self.show_international_numbers_link = show_international_numbers_link
        if telephony_regions is not None:
            self.telephony_regions = telephony_regions
        if third_party_audio is not None:
            self.third_party_audio = third_party_audio

    @property
    def audio_conference_info(self):
        """Gets the audio_conference_info of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501

        Third party audio conference info.  # noqa: E501

        :return: The audio_conference_info of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :rtype: str
        """
        return self._audio_conference_info

    @audio_conference_info.setter
    def audio_conference_info(self, audio_conference_info):
        """Sets the audio_conference_info of this TelephonyUpdateSettingsMeetingSettings.

        Third party audio conference info.  # noqa: E501

        :param audio_conference_info: The audio_conference_info of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :type: str
        """

        self._audio_conference_info = audio_conference_info

    @property
    def show_international_numbers_link(self):
        """Gets the show_international_numbers_link of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501

        Show the international numbers link on the invitation email.  # noqa: E501

        :return: The show_international_numbers_link of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_international_numbers_link

    @show_international_numbers_link.setter
    def show_international_numbers_link(self, show_international_numbers_link):
        """Sets the show_international_numbers_link of this TelephonyUpdateSettingsMeetingSettings.

        Show the international numbers link on the invitation email.  # noqa: E501

        :param show_international_numbers_link: The show_international_numbers_link of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :type: bool
        """

        self._show_international_numbers_link = show_international_numbers_link

    @property
    def telephony_regions(self):
        """Gets the telephony_regions of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501


        :return: The telephony_regions of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :rtype: TelephonyUpdateSettingsMeetingSettingsTelephonyRegions
        """
        return self._telephony_regions

    @telephony_regions.setter
    def telephony_regions(self, telephony_regions):
        """Sets the telephony_regions of this TelephonyUpdateSettingsMeetingSettings.


        :param telephony_regions: The telephony_regions of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :type: TelephonyUpdateSettingsMeetingSettingsTelephonyRegions
        """

        self._telephony_regions = telephony_regions

    @property
    def third_party_audio(self):
        """Gets the third_party_audio of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501

        Third party audio conference.  # noqa: E501

        :return: The third_party_audio of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :rtype: bool
        """
        return self._third_party_audio

    @third_party_audio.setter
    def third_party_audio(self, third_party_audio):
        """Sets the third_party_audio of this TelephonyUpdateSettingsMeetingSettings.

        Third party audio conference.  # noqa: E501

        :param third_party_audio: The third_party_audio of this TelephonyUpdateSettingsMeetingSettings.  # noqa: E501
        :type: bool
        """

        self._third_party_audio = third_party_audio

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
        if issubclass(TelephonyUpdateSettingsMeetingSettings, dict):
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
        if not isinstance(other, TelephonyUpdateSettingsMeetingSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
