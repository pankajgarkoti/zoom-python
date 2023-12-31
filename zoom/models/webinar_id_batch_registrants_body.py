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

class WebinarIdBatchRegistrantsBody(object):
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
        'auto_approve': 'bool',
        'registrants': 'list[WebinarswebinarIdbatchRegistrantsRegistrants]'
    }

    attribute_map = {
        'auto_approve': 'auto_approve',
        'registrants': 'registrants'
    }

    def __init__(self, auto_approve=None, registrants=None):  # noqa: E501
        """WebinarIdBatchRegistrantsBody - a model defined in Swagger"""  # noqa: E501
        self._auto_approve = None
        self._registrants = None
        self.discriminator = None
        if auto_approve is not None:
            self.auto_approve = auto_approve
        if registrants is not None:
            self.registrants = registrants

    @property
    def auto_approve(self):
        """Gets the auto_approve of this WebinarIdBatchRegistrantsBody.  # noqa: E501

        If a meeting was scheduled with approval_type `1` (manual approval), but you want to automatically approve registrants added via this API, set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting that was originally scheduled with approval_type `0` (automatic approval).  # noqa: E501

        :return: The auto_approve of this WebinarIdBatchRegistrantsBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve

    @auto_approve.setter
    def auto_approve(self, auto_approve):
        """Sets the auto_approve of this WebinarIdBatchRegistrantsBody.

        If a meeting was scheduled with approval_type `1` (manual approval), but you want to automatically approve registrants added via this API, set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting that was originally scheduled with approval_type `0` (automatic approval).  # noqa: E501

        :param auto_approve: The auto_approve of this WebinarIdBatchRegistrantsBody.  # noqa: E501
        :type: bool
        """

        self._auto_approve = auto_approve

    @property
    def registrants(self):
        """Gets the registrants of this WebinarIdBatchRegistrantsBody.  # noqa: E501


        :return: The registrants of this WebinarIdBatchRegistrantsBody.  # noqa: E501
        :rtype: list[WebinarswebinarIdbatchRegistrantsRegistrants]
        """
        return self._registrants

    @registrants.setter
    def registrants(self, registrants):
        """Sets the registrants of this WebinarIdBatchRegistrantsBody.


        :param registrants: The registrants of this WebinarIdBatchRegistrantsBody.  # noqa: E501
        :type: list[WebinarswebinarIdbatchRegistrantsRegistrants]
        """

        self._registrants = registrants

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
        if issubclass(WebinarIdBatchRegistrantsBody, dict):
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
        if not isinstance(other, WebinarIdBatchRegistrantsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
