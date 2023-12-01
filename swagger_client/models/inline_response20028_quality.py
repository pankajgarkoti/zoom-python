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

class InlineResponse20028Quality(object):
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
        'audio': 'MeetingQualityObject',
        'screen_share': 'MeetingQualityObject',
        'video': 'MeetingQualityObject'
    }

    attribute_map = {
        'audio': 'audio',
        'screen_share': 'screen_share',
        'video': 'video'
    }

    def __init__(self, audio=None, screen_share=None, video=None):  # noqa: E501
        """InlineResponse20028Quality - a model defined in Swagger"""  # noqa: E501
        self._audio = None
        self._screen_share = None
        self._video = None
        self.discriminator = None
        if audio is not None:
            self.audio = audio
        if screen_share is not None:
            self.screen_share = screen_share
        if video is not None:
            self.video = video

    @property
    def audio(self):
        """Gets the audio of this InlineResponse20028Quality.  # noqa: E501


        :return: The audio of this InlineResponse20028Quality.  # noqa: E501
        :rtype: MeetingQualityObject
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this InlineResponse20028Quality.


        :param audio: The audio of this InlineResponse20028Quality.  # noqa: E501
        :type: MeetingQualityObject
        """

        self._audio = audio

    @property
    def screen_share(self):
        """Gets the screen_share of this InlineResponse20028Quality.  # noqa: E501


        :return: The screen_share of this InlineResponse20028Quality.  # noqa: E501
        :rtype: MeetingQualityObject
        """
        return self._screen_share

    @screen_share.setter
    def screen_share(self, screen_share):
        """Sets the screen_share of this InlineResponse20028Quality.


        :param screen_share: The screen_share of this InlineResponse20028Quality.  # noqa: E501
        :type: MeetingQualityObject
        """

        self._screen_share = screen_share

    @property
    def video(self):
        """Gets the video of this InlineResponse20028Quality.  # noqa: E501


        :return: The video of this InlineResponse20028Quality.  # noqa: E501
        :rtype: MeetingQualityObject
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this InlineResponse20028Quality.


        :param video: The video of this InlineResponse20028Quality.  # noqa: E501
        :type: MeetingQualityObject
        """

        self._video = video

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
        if issubclass(InlineResponse20028Quality, dict):
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
        if not isinstance(other, InlineResponse20028Quality):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other