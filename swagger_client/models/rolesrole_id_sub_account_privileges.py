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

class RolesroleIdSubAccountPrivileges(object):
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
        'second_level': 'int'
    }

    attribute_map = {
        'second_level': 'second_level'
    }

    def __init__(self, second_level=None):  # noqa: E501
        """RolesroleIdSubAccountPrivileges - a model defined in Swagger"""  # noqa: E501
        self._second_level = None
        self.discriminator = None
        if second_level is not None:
            self.second_level = second_level

    @property
    def second_level(self):
        """Gets the second_level of this RolesroleIdSubAccountPrivileges.  # noqa: E501

        Indicates how the account can manage sub-accounts.   `1` - Manage the sub account as an owner of the account.  `2` - Manage the sub-account with the same privileges as the current account.     `3` - Manage the sub-account with specified privileges.  # noqa: E501

        :return: The second_level of this RolesroleIdSubAccountPrivileges.  # noqa: E501
        :rtype: int
        """
        return self._second_level

    @second_level.setter
    def second_level(self, second_level):
        """Sets the second_level of this RolesroleIdSubAccountPrivileges.

        Indicates how the account can manage sub-accounts.   `1` - Manage the sub account as an owner of the account.  `2` - Manage the sub-account with the same privileges as the current account.     `3` - Manage the sub-account with specified privileges.  # noqa: E501

        :param second_level: The second_level of this RolesroleIdSubAccountPrivileges.  # noqa: E501
        :type: int
        """

        self._second_level = second_level

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
        if issubclass(RolesroleIdSubAccountPrivileges, dict):
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
        if not isinstance(other, RolesroleIdSubAccountPrivileges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
