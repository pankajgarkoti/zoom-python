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

class InlineResponse20110Prompts(object):
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
        'prompt_question': 'str',
        'prompt_right_answers': 'list[str]'
    }

    attribute_map = {
        'prompt_question': 'prompt_question',
        'prompt_right_answers': 'prompt_right_answers'
    }

    def __init__(self, prompt_question=None, prompt_right_answers=None):  # noqa: E501
        """InlineResponse20110Prompts - a model defined in Swagger"""  # noqa: E501
        self._prompt_question = None
        self._prompt_right_answers = None
        self.discriminator = None
        if prompt_question is not None:
            self.prompt_question = prompt_question
        if prompt_right_answers is not None:
            self.prompt_right_answers = prompt_right_answers

    @property
    def prompt_question(self):
        """Gets the prompt_question of this InlineResponse20110Prompts.  # noqa: E501

        The question prompt's title.  # noqa: E501

        :return: The prompt_question of this InlineResponse20110Prompts.  # noqa: E501
        :rtype: str
        """
        return self._prompt_question

    @prompt_question.setter
    def prompt_question(self, prompt_question):
        """Sets the prompt_question of this InlineResponse20110Prompts.

        The question prompt's title.  # noqa: E501

        :param prompt_question: The prompt_question of this InlineResponse20110Prompts.  # noqa: E501
        :type: str
        """

        self._prompt_question = prompt_question

    @property
    def prompt_right_answers(self):
        """Gets the prompt_right_answers of this InlineResponse20110Prompts.  # noqa: E501

        The question prompt's correct answers.  # noqa: E501

        :return: The prompt_right_answers of this InlineResponse20110Prompts.  # noqa: E501
        :rtype: list[str]
        """
        return self._prompt_right_answers

    @prompt_right_answers.setter
    def prompt_right_answers(self, prompt_right_answers):
        """Sets the prompt_right_answers of this InlineResponse20110Prompts.

        The question prompt's correct answers.  # noqa: E501

        :param prompt_right_answers: The prompt_right_answers of this InlineResponse20110Prompts.  # noqa: E501
        :type: list[str]
        """

        self._prompt_right_answers = prompt_right_answers

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
        if issubclass(InlineResponse20110Prompts, dict):
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
        if not isinstance(other, InlineResponse20110Prompts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
