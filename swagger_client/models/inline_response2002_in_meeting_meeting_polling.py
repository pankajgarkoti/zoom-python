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

class InlineResponse2002InMeetingMeetingPolling(object):
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
        'advanced_polls': 'bool',
        'allow_alternative_host_to_add_edit': 'bool',
        'manage_saved_polls_and_quizzes': 'bool',
        'allow_host_to_upload_image': 'bool',
        'require_answers_to_be_anonymous': 'bool',
        'enable': 'bool'
    }

    attribute_map = {
        'advanced_polls': 'advanced_polls',
        'allow_alternative_host_to_add_edit': 'allow_alternative_host_to_add_edit',
        'manage_saved_polls_and_quizzes': 'manage_saved_polls_and_quizzes',
        'allow_host_to_upload_image': 'allow_host_to_upload_image',
        'require_answers_to_be_anonymous': 'require_answers_to_be_anonymous',
        'enable': 'enable'
    }

    def __init__(self, advanced_polls=None, allow_alternative_host_to_add_edit=None, manage_saved_polls_and_quizzes=None, allow_host_to_upload_image=None, require_answers_to_be_anonymous=None, enable=None):  # noqa: E501
        """InlineResponse2002InMeetingMeetingPolling - a model defined in Swagger"""  # noqa: E501
        self._advanced_polls = None
        self._allow_alternative_host_to_add_edit = None
        self._manage_saved_polls_and_quizzes = None
        self._allow_host_to_upload_image = None
        self._require_answers_to_be_anonymous = None
        self._enable = None
        self.discriminator = None
        if advanced_polls is not None:
            self.advanced_polls = advanced_polls
        if allow_alternative_host_to_add_edit is not None:
            self.allow_alternative_host_to_add_edit = allow_alternative_host_to_add_edit
        if manage_saved_polls_and_quizzes is not None:
            self.manage_saved_polls_and_quizzes = manage_saved_polls_and_quizzes
        if allow_host_to_upload_image is not None:
            self.allow_host_to_upload_image = allow_host_to_upload_image
        if require_answers_to_be_anonymous is not None:
            self.require_answers_to_be_anonymous = require_answers_to_be_anonymous
        if enable is not None:
            self.enable = enable

    @property
    def advanced_polls(self):
        """Gets the advanced_polls of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to allow host to create advanced polls and quizzes. Advanced polls and quizzes include single choice, multiple choice, drop down, matching, short answer, long answer, rank order, and fill-in-the-blank questions. Hosts can also set the correct answers for quizzes they create.  # noqa: E501

        :return: The advanced_polls of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._advanced_polls

    @advanced_polls.setter
    def advanced_polls(self, advanced_polls):
        """Sets the advanced_polls of this InlineResponse2002InMeetingMeetingPolling.

        Whether to allow host to create advanced polls and quizzes. Advanced polls and quizzes include single choice, multiple choice, drop down, matching, short answer, long answer, rank order, and fill-in-the-blank questions. Hosts can also set the correct answers for quizzes they create.  # noqa: E501

        :param advanced_polls: The advanced_polls of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._advanced_polls = advanced_polls

    @property
    def allow_alternative_host_to_add_edit(self):
        """Gets the allow_alternative_host_to_add_edit of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to allow the alternative host to add or edit polls and quizzes.  # noqa: E501

        :return: The allow_alternative_host_to_add_edit of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._allow_alternative_host_to_add_edit

    @allow_alternative_host_to_add_edit.setter
    def allow_alternative_host_to_add_edit(self, allow_alternative_host_to_add_edit):
        """Sets the allow_alternative_host_to_add_edit of this InlineResponse2002InMeetingMeetingPolling.

        Whether to allow the alternative host to add or edit polls and quizzes.  # noqa: E501

        :param allow_alternative_host_to_add_edit: The allow_alternative_host_to_add_edit of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._allow_alternative_host_to_add_edit = allow_alternative_host_to_add_edit

    @property
    def manage_saved_polls_and_quizzes(self):
        """Gets the manage_saved_polls_and_quizzes of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to allow users to manage saved polls and quizzes from Meetings  # noqa: E501

        :return: The manage_saved_polls_and_quizzes of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._manage_saved_polls_and_quizzes

    @manage_saved_polls_and_quizzes.setter
    def manage_saved_polls_and_quizzes(self, manage_saved_polls_and_quizzes):
        """Sets the manage_saved_polls_and_quizzes of this InlineResponse2002InMeetingMeetingPolling.

        Whether to allow users to manage saved polls and quizzes from Meetings  # noqa: E501

        :param manage_saved_polls_and_quizzes: The manage_saved_polls_and_quizzes of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._manage_saved_polls_and_quizzes = manage_saved_polls_and_quizzes

    @property
    def allow_host_to_upload_image(self):
        """Gets the allow_host_to_upload_image of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to allow host to upload an image for each question.  # noqa: E501

        :return: The allow_host_to_upload_image of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._allow_host_to_upload_image

    @allow_host_to_upload_image.setter
    def allow_host_to_upload_image(self, allow_host_to_upload_image):
        """Sets the allow_host_to_upload_image of this InlineResponse2002InMeetingMeetingPolling.

        Whether to allow host to upload an image for each question.  # noqa: E501

        :param allow_host_to_upload_image: The allow_host_to_upload_image of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._allow_host_to_upload_image = allow_host_to_upload_image

    @property
    def require_answers_to_be_anonymous(self):
        """Gets the require_answers_to_be_anonymous of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to require answers to be anonymous.  # noqa: E501

        :return: The require_answers_to_be_anonymous of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._require_answers_to_be_anonymous

    @require_answers_to_be_anonymous.setter
    def require_answers_to_be_anonymous(self, require_answers_to_be_anonymous):
        """Sets the require_answers_to_be_anonymous of this InlineResponse2002InMeetingMeetingPolling.

        Whether to require answers to be anonymous.  # noqa: E501

        :param require_answers_to_be_anonymous: The require_answers_to_be_anonymous of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._require_answers_to_be_anonymous = require_answers_to_be_anonymous

    @property
    def enable(self):
        """Gets the enable of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501

        Whether to allow the host to add polls before or during a meeting.  # noqa: E501

        :return: The enable of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse2002InMeetingMeetingPolling.

        Whether to allow the host to add polls before or during a meeting.  # noqa: E501

        :param enable: The enable of this InlineResponse2002InMeetingMeetingPolling.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if issubclass(InlineResponse2002InMeetingMeetingPolling, dict):
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
        if not isinstance(other, InlineResponse2002InMeetingMeetingPolling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
