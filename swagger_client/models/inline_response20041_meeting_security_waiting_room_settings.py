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

class InlineResponse20041MeetingSecurityWaitingRoomSettings(object):
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
        'participants_to_place_in_waiting_room': 'int',
        'users_who_can_admit_participants_from_waiting_room': 'int',
        'whitelisted_domains_for_waiting_room': 'str'
    }

    attribute_map = {
        'participants_to_place_in_waiting_room': 'participants_to_place_in_waiting_room',
        'users_who_can_admit_participants_from_waiting_room': 'users_who_can_admit_participants_from_waiting_room',
        'whitelisted_domains_for_waiting_room': 'whitelisted_domains_for_waiting_room'
    }

    def __init__(self, participants_to_place_in_waiting_room=None, users_who_can_admit_participants_from_waiting_room=None, whitelisted_domains_for_waiting_room=None):  # noqa: E501
        """InlineResponse20041MeetingSecurityWaitingRoomSettings - a model defined in Swagger"""  # noqa: E501
        self._participants_to_place_in_waiting_room = None
        self._users_who_can_admit_participants_from_waiting_room = None
        self._whitelisted_domains_for_waiting_room = None
        self.discriminator = None
        if participants_to_place_in_waiting_room is not None:
            self.participants_to_place_in_waiting_room = participants_to_place_in_waiting_room
        if users_who_can_admit_participants_from_waiting_room is not None:
            self.users_who_can_admit_participants_from_waiting_room = users_who_can_admit_participants_from_waiting_room
        if whitelisted_domains_for_waiting_room is not None:
            self.whitelisted_domains_for_waiting_room = whitelisted_domains_for_waiting_room

    @property
    def participants_to_place_in_waiting_room(self):
        """Gets the participants_to_place_in_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501

        The type of participants to be admitted to the waiting room.  * `0` - All attendees.  * `1` - Users who are not in your account.  * `2` - Users who are not in your account and are not part of your [allowed domains list](https://support.zoom.us/hc/en-us/articles/360037117472-Configuring-authentication-profiles#h_e3cf0d5f-eec7-4c2a-ad29-ef2a5079a7da).  # noqa: E501

        :return: The participants_to_place_in_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :rtype: int
        """
        return self._participants_to_place_in_waiting_room

    @participants_to_place_in_waiting_room.setter
    def participants_to_place_in_waiting_room(self, participants_to_place_in_waiting_room):
        """Sets the participants_to_place_in_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.

        The type of participants to be admitted to the waiting room.  * `0` - All attendees.  * `1` - Users who are not in your account.  * `2` - Users who are not in your account and are not part of your [allowed domains list](https://support.zoom.us/hc/en-us/articles/360037117472-Configuring-authentication-profiles#h_e3cf0d5f-eec7-4c2a-ad29-ef2a5079a7da).  # noqa: E501

        :param participants_to_place_in_waiting_room: The participants_to_place_in_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if participants_to_place_in_waiting_room not in allowed_values:
            raise ValueError(
                "Invalid value for `participants_to_place_in_waiting_room` ({0}), must be one of {1}"  # noqa: E501
                .format(participants_to_place_in_waiting_room, allowed_values)
            )

        self._participants_to_place_in_waiting_room = participants_to_place_in_waiting_room

    @property
    def users_who_can_admit_participants_from_waiting_room(self):
        """Gets the users_who_can_admit_participants_from_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501

        The users who can admit participants from the waiting room.  * `0` - Host and co-hosts only.  * `1` - Host, co-hosts, and anyone who bypassed the Waiting Room if the host and co-hosts are not present.  # noqa: E501

        :return: The users_who_can_admit_participants_from_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :rtype: int
        """
        return self._users_who_can_admit_participants_from_waiting_room

    @users_who_can_admit_participants_from_waiting_room.setter
    def users_who_can_admit_participants_from_waiting_room(self, users_who_can_admit_participants_from_waiting_room):
        """Sets the users_who_can_admit_participants_from_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.

        The users who can admit participants from the waiting room.  * `0` - Host and co-hosts only.  * `1` - Host, co-hosts, and anyone who bypassed the Waiting Room if the host and co-hosts are not present.  # noqa: E501

        :param users_who_can_admit_participants_from_waiting_room: The users_who_can_admit_participants_from_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if users_who_can_admit_participants_from_waiting_room not in allowed_values:
            raise ValueError(
                "Invalid value for `users_who_can_admit_participants_from_waiting_room` ({0}), must be one of {1}"  # noqa: E501
                .format(users_who_can_admit_participants_from_waiting_room, allowed_values)
            )

        self._users_who_can_admit_participants_from_waiting_room = users_who_can_admit_participants_from_waiting_room

    @property
    def whitelisted_domains_for_waiting_room(self):
        """Gets the whitelisted_domains_for_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501

        If the `participants_to_place_in_waiting_room` field is `2`, a comma-separated list of the domains that can bypass the waiting room (`example.com,example2.com`).  # noqa: E501

        :return: The whitelisted_domains_for_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :rtype: str
        """
        return self._whitelisted_domains_for_waiting_room

    @whitelisted_domains_for_waiting_room.setter
    def whitelisted_domains_for_waiting_room(self, whitelisted_domains_for_waiting_room):
        """Sets the whitelisted_domains_for_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.

        If the `participants_to_place_in_waiting_room` field is `2`, a comma-separated list of the domains that can bypass the waiting room (`example.com,example2.com`).  # noqa: E501

        :param whitelisted_domains_for_waiting_room: The whitelisted_domains_for_waiting_room of this InlineResponse20041MeetingSecurityWaitingRoomSettings.  # noqa: E501
        :type: str
        """

        self._whitelisted_domains_for_waiting_room = whitelisted_domains_for_waiting_room

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
        if issubclass(InlineResponse20041MeetingSecurityWaitingRoomSettings, dict):
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
        if not isinstance(other, InlineResponse20041MeetingSecurityWaitingRoomSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
