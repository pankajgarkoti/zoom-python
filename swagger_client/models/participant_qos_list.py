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

class ParticipantQOSList(object):
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
        'next_page_token': 'str',
        'page_count': 'int',
        'page_size': 'int',
        'total_records': 'int',
        'participants': 'list[ParticipantQOS2]'
    }

    attribute_map = {
        'next_page_token': 'next_page_token',
        'page_count': 'page_count',
        'page_size': 'page_size',
        'total_records': 'total_records',
        'participants': 'participants'
    }

    def __init__(self, next_page_token=None, page_count=None, page_size=1, total_records=None, participants=None):  # noqa: E501
        """ParticipantQOSList - a model defined in Swagger"""  # noqa: E501
        self._next_page_token = None
        self._page_count = None
        self._page_size = None
        self._total_records = None
        self._participants = None
        self.discriminator = None
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if page_count is not None:
            self.page_count = page_count
        if page_size is not None:
            self.page_size = page_size
        if total_records is not None:
            self.total_records = total_records
        if participants is not None:
            self.participants = participants

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ParticipantQOSList.  # noqa: E501

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :return: The next_page_token of this ParticipantQOSList.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ParticipantQOSList.

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :param next_page_token: The next_page_token of this ParticipantQOSList.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def page_count(self):
        """Gets the page_count of this ParticipantQOSList.  # noqa: E501

        The number of pages returned for the request made.  # noqa: E501

        :return: The page_count of this ParticipantQOSList.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this ParticipantQOSList.

        The number of pages returned for the request made.  # noqa: E501

        :param page_count: The page_count of this ParticipantQOSList.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def page_size(self):
        """Gets the page_size of this ParticipantQOSList.  # noqa: E501

        The number of items per page.  # noqa: E501

        :return: The page_size of this ParticipantQOSList.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ParticipantQOSList.

        The number of items per page.  # noqa: E501

        :param page_size: The page_size of this ParticipantQOSList.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_records(self):
        """Gets the total_records of this ParticipantQOSList.  # noqa: E501

        The number of all records available across pages.  # noqa: E501

        :return: The total_records of this ParticipantQOSList.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this ParticipantQOSList.

        The number of all records available across pages.  # noqa: E501

        :param total_records: The total_records of this ParticipantQOSList.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def participants(self):
        """Gets the participants of this ParticipantQOSList.  # noqa: E501

        Information about the participant.  # noqa: E501

        :return: The participants of this ParticipantQOSList.  # noqa: E501
        :rtype: list[ParticipantQOS2]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this ParticipantQOSList.

        Information about the participant.  # noqa: E501

        :param participants: The participants of this ParticipantQOSList.  # noqa: E501
        :type: list[ParticipantQOS2]
        """

        self._participants = participants

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
        if issubclass(ParticipantQOSList, dict):
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
        if not isinstance(other, ParticipantQOSList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
