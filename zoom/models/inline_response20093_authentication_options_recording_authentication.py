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

class InlineResponse20093AuthenticationOptionsRecordingAuthentication(object):
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
        'authentication_options': 'list[InlineResponse20093AuthenticationOptionsRecordingAuthenticationAuthenticationOptions]',
        'recording_authentication': 'bool'
    }

    attribute_map = {
        'authentication_options': 'authentication_options',
        'recording_authentication': 'recording_authentication'
    }

    def __init__(self, authentication_options=None, recording_authentication=None):  # noqa: E501
        """InlineResponse20093AuthenticationOptionsRecordingAuthentication - a model defined in Swagger"""  # noqa: E501
        self._authentication_options = None
        self._recording_authentication = None
        self.discriminator = None
        if authentication_options is not None:
            self.authentication_options = authentication_options
        if recording_authentication is not None:
            self.recording_authentication = recording_authentication

    @property
    def authentication_options(self):
        """Gets the authentication_options of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501

        The user's authentication options.  # noqa: E501

        :return: The authentication_options of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501
        :rtype: list[InlineResponse20093AuthenticationOptionsRecordingAuthenticationAuthenticationOptions]
        """
        return self._authentication_options

    @authentication_options.setter
    def authentication_options(self, authentication_options):
        """Sets the authentication_options of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.

        The user's authentication options.  # noqa: E501

        :param authentication_options: The authentication_options of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501
        :type: list[InlineResponse20093AuthenticationOptionsRecordingAuthenticationAuthenticationOptions]
        """

        self._authentication_options = authentication_options

    @property
    def recording_authentication(self):
        """Gets the recording_authentication of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501

        Whether only authenticated users can view cloud recordings.  # noqa: E501

        :return: The recording_authentication of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501
        :rtype: bool
        """
        return self._recording_authentication

    @recording_authentication.setter
    def recording_authentication(self, recording_authentication):
        """Sets the recording_authentication of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.

        Whether only authenticated users can view cloud recordings.  # noqa: E501

        :param recording_authentication: The recording_authentication of this InlineResponse20093AuthenticationOptionsRecordingAuthentication.  # noqa: E501
        :type: bool
        """

        self._recording_authentication = recording_authentication

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
        if issubclass(InlineResponse20093AuthenticationOptionsRecordingAuthentication, dict):
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
        if not isinstance(other, InlineResponse20093AuthenticationOptionsRecordingAuthentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
