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

class InlineResponse20036(object):
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
        'groups': 'list[InlineResponse20036Groups]',
        'total_records': 'int'
    }

    attribute_map = {
        'groups': 'groups',
        'total_records': 'total_records'
    }

    def __init__(self, groups=None, total_records=None):  # noqa: E501
        """InlineResponse20036 - a model defined in Swagger"""  # noqa: E501
        self._groups = None
        self._total_records = None
        self.discriminator = None
        if groups is not None:
            self.groups = groups
        if total_records is not None:
            self.total_records = total_records

    @property
    def groups(self):
        """Gets the groups of this InlineResponse20036.  # noqa: E501

        List of Group objects.  # noqa: E501

        :return: The groups of this InlineResponse20036.  # noqa: E501
        :rtype: list[InlineResponse20036Groups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this InlineResponse20036.

        List of Group objects.  # noqa: E501

        :param groups: The groups of this InlineResponse20036.  # noqa: E501
        :type: list[InlineResponse20036Groups]
        """

        self._groups = groups

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponse20036.  # noqa: E501

        Total records.  # noqa: E501

        :return: The total_records of this InlineResponse20036.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponse20036.

        Total records.  # noqa: E501

        :param total_records: The total_records of this InlineResponse20036.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

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
        if issubclass(InlineResponse20036, dict):
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
        if not isinstance(other, InlineResponse20036):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
