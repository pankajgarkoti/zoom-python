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

class WebinarIdLivestreamBody(object):
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
        'page_url': 'str',
        'stream_key': 'str',
        'stream_url': 'str',
        'resolution': 'str'
    }

    attribute_map = {
        'page_url': 'page_url',
        'stream_key': 'stream_key',
        'stream_url': 'stream_url',
        'resolution': 'resolution'
    }

    def __init__(self, page_url=None, stream_key=None, stream_url=None, resolution=None):  # noqa: E501
        """WebinarIdLivestreamBody - a model defined in Swagger"""  # noqa: E501
        self._page_url = None
        self._stream_key = None
        self._stream_url = None
        self._resolution = None
        self.discriminator = None
        self.page_url = page_url
        self.stream_key = stream_key
        self.stream_url = stream_url
        if resolution is not None:
            self.resolution = resolution

    @property
    def page_url(self):
        """Gets the page_url of this WebinarIdLivestreamBody.  # noqa: E501

        The webinar live stream page's URL.  # noqa: E501

        :return: The page_url of this WebinarIdLivestreamBody.  # noqa: E501
        :rtype: str
        """
        return self._page_url

    @page_url.setter
    def page_url(self, page_url):
        """Sets the page_url of this WebinarIdLivestreamBody.

        The webinar live stream page's URL.  # noqa: E501

        :param page_url: The page_url of this WebinarIdLivestreamBody.  # noqa: E501
        :type: str
        """
        if page_url is None:
            raise ValueError("Invalid value for `page_url`, must not be `None`")  # noqa: E501

        self._page_url = page_url

    @property
    def stream_key(self):
        """Gets the stream_key of this WebinarIdLivestreamBody.  # noqa: E501

        The webinar live stream name and key.  # noqa: E501

        :return: The stream_key of this WebinarIdLivestreamBody.  # noqa: E501
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this WebinarIdLivestreamBody.

        The webinar live stream name and key.  # noqa: E501

        :param stream_key: The stream_key of this WebinarIdLivestreamBody.  # noqa: E501
        :type: str
        """
        if stream_key is None:
            raise ValueError("Invalid value for `stream_key`, must not be `None`")  # noqa: E501

        self._stream_key = stream_key

    @property
    def stream_url(self):
        """Gets the stream_url of this WebinarIdLivestreamBody.  # noqa: E501

        The webinar live stream URL.  # noqa: E501

        :return: The stream_url of this WebinarIdLivestreamBody.  # noqa: E501
        :rtype: str
        """
        return self._stream_url

    @stream_url.setter
    def stream_url(self, stream_url):
        """Sets the stream_url of this WebinarIdLivestreamBody.

        The webinar live stream URL.  # noqa: E501

        :param stream_url: The stream_url of this WebinarIdLivestreamBody.  # noqa: E501
        :type: str
        """
        if stream_url is None:
            raise ValueError("Invalid value for `stream_url`, must not be `None`")  # noqa: E501

        self._stream_url = stream_url

    @property
    def resolution(self):
        """Gets the resolution of this WebinarIdLivestreamBody.  # noqa: E501

        The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`  # noqa: E501

        :return: The resolution of this WebinarIdLivestreamBody.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this WebinarIdLivestreamBody.

        The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`  # noqa: E501

        :param resolution: The resolution of this WebinarIdLivestreamBody.  # noqa: E501
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
        if issubclass(WebinarIdLivestreamBody, dict):
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
        if not isinstance(other, WebinarIdLivestreamBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
