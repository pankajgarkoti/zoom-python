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

class DeviceIdAssignmentBody(object):
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
        'room_id': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'app_type': 'app_type'
    }

    def __init__(self, room_id=None, app_type='ZR'):  # noqa: E501
        """DeviceIdAssignmentBody - a model defined in Swagger"""  # noqa: E501
        self._room_id = None
        self._app_type = None
        self.discriminator = None
        if room_id is not None:
            self.room_id = room_id
        if app_type is not None:
            self.app_type = app_type

    @property
    def room_id(self):
        """Gets the room_id of this DeviceIdAssignmentBody.  # noqa: E501

        The Zoom Room ID which device is being associated to. The `room_id` is required when `assign` is selected for `action` field.  # noqa: E501

        :return: The room_id of this DeviceIdAssignmentBody.  # noqa: E501
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this DeviceIdAssignmentBody.

        The Zoom Room ID which device is being associated to. The `room_id` is required when `assign` is selected for `action` field.  # noqa: E501

        :param room_id: The room_id of this DeviceIdAssignmentBody.  # noqa: E501
        :type: str
        """

        self._room_id = room_id

    @property
    def app_type(self):
        """Gets the app_type of this DeviceIdAssignmentBody.  # noqa: E501

        Specify one of the following values for this field:  `ZR`: Zoom Room Computer.     `ZRC`: Zoom Room Controller.     `ZRP`: Scheduling Display.     `ZRW`: Companion Whiteboard.  # noqa: E501

        :return: The app_type of this DeviceIdAssignmentBody.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this DeviceIdAssignmentBody.

        Specify one of the following values for this field:  `ZR`: Zoom Room Computer.     `ZRC`: Zoom Room Controller.     `ZRP`: Scheduling Display.     `ZRW`: Companion Whiteboard.  # noqa: E501

        :param app_type: The app_type of this DeviceIdAssignmentBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["ZR", "ZRC", "ZRP", "ZRW"]  # noqa: E501
        if app_type not in allowed_values:
            raise ValueError(
                "Invalid value for `app_type` ({0}), must be one of {1}"  # noqa: E501
                .format(app_type, allowed_values)
            )

        self._app_type = app_type

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
        if issubclass(DeviceIdAssignmentBody, dict):
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
        if not isinstance(other, DeviceIdAssignmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
