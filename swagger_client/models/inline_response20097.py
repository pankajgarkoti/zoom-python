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

class InlineResponse20097(object):
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
        'id': 'int',
        'questions': 'list[InlineResponse20097Questions]',
        'start_time': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'questions': 'questions',
        'start_time': 'start_time',
        'uuid': 'uuid'
    }

    def __init__(self, id=None, questions=None, start_time=None, uuid=None):  # noqa: E501
        """InlineResponse20097 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._questions = None
        self._start_time = None
        self._uuid = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if questions is not None:
            self.questions = questions
        if start_time is not None:
            self.start_time = start_time
        if uuid is not None:
            self.uuid = uuid

    @property
    def id(self):
        """Gets the id of this InlineResponse20097.  # noqa: E501

        Webinar ID in **long** format, represented as int64 data type in JSON, also known as the webinar number.  # noqa: E501

        :return: The id of this InlineResponse20097.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20097.

        Webinar ID in **long** format, represented as int64 data type in JSON, also known as the webinar number.  # noqa: E501

        :param id: The id of this InlineResponse20097.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def questions(self):
        """Gets the questions of this InlineResponse20097.  # noqa: E501


        :return: The questions of this InlineResponse20097.  # noqa: E501
        :rtype: list[InlineResponse20097Questions]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this InlineResponse20097.


        :param questions: The questions of this InlineResponse20097.  # noqa: E501
        :type: list[InlineResponse20097Questions]
        """

        self._questions = questions

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20097.  # noqa: E501

        The webinar's start time.  # noqa: E501

        :return: The start_time of this InlineResponse20097.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20097.

        The webinar's start time.  # noqa: E501

        :param start_time: The start_time of this InlineResponse20097.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20097.  # noqa: E501

        Webinar UUID.  # noqa: E501

        :return: The uuid of this InlineResponse20097.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20097.

        Webinar UUID.  # noqa: E501

        :param uuid: The uuid of this InlineResponse20097.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(InlineResponse20097, dict):
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
        if not isinstance(other, InlineResponse20097):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other