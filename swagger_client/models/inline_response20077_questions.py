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

class InlineResponse20077Questions(object):
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
        'email': 'str',
        'name': 'str',
        'question_details': 'list[InlineResponse20077QuestionDetails]'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'question_details': 'question_details'
    }

    def __init__(self, email=None, name=None, question_details=None):  # noqa: E501
        """InlineResponse20077Questions - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._name = None
        self._question_details = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if question_details is not None:
            self.question_details = question_details

    @property
    def email(self):
        """Gets the email of this InlineResponse20077Questions.  # noqa: E501

        Participant email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :return: The email of this InlineResponse20077Questions.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20077Questions.

        Participant email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :param email: The email of this InlineResponse20077Questions.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this InlineResponse20077Questions.  # noqa: E501

        Participant display name.       If anonymous [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) option is enabled and if a participant submits the Q&amp;A without providing their name, the value of the `name` field will be &quot;Anonymous Attendee&quot;.  # noqa: E501

        :return: The name of this InlineResponse20077Questions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20077Questions.

        Participant display name.       If anonymous [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) option is enabled and if a participant submits the Q&amp;A without providing their name, the value of the `name` field will be &quot;Anonymous Attendee&quot;.  # noqa: E501

        :param name: The name of this InlineResponse20077Questions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def question_details(self):
        """Gets the question_details of this InlineResponse20077Questions.  # noqa: E501

        Array of questions from user.  # noqa: E501

        :return: The question_details of this InlineResponse20077Questions.  # noqa: E501
        :rtype: list[InlineResponse20077QuestionDetails]
        """
        return self._question_details

    @question_details.setter
    def question_details(self, question_details):
        """Sets the question_details of this InlineResponse20077Questions.

        Array of questions from user.  # noqa: E501

        :param question_details: The question_details of this InlineResponse20077Questions.  # noqa: E501
        :type: list[InlineResponse20077QuestionDetails]
        """

        self._question_details = question_details

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
        if issubclass(InlineResponse20077Questions, dict):
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
        if not isinstance(other, InlineResponse20077Questions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
