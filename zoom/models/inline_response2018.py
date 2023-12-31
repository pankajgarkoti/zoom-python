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

class InlineResponse2018(object):
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
        'search_by_account': 'bool',
        'search_by_domain': 'bool',
        'search_by_ma_account': 'bool',
        'total_members': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'search_by_account': 'search_by_account',
        'search_by_domain': 'search_by_domain',
        'search_by_ma_account': 'search_by_ma_account',
        'total_members': 'total_members'
    }

    def __init__(self, id=None, name=None, search_by_account=None, search_by_domain=None, search_by_ma_account=None, total_members=None):  # noqa: E501
        """InlineResponse2018 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._search_by_account = None
        self._search_by_domain = None
        self._search_by_ma_account = None
        self._total_members = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if search_by_account is not None:
            self.search_by_account = search_by_account
        if search_by_domain is not None:
            self.search_by_domain = search_by_domain
        if search_by_ma_account is not None:
            self.search_by_ma_account = search_by_ma_account
        if total_members is not None:
            self.total_members = total_members

    @property
    def id(self):
        """Gets the id of this InlineResponse2018.  # noqa: E501

        Group ID.  # noqa: E501

        :return: The id of this InlineResponse2018.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2018.

        Group ID.  # noqa: E501

        :param id: The id of this InlineResponse2018.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2018.  # noqa: E501

        Group name.  # noqa: E501

        :return: The name of this InlineResponse2018.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2018.

        Group name.  # noqa: E501

        :param name: The name of this InlineResponse2018.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def search_by_account(self):
        """Gets the search_by_account of this InlineResponse2018.  # noqa: E501

        Members can search for others under same account.  # noqa: E501

        :return: The search_by_account of this InlineResponse2018.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_account

    @search_by_account.setter
    def search_by_account(self, search_by_account):
        """Sets the search_by_account of this InlineResponse2018.

        Members can search for others under same account.  # noqa: E501

        :param search_by_account: The search_by_account of this InlineResponse2018.  # noqa: E501
        :type: bool
        """

        self._search_by_account = search_by_account

    @property
    def search_by_domain(self):
        """Gets the search_by_domain of this InlineResponse2018.  # noqa: E501

        Members can search for others in the same email domain.  # noqa: E501

        :return: The search_by_domain of this InlineResponse2018.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_domain

    @search_by_domain.setter
    def search_by_domain(self, search_by_domain):
        """Sets the search_by_domain of this InlineResponse2018.

        Members can search for others in the same email domain.  # noqa: E501

        :param search_by_domain: The search_by_domain of this InlineResponse2018.  # noqa: E501
        :type: bool
        """

        self._search_by_domain = search_by_domain

    @property
    def search_by_ma_account(self):
        """Gets the search_by_ma_account of this InlineResponse2018.  # noqa: E501

        Members can search for others under same master account, including all sub accounts.  # noqa: E501

        :return: The search_by_ma_account of this InlineResponse2018.  # noqa: E501
        :rtype: bool
        """
        return self._search_by_ma_account

    @search_by_ma_account.setter
    def search_by_ma_account(self, search_by_ma_account):
        """Sets the search_by_ma_account of this InlineResponse2018.

        Members can search for others under same master account, including all sub accounts.  # noqa: E501

        :param search_by_ma_account: The search_by_ma_account of this InlineResponse2018.  # noqa: E501
        :type: bool
        """

        self._search_by_ma_account = search_by_ma_account

    @property
    def total_members(self):
        """Gets the total_members of this InlineResponse2018.  # noqa: E501

        Group member count.  # noqa: E501

        :return: The total_members of this InlineResponse2018.  # noqa: E501
        :rtype: int
        """
        return self._total_members

    @total_members.setter
    def total_members(self, total_members):
        """Sets the total_members of this InlineResponse2018.

        Group member count.  # noqa: E501

        :param total_members: The total_members of this InlineResponse2018.  # noqa: E501
        :type: int
        """

        self._total_members = total_members

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
        if issubclass(InlineResponse2018, dict):
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
        if not isinstance(other, InlineResponse2018):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
