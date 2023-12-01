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

class RecordingSettings1(object):
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
        'approval_type': 'int',
        'authentication_domains': 'str',
        'authentication_option': 'str',
        'on_demand': 'bool',
        'password': 'str',
        'recording_authentication': 'bool',
        'send_email_to_host': 'bool',
        'share_recording': 'str',
        'show_social_share_buttons': 'bool',
        'topic': 'str',
        'viewer_download': 'bool'
    }

    attribute_map = {
        'approval_type': 'approval_type',
        'authentication_domains': 'authentication_domains',
        'authentication_option': 'authentication_option',
        'on_demand': 'on_demand',
        'password': 'password',
        'recording_authentication': 'recording_authentication',
        'send_email_to_host': 'send_email_to_host',
        'share_recording': 'share_recording',
        'show_social_share_buttons': 'show_social_share_buttons',
        'topic': 'topic',
        'viewer_download': 'viewer_download'
    }

    def __init__(self, approval_type=None, authentication_domains=None, authentication_option=None, on_demand=None, password=None, recording_authentication=None, send_email_to_host=None, share_recording=None, show_social_share_buttons=None, topic=None, viewer_download=None):  # noqa: E501
        """RecordingSettings1 - a model defined in Swagger"""  # noqa: E501
        self._approval_type = None
        self._authentication_domains = None
        self._authentication_option = None
        self._on_demand = None
        self._password = None
        self._recording_authentication = None
        self._send_email_to_host = None
        self._share_recording = None
        self._show_social_share_buttons = None
        self._topic = None
        self._viewer_download = None
        self.discriminator = None
        if approval_type is not None:
            self.approval_type = approval_type
        if authentication_domains is not None:
            self.authentication_domains = authentication_domains
        if authentication_option is not None:
            self.authentication_option = authentication_option
        if on_demand is not None:
            self.on_demand = on_demand
        if password is not None:
            self.password = password
        if recording_authentication is not None:
            self.recording_authentication = recording_authentication
        if send_email_to_host is not None:
            self.send_email_to_host = send_email_to_host
        if share_recording is not None:
            self.share_recording = share_recording
        if show_social_share_buttons is not None:
            self.show_social_share_buttons = show_social_share_buttons
        if topic is not None:
            self.topic = topic
        if viewer_download is not None:
            self.viewer_download = viewer_download

    @property
    def approval_type(self):
        """Gets the approval_type of this RecordingSettings1.  # noqa: E501

        The approval type for the registration.     `0`- Automatically approve the registration when a user registers.     `1` - Manually approve or deny the registration of a user.     `2` - No registration required to view the recording.  # noqa: E501

        :return: The approval_type of this RecordingSettings1.  # noqa: E501
        :rtype: int
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this RecordingSettings1.

        The approval type for the registration.     `0`- Automatically approve the registration when a user registers.     `1` - Manually approve or deny the registration of a user.     `2` - No registration required to view the recording.  # noqa: E501

        :param approval_type: The approval_type of this RecordingSettings1.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if approval_type not in allowed_values:
            raise ValueError(
                "Invalid value for `approval_type` ({0}), must be one of {1}"  # noqa: E501
                .format(approval_type, allowed_values)
            )

        self._approval_type = approval_type

    @property
    def authentication_domains(self):
        """Gets the authentication_domains of this RecordingSettings1.  # noqa: E501

        The authentication domains.  # noqa: E501

        :return: The authentication_domains of this RecordingSettings1.  # noqa: E501
        :rtype: str
        """
        return self._authentication_domains

    @authentication_domains.setter
    def authentication_domains(self, authentication_domains):
        """Sets the authentication_domains of this RecordingSettings1.

        The authentication domains.  # noqa: E501

        :param authentication_domains: The authentication_domains of this RecordingSettings1.  # noqa: E501
        :type: str
        """

        self._authentication_domains = authentication_domains

    @property
    def authentication_option(self):
        """Gets the authentication_option of this RecordingSettings1.  # noqa: E501

        The authentication options.  # noqa: E501

        :return: The authentication_option of this RecordingSettings1.  # noqa: E501
        :rtype: str
        """
        return self._authentication_option

    @authentication_option.setter
    def authentication_option(self, authentication_option):
        """Sets the authentication_option of this RecordingSettings1.

        The authentication options.  # noqa: E501

        :param authentication_option: The authentication_option of this RecordingSettings1.  # noqa: E501
        :type: str
        """

        self._authentication_option = authentication_option

    @property
    def on_demand(self):
        """Gets the on_demand of this RecordingSettings1.  # noqa: E501

        This field determines whether the registration is required to view the recording.  # noqa: E501

        :return: The on_demand of this RecordingSettings1.  # noqa: E501
        :rtype: bool
        """
        return self._on_demand

    @on_demand.setter
    def on_demand(self, on_demand):
        """Sets the on_demand of this RecordingSettings1.

        This field determines whether the registration is required to view the recording.  # noqa: E501

        :param on_demand: The on_demand of this RecordingSettings1.  # noqa: E501
        :type: bool
        """

        self._on_demand = on_demand

    @property
    def password(self):
        """Gets the password of this RecordingSettings1.  # noqa: E501

        This field enables passcode protection for the recording by setting a passcode.   The passcode must have a minimum of **eight** characters with a mix of numbers, letters and special characters.         **Note:** If the account owner or the admin has set minimum passcode strength requirements for recordings through Account Settings, the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/api-reference/zoom-api/ma#operation/accountSettings) API.  # noqa: E501

        :return: The password of this RecordingSettings1.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RecordingSettings1.

        This field enables passcode protection for the recording by setting a passcode.   The passcode must have a minimum of **eight** characters with a mix of numbers, letters and special characters.         **Note:** If the account owner or the admin has set minimum passcode strength requirements for recordings through Account Settings, the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/api-reference/zoom-api/ma#operation/accountSettings) API.  # noqa: E501

        :param password: The password of this RecordingSettings1.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def recording_authentication(self):
        """Gets the recording_authentication of this RecordingSettings1.  # noqa: E501

        This field indicates that only authenticated users can view.  # noqa: E501

        :return: The recording_authentication of this RecordingSettings1.  # noqa: E501
        :rtype: bool
        """
        return self._recording_authentication

    @recording_authentication.setter
    def recording_authentication(self, recording_authentication):
        """Sets the recording_authentication of this RecordingSettings1.

        This field indicates that only authenticated users can view.  # noqa: E501

        :param recording_authentication: The recording_authentication of this RecordingSettings1.  # noqa: E501
        :type: bool
        """

        self._recording_authentication = recording_authentication

    @property
    def send_email_to_host(self):
        """Gets the send_email_to_host of this RecordingSettings1.  # noqa: E501

        This field sends an email to host when someone registers to view the recording. This setting applies for On-demand recordings only.  # noqa: E501

        :return: The send_email_to_host of this RecordingSettings1.  # noqa: E501
        :rtype: bool
        """
        return self._send_email_to_host

    @send_email_to_host.setter
    def send_email_to_host(self, send_email_to_host):
        """Sets the send_email_to_host of this RecordingSettings1.

        This field sends an email to host when someone registers to view the recording. This setting applies for On-demand recordings only.  # noqa: E501

        :param send_email_to_host: The send_email_to_host of this RecordingSettings1.  # noqa: E501
        :type: bool
        """

        self._send_email_to_host = send_email_to_host

    @property
    def share_recording(self):
        """Gets the share_recording of this RecordingSettings1.  # noqa: E501

        This field determines how the meeting recording is shared.  # noqa: E501

        :return: The share_recording of this RecordingSettings1.  # noqa: E501
        :rtype: str
        """
        return self._share_recording

    @share_recording.setter
    def share_recording(self, share_recording):
        """Sets the share_recording of this RecordingSettings1.

        This field determines how the meeting recording is shared.  # noqa: E501

        :param share_recording: The share_recording of this RecordingSettings1.  # noqa: E501
        :type: str
        """
        allowed_values = ["publicly", "internally", "none"]  # noqa: E501
        if share_recording not in allowed_values:
            raise ValueError(
                "Invalid value for `share_recording` ({0}), must be one of {1}"  # noqa: E501
                .format(share_recording, allowed_values)
            )

        self._share_recording = share_recording

    @property
    def show_social_share_buttons(self):
        """Gets the show_social_share_buttons of this RecordingSettings1.  # noqa: E501

        This field shows social share buttons on registration page. This setting applies for On-demand recordings only.  # noqa: E501

        :return: The show_social_share_buttons of this RecordingSettings1.  # noqa: E501
        :rtype: bool
        """
        return self._show_social_share_buttons

    @show_social_share_buttons.setter
    def show_social_share_buttons(self, show_social_share_buttons):
        """Sets the show_social_share_buttons of this RecordingSettings1.

        This field shows social share buttons on registration page. This setting applies for On-demand recordings only.  # noqa: E501

        :param show_social_share_buttons: The show_social_share_buttons of this RecordingSettings1.  # noqa: E501
        :type: bool
        """

        self._show_social_share_buttons = show_social_share_buttons

    @property
    def topic(self):
        """Gets the topic of this RecordingSettings1.  # noqa: E501

        The name of the recording.  # noqa: E501

        :return: The topic of this RecordingSettings1.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this RecordingSettings1.

        The name of the recording.  # noqa: E501

        :param topic: The topic of this RecordingSettings1.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def viewer_download(self):
        """Gets the viewer_download of this RecordingSettings1.  # noqa: E501

        This field determines whether a viewer can download the recording file or not.  # noqa: E501

        :return: The viewer_download of this RecordingSettings1.  # noqa: E501
        :rtype: bool
        """
        return self._viewer_download

    @viewer_download.setter
    def viewer_download(self, viewer_download):
        """Sets the viewer_download of this RecordingSettings1.

        This field determines whether a viewer can download the recording file or not.  # noqa: E501

        :param viewer_download: The viewer_download of this RecordingSettings1.  # noqa: E501
        :type: bool
        """

        self._viewer_download = viewer_download

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
        if issubclass(RecordingSettings1, dict):
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
        if not isinstance(other, RecordingSettings1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other