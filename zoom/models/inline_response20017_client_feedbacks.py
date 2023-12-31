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

class InlineResponse20017ClientFeedbacks(object):
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
        'feedback_id': 'str',
        'feedback_name': 'str',
        'participants_count': 'int'
    }

    attribute_map = {
        'feedback_id': 'feedback_id',
        'feedback_name': 'feedback_name',
        'participants_count': 'participants_count'
    }

    def __init__(self, feedback_id=None, feedback_name=None, participants_count=None):  # noqa: E501
        """InlineResponse20017ClientFeedbacks - a model defined in Swagger"""  # noqa: E501
        self._feedback_id = None
        self._feedback_name = None
        self._participants_count = None
        self.discriminator = None
        if feedback_id is not None:
            self.feedback_id = feedback_id
        if feedback_name is not None:
            self.feedback_name = feedback_name
        if participants_count is not None:
            self.participants_count = participants_count

    @property
    def feedback_id(self):
        """Gets the feedback_id of this InlineResponse20017ClientFeedbacks.  # noqa: E501

        Feedback Id  # noqa: E501

        :return: The feedback_id of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :rtype: str
        """
        return self._feedback_id

    @feedback_id.setter
    def feedback_id(self, feedback_id):
        """Sets the feedback_id of this InlineResponse20017ClientFeedbacks.

        Feedback Id  # noqa: E501

        :param feedback_id: The feedback_id of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :type: str
        """

        self._feedback_id = feedback_id

    @property
    def feedback_name(self):
        """Gets the feedback_name of this InlineResponse20017ClientFeedbacks.  # noqa: E501

        Feedback Name  # noqa: E501

        :return: The feedback_name of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :rtype: str
        """
        return self._feedback_name

    @feedback_name.setter
    def feedback_name(self, feedback_name):
        """Sets the feedback_name of this InlineResponse20017ClientFeedbacks.

        Feedback Name  # noqa: E501

        :param feedback_name: The feedback_name of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :type: str
        """

        self._feedback_name = feedback_name

    @property
    def participants_count(self):
        """Gets the participants_count of this InlineResponse20017ClientFeedbacks.  # noqa: E501

        The number of participants that upvoted the feedback.  # noqa: E501

        :return: The participants_count of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :rtype: int
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """Sets the participants_count of this InlineResponse20017ClientFeedbacks.

        The number of participants that upvoted the feedback.  # noqa: E501

        :param participants_count: The participants_count of this InlineResponse20017ClientFeedbacks.  # noqa: E501
        :type: int
        """

        self._participants_count = participants_count

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
        if issubclass(InlineResponse20017ClientFeedbacks, dict):
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
        if not isinstance(other, InlineResponse20017ClientFeedbacks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
