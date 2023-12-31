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

class UserIdPresenceStatusBody(object):
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
        'duration': 'int',
        'status': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'status': 'status'
    }

    def __init__(self, duration=None, status=None):  # noqa: E501
        """UserIdPresenceStatusBody - a model defined in Swagger"""  # noqa: E501
        self._duration = None
        self._status = None
        self.discriminator = None
        if duration is not None:
            self.duration = duration
        if status is not None:
            self.status = status

    @property
    def duration(self):
        """Gets the duration of this UserIdPresenceStatusBody.  # noqa: E501

        If updating the user's status to `Do_Not_Disturb`, the duration that the status should remain as `Do_Not_Disturb`, in minutes.  # noqa: E501

        :return: The duration of this UserIdPresenceStatusBody.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UserIdPresenceStatusBody.

        If updating the user's status to `Do_Not_Disturb`, the duration that the status should remain as `Do_Not_Disturb`, in minutes.  # noqa: E501

        :param duration: The duration of this UserIdPresenceStatusBody.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def status(self):
        """Gets the status of this UserIdPresenceStatusBody.  # noqa: E501

        The user's presence status.  * `Away`  * `Do_Not_Disturb`  * `Available`  * `In_Calendar_Event`  * `Presenting`  * `In_A_Zoom_Meeting`  * `On_A_Call`  * `Out_of_Office` * `Busy`  Users who are on Zoom Client with a version **lower than 5.3.0** can update the status from:  * `Away` to `Do_Not_Disturb`  * `Available` to `Do_Not_Disturb`   Users who are on **Zoom Client 5.3.0 or higher** can update the status from:  * `Do_Not_Disturb` to `Away` * `Do_Not_Disturb` to `Available`  * `Available` to `Away`  * `Away` to `Available`  # noqa: E501

        :return: The status of this UserIdPresenceStatusBody.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserIdPresenceStatusBody.

        The user's presence status.  * `Away`  * `Do_Not_Disturb`  * `Available`  * `In_Calendar_Event`  * `Presenting`  * `In_A_Zoom_Meeting`  * `On_A_Call`  * `Out_of_Office` * `Busy`  Users who are on Zoom Client with a version **lower than 5.3.0** can update the status from:  * `Away` to `Do_Not_Disturb`  * `Available` to `Do_Not_Disturb`   Users who are on **Zoom Client 5.3.0 or higher** can update the status from:  * `Do_Not_Disturb` to `Away` * `Do_Not_Disturb` to `Available`  * `Available` to `Away`  * `Away` to `Available`  # noqa: E501

        :param status: The status of this UserIdPresenceStatusBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["Do_No_Disturb", "Away", "Available", "In_Calendar_Event", "Presenting", "In_A_Zoom_Meeting", "On_A_Call", "Out_of_Office", "Busy"]  # noqa: E501
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
        if issubclass(UserIdPresenceStatusBody, dict):
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
        if not isinstance(other, UserIdPresenceStatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
