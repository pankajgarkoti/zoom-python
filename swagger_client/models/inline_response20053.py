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

class InlineResponse20053(object):
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
        'id': 'int',
        'uuid': 'str',
        'duration': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'host_id': 'str',
        'dept': 'str',
        'participants_count': 'int',
        'source': 'str',
        'topic': 'str',
        'total_minutes': 'int',
        'type': 'int',
        'user_email': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'duration': 'duration',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'host_id': 'host_id',
        'dept': 'dept',
        'participants_count': 'participants_count',
        'source': 'source',
        'topic': 'topic',
        'total_minutes': 'total_minutes',
        'type': 'type',
        'user_email': 'user_email',
        'user_name': 'user_name'
    }

    def __init__(self, id=None, uuid=None, duration=None, start_time=None, end_time=None, host_id=None, dept=None, participants_count=None, source=None, topic=None, total_minutes=None, type=None, user_email=None, user_name=None):  # noqa: E501
        """InlineResponse20053 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uuid = None
        self._duration = None
        self._start_time = None
        self._end_time = None
        self._host_id = None
        self._dept = None
        self._participants_count = None
        self._source = None
        self._topic = None
        self._total_minutes = None
        self._type = None
        self._user_email = None
        self._user_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if host_id is not None:
            self.host_id = host_id
        if dept is not None:
            self.dept = dept
        if participants_count is not None:
            self.participants_count = participants_count
        if source is not None:
            self.source = source
        if topic is not None:
            self.topic = topic
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if type is not None:
            self.type = type
        if user_email is not None:
            self.user_email = user_email
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        """Gets the id of this InlineResponse20053.  # noqa: E501

        The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).  # noqa: E501

        :return: The id of this InlineResponse20053.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20053.

        The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).  # noqa: E501

        :param id: The id of this InlineResponse20053.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20053.  # noqa: E501

        The meeting's UUID. You **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) this value if the meeting UUID begins with a `/` character or contains the `//` character.  # noqa: E501

        :return: The uuid of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20053.

        The meeting's UUID. You **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) this value if the meeting UUID begins with a `/` character or contains the `//` character.  # noqa: E501

        :param uuid: The uuid of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20053.  # noqa: E501

        The meeting's duration, in minutes.  # noqa: E501

        :return: The duration of this InlineResponse20053.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20053.

        The meeting's duration, in minutes.  # noqa: E501

        :param duration: The duration of this InlineResponse20053.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20053.  # noqa: E501

        The meeting's start date and time.  # noqa: E501

        :return: The start_time of this InlineResponse20053.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20053.

        The meeting's start date and time.  # noqa: E501

        :param start_time: The start_time of this InlineResponse20053.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InlineResponse20053.  # noqa: E501

        The meeting's end date and time.  # noqa: E501

        :return: The end_time of this InlineResponse20053.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InlineResponse20053.

        The meeting's end date and time.  # noqa: E501

        :param end_time: The end_time of this InlineResponse20053.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def host_id(self):
        """Gets the host_id of this InlineResponse20053.  # noqa: E501

        The host's ID.  # noqa: E501

        :return: The host_id of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this InlineResponse20053.

        The host's ID.  # noqa: E501

        :param host_id: The host_id of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def dept(self):
        """Gets the dept of this InlineResponse20053.  # noqa: E501

        The meeting host's department.  # noqa: E501

        :return: The dept of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this InlineResponse20053.

        The meeting host's department.  # noqa: E501

        :param dept: The dept of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._dept = dept

    @property
    def participants_count(self):
        """Gets the participants_count of this InlineResponse20053.  # noqa: E501

        The number of meeting participants.  # noqa: E501

        :return: The participants_count of this InlineResponse20053.  # noqa: E501
        :rtype: int
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """Sets the participants_count of this InlineResponse20053.

        The number of meeting participants.  # noqa: E501

        :param participants_count: The participants_count of this InlineResponse20053.  # noqa: E501
        :type: int
        """

        self._participants_count = participants_count

    @property
    def source(self):
        """Gets the source of this InlineResponse20053.  # noqa: E501

        Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.  # noqa: E501

        :return: The source of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InlineResponse20053.

        Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.  # noqa: E501

        :param source: The source of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def topic(self):
        """Gets the topic of this InlineResponse20053.  # noqa: E501

        The meeting's topic.  # noqa: E501

        :return: The topic of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this InlineResponse20053.

        The meeting's topic.  # noqa: E501

        :param topic: The topic of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def total_minutes(self):
        """Gets the total_minutes of this InlineResponse20053.  # noqa: E501

        The total number of minutes attended by the meeting's host and participants.  # noqa: E501

        :return: The total_minutes of this InlineResponse20053.  # noqa: E501
        :rtype: int
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this InlineResponse20053.

        The total number of minutes attended by the meeting's host and participants.  # noqa: E501

        :param total_minutes: The total_minutes of this InlineResponse20053.  # noqa: E501
        :type: int
        """

        self._total_minutes = total_minutes

    @property
    def type(self):
        """Gets the type of this InlineResponse20053.  # noqa: E501

        The meeting type:  * `0` &mdash; A prescheduled meeting.  * `1` &mdash; An instant meeting.  * `2` &mdash; A scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A [personal meeting room](https://support.zoom.us/hc/en-us/articles/201362843).  * `7` &mdash; A [PAC (Personal Audio Conference)](https://support.zoom.us/hc/en-us/articles/205172455-Hosting-a-Personal-Audio-Conference-PAC-meeting) meeting.  * `8` &mdash; A recurring meeting with a fixed time.  # noqa: E501

        :return: The type of this InlineResponse20053.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20053.

        The meeting type:  * `0` &mdash; A prescheduled meeting.  * `1` &mdash; An instant meeting.  * `2` &mdash; A scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A [personal meeting room](https://support.zoom.us/hc/en-us/articles/201362843).  * `7` &mdash; A [PAC (Personal Audio Conference)](https://support.zoom.us/hc/en-us/articles/205172455-Hosting-a-Personal-Audio-Conference-PAC-meeting) meeting.  * `8` &mdash; A recurring meeting with a fixed time.  # noqa: E501

        :param type: The type of this InlineResponse20053.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 7, 8]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_email(self):
        """Gets the user_email of this InlineResponse20053.  # noqa: E501

        The user's email address.  # noqa: E501

        :return: The user_email of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this InlineResponse20053.

        The user's email address.  # noqa: E501

        :param user_email: The user_email of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

    @property
    def user_name(self):
        """Gets the user_name of this InlineResponse20053.  # noqa: E501

        The user's display name.  # noqa: E501

        :return: The user_name of this InlineResponse20053.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InlineResponse20053.

        The user's display name.  # noqa: E501

        :param user_name: The user_name of this InlineResponse20053.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(InlineResponse20053, dict):
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
        if not isinstance(other, InlineResponse20053):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
