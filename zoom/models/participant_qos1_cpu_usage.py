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

class ParticipantQOS1CpuUsage(object):
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
        'system_max_cpu_usage': 'str',
        'zoom_avg_cpu_usage': 'str',
        'zoom_max_cpu_usage': 'str',
        'zoom_min_cpu_usage': 'str'
    }

    attribute_map = {
        'system_max_cpu_usage': 'system_max_cpu_usage',
        'zoom_avg_cpu_usage': 'zoom_avg_cpu_usage',
        'zoom_max_cpu_usage': 'zoom_max_cpu_usage',
        'zoom_min_cpu_usage': 'zoom_min_cpu_usage'
    }

    def __init__(self, system_max_cpu_usage=None, zoom_avg_cpu_usage=None, zoom_max_cpu_usage=None, zoom_min_cpu_usage=None):  # noqa: E501
        """ParticipantQOS1CpuUsage - a model defined in Swagger"""  # noqa: E501
        self._system_max_cpu_usage = None
        self._zoom_avg_cpu_usage = None
        self._zoom_max_cpu_usage = None
        self._zoom_min_cpu_usage = None
        self.discriminator = None
        if system_max_cpu_usage is not None:
            self.system_max_cpu_usage = system_max_cpu_usage
        if zoom_avg_cpu_usage is not None:
            self.zoom_avg_cpu_usage = zoom_avg_cpu_usage
        if zoom_max_cpu_usage is not None:
            self.zoom_max_cpu_usage = zoom_max_cpu_usage
        if zoom_min_cpu_usage is not None:
            self.zoom_min_cpu_usage = zoom_min_cpu_usage

    @property
    def system_max_cpu_usage(self):
        """Gets the system_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501

        The system's maximum CPU usage.  # noqa: E501

        :return: The system_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :rtype: str
        """
        return self._system_max_cpu_usage

    @system_max_cpu_usage.setter
    def system_max_cpu_usage(self, system_max_cpu_usage):
        """Sets the system_max_cpu_usage of this ParticipantQOS1CpuUsage.

        The system's maximum CPU usage.  # noqa: E501

        :param system_max_cpu_usage: The system_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :type: str
        """

        self._system_max_cpu_usage = system_max_cpu_usage

    @property
    def zoom_avg_cpu_usage(self):
        """Gets the zoom_avg_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501

        Zoom's average CPU usage.  # noqa: E501

        :return: The zoom_avg_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :rtype: str
        """
        return self._zoom_avg_cpu_usage

    @zoom_avg_cpu_usage.setter
    def zoom_avg_cpu_usage(self, zoom_avg_cpu_usage):
        """Sets the zoom_avg_cpu_usage of this ParticipantQOS1CpuUsage.

        Zoom's average CPU usage.  # noqa: E501

        :param zoom_avg_cpu_usage: The zoom_avg_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :type: str
        """

        self._zoom_avg_cpu_usage = zoom_avg_cpu_usage

    @property
    def zoom_max_cpu_usage(self):
        """Gets the zoom_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501

        Zoom's maximum CPU usage.  # noqa: E501

        :return: The zoom_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :rtype: str
        """
        return self._zoom_max_cpu_usage

    @zoom_max_cpu_usage.setter
    def zoom_max_cpu_usage(self, zoom_max_cpu_usage):
        """Sets the zoom_max_cpu_usage of this ParticipantQOS1CpuUsage.

        Zoom's maximum CPU usage.  # noqa: E501

        :param zoom_max_cpu_usage: The zoom_max_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :type: str
        """

        self._zoom_max_cpu_usage = zoom_max_cpu_usage

    @property
    def zoom_min_cpu_usage(self):
        """Gets the zoom_min_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501

        Zoom's minimum CPU usage.  # noqa: E501

        :return: The zoom_min_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :rtype: str
        """
        return self._zoom_min_cpu_usage

    @zoom_min_cpu_usage.setter
    def zoom_min_cpu_usage(self, zoom_min_cpu_usage):
        """Sets the zoom_min_cpu_usage of this ParticipantQOS1CpuUsage.

        Zoom's minimum CPU usage.  # noqa: E501

        :param zoom_min_cpu_usage: The zoom_min_cpu_usage of this ParticipantQOS1CpuUsage.  # noqa: E501
        :type: str
        """

        self._zoom_min_cpu_usage = zoom_min_cpu_usage

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
        if issubclass(ParticipantQOS1CpuUsage, dict):
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
        if not isinstance(other, ParticipantQOS1CpuUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other