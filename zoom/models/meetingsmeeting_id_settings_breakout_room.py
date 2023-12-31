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

class MeetingsmeetingIdSettingsBreakoutRoom(object):
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
        'rooms': 'list[MeetingsmeetingIdSettingsBreakoutRoomRooms]'
    }

    attribute_map = {
        'enable': 'enable',
        'rooms': 'rooms'
    }

    def __init__(self, enable=None, rooms=None):  # noqa: E501
        """MeetingsmeetingIdSettingsBreakoutRoom - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._rooms = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if rooms is not None:
            self.rooms = rooms

    @property
    def enable(self):
        """Gets the enable of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501

        Set this field's value to `true` to enable the [breakout room pre-assign](https://support.zoom.us/hc/en-us/articles/360032752671-Pre-assigning-participants-to-breakout-rooms#h_36f71353-4190-48a2-b999-ca129861c1f4) option.  # noqa: E501

        :return: The enable of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this MeetingsmeetingIdSettingsBreakoutRoom.

        Set this field's value to `true` to enable the [breakout room pre-assign](https://support.zoom.us/hc/en-us/articles/360032752671-Pre-assigning-participants-to-breakout-rooms#h_36f71353-4190-48a2-b999-ca129861c1f4) option.  # noqa: E501

        :param enable: The enable of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def rooms(self):
        """Gets the rooms of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501

        Create room(s).  # noqa: E501

        :return: The rooms of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501
        :rtype: list[MeetingsmeetingIdSettingsBreakoutRoomRooms]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """Sets the rooms of this MeetingsmeetingIdSettingsBreakoutRoom.

        Create room(s).  # noqa: E501

        :param rooms: The rooms of this MeetingsmeetingIdSettingsBreakoutRoom.  # noqa: E501
        :type: list[MeetingsmeetingIdSettingsBreakoutRoomRooms]
        """

        self._rooms = rooms

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
        if issubclass(MeetingsmeetingIdSettingsBreakoutRoom, dict):
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
        if not isinstance(other, MeetingsmeetingIdSettingsBreakoutRoom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
