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

class InlineResponse20016(object):
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
        'next_page_token': 'str',
        'page_size': 'int',
        'to': 'date',
        'users': 'list[InlineResponse20016Users]'
    }

    attribute_map = {
        '_from': 'from',
        'next_page_token': 'next_page_token',
        'page_size': 'page_size',
        'to': 'to',
        'users': 'users'
    }

    def __init__(self, _from=None, next_page_token=None, page_size=30, to=None, users=None):  # noqa: E501
        """InlineResponse20016 - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._next_page_token = None
        self._page_size = None
        self._to = None
        self._users = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if page_size is not None:
            self.page_size = page_size
        if to is not None:
            self.to = to
        if users is not None:
            self.users = users

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20016.  # noqa: E501

        The report's start date.  # noqa: E501

        :return: The _from of this InlineResponse20016.  # noqa: E501
        :rtype: date
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20016.

        The report's start date.  # noqa: E501

        :param _from: The _from of this InlineResponse20016.  # noqa: E501
        :type: date
        """

        self.__from = _from

    @property
    def next_page_token(self):
        """Gets the next_page_token of this InlineResponse20016.  # noqa: E501

        The report's [`next_page_token` value](https://marketplace.zoom.us/docs/api-reference/pagination#next-page-token). The API returns this value when the set of available results exceeds the current page size. This token expires after 15 minutes.  # noqa: E501

        :return: The next_page_token of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this InlineResponse20016.

        The report's [`next_page_token` value](https://marketplace.zoom.us/docs/api-reference/pagination#next-page-token). The API returns this value when the set of available results exceeds the current page size. This token expires after 15 minutes.  # noqa: E501

        :param next_page_token: The next_page_token of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def page_size(self):
        """Gets the page_size of this InlineResponse20016.  # noqa: E501

        The number of records to return within a single API call.  # noqa: E501

        :return: The page_size of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineResponse20016.

        The number of records to return within a single API call.  # noqa: E501

        :param page_size: The page_size of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def to(self):
        """Gets the to of this InlineResponse20016.  # noqa: E501

        The report's end date.  # noqa: E501

        :return: The to of this InlineResponse20016.  # noqa: E501
        :rtype: date
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this InlineResponse20016.

        The report's end date.  # noqa: E501

        :param to: The to of this InlineResponse20016.  # noqa: E501
        :type: date
        """

        self._to = to

    @property
    def users(self):
        """Gets the users of this InlineResponse20016.  # noqa: E501


        :return: The users of this InlineResponse20016.  # noqa: E501
        :rtype: list[InlineResponse20016Users]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this InlineResponse20016.


        :param users: The users of this InlineResponse20016.  # noqa: E501
        :type: list[InlineResponse20016Users]
        """

        self._users = users

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
        if issubclass(InlineResponse20016, dict):
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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
