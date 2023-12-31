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

class InlineResponse200101VirtualBackgrounds(object):
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
        'id': 'str',
        'name': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_default': 'is_default'
    }

    def __init__(self, id=None, name=None, is_default=None):  # noqa: E501
        """InlineResponse200101VirtualBackgrounds - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_default = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this InlineResponse200101VirtualBackgrounds.  # noqa: E501

        The Virtual Background's file ID.  # noqa: E501

        :return: The id of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200101VirtualBackgrounds.

        The Virtual Background's file ID.  # noqa: E501

        :param id: The id of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse200101VirtualBackgrounds.  # noqa: E501

        The Virtual Background's file name.  # noqa: E501

        :return: The name of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200101VirtualBackgrounds.

        The Virtual Background's file name.  # noqa: E501

        :param name: The name of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this InlineResponse200101VirtualBackgrounds.  # noqa: E501

        Whether the file is the default Virtual Background file.  # noqa: E501

        :return: The is_default of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this InlineResponse200101VirtualBackgrounds.

        Whether the file is the default Virtual Background file.  # noqa: E501

        :param is_default: The is_default of this InlineResponse200101VirtualBackgrounds.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(InlineResponse200101VirtualBackgrounds, dict):
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
        if not isinstance(other, InlineResponse200101VirtualBackgrounds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
