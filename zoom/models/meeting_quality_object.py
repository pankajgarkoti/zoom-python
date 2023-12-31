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

class MeetingQualityObject(object):
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
        'bad': 'int',
        'fair': 'int',
        'good': 'int',
        'poor': 'int'
    }

    attribute_map = {
        'bad': 'bad',
        'fair': 'fair',
        'good': 'good',
        'poor': 'poor'
    }

    def __init__(self, bad=None, fair=None, good=None, poor=None):  # noqa: E501
        """MeetingQualityObject - a model defined in Swagger"""  # noqa: E501
        self._bad = None
        self._fair = None
        self._good = None
        self._poor = None
        self.discriminator = None
        if bad is not None:
            self.bad = bad
        if fair is not None:
            self.fair = fair
        if good is not None:
            self.good = good
        if poor is not None:
            self.poor = poor

    @property
    def bad(self):
        """Gets the bad of this MeetingQualityObject.  # noqa: E501

        The total number of &quot;Bad&quot; quality scores.  # noqa: E501

        :return: The bad of this MeetingQualityObject.  # noqa: E501
        :rtype: int
        """
        return self._bad

    @bad.setter
    def bad(self, bad):
        """Sets the bad of this MeetingQualityObject.

        The total number of &quot;Bad&quot; quality scores.  # noqa: E501

        :param bad: The bad of this MeetingQualityObject.  # noqa: E501
        :type: int
        """

        self._bad = bad

    @property
    def fair(self):
        """Gets the fair of this MeetingQualityObject.  # noqa: E501

        The total number of &quot;Fair&quot; quality scores.  # noqa: E501

        :return: The fair of this MeetingQualityObject.  # noqa: E501
        :rtype: int
        """
        return self._fair

    @fair.setter
    def fair(self, fair):
        """Sets the fair of this MeetingQualityObject.

        The total number of &quot;Fair&quot; quality scores.  # noqa: E501

        :param fair: The fair of this MeetingQualityObject.  # noqa: E501
        :type: int
        """

        self._fair = fair

    @property
    def good(self):
        """Gets the good of this MeetingQualityObject.  # noqa: E501

        The total number of &quot;Good&quot; quality scores.  # noqa: E501

        :return: The good of this MeetingQualityObject.  # noqa: E501
        :rtype: int
        """
        return self._good

    @good.setter
    def good(self, good):
        """Sets the good of this MeetingQualityObject.

        The total number of &quot;Good&quot; quality scores.  # noqa: E501

        :param good: The good of this MeetingQualityObject.  # noqa: E501
        :type: int
        """

        self._good = good

    @property
    def poor(self):
        """Gets the poor of this MeetingQualityObject.  # noqa: E501

        The total number of &quot;Poor&quot; quality scores.  # noqa: E501

        :return: The poor of this MeetingQualityObject.  # noqa: E501
        :rtype: int
        """
        return self._poor

    @poor.setter
    def poor(self, poor):
        """Sets the poor of this MeetingQualityObject.

        The total number of &quot;Poor&quot; quality scores.  # noqa: E501

        :param poor: The poor of this MeetingQualityObject.  # noqa: E501
        :type: int
        """

        self._poor = poor

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
        if issubclass(MeetingQualityObject, dict):
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
        if not isinstance(other, MeetingQualityObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
