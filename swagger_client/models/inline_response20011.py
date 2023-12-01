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

class InlineResponse20011(object):
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
        '_from': 'date',
        'to': 'date',
        'analytics_summary': 'list[InlineResponse20011AnalyticsSummary]'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'analytics_summary': 'analytics_summary'
    }

    def __init__(self, _from=None, to=None, analytics_summary=None):  # noqa: E501
        """InlineResponse20011 - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self._analytics_summary = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if analytics_summary is not None:
            self.analytics_summary = analytics_summary

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20011.  # noqa: E501

        The queried start date  # noqa: E501

        :return: The _from of this InlineResponse20011.  # noqa: E501
        :rtype: date
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20011.

        The queried start date  # noqa: E501

        :param _from: The _from of this InlineResponse20011.  # noqa: E501
        :type: date
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this InlineResponse20011.  # noqa: E501

        The queried end date.  # noqa: E501

        :return: The to of this InlineResponse20011.  # noqa: E501
        :rtype: date
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this InlineResponse20011.

        The queried end date.  # noqa: E501

        :param to: The to of this InlineResponse20011.  # noqa: E501
        :type: date
        """

        self._to = to

    @property
    def analytics_summary(self):
        """Gets the analytics_summary of this InlineResponse20011.  # noqa: E501

        Analytics Summary.  # noqa: E501

        :return: The analytics_summary of this InlineResponse20011.  # noqa: E501
        :rtype: list[InlineResponse20011AnalyticsSummary]
        """
        return self._analytics_summary

    @analytics_summary.setter
    def analytics_summary(self, analytics_summary):
        """Sets the analytics_summary of this InlineResponse20011.

        Analytics Summary.  # noqa: E501

        :param analytics_summary: The analytics_summary of this InlineResponse20011.  # noqa: E501
        :type: list[InlineResponse20011AnalyticsSummary]
        """

        self._analytics_summary = analytics_summary

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
        if issubclass(InlineResponse20011, dict):
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
        if not isinstance(other, InlineResponse20011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
