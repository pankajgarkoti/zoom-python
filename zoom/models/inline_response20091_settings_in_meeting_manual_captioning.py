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

class InlineResponse20091SettingsInMeetingManualCaptioning(object):
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
        'auto_generated_captions': 'bool',
        'allow_to_type': 'bool',
        'manual_captions': 'bool',
        'save_captions': 'bool'
    }

    attribute_map = {
        'auto_generated_captions': 'auto_generated_captions',
        'allow_to_type': 'allow_to_type',
        'manual_captions': 'manual_captions',
        'save_captions': 'save_captions'
    }

    def __init__(self, auto_generated_captions=None, allow_to_type=None, manual_captions=None, save_captions=None):  # noqa: E501
        """InlineResponse20091SettingsInMeetingManualCaptioning - a model defined in Swagger"""  # noqa: E501
        self._auto_generated_captions = None
        self._allow_to_type = None
        self._manual_captions = None
        self._save_captions = None
        self.discriminator = None
        if auto_generated_captions is not None:
            self.auto_generated_captions = auto_generated_captions
        if allow_to_type is not None:
            self.allow_to_type = allow_to_type
        if manual_captions is not None:
            self.manual_captions = manual_captions
        if save_captions is not None:
            self.save_captions = save_captions

    @property
    def auto_generated_captions(self):
        """Gets the auto_generated_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501

        Whether to enable Zoom's [live transcription feature](https://support.zoom.us/hc/en-us/articles/207279736-Managing-closed-captioning-and-live-transcription#h_01FHGGHYJ4457H4GSZY0KM3NSB).  # noqa: E501

        :return: The auto_generated_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :rtype: bool
        """
        return self._auto_generated_captions

    @auto_generated_captions.setter
    def auto_generated_captions(self, auto_generated_captions):
        """Sets the auto_generated_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.

        Whether to enable Zoom's [live transcription feature](https://support.zoom.us/hc/en-us/articles/207279736-Managing-closed-captioning-and-live-transcription#h_01FHGGHYJ4457H4GSZY0KM3NSB).  # noqa: E501

        :param auto_generated_captions: The auto_generated_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :type: bool
        """

        self._auto_generated_captions = auto_generated_captions

    @property
    def allow_to_type(self):
        """Gets the allow_to_type of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501

        Whether the host can manually caption or let the host assign a participant to provide manual captioning.  # noqa: E501

        :return: The allow_to_type of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :rtype: bool
        """
        return self._allow_to_type

    @allow_to_type.setter
    def allow_to_type(self, allow_to_type):
        """Sets the allow_to_type of this InlineResponse20091SettingsInMeetingManualCaptioning.

        Whether the host can manually caption or let the host assign a participant to provide manual captioning.  # noqa: E501

        :param allow_to_type: The allow_to_type of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :type: bool
        """

        self._allow_to_type = allow_to_type

    @property
    def manual_captions(self):
        """Gets the manual_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501

        Whether to [enable manual closed captioning](https://support.zoom.us/hc/en-us/articles/207279736-Managing-closed-captioning-and-live-transcription).  # noqa: E501

        :return: The manual_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :rtype: bool
        """
        return self._manual_captions

    @manual_captions.setter
    def manual_captions(self, manual_captions):
        """Sets the manual_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.

        Whether to [enable manual closed captioning](https://support.zoom.us/hc/en-us/articles/207279736-Managing-closed-captioning-and-live-transcription).  # noqa: E501

        :param manual_captions: The manual_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :type: bool
        """

        self._manual_captions = manual_captions

    @property
    def save_captions(self):
        """Gets the save_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501

        Allow participants to save closed captions.  # noqa: E501

        :return: The save_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :rtype: bool
        """
        return self._save_captions

    @save_captions.setter
    def save_captions(self, save_captions):
        """Sets the save_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.

        Allow participants to save closed captions.  # noqa: E501

        :param save_captions: The save_captions of this InlineResponse20091SettingsInMeetingManualCaptioning.  # noqa: E501
        :type: bool
        """

        self._save_captions = save_captions

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
        if issubclass(InlineResponse20091SettingsInMeetingManualCaptioning, dict):
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
        if not isinstance(other, InlineResponse20091SettingsInMeetingManualCaptioning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
