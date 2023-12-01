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

class InlineResponse200107TrackingSources(object):
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
        'registration_count': 'int',
        'source_name': 'str',
        'tracking_url': 'str',
        'visitor_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'registration_count': 'registration_count',
        'source_name': 'source_name',
        'tracking_url': 'tracking_url',
        'visitor_count': 'visitor_count'
    }

    def __init__(self, id=None, registration_count=None, source_name=None, tracking_url=None, visitor_count=None):  # noqa: E501
        """InlineResponse200107TrackingSources - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._registration_count = None
        self._source_name = None
        self._tracking_url = None
        self._visitor_count = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if registration_count is not None:
            self.registration_count = registration_count
        if source_name is not None:
            self.source_name = source_name
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if visitor_count is not None:
            self.visitor_count = visitor_count

    @property
    def id(self):
        """Gets the id of this InlineResponse200107TrackingSources.  # noqa: E501

        Unique Identifier of the tracking source.  # noqa: E501

        :return: The id of this InlineResponse200107TrackingSources.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200107TrackingSources.

        Unique Identifier of the tracking source.  # noqa: E501

        :param id: The id of this InlineResponse200107TrackingSources.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def registration_count(self):
        """Gets the registration_count of this InlineResponse200107TrackingSources.  # noqa: E501

        Number of registrations made from this source.  # noqa: E501

        :return: The registration_count of this InlineResponse200107TrackingSources.  # noqa: E501
        :rtype: int
        """
        return self._registration_count

    @registration_count.setter
    def registration_count(self, registration_count):
        """Sets the registration_count of this InlineResponse200107TrackingSources.

        Number of registrations made from this source.  # noqa: E501

        :param registration_count: The registration_count of this InlineResponse200107TrackingSources.  # noqa: E501
        :type: int
        """

        self._registration_count = registration_count

    @property
    def source_name(self):
        """Gets the source_name of this InlineResponse200107TrackingSources.  # noqa: E501

        Name of the source (platform) where the registration URL was shared.  # noqa: E501

        :return: The source_name of this InlineResponse200107TrackingSources.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this InlineResponse200107TrackingSources.

        Name of the source (platform) where the registration URL was shared.  # noqa: E501

        :param source_name: The source_name of this InlineResponse200107TrackingSources.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def tracking_url(self):
        """Gets the tracking_url of this InlineResponse200107TrackingSources.  # noqa: E501

        Tracking URL. The URL that was shared for the registration.  # noqa: E501

        :return: The tracking_url of this InlineResponse200107TrackingSources.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this InlineResponse200107TrackingSources.

        Tracking URL. The URL that was shared for the registration.  # noqa: E501

        :param tracking_url: The tracking_url of this InlineResponse200107TrackingSources.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def visitor_count(self):
        """Gets the visitor_count of this InlineResponse200107TrackingSources.  # noqa: E501

        Number of visitors who visited the registration page from this source.  # noqa: E501

        :return: The visitor_count of this InlineResponse200107TrackingSources.  # noqa: E501
        :rtype: int
        """
        return self._visitor_count

    @visitor_count.setter
    def visitor_count(self, visitor_count):
        """Sets the visitor_count of this InlineResponse200107TrackingSources.

        Number of visitors who visited the registration page from this source.  # noqa: E501

        :param visitor_count: The visitor_count of this InlineResponse200107TrackingSources.  # noqa: E501
        :type: int
        """

        self._visitor_count = visitor_count

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
        if issubclass(InlineResponse200107TrackingSources, dict):
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
        if not isinstance(other, InlineResponse200107TrackingSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
