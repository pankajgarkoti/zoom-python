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

class GroupsgroupIdsettingsScheduleMeeting(object):
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
        'audio_type': 'str',
        'embed_password_in_join_link': 'bool',
        'force_pmi_jbh_password': 'bool',
        'host_video': 'bool',
        'join_before_host': 'bool',
        'mute_upon_entry': 'bool',
        'participant_video': 'bool',
        'pstn_password_protected': 'bool',
        'require_password_for_all_meetings': 'bool',
        'require_password_for_instant_meetings': 'bool',
        'require_password_for_pmi_meetings': 'str',
        'require_password_for_scheduled_meetings': 'bool',
        'require_password_for_scheduling_new_meetings': 'bool',
        'upcoming_meeting_reminder': 'bool',
        'always_display_zoom_meeting_as_topic': 'GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomMeetingAsTopic',
        'always_display_zoom_webinar_as_topic': 'GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomWebinarAsTopic',
        'continuous_meeting_chat': 'AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat'
    }

    attribute_map = {
        'audio_type': 'audio_type',
        'embed_password_in_join_link': 'embed_password_in_join_link',
        'force_pmi_jbh_password': 'force_pmi_jbh_password',
        'host_video': 'host_video',
        'join_before_host': 'join_before_host',
        'mute_upon_entry': 'mute_upon_entry',
        'participant_video': 'participant_video',
        'pstn_password_protected': 'pstn_password_protected',
        'require_password_for_all_meetings': 'require_password_for_all_meetings',
        'require_password_for_instant_meetings': 'require_password_for_instant_meetings',
        'require_password_for_pmi_meetings': 'require_password_for_pmi_meetings',
        'require_password_for_scheduled_meetings': 'require_password_for_scheduled_meetings',
        'require_password_for_scheduling_new_meetings': 'require_password_for_scheduling_new_meetings',
        'upcoming_meeting_reminder': 'upcoming_meeting_reminder',
        'always_display_zoom_meeting_as_topic': 'always_display_zoom_meeting_as_topic',
        'always_display_zoom_webinar_as_topic': 'always_display_zoom_webinar_as_topic',
        'continuous_meeting_chat': 'continuous_meeting_chat'
    }

    def __init__(self, audio_type=None, embed_password_in_join_link=None, force_pmi_jbh_password=None, host_video=None, join_before_host=None, mute_upon_entry=None, participant_video=None, pstn_password_protected=None, require_password_for_all_meetings=None, require_password_for_instant_meetings=None, require_password_for_pmi_meetings=None, require_password_for_scheduled_meetings=None, require_password_for_scheduling_new_meetings=None, upcoming_meeting_reminder=None, always_display_zoom_meeting_as_topic=None, always_display_zoom_webinar_as_topic=None, continuous_meeting_chat=None):  # noqa: E501
        """GroupsgroupIdsettingsScheduleMeeting - a model defined in Swagger"""  # noqa: E501
        self._audio_type = None
        self._embed_password_in_join_link = None
        self._force_pmi_jbh_password = None
        self._host_video = None
        self._join_before_host = None
        self._mute_upon_entry = None
        self._participant_video = None
        self._pstn_password_protected = None
        self._require_password_for_all_meetings = None
        self._require_password_for_instant_meetings = None
        self._require_password_for_pmi_meetings = None
        self._require_password_for_scheduled_meetings = None
        self._require_password_for_scheduling_new_meetings = None
        self._upcoming_meeting_reminder = None
        self._always_display_zoom_meeting_as_topic = None
        self._always_display_zoom_webinar_as_topic = None
        self._continuous_meeting_chat = None
        self.discriminator = None
        if audio_type is not None:
            self.audio_type = audio_type
        if embed_password_in_join_link is not None:
            self.embed_password_in_join_link = embed_password_in_join_link
        if force_pmi_jbh_password is not None:
            self.force_pmi_jbh_password = force_pmi_jbh_password
        if host_video is not None:
            self.host_video = host_video
        if join_before_host is not None:
            self.join_before_host = join_before_host
        if mute_upon_entry is not None:
            self.mute_upon_entry = mute_upon_entry
        if participant_video is not None:
            self.participant_video = participant_video
        if pstn_password_protected is not None:
            self.pstn_password_protected = pstn_password_protected
        if require_password_for_all_meetings is not None:
            self.require_password_for_all_meetings = require_password_for_all_meetings
        if require_password_for_instant_meetings is not None:
            self.require_password_for_instant_meetings = require_password_for_instant_meetings
        if require_password_for_pmi_meetings is not None:
            self.require_password_for_pmi_meetings = require_password_for_pmi_meetings
        if require_password_for_scheduled_meetings is not None:
            self.require_password_for_scheduled_meetings = require_password_for_scheduled_meetings
        if require_password_for_scheduling_new_meetings is not None:
            self.require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings
        if upcoming_meeting_reminder is not None:
            self.upcoming_meeting_reminder = upcoming_meeting_reminder
        if always_display_zoom_meeting_as_topic is not None:
            self.always_display_zoom_meeting_as_topic = always_display_zoom_meeting_as_topic
        if always_display_zoom_webinar_as_topic is not None:
            self.always_display_zoom_webinar_as_topic = always_display_zoom_webinar_as_topic
        if continuous_meeting_chat is not None:
            self.continuous_meeting_chat = continuous_meeting_chat

    @property
    def audio_type(self):
        """Gets the audio_type of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Determine how participants can join the audio portion of the meeting.  # noqa: E501

        :return: The audio_type of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: str
        """
        return self._audio_type

    @audio_type.setter
    def audio_type(self, audio_type):
        """Sets the audio_type of this GroupsgroupIdsettingsScheduleMeeting.

        Determine how participants can join the audio portion of the meeting.  # noqa: E501

        :param audio_type: The audio_type of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: str
        """

        self._audio_type = audio_type

    @property
    def embed_password_in_join_link(self):
        """Gets the embed_password_in_join_link of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        If the value is set to `true`, the meeting passcode will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the passcode.    # noqa: E501

        :return: The embed_password_in_join_link of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._embed_password_in_join_link

    @embed_password_in_join_link.setter
    def embed_password_in_join_link(self, embed_password_in_join_link):
        """Sets the embed_password_in_join_link of this GroupsgroupIdsettingsScheduleMeeting.

        If the value is set to `true`, the meeting passcode will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the passcode.    # noqa: E501

        :param embed_password_in_join_link: The embed_password_in_join_link of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._embed_password_in_join_link = embed_password_in_join_link

    @property
    def force_pmi_jbh_password(self):
        """Gets the force_pmi_jbh_password of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        If join before host option is enabled for a personal meeting, then enforce passcode requirement.  # noqa: E501

        :return: The force_pmi_jbh_password of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._force_pmi_jbh_password

    @force_pmi_jbh_password.setter
    def force_pmi_jbh_password(self, force_pmi_jbh_password):
        """Sets the force_pmi_jbh_password of this GroupsgroupIdsettingsScheduleMeeting.

        If join before host option is enabled for a personal meeting, then enforce passcode requirement.  # noqa: E501

        :param force_pmi_jbh_password: The force_pmi_jbh_password of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._force_pmi_jbh_password = force_pmi_jbh_password

    @property
    def host_video(self):
        """Gets the host_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Start meetings with host video on.  # noqa: E501

        :return: The host_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._host_video

    @host_video.setter
    def host_video(self, host_video):
        """Sets the host_video of this GroupsgroupIdsettingsScheduleMeeting.

        Start meetings with host video on.  # noqa: E501

        :param host_video: The host_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._host_video = host_video

    @property
    def join_before_host(self):
        """Gets the join_before_host of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Allow participants to join the meeting before the host arrives  # noqa: E501

        :return: The join_before_host of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._join_before_host

    @join_before_host.setter
    def join_before_host(self, join_before_host):
        """Sets the join_before_host of this GroupsgroupIdsettingsScheduleMeeting.

        Allow participants to join the meeting before the host arrives  # noqa: E501

        :param join_before_host: The join_before_host of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._join_before_host = join_before_host

    @property
    def mute_upon_entry(self):
        """Gets the mute_upon_entry of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Automatically mute all participants when they join the meeting.  # noqa: E501

        :return: The mute_upon_entry of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._mute_upon_entry

    @mute_upon_entry.setter
    def mute_upon_entry(self, mute_upon_entry):
        """Sets the mute_upon_entry of this GroupsgroupIdsettingsScheduleMeeting.

        Automatically mute all participants when they join the meeting.  # noqa: E501

        :param mute_upon_entry: The mute_upon_entry of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._mute_upon_entry = mute_upon_entry

    @property
    def participant_video(self):
        """Gets the participant_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Start meetings with participant video on.  # noqa: E501

        :return: The participant_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._participant_video

    @participant_video.setter
    def participant_video(self, participant_video):
        """Sets the participant_video of this GroupsgroupIdsettingsScheduleMeeting.

        Start meetings with participant video on.  # noqa: E501

        :param participant_video: The participant_video of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._participant_video = participant_video

    @property
    def pstn_password_protected(self):
        """Gets the pstn_password_protected of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Generate and send new passcodes for newly scheduled or edited meetings.  # noqa: E501

        :return: The pstn_password_protected of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._pstn_password_protected

    @pstn_password_protected.setter
    def pstn_password_protected(self, pstn_password_protected):
        """Sets the pstn_password_protected of this GroupsgroupIdsettingsScheduleMeeting.

        Generate and send new passcodes for newly scheduled or edited meetings.  # noqa: E501

        :param pstn_password_protected: The pstn_password_protected of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._pstn_password_protected = pstn_password_protected

    @property
    def require_password_for_all_meetings(self):
        """Gets the require_password_for_all_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Require passcode from all participants before joining a meeting.  # noqa: E501

        :return: The require_password_for_all_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_all_meetings

    @require_password_for_all_meetings.setter
    def require_password_for_all_meetings(self, require_password_for_all_meetings):
        """Sets the require_password_for_all_meetings of this GroupsgroupIdsettingsScheduleMeeting.

        Require passcode from all participants before joining a meeting.  # noqa: E501

        :param require_password_for_all_meetings: The require_password_for_all_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_all_meetings = require_password_for_all_meetings

    @property
    def require_password_for_instant_meetings(self):
        """Gets the require_password_for_instant_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        If enabled, a random passcode will be generated on the user's end who starts the instant meeting. Other participants will have to enter the passcode to join the meeting. If you use PMI for your instant meetings, this option will be disabled.  # noqa: E501

        :return: The require_password_for_instant_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_instant_meetings

    @require_password_for_instant_meetings.setter
    def require_password_for_instant_meetings(self, require_password_for_instant_meetings):
        """Sets the require_password_for_instant_meetings of this GroupsgroupIdsettingsScheduleMeeting.

        If enabled, a random passcode will be generated on the user's end who starts the instant meeting. Other participants will have to enter the passcode to join the meeting. If you use PMI for your instant meetings, this option will be disabled.  # noqa: E501

        :param require_password_for_instant_meetings: The require_password_for_instant_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_instant_meetings = require_password_for_instant_meetings

    @property
    def require_password_for_pmi_meetings(self):
        """Gets the require_password_for_pmi_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Indicates whether a passcode is required for [PMI](https://support.zoom.us/hc/en-us/articles/203276937-Using-Personal-Meeting-ID-PMI-) meetings or not. The value can be one of the following:     `none`: Do not require passcode for PMI meetings.      `all`: Require participants to enter passcode for all PMI enabled meetings.     `jbh_only`: Require passcode only for meetings where the **join before host** setting is enabled.  # noqa: E501

        :return: The require_password_for_pmi_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: str
        """
        return self._require_password_for_pmi_meetings

    @require_password_for_pmi_meetings.setter
    def require_password_for_pmi_meetings(self, require_password_for_pmi_meetings):
        """Sets the require_password_for_pmi_meetings of this GroupsgroupIdsettingsScheduleMeeting.

        Indicates whether a passcode is required for [PMI](https://support.zoom.us/hc/en-us/articles/203276937-Using-Personal-Meeting-ID-PMI-) meetings or not. The value can be one of the following:     `none`: Do not require passcode for PMI meetings.      `all`: Require participants to enter passcode for all PMI enabled meetings.     `jbh_only`: Require passcode only for meetings where the **join before host** setting is enabled.  # noqa: E501

        :param require_password_for_pmi_meetings: The require_password_for_pmi_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "jbh_only", "none"]  # noqa: E501
        if require_password_for_pmi_meetings not in allowed_values:
            raise ValueError(
                "Invalid value for `require_password_for_pmi_meetings` ({0}), must be one of {1}"  # noqa: E501
                .format(require_password_for_pmi_meetings, allowed_values)
            )

        self._require_password_for_pmi_meetings = require_password_for_pmi_meetings

    @property
    def require_password_for_scheduled_meetings(self):
        """Gets the require_password_for_scheduled_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Require a passcode for meetings which have already been scheduled.   # noqa: E501

        :return: The require_password_for_scheduled_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduled_meetings

    @require_password_for_scheduled_meetings.setter
    def require_password_for_scheduled_meetings(self, require_password_for_scheduled_meetings):
        """Sets the require_password_for_scheduled_meetings of this GroupsgroupIdsettingsScheduleMeeting.

        Require a passcode for meetings which have already been scheduled.   # noqa: E501

        :param require_password_for_scheduled_meetings: The require_password_for_scheduled_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduled_meetings = require_password_for_scheduled_meetings

    @property
    def require_password_for_scheduling_new_meetings(self):
        """Gets the require_password_for_scheduling_new_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        This setting applies for regular meetings that do not use PMI. If enabled, a passcode will be generated while a host schedules a new meeting and participants will be required to enter the passcode before they can join the meeting.   # noqa: E501

        :return: The require_password_for_scheduling_new_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduling_new_meetings

    @require_password_for_scheduling_new_meetings.setter
    def require_password_for_scheduling_new_meetings(self, require_password_for_scheduling_new_meetings):
        """Sets the require_password_for_scheduling_new_meetings of this GroupsgroupIdsettingsScheduleMeeting.

        This setting applies for regular meetings that do not use PMI. If enabled, a passcode will be generated while a host schedules a new meeting and participants will be required to enter the passcode before they can join the meeting.   # noqa: E501

        :param require_password_for_scheduling_new_meetings: The require_password_for_scheduling_new_meetings of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings

    @property
    def upcoming_meeting_reminder(self):
        """Gets the upcoming_meeting_reminder of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501

        Receive desktop notification for upcoming meetings.  # noqa: E501

        :return: The upcoming_meeting_reminder of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._upcoming_meeting_reminder

    @upcoming_meeting_reminder.setter
    def upcoming_meeting_reminder(self, upcoming_meeting_reminder):
        """Sets the upcoming_meeting_reminder of this GroupsgroupIdsettingsScheduleMeeting.

        Receive desktop notification for upcoming meetings.  # noqa: E501

        :param upcoming_meeting_reminder: The upcoming_meeting_reminder of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._upcoming_meeting_reminder = upcoming_meeting_reminder

    @property
    def always_display_zoom_meeting_as_topic(self):
        """Gets the always_display_zoom_meeting_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501


        :return: The always_display_zoom_meeting_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomMeetingAsTopic
        """
        return self._always_display_zoom_meeting_as_topic

    @always_display_zoom_meeting_as_topic.setter
    def always_display_zoom_meeting_as_topic(self, always_display_zoom_meeting_as_topic):
        """Sets the always_display_zoom_meeting_as_topic of this GroupsgroupIdsettingsScheduleMeeting.


        :param always_display_zoom_meeting_as_topic: The always_display_zoom_meeting_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomMeetingAsTopic
        """

        self._always_display_zoom_meeting_as_topic = always_display_zoom_meeting_as_topic

    @property
    def always_display_zoom_webinar_as_topic(self):
        """Gets the always_display_zoom_webinar_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501


        :return: The always_display_zoom_webinar_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomWebinarAsTopic
        """
        return self._always_display_zoom_webinar_as_topic

    @always_display_zoom_webinar_as_topic.setter
    def always_display_zoom_webinar_as_topic(self, always_display_zoom_webinar_as_topic):
        """Sets the always_display_zoom_webinar_as_topic of this GroupsgroupIdsettingsScheduleMeeting.


        :param always_display_zoom_webinar_as_topic: The always_display_zoom_webinar_as_topic of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: GroupsgroupIdsettingsScheduleMeetingAlwaysDisplayZoomWebinarAsTopic
        """

        self._always_display_zoom_webinar_as_topic = always_display_zoom_webinar_as_topic

    @property
    def continuous_meeting_chat(self):
        """Gets the continuous_meeting_chat of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501


        :return: The continuous_meeting_chat of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :rtype: AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat
        """
        return self._continuous_meeting_chat

    @continuous_meeting_chat.setter
    def continuous_meeting_chat(self, continuous_meeting_chat):
        """Sets the continuous_meeting_chat of this GroupsgroupIdsettingsScheduleMeeting.


        :param continuous_meeting_chat: The continuous_meeting_chat of this GroupsgroupIdsettingsScheduleMeeting.  # noqa: E501
        :type: AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat
        """

        self._continuous_meeting_chat = continuous_meeting_chat

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
        if issubclass(GroupsgroupIdsettingsScheduleMeeting, dict):
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
        if not isinstance(other, GroupsgroupIdsettingsScheduleMeeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
