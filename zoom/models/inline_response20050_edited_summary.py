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

class InlineResponse20050EditedSummary(object):
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
        'summary_details': 'str',
        'next_steps': 'list[str]'
    }

    attribute_map = {
        'summary_details': 'summary_details',
        'next_steps': 'next_steps'
    }

    def __init__(self, summary_details=None, next_steps=None):  # noqa: E501
        """InlineResponse20050EditedSummary - a model defined in Swagger"""  # noqa: E501
        self._summary_details = None
        self._next_steps = None
        self.discriminator = None
        if summary_details is not None:
            self.summary_details = summary_details
        if next_steps is not None:
            self.next_steps = next_steps

    @property
    def summary_details(self):
        """Gets the summary_details of this InlineResponse20050EditedSummary.  # noqa: E501

        The user edited summary details.  # noqa: E501

        :return: The summary_details of this InlineResponse20050EditedSummary.  # noqa: E501
        :rtype: str
        """
        return self._summary_details

    @summary_details.setter
    def summary_details(self, summary_details):
        """Sets the summary_details of this InlineResponse20050EditedSummary.

        The user edited summary details.  # noqa: E501

        :param summary_details: The summary_details of this InlineResponse20050EditedSummary.  # noqa: E501
        :type: str
        """

        self._summary_details = summary_details

    @property
    def next_steps(self):
        """Gets the next_steps of this InlineResponse20050EditedSummary.  # noqa: E501

        The user edited next steps.  # noqa: E501

        :return: The next_steps of this InlineResponse20050EditedSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._next_steps

    @next_steps.setter
    def next_steps(self, next_steps):
        """Sets the next_steps of this InlineResponse20050EditedSummary.

        The user edited next steps.  # noqa: E501

        :param next_steps: The next_steps of this InlineResponse20050EditedSummary.  # noqa: E501
        :type: list[str]
        """

        self._next_steps = next_steps

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
        if issubclass(InlineResponse20050EditedSummary, dict):
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
        if not isinstance(other, InlineResponse20050EditedSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other