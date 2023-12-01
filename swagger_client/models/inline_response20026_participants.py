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

class InlineResponse20026Participants(object):
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
        'date_time': 'datetime',
        'email': 'str',
        'quality': 'str',
        'user_id': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'date_time': 'date_time',
        'email': 'email',
        'quality': 'quality',
        'user_id': 'user_id',
        'comment': 'comment'
    }

    def __init__(self, date_time=None, email=None, quality=None, user_id=None, comment=None):  # noqa: E501
        """InlineResponse20026Participants - a model defined in Swagger"""  # noqa: E501
        self._date_time = None
        self._email = None
        self._quality = None
        self._user_id = None
        self._comment = None
        self.discriminator = None
        if date_time is not None:
            self.date_time = date_time
        if email is not None:
            self.email = email
        if quality is not None:
            self.quality = quality
        if user_id is not None:
            self.user_id = user_id
        if comment is not None:
            self.comment = comment

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse20026Participants.  # noqa: E501

        Date and time at which the feedback was submitted.  # noqa: E501

        :return: The date_time of this InlineResponse20026Participants.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse20026Participants.

        Date and time at which the feedback was submitted.  # noqa: E501

        :param date_time: The date_time of this InlineResponse20026Participants.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def email(self):
        """Gets the email of this InlineResponse20026Participants.  # noqa: E501

        Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :return: The email of this InlineResponse20026Participants.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20026Participants.

        Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :param email: The email of this InlineResponse20026Participants.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def quality(self):
        """Gets the quality of this InlineResponse20026Participants.  # noqa: E501

        Feedback submitted by the participant.   * `GOOD`: Thumbs up. * `NOT GOOD`: Thumbs down.  # noqa: E501

        :return: The quality of this InlineResponse20026Participants.  # noqa: E501
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this InlineResponse20026Participants.

        Feedback submitted by the participant.   * `GOOD`: Thumbs up. * `NOT GOOD`: Thumbs down.  # noqa: E501

        :param quality: The quality of this InlineResponse20026Participants.  # noqa: E501
        :type: str
        """
        allowed_values = ["GOOD", "NOT GOOD"]  # noqa: E501
        if quality not in allowed_values:
            raise ValueError(
                "Invalid value for `quality` ({0}), must be one of {1}"  # noqa: E501
                .format(quality, allowed_values)
            )

        self._quality = quality

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponse20026Participants.  # noqa: E501

        User ID of the participant.  # noqa: E501

        :return: The user_id of this InlineResponse20026Participants.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponse20026Participants.

        User ID of the participant.  # noqa: E501

        :param user_id: The user_id of this InlineResponse20026Participants.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def comment(self):
        """Gets the comment of this InlineResponse20026Participants.  # noqa: E501

        Post meeting comment of the participant.  # noqa: E501

        :return: The comment of this InlineResponse20026Participants.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this InlineResponse20026Participants.

        Post meeting comment of the participant.  # noqa: E501

        :param comment: The comment of this InlineResponse20026Participants.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(InlineResponse20026Participants, dict):
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
        if not isinstance(other, InlineResponse20026Participants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
