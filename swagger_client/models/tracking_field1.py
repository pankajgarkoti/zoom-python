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

class TrackingField1(object):
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
        'id': 'str',
        'field': 'str',
        'recommended_values': 'list[str]',
        'required': 'bool',
        'visible': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'field': 'field',
        'recommended_values': 'recommended_values',
        'required': 'required',
        'visible': 'visible'
    }

    def __init__(self, id=None, field=None, recommended_values=None, required=None, visible=None):  # noqa: E501
        """TrackingField1 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._field = None
        self._recommended_values = None
        self._required = None
        self._visible = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if field is not None:
            self.field = field
        if recommended_values is not None:
            self.recommended_values = recommended_values
        if required is not None:
            self.required = required
        if visible is not None:
            self.visible = visible

    @property
    def id(self):
        """Gets the id of this TrackingField1.  # noqa: E501

        Tracking Field ID  # noqa: E501

        :return: The id of this TrackingField1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackingField1.

        Tracking Field ID  # noqa: E501

        :param id: The id of this TrackingField1.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def field(self):
        """Gets the field of this TrackingField1.  # noqa: E501

        Label/ Name for the tracking field.  # noqa: E501

        :return: The field of this TrackingField1.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this TrackingField1.

        Label/ Name for the tracking field.  # noqa: E501

        :param field: The field of this TrackingField1.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def recommended_values(self):
        """Gets the recommended_values of this TrackingField1.  # noqa: E501

        Array of recommended values  # noqa: E501

        :return: The recommended_values of this TrackingField1.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_values

    @recommended_values.setter
    def recommended_values(self, recommended_values):
        """Sets the recommended_values of this TrackingField1.

        Array of recommended values  # noqa: E501

        :param recommended_values: The recommended_values of this TrackingField1.  # noqa: E501
        :type: list[str]
        """

        self._recommended_values = recommended_values

    @property
    def required(self):
        """Gets the required of this TrackingField1.  # noqa: E501

        Tracking Field Required  # noqa: E501

        :return: The required of this TrackingField1.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this TrackingField1.

        Tracking Field Required  # noqa: E501

        :param required: The required of this TrackingField1.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def visible(self):
        """Gets the visible of this TrackingField1.  # noqa: E501

        Tracking Field Visible  # noqa: E501

        :return: The visible of this TrackingField1.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this TrackingField1.

        Tracking Field Visible  # noqa: E501

        :param visible: The visible of this TrackingField1.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if issubclass(TrackingField1, dict):
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
        if not isinstance(other, TrackingField1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
