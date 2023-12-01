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

class AccountsaccountIdsettingsRecordingArchiveSettings(object):
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
        'audio_file': 'bool',
        'cc_transcript_file': 'bool',
        'chat_file': 'bool',
        'chat_with_sender_email': 'bool',
        'video_file': 'bool',
        'chat_with_direct_message': 'bool',
        'archive_retention': 'int',
        'action_when_archive_failed': 'int',
        'notification_when_archiving_starts': 'str',
        'play_voice_prompt_when_archiving_starts': 'str'
    }

    attribute_map = {
        'audio_file': 'audio_file',
        'cc_transcript_file': 'cc_transcript_file',
        'chat_file': 'chat_file',
        'chat_with_sender_email': 'chat_with_sender_email',
        'video_file': 'video_file',
        'chat_with_direct_message': 'chat_with_direct_message',
        'archive_retention': 'archive_retention',
        'action_when_archive_failed': 'action_when_archive_failed',
        'notification_when_archiving_starts': 'notification_when_archiving_starts',
        'play_voice_prompt_when_archiving_starts': 'play_voice_prompt_when_archiving_starts'
    }

    def __init__(self, audio_file=None, cc_transcript_file=None, chat_file=None, chat_with_sender_email=None, video_file=None, chat_with_direct_message=None, archive_retention=None, action_when_archive_failed=None, notification_when_archiving_starts=None, play_voice_prompt_when_archiving_starts=None):  # noqa: E501
        """AccountsaccountIdsettingsRecordingArchiveSettings - a model defined in Swagger"""  # noqa: E501
        self._audio_file = None
        self._cc_transcript_file = None
        self._chat_file = None
        self._chat_with_sender_email = None
        self._video_file = None
        self._chat_with_direct_message = None
        self._archive_retention = None
        self._action_when_archive_failed = None
        self._notification_when_archiving_starts = None
        self._play_voice_prompt_when_archiving_starts = None
        self.discriminator = None
        if audio_file is not None:
            self.audio_file = audio_file
        if cc_transcript_file is not None:
            self.cc_transcript_file = cc_transcript_file
        if chat_file is not None:
            self.chat_file = chat_file
        if chat_with_sender_email is not None:
            self.chat_with_sender_email = chat_with_sender_email
        if video_file is not None:
            self.video_file = video_file
        if chat_with_direct_message is not None:
            self.chat_with_direct_message = chat_with_direct_message
        if archive_retention is not None:
            self.archive_retention = archive_retention
        if action_when_archive_failed is not None:
            self.action_when_archive_failed = action_when_archive_failed
        if notification_when_archiving_starts is not None:
            self.notification_when_archiving_starts = notification_when_archiving_starts
        if play_voice_prompt_when_archiving_starts is not None:
            self.play_voice_prompt_when_archiving_starts = play_voice_prompt_when_archiving_starts

    @property
    def audio_file(self):
        """Gets the audio_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include in-meeting and/or in-webinar audio in the archive.  # noqa: E501

        :return: The audio_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._audio_file

    @audio_file.setter
    def audio_file(self, audio_file):
        """Sets the audio_file of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include in-meeting and/or in-webinar audio in the archive.  # noqa: E501

        :param audio_file: The audio_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._audio_file = audio_file

    @property
    def cc_transcript_file(self):
        """Gets the cc_transcript_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include closed caption or transcript in the archive.  # noqa: E501

        :return: The cc_transcript_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._cc_transcript_file

    @cc_transcript_file.setter
    def cc_transcript_file(self, cc_transcript_file):
        """Sets the cc_transcript_file of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include closed caption or transcript in the archive.  # noqa: E501

        :param cc_transcript_file: The cc_transcript_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._cc_transcript_file = cc_transcript_file

    @property
    def chat_file(self):
        """Gets the chat_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include in-meeting chat in the archive.  # noqa: E501

        :return: The chat_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._chat_file

    @chat_file.setter
    def chat_file(self, chat_file):
        """Sets the chat_file of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include in-meeting chat in the archive.  # noqa: E501

        :param chat_file: The chat_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._chat_file = chat_file

    @property
    def chat_with_sender_email(self):
        """Gets the chat_with_sender_email of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include user email in in-meeting chat file.  # noqa: E501

        :return: The chat_with_sender_email of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._chat_with_sender_email

    @chat_with_sender_email.setter
    def chat_with_sender_email(self, chat_with_sender_email):
        """Sets the chat_with_sender_email of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include user email in in-meeting chat file.  # noqa: E501

        :param chat_with_sender_email: The chat_with_sender_email of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._chat_with_sender_email = chat_with_sender_email

    @property
    def video_file(self):
        """Gets the video_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include in-meeting and/or in-webinar video in the archive.  # noqa: E501

        :return: The video_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file):
        """Sets the video_file of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include in-meeting and/or in-webinar video in the archive.  # noqa: E501

        :param video_file: The video_file of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._video_file = video_file

    @property
    def chat_with_direct_message(self):
        """Gets the chat_with_direct_message of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Include direct message in in-meeting chat file.  # noqa: E501

        :return: The chat_with_direct_message of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: bool
        """
        return self._chat_with_direct_message

    @chat_with_direct_message.setter
    def chat_with_direct_message(self, chat_with_direct_message):
        """Sets the chat_with_direct_message of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Include direct message in in-meeting chat file.  # noqa: E501

        :param chat_with_direct_message: The chat_with_direct_message of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: bool
        """

        self._chat_with_direct_message = chat_with_direct_message

    @property
    def archive_retention(self):
        """Gets the archive_retention of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        The retention period for archiving content, in days.  # noqa: E501

        :return: The archive_retention of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: int
        """
        return self._archive_retention

    @archive_retention.setter
    def archive_retention(self, archive_retention):
        """Sets the archive_retention of this AccountsaccountIdsettingsRecordingArchiveSettings.

        The retention period for archiving content, in days.  # noqa: E501

        :param archive_retention: The archive_retention of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]  # noqa: E501
        if archive_retention not in allowed_values:
            raise ValueError(
                "Invalid value for `archive_retention` ({0}), must be one of {1}"  # noqa: E501
                .format(archive_retention, allowed_values)
            )

        self._archive_retention = archive_retention

    @property
    def action_when_archive_failed(self):
        """Gets the action_when_archive_failed of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Perform the action when meetings or webinars cannot be archived.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :return: The action_when_archive_failed of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: int
        """
        return self._action_when_archive_failed

    @action_when_archive_failed.setter
    def action_when_archive_failed(self, action_when_archive_failed):
        """Sets the action_when_archive_failed of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Perform the action when meetings or webinars cannot be archived.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :param action_when_archive_failed: The action_when_archive_failed of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if action_when_archive_failed not in allowed_values:
            raise ValueError(
                "Invalid value for `action_when_archive_failed` ({0}), must be one of {1}"  # noqa: E501
                .format(action_when_archive_failed, allowed_values)
            )

        self._action_when_archive_failed = action_when_archive_failed

    @property
    def notification_when_archiving_starts(self):
        """Gets the notification_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Show notification when video or audio archiving starts.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :return: The notification_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: str
        """
        return self._notification_when_archiving_starts

    @notification_when_archiving_starts.setter
    def notification_when_archiving_starts(self, notification_when_archiving_starts):
        """Sets the notification_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Show notification when video or audio archiving starts.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :param notification_when_archiving_starts: The notification_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["participants", "guest"]  # noqa: E501
        if notification_when_archiving_starts not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_when_archiving_starts` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_when_archiving_starts, allowed_values)
            )

        self._notification_when_archiving_starts = notification_when_archiving_starts

    @property
    def play_voice_prompt_when_archiving_starts(self):
        """Gets the play_voice_prompt_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501

        Play voice prompt when video or audio archiving starts.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :return: The play_voice_prompt_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :rtype: str
        """
        return self._play_voice_prompt_when_archiving_starts

    @play_voice_prompt_when_archiving_starts.setter
    def play_voice_prompt_when_archiving_starts(self, play_voice_prompt_when_archiving_starts):
        """Sets the play_voice_prompt_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.

        Play voice prompt when video or audio archiving starts.    `1` - Participants can stay in the meeting and will receive a notification.    `2` - Nobody can join or stay in the meeting.  # noqa: E501

        :param play_voice_prompt_when_archiving_starts: The play_voice_prompt_when_archiving_starts of this AccountsaccountIdsettingsRecordingArchiveSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["participants", "guest", "none"]  # noqa: E501
        if play_voice_prompt_when_archiving_starts not in allowed_values:
            raise ValueError(
                "Invalid value for `play_voice_prompt_when_archiving_starts` ({0}), must be one of {1}"  # noqa: E501
                .format(play_voice_prompt_when_archiving_starts, allowed_values)
            )

        self._play_voice_prompt_when_archiving_starts = play_voice_prompt_when_archiving_starts

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
        if issubclass(AccountsaccountIdsettingsRecordingArchiveSettings, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsRecordingArchiveSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
