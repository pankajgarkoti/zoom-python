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

class InlineResponse20067Questions(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'question_details': 'list[InlineResponse20076QuestionDetails]'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'question_details': 'question_details'
    }

    def __init__(self, email=None, name=None, first_name=None, last_name=None, question_details=None):  # noqa: E501
        """InlineResponse20067Questions - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._name = None
        self._first_name = None
        self._last_name = None
        self._question_details = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if question_details is not None:
            self.question_details = question_details

    @property
    def email(self):
        """Gets the email of this InlineResponse20067Questions.  # noqa: E501

        The participant's email address.  # noqa: E501

        :return: The email of this InlineResponse20067Questions.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20067Questions.

        The participant's email address.  # noqa: E501

        :param email: The email of this InlineResponse20067Questions.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this InlineResponse20067Questions.  # noqa: E501

        The participant's display name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :return: The name of this InlineResponse20067Questions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20067Questions.

        The participant's display name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :param name: The name of this InlineResponse20067Questions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this InlineResponse20067Questions.  # noqa: E501

        The participant's first name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `first_name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :return: The first_name of this InlineResponse20067Questions.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineResponse20067Questions.

        The participant's first name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `first_name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :param first_name: The first_name of this InlineResponse20067Questions.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this InlineResponse20067Questions.  # noqa: E501

        The participant's last name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `last_name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :return: The last_name of this InlineResponse20067Questions.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InlineResponse20067Questions.

        The participant's last name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `last_name` field will return the &quot;Anonymous Attendee&quot; value.  # noqa: E501

        :param last_name: The last_name of this InlineResponse20067Questions.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def question_details(self):
        """Gets the question_details of this InlineResponse20067Questions.  # noqa: E501

        Information about the user's questions and answers.  # noqa: E501

        :return: The question_details of this InlineResponse20067Questions.  # noqa: E501
        :rtype: list[InlineResponse20076QuestionDetails]
        """
        return self._question_details

    @question_details.setter
    def question_details(self, question_details):
        """Sets the question_details of this InlineResponse20067Questions.

        Information about the user's questions and answers.  # noqa: E501

        :param question_details: The question_details of this InlineResponse20067Questions.  # noqa: E501
        :type: list[InlineResponse20076QuestionDetails]
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
        if issubclass(InlineResponse20067Questions, dict):
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
        if not isinstance(other, InlineResponse20067Questions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
