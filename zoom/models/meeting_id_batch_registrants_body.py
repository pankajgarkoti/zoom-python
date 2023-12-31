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

class MeetingIdBatchRegistrantsBody(object):
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
        'auto_approve': 'bool',
        'registrants_confirmation_email': 'bool',
        'registrants': 'list[MeetingsmeetingIdbatchRegistrantsRegistrants]'
    }

    attribute_map = {
        'auto_approve': 'auto_approve',
        'registrants_confirmation_email': 'registrants_confirmation_email',
        'registrants': 'registrants'
    }

    def __init__(self, auto_approve=None, registrants_confirmation_email=None, registrants=None):  # noqa: E501
        """MeetingIdBatchRegistrantsBody - a model defined in Swagger"""  # noqa: E501
        self._auto_approve = None
        self._registrants_confirmation_email = None
        self._registrants = None
        self.discriminator = None
        if auto_approve is not None:
            self.auto_approve = auto_approve
        if registrants_confirmation_email is not None:
            self.registrants_confirmation_email = registrants_confirmation_email
        if registrants is not None:
            self.registrants = registrants

    @property
    def auto_approve(self):
        """Gets the auto_approve of this MeetingIdBatchRegistrantsBody.  # noqa: E501

        If a meeting was scheduled with approval_type `1` (manual approval), but you would like to automatically approve the registrants that are added via this API, you can set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting  that was originally scheduled with approval_type `0` (automatic approval).  # noqa: E501

        :return: The auto_approve of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve

    @auto_approve.setter
    def auto_approve(self, auto_approve):
        """Sets the auto_approve of this MeetingIdBatchRegistrantsBody.

        If a meeting was scheduled with approval_type `1` (manual approval), but you would like to automatically approve the registrants that are added via this API, you can set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting  that was originally scheduled with approval_type `0` (automatic approval).  # noqa: E501

        :param auto_approve: The auto_approve of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :type: bool
        """

        self._auto_approve = auto_approve

    @property
    def registrants_confirmation_email(self):
        """Gets the registrants_confirmation_email of this MeetingIdBatchRegistrantsBody.  # noqa: E501

        Send confirmation Email to Registrants  # noqa: E501

        :return: The registrants_confirmation_email of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :rtype: bool
        """
        return self._registrants_confirmation_email

    @registrants_confirmation_email.setter
    def registrants_confirmation_email(self, registrants_confirmation_email):
        """Sets the registrants_confirmation_email of this MeetingIdBatchRegistrantsBody.

        Send confirmation Email to Registrants  # noqa: E501

        :param registrants_confirmation_email: The registrants_confirmation_email of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :type: bool
        """

        self._registrants_confirmation_email = registrants_confirmation_email

    @property
    def registrants(self):
        """Gets the registrants of this MeetingIdBatchRegistrantsBody.  # noqa: E501


        :return: The registrants of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :rtype: list[MeetingsmeetingIdbatchRegistrantsRegistrants]
        """
        return self._registrants

    @registrants.setter
    def registrants(self, registrants):
        """Sets the registrants of this MeetingIdBatchRegistrantsBody.


        :param registrants: The registrants of this MeetingIdBatchRegistrantsBody.  # noqa: E501
        :type: list[MeetingsmeetingIdbatchRegistrantsRegistrants]
        """

        self._registrants = registrants

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
        if issubclass(MeetingIdBatchRegistrantsBody, dict):
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
        if not isinstance(other, MeetingIdBatchRegistrantsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
