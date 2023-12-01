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

class InlineResponse20015Members(object):
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
        'type': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, type=None, id=None, name=None):  # noqa: E501
        """InlineResponse20015Members - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._name = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def type(self):
        """Gets the type of this InlineResponse20015Members.  # noqa: E501

        Contact group member types:    `1` - user.    `2` - user group.  # noqa: E501

        :return: The type of this InlineResponse20015Members.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20015Members.

        Contact group member types:    `1` - user.    `2` - user group.  # noqa: E501

        :param type: The type of this InlineResponse20015Members.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this InlineResponse20015Members.  # noqa: E501

        The member ID: user ID (`user`) or user group ID (`user group`).  # noqa: E501

        :return: The id of this InlineResponse20015Members.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20015Members.

        The member ID: user ID (`user`) or user group ID (`user group`).  # noqa: E501

        :param id: The id of this InlineResponse20015Members.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20015Members.  # noqa: E501

        The member's name: user's name (`user`) or the group's name (`user group`).  # noqa: E501

        :return: The name of this InlineResponse20015Members.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20015Members.

        The member's name: user's name (`user`) or the group's name (`user group`).  # noqa: E501

        :param name: The name of this InlineResponse20015Members.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(InlineResponse20015Members, dict):
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
        if not isinstance(other, InlineResponse20015Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other