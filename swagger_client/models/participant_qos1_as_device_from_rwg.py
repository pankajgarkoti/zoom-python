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

class ParticipantQOS1AsDeviceFromRwg(object):
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
        'avg_loss': 'str',
        'bitrate': 'str',
        'jitter': 'str',
        'latency': 'str',
        'max_loss': 'str',
        'frame_rate': 'str',
        'resolution': 'str'
    }

    attribute_map = {
        'avg_loss': 'avg_loss',
        'bitrate': 'bitrate',
        'jitter': 'jitter',
        'latency': 'latency',
        'max_loss': 'max_loss',
        'frame_rate': 'frame_rate',
        'resolution': 'resolution'
    }

    def __init__(self, avg_loss=None, bitrate=None, jitter=None, latency=None, max_loss=None, frame_rate=None, resolution=None):  # noqa: E501
        """ParticipantQOS1AsDeviceFromRwg - a model defined in Swagger"""  # noqa: E501
        self._avg_loss = None
        self._bitrate = None
        self._jitter = None
        self._latency = None
        self._max_loss = None
        self._frame_rate = None
        self._resolution = None
        self.discriminator = None
        if avg_loss is not None:
            self.avg_loss = avg_loss
        if bitrate is not None:
            self.bitrate = bitrate
        if jitter is not None:
            self.jitter = jitter
        if latency is not None:
            self.latency = latency
        if max_loss is not None:
            self.max_loss = max_loss
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if resolution is not None:
            self.resolution = resolution

    @property
    def avg_loss(self):
        """Gets the avg_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The average amount of packet loss, such as the percentage of packets that failed to arrive at their destination.  # noqa: E501

        :return: The avg_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._avg_loss

    @avg_loss.setter
    def avg_loss(self, avg_loss):
        """Sets the avg_loss of this ParticipantQOS1AsDeviceFromRwg.

        The average amount of packet loss, such as the percentage of packets that failed to arrive at their destination.  # noqa: E501

        :param avg_loss: The avg_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._avg_loss = avg_loss

    @property
    def bitrate(self):
        """Gets the bitrate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The bits per second transmitted along a digital network, in kbps.  # noqa: E501

        :return: The bitrate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this ParticipantQOS1AsDeviceFromRwg.

        The bits per second transmitted along a digital network, in kbps.  # noqa: E501

        :param bitrate: The bitrate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._bitrate = bitrate

    @property
    def jitter(self):
        """Gets the jitter of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The variation in the delay of received packets, in milliseconds.  # noqa: E501

        :return: The jitter of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this ParticipantQOS1AsDeviceFromRwg.

        The variation in the delay of received packets, in milliseconds.  # noqa: E501

        :param jitter: The jitter of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._jitter = jitter

    @property
    def latency(self):
        """Gets the latency of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The time it took a packet to travel from one point to another, in milliseconds.  # noqa: E501

        :return: The latency of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this ParticipantQOS1AsDeviceFromRwg.

        The time it took a packet to travel from one point to another, in milliseconds.  # noqa: E501

        :param latency: The latency of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._latency = latency

    @property
    def max_loss(self):
        """Gets the max_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The maximum amount of packet loss, such as the maximum percentage of packets that failed to arrive at their destination.  # noqa: E501

        :return: The max_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._max_loss

    @max_loss.setter
    def max_loss(self, max_loss):
        """Sets the max_loss of this ParticipantQOS1AsDeviceFromRwg.

        The maximum amount of packet loss, such as the maximum percentage of packets that failed to arrive at their destination.  # noqa: E501

        :param max_loss: The max_loss of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._max_loss = max_loss

    @property
    def frame_rate(self):
        """Gets the frame_rate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The rate where the video camera can produce unique images (frames). Zoom supports a frame rate of up to 30 fps.  # noqa: E501

        :return: The frame_rate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this ParticipantQOS1AsDeviceFromRwg.

        The rate where the video camera can produce unique images (frames). Zoom supports a frame rate of up to 30 fps.  # noqa: E501

        :param frame_rate: The frame_rate of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._frame_rate = frame_rate

    @property
    def resolution(self):
        """Gets the resolution of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501

        The number of pixels in each dimension that the video camera can display.  # noqa: E501

        :return: The resolution of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ParticipantQOS1AsDeviceFromRwg.

        The number of pixels in each dimension that the video camera can display.  # noqa: E501

        :param resolution: The resolution of this ParticipantQOS1AsDeviceFromRwg.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

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
        if issubclass(ParticipantQOS1AsDeviceFromRwg, dict):
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
        if not isinstance(other, ParticipantQOS1AsDeviceFromRwg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
