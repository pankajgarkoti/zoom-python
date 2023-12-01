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

class InlineResponse20042(object):
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
        'total_members': 'int',
        'search_by_account': 'bool',
        'search_by_domain': 'bool',
        'search_by_ma_account': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'total_members': 'total_members',
        'search_by_account': 'search_by_account',
        'search_by_domain': 'search_by_domain',
        'search_by_ma_account': 'search_by_ma_account',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, total_members=None, search_by_account=None, search_by_domain=None, search_by_ma_account=None, type='normal'):  # noqa: E501
        """InlineResponse20042 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._total_members = None
        self._search_by_account = None
        self._search_by_domain = None
        self._search_by_ma_account = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if total_members is not None:
            self.total_members = total_members
        if search_by_account is not None:
            self.search_by_account = search_by_account
        if search_by_domain is not None:
            self.search_by_domain = search_by_domain
        if search_by_ma_account is not None:
            self.search_by_ma_account = search_by_ma_account
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this InlineResponse20042.  # noqa: E501

        Group ID.  # noqa: E501

        :return: The id of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20042.

        Group ID.  # noqa: E501

        :param id: The id of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20042.  # noqa: E501

        Group name.  # noqa: E501

        :return: The name of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20042.

        Group name.  # noqa: E501

        :param name: The name of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def total_members(self):
        """Gets the total_members of this InlineResponse20042.  # noqa: E501

        Total number of members in this group.  # noqa: E501

        :return: The total_members of this InlineResponse20042.  # noqa: E501
        :rtype: int
        """
        return self._total_members

    @total_members.setter
    def total_members(self, total_members):
        """Sets the total_members of this InlineResponse20042.

        Total number of members in this group.  # noqa: E501

        :param total_members: The total_members of this InlineResponse20042.  # noqa: E501
        :type: int
        """

        self._total_members = total_members

    @property
    def search_by_account(self):
        """Gets the search_by_account of this InlineResponse20042.  # noqa: E501

        Members can search for others under same account.  # noqa: E501

        :return: The search_by_account of this InlineResponse20042.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_account

    @search_by_account.setter
    def search_by_account(self, search_by_account):
        """Sets the search_by_account of this InlineResponse20042.

        Members can search for others under same account.  # noqa: E501

        :param search_by_account: The search_by_account of this InlineResponse20042.  # noqa: E501
        :type: bool
        """

        self._search_by_account = search_by_account

    @property
    def search_by_domain(self):
        """Gets the search_by_domain of this InlineResponse20042.  # noqa: E501

        Members can search for others in the same email domain.  # noqa: E501

        :return: The search_by_domain of this InlineResponse20042.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_domain

    @search_by_domain.setter
    def search_by_domain(self, search_by_domain):
        """Sets the search_by_domain of this InlineResponse20042.

        Members can search for others in the same email domain.  # noqa: E501

        :param search_by_domain: The search_by_domain of this InlineResponse20042.  # noqa: E501
        :type: bool
        """

        self._search_by_domain = search_by_domain

    @property
    def search_by_ma_account(self):
        """Gets the search_by_ma_account of this InlineResponse20042.  # noqa: E501

        Members can search for others under same master account - including all sub accounts.  # noqa: E501

        :return: The search_by_ma_account of this InlineResponse20042.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_ma_account

    @search_by_ma_account.setter
    def search_by_ma_account(self, search_by_ma_account):
        """Sets the search_by_ma_account of this InlineResponse20042.

        Members can search for others under same master account - including all sub accounts.  # noqa: E501

        :param search_by_ma_account: The search_by_ma_account of this InlineResponse20042.  # noqa: E501
        :type: bool
        """

        self._search_by_ma_account = search_by_ma_account

    @property
    def type(self):
        """Gets the type of this InlineResponse20042.  # noqa: E501

        IM Group types:    `normal` - Only members can see the other members in the group. Other people can search for members in the group.    `shared` - Everyone in the account can see the group and members.     `restricted` - No one except group members can see the group or search for other group members.   # noqa: E501

        :return: The type of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20042.

        IM Group types:    `normal` - Only members can see the other members in the group. Other people can search for members in the group.    `shared` - Everyone in the account can see the group and members.     `restricted` - No one except group members can see the group or search for other group members.   # noqa: E501

        :param type: The type of this InlineResponse20042.  # noqa: E501
        :type: str
        """
        allowed_values = ["normal", "shared", "restricted"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(InlineResponse20042, dict):
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
        if not isinstance(other, InlineResponse20042):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
