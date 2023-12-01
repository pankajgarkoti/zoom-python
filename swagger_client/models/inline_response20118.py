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

class InlineResponse20118(object):
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
        'success_user_ids': 'list[str]',
        'fail_details': 'list[InlineResponse20118FailDetails]'
    }

    attribute_map = {
        'success_user_ids': 'success_user_ids',
        'fail_details': 'fail_details'
    }

    def __init__(self, success_user_ids=None, fail_details=None):  # noqa: E501
        """InlineResponse20118 - a model defined in Swagger"""  # noqa: E501
        self._success_user_ids = None
        self._fail_details = None
        self.discriminator = None
        if success_user_ids is not None:
            self.success_user_ids = success_user_ids
        if fail_details is not None:
            self.fail_details = fail_details

    @property
    def success_user_ids(self):
        """Gets the success_user_ids of this InlineResponse20118.  # noqa: E501

        The IDs of users for whom the feature was updated successfully  # noqa: E501

        :return: The success_user_ids of this InlineResponse20118.  # noqa: E501
        :rtype: list[str]
        """
        return self._success_user_ids

    @success_user_ids.setter
    def success_user_ids(self, success_user_ids):
        """Sets the success_user_ids of this InlineResponse20118.

        The IDs of users for whom the feature was updated successfully  # noqa: E501

        :param success_user_ids: The success_user_ids of this InlineResponse20118.  # noqa: E501
        :type: list[str]
        """

        self._success_user_ids = success_user_ids

    @property
    def fail_details(self):
        """Gets the fail_details of this InlineResponse20118.  # noqa: E501

        The details why these users' feature was not updated successfully.  # noqa: E501

        :return: The fail_details of this InlineResponse20118.  # noqa: E501
        :rtype: list[InlineResponse20118FailDetails]
        """
        return self._fail_details

    @fail_details.setter
    def fail_details(self, fail_details):
        """Sets the fail_details of this InlineResponse20118.

        The details why these users' feature was not updated successfully.  # noqa: E501

        :param fail_details: The fail_details of this InlineResponse20118.  # noqa: E501
        :type: list[InlineResponse20118FailDetails]
        """

        self._fail_details = fail_details

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
        if issubclass(InlineResponse20118, dict):
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
        if not isinstance(other, InlineResponse20118):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
