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

class UserSettingsMeetingSettings2(object):
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
        'default_password_for_scheduled_meetings': 'str',
        'embed_password_in_join_link': 'bool',
        'force_pmi_jbh_password': 'bool',
        'host_video': 'bool',
        'join_before_host': 'bool',
        'meeting_password_requirement': 'UserSettingsMeetingSettings2MeetingPasswordRequirement',
        'participants_video': 'bool',
        'personal_meeting': 'bool',
        'pmi_password': 'str',
        'pstn_password_protected': 'bool',
        'require_password_for_instant_meetings': 'bool',
        'require_password_for_pmi_meetings': 'str',
        'require_password_for_scheduled_meetings': 'bool',
        'require_password_for_scheduling_new_meetings': 'bool',
        'use_pmi_for_instant_meetings': 'bool',
        'use_pmi_for_scheduled_meetings': 'bool',
        'continuous_meeting_chat': 'AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat'
    }

    attribute_map = {
        'audio_type': 'audio_type',
        'default_password_for_scheduled_meetings': 'default_password_for_scheduled_meetings',
        'embed_password_in_join_link': 'embed_password_in_join_link',
        'force_pmi_jbh_password': 'force_pmi_jbh_password',
        'host_video': 'host_video',
        'join_before_host': 'join_before_host',
        'meeting_password_requirement': 'meeting_password_requirement',
        'participants_video': 'participants_video',
        'personal_meeting': 'personal_meeting',
        'pmi_password': 'pmi_password',
        'pstn_password_protected': 'pstn_password_protected',
        'require_password_for_instant_meetings': 'require_password_for_instant_meetings',
        'require_password_for_pmi_meetings': 'require_password_for_pmi_meetings',
        'require_password_for_scheduled_meetings': 'require_password_for_scheduled_meetings',
        'require_password_for_scheduling_new_meetings': 'require_password_for_scheduling_new_meetings',
        'use_pmi_for_instant_meetings': 'use_pmi_for_instant_meetings',
        'use_pmi_for_scheduled_meetings': 'use_pmi_for_scheduled_meetings',
        'continuous_meeting_chat': 'continuous_meeting_chat'
    }

    def __init__(self, audio_type='voip', default_password_for_scheduled_meetings=None, embed_password_in_join_link=None, force_pmi_jbh_password=None, host_video=None, join_before_host=None, meeting_password_requirement=None, participants_video=None, personal_meeting=None, pmi_password=None, pstn_password_protected=None, require_password_for_instant_meetings=None, require_password_for_pmi_meetings=None, require_password_for_scheduled_meetings=None, require_password_for_scheduling_new_meetings=None, use_pmi_for_instant_meetings=None, use_pmi_for_scheduled_meetings=None, continuous_meeting_chat=None):  # noqa: E501
        """UserSettingsMeetingSettings2 - a model defined in Swagger"""  # noqa: E501
        self._audio_type = None
        self._default_password_for_scheduled_meetings = None
        self._embed_password_in_join_link = None
        self._force_pmi_jbh_password = None
        self._host_video = None
        self._join_before_host = None
        self._meeting_password_requirement = None
        self._participants_video = None
        self._personal_meeting = None
        self._pmi_password = None
        self._pstn_password_protected = None
        self._require_password_for_instant_meetings = None
        self._require_password_for_pmi_meetings = None
        self._require_password_for_scheduled_meetings = None
        self._require_password_for_scheduling_new_meetings = None
        self._use_pmi_for_instant_meetings = None
        self._use_pmi_for_scheduled_meetings = None
        self._continuous_meeting_chat = None
        self.discriminator = None
        if audio_type is not None:
            self.audio_type = audio_type
        if default_password_for_scheduled_meetings is not None:
            self.default_password_for_scheduled_meetings = default_password_for_scheduled_meetings
        if embed_password_in_join_link is not None:
            self.embed_password_in_join_link = embed_password_in_join_link
        if force_pmi_jbh_password is not None:
            self.force_pmi_jbh_password = force_pmi_jbh_password
        if host_video is not None:
            self.host_video = host_video
        if join_before_host is not None:
            self.join_before_host = join_before_host
        if meeting_password_requirement is not None:
            self.meeting_password_requirement = meeting_password_requirement
        if participants_video is not None:
            self.participants_video = participants_video
        if personal_meeting is not None:
            self.personal_meeting = personal_meeting
        if pmi_password is not None:
            self.pmi_password = pmi_password
        if pstn_password_protected is not None:
            self.pstn_password_protected = pstn_password_protected
        if require_password_for_instant_meetings is not None:
            self.require_password_for_instant_meetings = require_password_for_instant_meetings
        if require_password_for_pmi_meetings is not None:
            self.require_password_for_pmi_meetings = require_password_for_pmi_meetings
        if require_password_for_scheduled_meetings is not None:
            self.require_password_for_scheduled_meetings = require_password_for_scheduled_meetings
        if require_password_for_scheduling_new_meetings is not None:
            self.require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings
        if use_pmi_for_instant_meetings is not None:
            self.use_pmi_for_instant_meetings = use_pmi_for_instant_meetings
        if use_pmi_for_scheduled_meetings is not None:
            self.use_pmi_for_scheduled_meetings = use_pmi_for_scheduled_meetings
        if continuous_meeting_chat is not None:
            self.continuous_meeting_chat = continuous_meeting_chat

    @property
    def audio_type(self):
        """Gets the audio_type of this UserSettingsMeetingSettings2.  # noqa: E501

        Determine how participants can join the audio portion of the meeting:    `both` - Telephony and VoIP.    `telephony` - Audio PSTN telephony only.    `voip` - VoIP only.    `thirdParty` - Third party audio conference.  # noqa: E501

        :return: The audio_type of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: str
        """
        return self._audio_type

    @audio_type.setter
    def audio_type(self, audio_type):
        """Sets the audio_type of this UserSettingsMeetingSettings2.

        Determine how participants can join the audio portion of the meeting:    `both` - Telephony and VoIP.    `telephony` - Audio PSTN telephony only.    `voip` - VoIP only.    `thirdParty` - Third party audio conference.  # noqa: E501

        :param audio_type: The audio_type of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: str
        """
        allowed_values = ["both", "telephony", "voip", "thirdParty"]  # noqa: E501
        if audio_type not in allowed_values:
            raise ValueError(
                "Invalid value for `audio_type` ({0}), must be one of {1}"  # noqa: E501
                .format(audio_type, allowed_values)
            )

        self._audio_type = audio_type

    @property
    def default_password_for_scheduled_meetings(self):
        """Gets the default_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Passcode for already scheduled meetings   # noqa: E501

        :return: The default_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: str
        """
        return self._default_password_for_scheduled_meetings

    @default_password_for_scheduled_meetings.setter
    def default_password_for_scheduled_meetings(self, default_password_for_scheduled_meetings):
        """Sets the default_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.

        Passcode for already scheduled meetings   # noqa: E501

        :param default_password_for_scheduled_meetings: The default_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: str
        """

        self._default_password_for_scheduled_meetings = default_password_for_scheduled_meetings

    @property
    def embed_password_in_join_link(self):
        """Gets the embed_password_in_join_link of this UserSettingsMeetingSettings2.  # noqa: E501

        Encrypt the meeting passcode and include it in the join meeting link to allow participants to join with just one click without having to enter the passcode.    # noqa: E501

        :return: The embed_password_in_join_link of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._embed_password_in_join_link

    @embed_password_in_join_link.setter
    def embed_password_in_join_link(self, embed_password_in_join_link):
        """Sets the embed_password_in_join_link of this UserSettingsMeetingSettings2.

        Encrypt the meeting passcode and include it in the join meeting link to allow participants to join with just one click without having to enter the passcode.    # noqa: E501

        :param embed_password_in_join_link: The embed_password_in_join_link of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._embed_password_in_join_link = embed_password_in_join_link

    @property
    def force_pmi_jbh_password(self):
        """Gets the force_pmi_jbh_password of this UserSettingsMeetingSettings2.  # noqa: E501

        Require a passcode for personal meetings if attendees can join before host.  # noqa: E501

        :return: The force_pmi_jbh_password of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._force_pmi_jbh_password

    @force_pmi_jbh_password.setter
    def force_pmi_jbh_password(self, force_pmi_jbh_password):
        """Sets the force_pmi_jbh_password of this UserSettingsMeetingSettings2.

        Require a passcode for personal meetings if attendees can join before host.  # noqa: E501

        :param force_pmi_jbh_password: The force_pmi_jbh_password of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._force_pmi_jbh_password = force_pmi_jbh_password

    @property
    def host_video(self):
        """Gets the host_video of this UserSettingsMeetingSettings2.  # noqa: E501

        Start meetings with host video on.  # noqa: E501

        :return: The host_video of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._host_video

    @host_video.setter
    def host_video(self, host_video):
        """Sets the host_video of this UserSettingsMeetingSettings2.

        Start meetings with host video on.  # noqa: E501

        :param host_video: The host_video of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._host_video = host_video

    @property
    def join_before_host(self):
        """Gets the join_before_host of this UserSettingsMeetingSettings2.  # noqa: E501

        Join the meeting before host arrives.  # noqa: E501

        :return: The join_before_host of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._join_before_host

    @join_before_host.setter
    def join_before_host(self, join_before_host):
        """Sets the join_before_host of this UserSettingsMeetingSettings2.

        Join the meeting before host arrives.  # noqa: E501

        :param join_before_host: The join_before_host of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._join_before_host = join_before_host

    @property
    def meeting_password_requirement(self):
        """Gets the meeting_password_requirement of this UserSettingsMeetingSettings2.  # noqa: E501


        :return: The meeting_password_requirement of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: UserSettingsMeetingSettings2MeetingPasswordRequirement
        """
        return self._meeting_password_requirement

    @meeting_password_requirement.setter
    def meeting_password_requirement(self, meeting_password_requirement):
        """Sets the meeting_password_requirement of this UserSettingsMeetingSettings2.


        :param meeting_password_requirement: The meeting_password_requirement of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: UserSettingsMeetingSettings2MeetingPasswordRequirement
        """

        self._meeting_password_requirement = meeting_password_requirement

    @property
    def participants_video(self):
        """Gets the participants_video of this UserSettingsMeetingSettings2.  # noqa: E501

        Start meetings with participants video on.  # noqa: E501

        :return: The participants_video of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._participants_video

    @participants_video.setter
    def participants_video(self, participants_video):
        """Sets the participants_video of this UserSettingsMeetingSettings2.

        Start meetings with participants video on.  # noqa: E501

        :param participants_video: The participants_video of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._participants_video = participants_video

    @property
    def personal_meeting(self):
        """Gets the personal_meeting of this UserSettingsMeetingSettings2.  # noqa: E501

        Personal meeting setting.      `true` - Indicates that the **Enable [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi)** setting is turned on. Users can choose to use a PMI for their meetings.       `false` - Indicates that the **Enable Personal Meeting ID** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **Elevate to Zoom Meeting** on desk phone will be disabled.     # noqa: E501

        :return: The personal_meeting of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._personal_meeting

    @personal_meeting.setter
    def personal_meeting(self, personal_meeting):
        """Sets the personal_meeting of this UserSettingsMeetingSettings2.

        Personal meeting setting.      `true` - Indicates that the **Enable [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi)** setting is turned on. Users can choose to use a PMI for their meetings.       `false` - Indicates that the **Enable Personal Meeting ID** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **Elevate to Zoom Meeting** on desk phone will be disabled.     # noqa: E501

        :param personal_meeting: The personal_meeting of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._personal_meeting = personal_meeting

    @property
    def pmi_password(self):
        """Gets the pmi_password of this UserSettingsMeetingSettings2.  # noqa: E501

        PMI passcode   # noqa: E501

        :return: The pmi_password of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: str
        """
        return self._pmi_password

    @pmi_password.setter
    def pmi_password(self, pmi_password):
        """Sets the pmi_password of this UserSettingsMeetingSettings2.

        PMI passcode   # noqa: E501

        :param pmi_password: The pmi_password of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: str
        """

        self._pmi_password = pmi_password

    @property
    def pstn_password_protected(self):
        """Gets the pstn_password_protected of this UserSettingsMeetingSettings2.  # noqa: E501

        Generate and require passcode for participants joining by phone.  # noqa: E501

        :return: The pstn_password_protected of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._pstn_password_protected

    @pstn_password_protected.setter
    def pstn_password_protected(self, pstn_password_protected):
        """Sets the pstn_password_protected of this UserSettingsMeetingSettings2.

        Generate and require passcode for participants joining by phone.  # noqa: E501

        :param pstn_password_protected: The pstn_password_protected of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._pstn_password_protected = pstn_password_protected

    @property
    def require_password_for_instant_meetings(self):
        """Gets the require_password_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Require a passcode for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :return: The require_password_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_instant_meetings

    @require_password_for_instant_meetings.setter
    def require_password_for_instant_meetings(self, require_password_for_instant_meetings):
        """Sets the require_password_for_instant_meetings of this UserSettingsMeetingSettings2.

        Require a passcode for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :param require_password_for_instant_meetings: The require_password_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._require_password_for_instant_meetings = require_password_for_instant_meetings

    @property
    def require_password_for_pmi_meetings(self):
        """Gets the require_password_for_pmi_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Require a passcode for Personal Meeting ID (PMI). This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :return: The require_password_for_pmi_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: str
        """
        return self._require_password_for_pmi_meetings

    @require_password_for_pmi_meetings.setter
    def require_password_for_pmi_meetings(self, require_password_for_pmi_meetings):
        """Sets the require_password_for_pmi_meetings of this UserSettingsMeetingSettings2.

        Require a passcode for Personal Meeting ID (PMI). This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :param require_password_for_pmi_meetings: The require_password_for_pmi_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: str
        """
        allowed_values = ["jbh_only", "all", "none"]  # noqa: E501
        if require_password_for_pmi_meetings not in allowed_values:
            raise ValueError(
                "Invalid value for `require_password_for_pmi_meetings` ({0}), must be one of {1}"  # noqa: E501
                .format(require_password_for_pmi_meetings, allowed_values)
            )

        self._require_password_for_pmi_meetings = require_password_for_pmi_meetings

    @property
    def require_password_for_scheduled_meetings(self):
        """Gets the require_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Require a passcode for meetings which have already been scheduled.   # noqa: E501

        :return: The require_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduled_meetings

    @require_password_for_scheduled_meetings.setter
    def require_password_for_scheduled_meetings(self, require_password_for_scheduled_meetings):
        """Sets the require_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.

        Require a passcode for meetings which have already been scheduled.   # noqa: E501

        :param require_password_for_scheduled_meetings: The require_password_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduled_meetings = require_password_for_scheduled_meetings

    @property
    def require_password_for_scheduling_new_meetings(self):
        """Gets the require_password_for_scheduling_new_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Require a passcode when scheduling new meetings.This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :return: The require_password_for_scheduling_new_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduling_new_meetings

    @require_password_for_scheduling_new_meetings.setter
    def require_password_for_scheduling_new_meetings(self, require_password_for_scheduling_new_meetings):
        """Sets the require_password_for_scheduling_new_meetings of this UserSettingsMeetingSettings2.

        Require a passcode when scheduling new meetings.This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :param require_password_for_scheduling_new_meetings: The require_password_for_scheduling_new_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings

    @property
    def use_pmi_for_instant_meetings(self):
        """Gets the use_pmi_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) when starting an instant meeting.  # noqa: E501

        :return: The use_pmi_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi_for_instant_meetings

    @use_pmi_for_instant_meetings.setter
    def use_pmi_for_instant_meetings(self, use_pmi_for_instant_meetings):
        """Sets the use_pmi_for_instant_meetings of this UserSettingsMeetingSettings2.

        Use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) when starting an instant meeting.  # noqa: E501

        :param use_pmi_for_instant_meetings: The use_pmi_for_instant_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._use_pmi_for_instant_meetings = use_pmi_for_instant_meetings

    @property
    def use_pmi_for_scheduled_meetings(self):
        """Gets the use_pmi_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501

        Use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) when scheduling a meeting.  # noqa: E501

        :return: The use_pmi_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi_for_scheduled_meetings

    @use_pmi_for_scheduled_meetings.setter
    def use_pmi_for_scheduled_meetings(self, use_pmi_for_scheduled_meetings):
        """Sets the use_pmi_for_scheduled_meetings of this UserSettingsMeetingSettings2.

        Use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) when scheduling a meeting.  # noqa: E501

        :param use_pmi_for_scheduled_meetings: The use_pmi_for_scheduled_meetings of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._use_pmi_for_scheduled_meetings = use_pmi_for_scheduled_meetings

    @property
    def continuous_meeting_chat(self):
        """Gets the continuous_meeting_chat of this UserSettingsMeetingSettings2.  # noqa: E501


        :return: The continuous_meeting_chat of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: AccountsaccountIdsettingsScheduleMeetingContinuousMeetingChat
        """
        return self._continuous_meeting_chat

    @continuous_meeting_chat.setter
    def continuous_meeting_chat(self, continuous_meeting_chat):
        """Sets the continuous_meeting_chat of this UserSettingsMeetingSettings2.


        :param continuous_meeting_chat: The continuous_meeting_chat of this UserSettingsMeetingSettings2.  # noqa: E501
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
        if issubclass(UserSettingsMeetingSettings2, dict):
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
        if not isinstance(other, UserSettingsMeetingSettings2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
