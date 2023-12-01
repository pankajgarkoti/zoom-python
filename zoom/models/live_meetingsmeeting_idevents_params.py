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

class LiveMeetingsmeetingIdeventsParams(object):
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
        'contacts': 'list[LiveMeetingsmeetingIdeventsParamsContacts]',
        'invitee_name': 'str',
        'phone_number': 'str',
        'invite_options': 'LiveMeetingsmeetingIdeventsParamsInviteOptions',
        'call_type': 'str',
        'device_ip': 'str',
        'h323_headers': 'LiveMeetingsmeetingIdeventsParamsH323Headers',
        'sip_headers': 'LiveMeetingsmeetingIdeventsParamsSipHeaders'
    }

    attribute_map = {
        'contacts': 'contacts',
        'invitee_name': 'invitee_name',
        'phone_number': 'phone_number',
        'invite_options': 'invite_options',
        'call_type': 'call_type',
        'device_ip': 'device_ip',
        'h323_headers': 'h323_headers',
        'sip_headers': 'sip_headers'
    }

    def __init__(self, contacts=None, invitee_name=None, phone_number=None, invite_options=None, call_type=None, device_ip=None, h323_headers=None, sip_headers=None):  # noqa: E501
        """LiveMeetingsmeetingIdeventsParams - a model defined in Swagger"""  # noqa: E501
        self._contacts = None
        self._invitee_name = None
        self._phone_number = None
        self._invite_options = None
        self._call_type = None
        self._device_ip = None
        self._h323_headers = None
        self._sip_headers = None
        self.discriminator = None
        if contacts is not None:
            self.contacts = contacts
        if invitee_name is not None:
            self.invitee_name = invitee_name
        if phone_number is not None:
            self.phone_number = phone_number
        if invite_options is not None:
            self.invite_options = invite_options
        if call_type is not None:
            self.call_type = call_type
        if device_ip is not None:
            self.device_ip = device_ip
        if h323_headers is not None:
            self.h323_headers = h323_headers
        if sip_headers is not None:
            self.sip_headers = sip_headers

    @property
    def contacts(self):
        """Gets the contacts of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501

        The user's email address or the user ID, up to a maximum of 10 contacts. The account must be a part of the meeting host's account.  # noqa: E501

        :return: The contacts of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: list[LiveMeetingsmeetingIdeventsParamsContacts]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this LiveMeetingsmeetingIdeventsParams.

        The user's email address or the user ID, up to a maximum of 10 contacts. The account must be a part of the meeting host's account.  # noqa: E501

        :param contacts: The contacts of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: list[LiveMeetingsmeetingIdeventsParamsContacts]
        """

        self._contacts = contacts

    @property
    def invitee_name(self):
        """Gets the invitee_name of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501

        The user's name to display in the meeting. Use this field if you pass the `participant.invite.callout` value for the `method` field.  # noqa: E501

        :return: The invitee_name of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: str
        """
        return self._invitee_name

    @invitee_name.setter
    def invitee_name(self, invitee_name):
        """Sets the invitee_name of this LiveMeetingsmeetingIdeventsParams.

        The user's name to display in the meeting. Use this field if you pass the `participant.invite.callout` value for the `method` field.  # noqa: E501

        :param invitee_name: The invitee_name of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: str
        """

        self._invitee_name = invitee_name

    @property
    def phone_number(self):
        """Gets the phone_number of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501

        The user's phone number. Use this field if you pass the `participant.invite.callout` value for the `method` field. As a best practice, ensure this includes a country code and area code.  # noqa: E501

        :return: The phone_number of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this LiveMeetingsmeetingIdeventsParams.

        The user's phone number. Use this field if you pass the `participant.invite.callout` value for the `method` field. As a best practice, ensure this includes a country code and area code.  # noqa: E501

        :param phone_number: The phone_number of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def invite_options(self):
        """Gets the invite_options of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501


        :return: The invite_options of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: LiveMeetingsmeetingIdeventsParamsInviteOptions
        """
        return self._invite_options

    @invite_options.setter
    def invite_options(self, invite_options):
        """Sets the invite_options of this LiveMeetingsmeetingIdeventsParams.


        :param invite_options: The invite_options of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: LiveMeetingsmeetingIdeventsParamsInviteOptions
        """

        self._invite_options = invite_options

    @property
    def call_type(self):
        """Gets the call_type of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501

        The type of call out. Use a value of `h323` or `sip`. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.  # noqa: E501

        :return: The call_type of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: str
        """
        return self._call_type

    @call_type.setter
    def call_type(self, call_type):
        """Sets the call_type of this LiveMeetingsmeetingIdeventsParams.

        The type of call out. Use a value of `h323` or `sip`. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.  # noqa: E501

        :param call_type: The call_type of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: str
        """

        self._call_type = call_type

    @property
    def device_ip(self):
        """Gets the device_ip of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501

        The user's device IP address or URI. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.  # noqa: E501

        :return: The device_ip of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: str
        """
        return self._device_ip

    @device_ip.setter
    def device_ip(self, device_ip):
        """Sets the device_ip of this LiveMeetingsmeetingIdeventsParams.

        The user's device IP address or URI. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.  # noqa: E501

        :param device_ip: The device_ip of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: str
        """

        self._device_ip = device_ip

    @property
    def h323_headers(self):
        """Gets the h323_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501


        :return: The h323_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: LiveMeetingsmeetingIdeventsParamsH323Headers
        """
        return self._h323_headers

    @h323_headers.setter
    def h323_headers(self, h323_headers):
        """Sets the h323_headers of this LiveMeetingsmeetingIdeventsParams.


        :param h323_headers: The h323_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: LiveMeetingsmeetingIdeventsParamsH323Headers
        """

        self._h323_headers = h323_headers

    @property
    def sip_headers(self):
        """Gets the sip_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501


        :return: The sip_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :rtype: LiveMeetingsmeetingIdeventsParamsSipHeaders
        """
        return self._sip_headers

    @sip_headers.setter
    def sip_headers(self, sip_headers):
        """Sets the sip_headers of this LiveMeetingsmeetingIdeventsParams.


        :param sip_headers: The sip_headers of this LiveMeetingsmeetingIdeventsParams.  # noqa: E501
        :type: LiveMeetingsmeetingIdeventsParamsSipHeaders
        """

        self._sip_headers = sip_headers

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
        if issubclass(LiveMeetingsmeetingIdeventsParams, dict):
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
        if not isinstance(other, LiveMeetingsmeetingIdeventsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other