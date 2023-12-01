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

class InlineResponse20044(object):
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
        'page_size': 'int',
        'next_page_token': 'str',
        '_from': 'datetime',
        'to': 'datetime',
        'summaries': 'list[InlineResponse20044Summaries]'
    }

    attribute_map = {
        'page_size': 'page_size',
        'next_page_token': 'next_page_token',
        '_from': 'from',
        'to': 'to',
        'summaries': 'summaries'
    }

    def __init__(self, page_size=30, next_page_token=None, _from=None, to=None, summaries=None):  # noqa: E501
        """InlineResponse20044 - a model defined in Swagger"""  # noqa: E501
        self._page_size = None
        self._next_page_token = None
        self.__from = None
        self._to = None
        self._summaries = None
        self.discriminator = None
        if page_size is not None:
            self.page_size = page_size
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if summaries is not None:
            self.summaries = summaries

    @property
    def page_size(self):
        """Gets the page_size of this InlineResponse20044.  # noqa: E501

        The number of records returned with a single API call.  # noqa: E501

        :return: The page_size of this InlineResponse20044.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineResponse20044.

        The number of records returned with a single API call.  # noqa: E501

        :param page_size: The page_size of this InlineResponse20044.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def next_page_token(self):
        """Gets the next_page_token of this InlineResponse20044.  # noqa: E501

        The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :return: The next_page_token of this InlineResponse20044.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this InlineResponse20044.

        The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :param next_page_token: The next_page_token of this InlineResponse20044.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20044.  # noqa: E501

        The start date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.  # noqa: E501

        :return: The _from of this InlineResponse20044.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20044.

        The start date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.  # noqa: E501

        :param _from: The _from of this InlineResponse20044.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this InlineResponse20044.  # noqa: E501

        The end date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.  # noqa: E501

        :return: The to of this InlineResponse20044.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this InlineResponse20044.

        The end date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.  # noqa: E501

        :param to: The to of this InlineResponse20044.  # noqa: E501
        :type: datetime
        """

        self._to = to

    @property
    def summaries(self):
        """Gets the summaries of this InlineResponse20044.  # noqa: E501

        List of meeting summary objects.  # noqa: E501

        :return: The summaries of this InlineResponse20044.  # noqa: E501
        :rtype: list[InlineResponse20044Summaries]
        """
        return self._summaries

    @summaries.setter
    def summaries(self, summaries):
        """Sets the summaries of this InlineResponse20044.

        List of meeting summary objects.  # noqa: E501

        :param summaries: The summaries of this InlineResponse20044.  # noqa: E501
        :type: list[InlineResponse20044Summaries]
        """

        self._summaries = summaries

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
        if issubclass(InlineResponse20044, dict):
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
        if not isinstance(other, InlineResponse20044):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other