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

class RolesRoleIdBody(object):
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
        'description': 'str',
        'name': 'str',
        'privileges': 'list[str]',
        'sub_account_privileges': 'RolesroleIdSubAccountPrivileges'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'privileges': 'privileges',
        'sub_account_privileges': 'sub_account_privileges'
    }

    def __init__(self, description=None, name=None, privileges=None, sub_account_privileges=None):  # noqa: E501
        """RolesRoleIdBody - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._privileges = None
        self._sub_account_privileges = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if privileges is not None:
            self.privileges = privileges
        if sub_account_privileges is not None:
            self.sub_account_privileges = sub_account_privileges

    @property
    def description(self):
        """Gets the description of this RolesRoleIdBody.  # noqa: E501

        The role's description.  # noqa: E501

        :return: The description of this RolesRoleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RolesRoleIdBody.

        The role's description.  # noqa: E501

        :param description: The description of this RolesRoleIdBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this RolesRoleIdBody.  # noqa: E501

        The role's name.  # noqa: E501

        :return: The name of this RolesRoleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RolesRoleIdBody.

        The role's name.  # noqa: E501

        :param name: The name of this RolesRoleIdBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def privileges(self):
        """Gets the privileges of this RolesRoleIdBody.  # noqa: E501

        The role's assigned privileges. Can be one or a combination of [these privileges](https://developers.zoom.us/docs/api/rest/other-references/privileges/).   # noqa: E501

        :return: The privileges of this RolesRoleIdBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this RolesRoleIdBody.

        The role's assigned privileges. Can be one or a combination of [these privileges](https://developers.zoom.us/docs/api/rest/other-references/privileges/).   # noqa: E501

        :param privileges: The privileges of this RolesRoleIdBody.  # noqa: E501
        :type: list[str]
        """

        self._privileges = privileges

    @property
    def sub_account_privileges(self):
        """Gets the sub_account_privileges of this RolesRoleIdBody.  # noqa: E501


        :return: The sub_account_privileges of this RolesRoleIdBody.  # noqa: E501
        :rtype: RolesroleIdSubAccountPrivileges
        """
        return self._sub_account_privileges

    @sub_account_privileges.setter
    def sub_account_privileges(self, sub_account_privileges):
        """Sets the sub_account_privileges of this RolesRoleIdBody.


        :param sub_account_privileges: The sub_account_privileges of this RolesRoleIdBody.  # noqa: E501
        :type: RolesroleIdSubAccountPrivileges
        """

        self._sub_account_privileges = sub_account_privileges

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
        if issubclass(RolesRoleIdBody, dict):
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
        if not isinstance(other, RolesRoleIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
