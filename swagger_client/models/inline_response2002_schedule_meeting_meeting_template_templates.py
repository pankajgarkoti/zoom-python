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

class InlineResponse2002ScheduleMeetingMeetingTemplateTemplates(object):
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
        'name': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enable': 'enable'
    }

    def __init__(self, id=None, name=None, enable=None):  # noqa: E501
        """InlineResponse2002ScheduleMeetingMeetingTemplateTemplates - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._enable = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable

    @property
    def id(self):
        """Gets the id of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501

        The meeting template ID.  # noqa: E501

        :return: The id of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.

        The meeting template ID.  # noqa: E501

        :param id: The id of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501

        The meeting template name.  # noqa: E501

        :return: The name of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.

        The meeting template name.  # noqa: E501

        :param name: The name of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enable(self):
        """Gets the enable of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501

        Whether to enable the meeting template. * `true` - Enable.  * `false` - Disable.  # noqa: E501

        :return: The enable of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.

        Whether to enable the meeting template. * `true` - Enable.  * `false` - Disable.  # noqa: E501

        :param enable: The enable of this InlineResponse2002ScheduleMeetingMeetingTemplateTemplates.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if issubclass(InlineResponse2002ScheduleMeetingMeetingTemplateTemplates, dict):
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
        if not isinstance(other, InlineResponse2002ScheduleMeetingMeetingTemplateTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
