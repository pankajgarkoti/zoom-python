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

class GroupIdAdminsBody(object):
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
        'admins': 'list[GroupsgroupIdadminsAdmins]'
    }

    attribute_map = {
        'admins': 'admins'
    }

    def __init__(self, admins=None):  # noqa: E501
        """GroupIdAdminsBody - a model defined in Swagger"""  # noqa: E501
        self._admins = None
        self.discriminator = None
        if admins is not None:
            self.admins = admins

    @property
    def admins(self):
        """Gets the admins of this GroupIdAdminsBody.  # noqa: E501

        A list of the administrators to add to a group.  # noqa: E501

        :return: The admins of this GroupIdAdminsBody.  # noqa: E501
        :rtype: list[GroupsgroupIdadminsAdmins]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this GroupIdAdminsBody.

        A list of the administrators to add to a group.  # noqa: E501

        :param admins: The admins of this GroupIdAdminsBody.  # noqa: E501
        :type: list[GroupsgroupIdadminsAdmins]
        """

        self._admins = admins

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
        if issubclass(GroupIdAdminsBody, dict):
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
        if not isinstance(other, GroupIdAdminsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other