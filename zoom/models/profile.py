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

class Profile(object):
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
        'recording_storage_location': 'ProfileRecordingStorageLocation'
    }

    attribute_map = {
        'recording_storage_location': 'recording_storage_location'
    }

    def __init__(self, recording_storage_location=None):  # noqa: E501
        """Profile - a model defined in Swagger"""  # noqa: E501
        self._recording_storage_location = None
        self.discriminator = None
        if recording_storage_location is not None:
            self.recording_storage_location = recording_storage_location

    @property
    def recording_storage_location(self):
        """Gets the recording_storage_location of this Profile.  # noqa: E501


        :return: The recording_storage_location of this Profile.  # noqa: E501
        :rtype: ProfileRecordingStorageLocation
        """
        return self._recording_storage_location

    @recording_storage_location.setter
    def recording_storage_location(self, recording_storage_location):
        """Sets the recording_storage_location of this Profile.


        :param recording_storage_location: The recording_storage_location of this Profile.  # noqa: E501
        :type: ProfileRecordingStorageLocation
        """

        self._recording_storage_location = recording_storage_location

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
        if issubclass(Profile, dict):
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
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
