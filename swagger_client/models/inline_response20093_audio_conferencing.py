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

class InlineResponse20093AudioConferencing(object):
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
        'toll_free_and_fee_based_toll_call': 'InlineResponse20093AudioConferencingTollFreeAndFeeBasedTollCall'
    }

    attribute_map = {
        'toll_free_and_fee_based_toll_call': 'toll_free_and_fee_based_toll_call'
    }

    def __init__(self, toll_free_and_fee_based_toll_call=None):  # noqa: E501
        """InlineResponse20093AudioConferencing - a model defined in Swagger"""  # noqa: E501
        self._toll_free_and_fee_based_toll_call = None
        self.discriminator = None
        if toll_free_and_fee_based_toll_call is not None:
            self.toll_free_and_fee_based_toll_call = toll_free_and_fee_based_toll_call

    @property
    def toll_free_and_fee_based_toll_call(self):
        """Gets the toll_free_and_fee_based_toll_call of this InlineResponse20093AudioConferencing.  # noqa: E501


        :return: The toll_free_and_fee_based_toll_call of this InlineResponse20093AudioConferencing.  # noqa: E501
        :rtype: InlineResponse20093AudioConferencingTollFreeAndFeeBasedTollCall
        """
        return self._toll_free_and_fee_based_toll_call

    @toll_free_and_fee_based_toll_call.setter
    def toll_free_and_fee_based_toll_call(self, toll_free_and_fee_based_toll_call):
        """Sets the toll_free_and_fee_based_toll_call of this InlineResponse20093AudioConferencing.


        :param toll_free_and_fee_based_toll_call: The toll_free_and_fee_based_toll_call of this InlineResponse20093AudioConferencing.  # noqa: E501
        :type: InlineResponse20093AudioConferencingTollFreeAndFeeBasedTollCall
        """

        self._toll_free_and_fee_based_toll_call = toll_free_and_fee_based_toll_call

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
        if issubclass(InlineResponse20093AudioConferencing, dict):
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
        if not isinstance(other, InlineResponse20093AudioConferencing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
