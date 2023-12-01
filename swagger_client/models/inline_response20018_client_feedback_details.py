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

class InlineResponse20018ClientFeedbackDetails(object):
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
        'meeting_id': 'str',
        'participant_name': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'email': 'email',
        'meeting_id': 'meeting_id',
        'participant_name': 'participant_name',
        'time': 'time'
    }

    def __init__(self, email=None, meeting_id=None, participant_name=None, time=None):  # noqa: E501
        """InlineResponse20018ClientFeedbackDetails - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._meeting_id = None
        self._participant_name = None
        self._time = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if meeting_id is not None:
            self.meeting_id = meeting_id
        if participant_name is not None:
            self.participant_name = participant_name
        if time is not None:
            self.time = time

    @property
    def email(self):
        """Gets the email of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501

        Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :return: The email of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20018ClientFeedbackDetails.

        Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for details.  # noqa: E501

        :param email: The email of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def meeting_id(self):
        """Gets the meeting_id of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501

        Meeting ID  # noqa: E501

        :return: The meeting_id of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :rtype: str
        """
        return self._meeting_id

    @meeting_id.setter
    def meeting_id(self, meeting_id):
        """Sets the meeting_id of this InlineResponse20018ClientFeedbackDetails.

        Meeting ID  # noqa: E501

        :param meeting_id: The meeting_id of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :type: str
        """

        self._meeting_id = meeting_id

    @property
    def participant_name(self):
        """Gets the participant_name of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501

        Participant Name  # noqa: E501

        :return: The participant_name of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name):
        """Sets the participant_name of this InlineResponse20018ClientFeedbackDetails.

        Participant Name  # noqa: E501

        :param participant_name: The participant_name of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :type: str
        """

        self._participant_name = participant_name

    @property
    def time(self):
        """Gets the time of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501

        Time at which the feedback was submitted by the participant.  # noqa: E501

        :return: The time of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20018ClientFeedbackDetails.

        Time at which the feedback was submitted by the participant.  # noqa: E501

        :param time: The time of this InlineResponse20018ClientFeedbackDetails.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if issubclass(InlineResponse20018ClientFeedbackDetails, dict):
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
        if not isinstance(other, InlineResponse20018ClientFeedbackDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
