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

class InlineResponse2008(object):
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
        'account_name': 'str',
        'archive_files': 'list[InlineResponse2008ArchiveFiles]',
        'complete_time': 'AnyOfinlineResponse2008CompleteTime',
        'duration': 'int',
        'duration_in_second': 'int',
        'host_id': 'str',
        'id': 'int',
        'is_breakout_room': 'bool',
        'meeting_type': 'str',
        'parent_meeting_id': 'str',
        'recording_count': 'int',
        'start_time': 'datetime',
        'timezone': 'str',
        'topic': 'str',
        'total_size': 'int',
        'type': 'int',
        'uuid': 'str',
        'status': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'archive_files': 'archive_files',
        'complete_time': 'complete_time',
        'duration': 'duration',
        'duration_in_second': 'duration_in_second',
        'host_id': 'host_id',
        'id': 'id',
        'is_breakout_room': 'is_breakout_room',
        'meeting_type': 'meeting_type',
        'parent_meeting_id': 'parent_meeting_id',
        'recording_count': 'recording_count',
        'start_time': 'start_time',
        'timezone': 'timezone',
        'topic': 'topic',
        'total_size': 'total_size',
        'type': 'type',
        'uuid': 'uuid',
        'status': 'status'
    }

    def __init__(self, account_name=None, archive_files=None, complete_time=None, duration=None, duration_in_second=None, host_id=None, id=None, is_breakout_room=None, meeting_type=None, parent_meeting_id=None, recording_count=None, start_time=None, timezone=None, topic=None, total_size=None, type=None, uuid=None, status=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._account_name = None
        self._archive_files = None
        self._complete_time = None
        self._duration = None
        self._duration_in_second = None
        self._host_id = None
        self._id = None
        self._is_breakout_room = None
        self._meeting_type = None
        self._parent_meeting_id = None
        self._recording_count = None
        self._start_time = None
        self._timezone = None
        self._topic = None
        self._total_size = None
        self._type = None
        self._uuid = None
        self._status = None
        self.discriminator = None
        self.account_name = account_name
        self.archive_files = archive_files
        self.complete_time = complete_time
        self.duration = duration
        self.duration_in_second = duration_in_second
        self.host_id = host_id
        self.id = id
        self.is_breakout_room = is_breakout_room
        self.meeting_type = meeting_type
        if parent_meeting_id is not None:
            self.parent_meeting_id = parent_meeting_id
        self.recording_count = recording_count
        self.start_time = start_time
        self.timezone = timezone
        self.topic = topic
        self.total_size = total_size
        self.type = type
        self.uuid = uuid
        self.status = status

    @property
    def account_name(self):
        """Gets the account_name of this InlineResponse2008.  # noqa: E501

        The user's account name.  # noqa: E501

        :return: The account_name of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this InlineResponse2008.

        The user's account name.  # noqa: E501

        :param account_name: The account_name of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def archive_files(self):
        """Gets the archive_files of this InlineResponse2008.  # noqa: E501

        Information about the archive files.  # noqa: E501

        :return: The archive_files of this InlineResponse2008.  # noqa: E501
        :rtype: list[InlineResponse2008ArchiveFiles]
        """
        return self._archive_files

    @archive_files.setter
    def archive_files(self, archive_files):
        """Sets the archive_files of this InlineResponse2008.

        Information about the archive files.  # noqa: E501

        :param archive_files: The archive_files of this InlineResponse2008.  # noqa: E501
        :type: list[InlineResponse2008ArchiveFiles]
        """
        if archive_files is None:
            raise ValueError("Invalid value for `archive_files`, must not be `None`")  # noqa: E501

        self._archive_files = archive_files

    @property
    def complete_time(self):
        """Gets the complete_time of this InlineResponse2008.  # noqa: E501

        The meeting or webinar's archive completion time.  # noqa: E501

        :return: The complete_time of this InlineResponse2008.  # noqa: E501
        :rtype: AnyOfinlineResponse2008CompleteTime
        """
        return self._complete_time

    @complete_time.setter
    def complete_time(self, complete_time):
        """Sets the complete_time of this InlineResponse2008.

        The meeting or webinar's archive completion time.  # noqa: E501

        :param complete_time: The complete_time of this InlineResponse2008.  # noqa: E501
        :type: AnyOfinlineResponse2008CompleteTime
        """
        if complete_time is None:
            raise ValueError("Invalid value for `complete_time`, must not be `None`")  # noqa: E501

        self._complete_time = complete_time

    @property
    def duration(self):
        """Gets the duration of this InlineResponse2008.  # noqa: E501

        The meeting or webinar's scheduled duration.  # noqa: E501

        :return: The duration of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse2008.

        The meeting or webinar's scheduled duration.  # noqa: E501

        :param duration: The duration of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def duration_in_second(self):
        """Gets the duration_in_second of this InlineResponse2008.  # noqa: E501

        The meeting or webinar's duration, in seconds.  # noqa: E501

        :return: The duration_in_second of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_second

    @duration_in_second.setter
    def duration_in_second(self, duration_in_second):
        """Sets the duration_in_second of this InlineResponse2008.

        The meeting or webinar's duration, in seconds.  # noqa: E501

        :param duration_in_second: The duration_in_second of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if duration_in_second is None:
            raise ValueError("Invalid value for `duration_in_second`, must not be `None`")  # noqa: E501

        self._duration_in_second = duration_in_second

    @property
    def host_id(self):
        """Gets the host_id of this InlineResponse2008.  # noqa: E501

        The host's user ID for the archived meeting or webinar.  # noqa: E501

        :return: The host_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this InlineResponse2008.

        The host's user ID for the archived meeting or webinar.  # noqa: E501

        :param host_id: The host_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if host_id is None:
            raise ValueError("Invalid value for `host_id`, must not be `None`")  # noqa: E501

        self._host_id = host_id

    @property
    def id(self):
        """Gets the id of this InlineResponse2008.  # noqa: E501

        The meeting or webinar ID, either `meetingId` or `webinarId`.  # noqa: E501

        :return: The id of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2008.

        The meeting or webinar ID, either `meetingId` or `webinarId`.  # noqa: E501

        :param id: The id of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_breakout_room(self):
        """Gets the is_breakout_room of this InlineResponse2008.  # noqa: E501

        Whether the room is a [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).  # noqa: E501

        :return: The is_breakout_room of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._is_breakout_room

    @is_breakout_room.setter
    def is_breakout_room(self, is_breakout_room):
        """Sets the is_breakout_room of this InlineResponse2008.

        Whether the room is a [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).  # noqa: E501

        :param is_breakout_room: The is_breakout_room of this InlineResponse2008.  # noqa: E501
        :type: bool
        """
        if is_breakout_room is None:
            raise ValueError("Invalid value for `is_breakout_room`, must not be `None`")  # noqa: E501

        self._is_breakout_room = is_breakout_room

    @property
    def meeting_type(self):
        """Gets the meeting_type of this InlineResponse2008.  # noqa: E501

        Whether the meeting or webinar is internal or external.  * `internal` - An internal meeting or webinar.  * `external` - An external meeting or webinar.    The `id`, `host_id`, and `topic` PII (Personal Identifiable Information) values in this response are removed when this value is `external`.  # noqa: E501

        :return: The meeting_type of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._meeting_type

    @meeting_type.setter
    def meeting_type(self, meeting_type):
        """Sets the meeting_type of this InlineResponse2008.

        Whether the meeting or webinar is internal or external.  * `internal` - An internal meeting or webinar.  * `external` - An external meeting or webinar.    The `id`, `host_id`, and `topic` PII (Personal Identifiable Information) values in this response are removed when this value is `external`.  # noqa: E501

        :param meeting_type: The meeting_type of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if meeting_type is None:
            raise ValueError("Invalid value for `meeting_type`, must not be `None`")  # noqa: E501
        allowed_values = ["internal", "external"]  # noqa: E501
        if meeting_type not in allowed_values:
            raise ValueError(
                "Invalid value for `meeting_type` ({0}), must be one of {1}"  # noqa: E501
                .format(meeting_type, allowed_values)
            )

        self._meeting_type = meeting_type

    @property
    def parent_meeting_id(self):
        """Gets the parent_meeting_id of this InlineResponse2008.  # noqa: E501

        The parent meeting's universally unique ID (UUID). Each meeting or webinar instance generates a UUID. If the `is_breakout_room` value is `true`, the API returns this value.  # noqa: E501

        :return: The parent_meeting_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._parent_meeting_id

    @parent_meeting_id.setter
    def parent_meeting_id(self, parent_meeting_id):
        """Sets the parent_meeting_id of this InlineResponse2008.

        The parent meeting's universally unique ID (UUID). Each meeting or webinar instance generates a UUID. If the `is_breakout_room` value is `true`, the API returns this value.  # noqa: E501

        :param parent_meeting_id: The parent_meeting_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """

        self._parent_meeting_id = parent_meeting_id

    @property
    def recording_count(self):
        """Gets the recording_count of this InlineResponse2008.  # noqa: E501

        The number of archived files returned in the API call response.  # noqa: E501

        :return: The recording_count of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._recording_count

    @recording_count.setter
    def recording_count(self, recording_count):
        """Sets the recording_count of this InlineResponse2008.

        The number of archived files returned in the API call response.  # noqa: E501

        :param recording_count: The recording_count of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if recording_count is None:
            raise ValueError("Invalid value for `recording_count`, must not be `None`")  # noqa: E501

        self._recording_count = recording_count

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse2008.  # noqa: E501

        The meeting or webinar's start time.  # noqa: E501

        :return: The start_time of this InlineResponse2008.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse2008.

        The meeting or webinar's start time.  # noqa: E501

        :param start_time: The start_time of this InlineResponse2008.  # noqa: E501
        :type: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def timezone(self):
        """Gets the timezone of this InlineResponse2008.  # noqa: E501

        The meeting or webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).  # noqa: E501

        :return: The timezone of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InlineResponse2008.

        The meeting or webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).  # noqa: E501

        :param timezone: The timezone of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def topic(self):
        """Gets the topic of this InlineResponse2008.  # noqa: E501

        The meeting or webinar topic.  # noqa: E501

        :return: The topic of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this InlineResponse2008.

        The meeting or webinar topic.  # noqa: E501

        :param topic: The topic of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if topic is None:
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

    @property
    def total_size(self):
        """Gets the total_size of this InlineResponse2008.  # noqa: E501

        The total size of the archive file, in bytes.  # noqa: E501

        :return: The total_size of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this InlineResponse2008.

        The total size of the archive file, in bytes.  # noqa: E501

        :param total_size: The total_size of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")  # noqa: E501

        self._total_size = total_size

    @property
    def type(self):
        """Gets the type of this InlineResponse2008.  # noqa: E501

        The type of archived meeting or webinar.    If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.    If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.    If the recording is **not** from a meeting or webinar:   * `100` - A [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).  # noqa: E501

        :return: The type of this InlineResponse2008.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2008.

        The type of archived meeting or webinar.    If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.    If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.    If the recording is **not** from a meeting or webinar:   * `100` - A [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).  # noqa: E501

        :param type: The type of this InlineResponse2008.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse2008.  # noqa: E501

        The universally unique identifier (UUID) of the recorded meeting or webinar instance. Each meeting or webinar instance generates a UUID.  # noqa: E501

        :return: The uuid of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse2008.

        The universally unique identifier (UUID) of the recorded meeting or webinar instance. Each meeting or webinar instance generates a UUID.  # noqa: E501

        :param uuid: The uuid of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this InlineResponse2008.  # noqa: E501

        The archive's processing status.  * `completed` - The archive's processing is complete.  * `processing` - The archive is processing.  # noqa: E501

        :return: The status of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2008.

        The archive's processing status.  * `completed` - The archive's processing is complete.  * `processing` - The archive is processing.  # noqa: E501

        :param status: The status of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["completed", "processing"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other