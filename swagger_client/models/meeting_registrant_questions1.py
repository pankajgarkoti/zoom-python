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

class MeetingRegistrantQuestions1(object):
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
        'custom_questions': 'list[MeetingsmeetingIdregistrantsquestionsCustomQuestions]',
        'questions': 'list[MeetingsmeetingIdregistrantsquestionsQuestions]'
    }

    attribute_map = {
        'custom_questions': 'custom_questions',
        'questions': 'questions'
    }

    def __init__(self, custom_questions=None, questions=None):  # noqa: E501
        """MeetingRegistrantQuestions1 - a model defined in Swagger"""  # noqa: E501
        self._custom_questions = None
        self._questions = None
        self.discriminator = None
        if custom_questions is not None:
            self.custom_questions = custom_questions
        if questions is not None:
            self.questions = questions

    @property
    def custom_questions(self):
        """Gets the custom_questions of this MeetingRegistrantQuestions1.  # noqa: E501

        Array of Registrant Custom Questions  # noqa: E501

        :return: The custom_questions of this MeetingRegistrantQuestions1.  # noqa: E501
        :rtype: list[MeetingsmeetingIdregistrantsquestionsCustomQuestions]
        """
        return self._custom_questions

    @custom_questions.setter
    def custom_questions(self, custom_questions):
        """Sets the custom_questions of this MeetingRegistrantQuestions1.

        Array of Registrant Custom Questions  # noqa: E501

        :param custom_questions: The custom_questions of this MeetingRegistrantQuestions1.  # noqa: E501
        :type: list[MeetingsmeetingIdregistrantsquestionsCustomQuestions]
        """

        self._custom_questions = custom_questions

    @property
    def questions(self):
        """Gets the questions of this MeetingRegistrantQuestions1.  # noqa: E501

        Array of Registrant Questions  # noqa: E501

        :return: The questions of this MeetingRegistrantQuestions1.  # noqa: E501
        :rtype: list[MeetingsmeetingIdregistrantsquestionsQuestions]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this MeetingRegistrantQuestions1.

        Array of Registrant Questions  # noqa: E501

        :param questions: The questions of this MeetingRegistrantQuestions1.  # noqa: E501
        :type: list[MeetingsmeetingIdregistrantsquestionsQuestions]
        """

        self._questions = questions

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
        if issubclass(MeetingRegistrantQuestions1, dict):
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
        if not isinstance(other, MeetingRegistrantQuestions1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
