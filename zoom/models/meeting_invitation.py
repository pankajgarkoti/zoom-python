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

class MeetingInvitation(object):
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
        'invitation': 'str',
        'sip_links': 'list[str]'
    }

    attribute_map = {
        'invitation': 'invitation',
        'sip_links': 'sip_links'
    }

    def __init__(self, invitation=None, sip_links=None):  # noqa: E501
        """MeetingInvitation - a model defined in Swagger"""  # noqa: E501
        self._invitation = None
        self._sip_links = None
        self.discriminator = None
        if invitation is not None:
            self.invitation = invitation
        if sip_links is not None:
            self.sip_links = sip_links

    @property
    def invitation(self):
        """Gets the invitation of this MeetingInvitation.  # noqa: E501

        Meeting invitation.  # noqa: E501

        :return: The invitation of this MeetingInvitation.  # noqa: E501
        :rtype: str
        """
        return self._invitation

    @invitation.setter
    def invitation(self, invitation):
        """Sets the invitation of this MeetingInvitation.

        Meeting invitation.  # noqa: E501

        :param invitation: The invitation of this MeetingInvitation.  # noqa: E501
        :type: str
        """

        self._invitation = invitation

    @property
    def sip_links(self):
        """Gets the sip_links of this MeetingInvitation.  # noqa: E501

        A list of SIP phone addresses.  # noqa: E501

        :return: The sip_links of this MeetingInvitation.  # noqa: E501
        :rtype: list[str]
        """
        return self._sip_links

    @sip_links.setter
    def sip_links(self, sip_links):
        """Sets the sip_links of this MeetingInvitation.

        A list of SIP phone addresses.  # noqa: E501

        :param sip_links: The sip_links of this MeetingInvitation.  # noqa: E501
        :type: list[str]
        """

        self._sip_links = sip_links

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
        if issubclass(MeetingInvitation, dict):
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
        if not isinstance(other, MeetingInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
