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

class InlineResponse20017(object):
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
        'client_feedbacks': 'list[InlineResponse20017ClientFeedbacks]',
        '_from': 'date',
        'to': 'date',
        'total_records': 'int'
    }

    attribute_map = {
        'client_feedbacks': 'client_feedbacks',
        '_from': 'from',
        'to': 'to',
        'total_records': 'total_records'
    }

    def __init__(self, client_feedbacks=None, _from=None, to=None, total_records=None):  # noqa: E501
        """InlineResponse20017 - a model defined in Swagger"""  # noqa: E501
        self._client_feedbacks = None
        self.__from = None
        self._to = None
        self._total_records = None
        self.discriminator = None
        if client_feedbacks is not None:
            self.client_feedbacks = client_feedbacks
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if total_records is not None:
            self.total_records = total_records

    @property
    def client_feedbacks(self):
        """Gets the client_feedbacks of this InlineResponse20017.  # noqa: E501


        :return: The client_feedbacks of this InlineResponse20017.  # noqa: E501
        :rtype: list[InlineResponse20017ClientFeedbacks]
        """
        return self._client_feedbacks

    @client_feedbacks.setter
    def client_feedbacks(self, client_feedbacks):
        """Sets the client_feedbacks of this InlineResponse20017.


        :param client_feedbacks: The client_feedbacks of this InlineResponse20017.  # noqa: E501
        :type: list[InlineResponse20017ClientFeedbacks]
        """

        self._client_feedbacks = client_feedbacks

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20017.  # noqa: E501

        Start date for this report  # noqa: E501

        :return: The _from of this InlineResponse20017.  # noqa: E501
        :rtype: date
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20017.

        Start date for this report  # noqa: E501

        :param _from: The _from of this InlineResponse20017.  # noqa: E501
        :type: date
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this InlineResponse20017.  # noqa: E501

        End date for this report  # noqa: E501

        :return: The to of this InlineResponse20017.  # noqa: E501
        :rtype: date
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this InlineResponse20017.

        End date for this report  # noqa: E501

        :param to: The to of this InlineResponse20017.  # noqa: E501
        :type: date
        """

        self._to = to

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponse20017.  # noqa: E501

        The number of all records available across pages  # noqa: E501

        :return: The total_records of this InlineResponse20017.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponse20017.

        The number of all records available across pages  # noqa: E501

        :param total_records: The total_records of this InlineResponse20017.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

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
        if issubclass(InlineResponse20017, dict):
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
        if not isinstance(other, InlineResponse20017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
