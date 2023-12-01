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

class InlineResponse2002TelephonyTelephonyRegions(object):
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
        'allowed_values': 'list[str]',
        'selection_values': 'str'
    }

    attribute_map = {
        'allowed_values': 'allowed_values',
        'selection_values': 'selection_values'
    }

    def __init__(self, allowed_values=None, selection_values=None):  # noqa: E501
        """InlineResponse2002TelephonyTelephonyRegions - a model defined in Swagger"""  # noqa: E501
        self._allowed_values = None
        self._selection_values = None
        self.discriminator = None
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if selection_values is not None:
            self.selection_values = selection_values

    @property
    def allowed_values(self):
        """Gets the allowed_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501

        Telephony region options provided by Zoom to select from.  # noqa: E501

        :return: The allowed_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this InlineResponse2002TelephonyTelephonyRegions.

        Telephony region options provided by Zoom to select from.  # noqa: E501

        :param allowed_values: The allowed_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501
        :type: list[str]
        """

        self._allowed_values = allowed_values

    @property
    def selection_values(self):
        """Gets the selection_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501

        The account's selected telephony regions that indicate where most participants call into or call from during a meeting.  # noqa: E501

        :return: The selection_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501
        :rtype: str
        """
        return self._selection_values

    @selection_values.setter
    def selection_values(self, selection_values):
        """Sets the selection_values of this InlineResponse2002TelephonyTelephonyRegions.

        The account's selected telephony regions that indicate where most participants call into or call from during a meeting.  # noqa: E501

        :param selection_values: The selection_values of this InlineResponse2002TelephonyTelephonyRegions.  # noqa: E501
        :type: str
        """

        self._selection_values = selection_values

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
        if issubclass(InlineResponse2002TelephonyTelephonyRegions, dict):
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
        if not isinstance(other, InlineResponse2002TelephonyTelephonyRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other