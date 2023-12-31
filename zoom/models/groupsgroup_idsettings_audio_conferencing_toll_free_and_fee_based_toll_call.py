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

class GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall(object):
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
        'allow_webinar_attendees_dial': 'bool',
        'enable': 'bool',
        'numbers': 'list[GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCallNumbers]'
    }

    attribute_map = {
        'allow_webinar_attendees_dial': 'allow_webinar_attendees_dial',
        'enable': 'enable',
        'numbers': 'numbers'
    }

    def __init__(self, allow_webinar_attendees_dial=None, enable=None, numbers=None):  # noqa: E501
        """GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall - a model defined in Swagger"""  # noqa: E501
        self._allow_webinar_attendees_dial = None
        self._enable = None
        self._numbers = None
        self.discriminator = None
        if allow_webinar_attendees_dial is not None:
            self.allow_webinar_attendees_dial = allow_webinar_attendees_dial
        if enable is not None:
            self.enable = enable
        if numbers is not None:
            self.numbers = numbers

    @property
    def allow_webinar_attendees_dial(self):
        """Gets the allow_webinar_attendees_dial of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501

        Whether webinar attendees can dial in through the account's **Toll-free and Fee-based Toll Call** phone numbers. This feature is only available in version 5.2.2 and higher.  # noqa: E501

        :return: The allow_webinar_attendees_dial of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :rtype: bool
        """
        return self._allow_webinar_attendees_dial

    @allow_webinar_attendees_dial.setter
    def allow_webinar_attendees_dial(self, allow_webinar_attendees_dial):
        """Sets the allow_webinar_attendees_dial of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.

        Whether webinar attendees can dial in through the account's **Toll-free and Fee-based Toll Call** phone numbers. This feature is only available in version 5.2.2 and higher.  # noqa: E501

        :param allow_webinar_attendees_dial: The allow_webinar_attendees_dial of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :type: bool
        """

        self._allow_webinar_attendees_dial = allow_webinar_attendees_dial

    @property
    def enable(self):
        """Gets the enable of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501

        Whether the group has the [**Toll-free and Fee-based Toll Call**](https://support.zoom.us/hc/en-us/articles/360060950711-Enabling-Toll-free-and-Fee-based-Toll-Call#h_01F51844DRCX3K7BRTMZ40381R) setting enabled.  # noqa: E501

        :return: The enable of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.

        Whether the group has the [**Toll-free and Fee-based Toll Call**](https://support.zoom.us/hc/en-us/articles/360060950711-Enabling-Toll-free-and-Fee-based-Toll-Call#h_01F51844DRCX3K7BRTMZ40381R) setting enabled.  # noqa: E501

        :param enable: The enable of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def numbers(self):
        """Gets the numbers of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501

        The group's **Toll-free and Fee-based Toll Call** phone number information.  # noqa: E501

        :return: The numbers of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :rtype: list[GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCallNumbers]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.

        The group's **Toll-free and Fee-based Toll Call** phone number information.  # noqa: E501

        :param numbers: The numbers of this GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall.  # noqa: E501
        :type: list[GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCallNumbers]
        """

        self._numbers = numbers

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
        if issubclass(GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall, dict):
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
        if not isinstance(other, GroupsgroupIdsettingsAudioConferencingTollFreeAndFeeBasedTollCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
