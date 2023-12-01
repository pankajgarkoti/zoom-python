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

class MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions(object):
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
        'approved_list': 'list[str]',
        'denied_list': 'list[str]',
        'enable': 'bool',
        'method': 'str'
    }

    attribute_map = {
        'approved_list': 'approved_list',
        'denied_list': 'denied_list',
        'enable': 'enable',
        'method': 'method'
    }

    def __init__(self, approved_list=None, denied_list=None, enable=None, method=None):  # noqa: E501
        """MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions - a model defined in Swagger"""  # noqa: E501
        self._approved_list = None
        self._denied_list = None
        self._enable = None
        self._method = None
        self.discriminator = None
        if approved_list is not None:
            self.approved_list = approved_list
        if denied_list is not None:
            self.denied_list = denied_list
        if enable is not None:
            self.enable = enable
        if method is not None:
            self.method = method

    @property
    def approved_list(self):
        """Gets the approved_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501

        List of countries or regions from where participants can join this meeting.   # noqa: E501

        :return: The approved_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :rtype: list[str]
        """
        return self._approved_list

    @approved_list.setter
    def approved_list(self, approved_list):
        """Sets the approved_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.

        List of countries or regions from where participants can join this meeting.   # noqa: E501

        :param approved_list: The approved_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :type: list[str]
        """

        self._approved_list = approved_list

    @property
    def denied_list(self):
        """Gets the denied_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501

        List of countries or regions from where participants can not join this meeting.   # noqa: E501

        :return: The denied_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :rtype: list[str]
        """
        return self._denied_list

    @denied_list.setter
    def denied_list(self, denied_list):
        """Sets the denied_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.

        List of countries or regions from where participants can not join this meeting.   # noqa: E501

        :param denied_list: The denied_list of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :type: list[str]
        """

        self._denied_list = denied_list

    @property
    def enable(self):
        """Gets the enable of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501

        `true` - Setting enabled to either allow users or block users from specific regions to join your meetings.    `false` - Setting disabled.  # noqa: E501

        :return: The enable of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.

        `true` - Setting enabled to either allow users or block users from specific regions to join your meetings.    `false` - Setting disabled.  # noqa: E501

        :param enable: The enable of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def method(self):
        """Gets the method of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501

        Specify whether to allow users from specific regions to join this meeting, or block users from specific regions from joining this meeting.    `approve` - Allow users from specific regions or countries to join this meeting. If this setting is selected, include the approved regions or countries in the `approved_list`.     `deny` - Block users from specific regions or countries from joining this meeting. If this setting is selected, include the approved regions orcountries in the `denied_list`  # noqa: E501

        :return: The method of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.

        Specify whether to allow users from specific regions to join this meeting, or block users from specific regions from joining this meeting.    `approve` - Allow users from specific regions or countries to join this meeting. If this setting is selected, include the approved regions or countries in the `approved_list`.     `deny` - Block users from specific regions or countries from joining this meeting. If this setting is selected, include the approved regions orcountries in the `denied_list`  # noqa: E501

        :param method: The method of this MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions.  # noqa: E501
        :type: str
        """
        allowed_values = ["approve", "deny"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

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
        if issubclass(MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions, dict):
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
        if not isinstance(other, MeetingsmeetingIdSettingsApprovedOrDeniedCountriesOrRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
