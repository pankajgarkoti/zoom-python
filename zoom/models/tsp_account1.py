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

class TSPAccount1(object):
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
        'conference_code': 'str',
        'dial_in_numbers': 'list[UsersuserIdtsptspIdDialInNumbers]',
        'leader_pin': 'str',
        'tsp_bridge': 'str'
    }

    attribute_map = {
        'conference_code': 'conference_code',
        'dial_in_numbers': 'dial_in_numbers',
        'leader_pin': 'leader_pin',
        'tsp_bridge': 'tsp_bridge'
    }

    def __init__(self, conference_code=None, dial_in_numbers=None, leader_pin=None, tsp_bridge=None):  # noqa: E501
        """TSPAccount1 - a model defined in Swagger"""  # noqa: E501
        self._conference_code = None
        self._dial_in_numbers = None
        self._leader_pin = None
        self._tsp_bridge = None
        self.discriminator = None
        self.conference_code = conference_code
        if dial_in_numbers is not None:
            self.dial_in_numbers = dial_in_numbers
        self.leader_pin = leader_pin
        if tsp_bridge is not None:
            self.tsp_bridge = tsp_bridge

    @property
    def conference_code(self):
        """Gets the conference_code of this TSPAccount1.  # noqa: E501

        Conference code: numeric value, length is less than 16.  # noqa: E501

        :return: The conference_code of this TSPAccount1.  # noqa: E501
        :rtype: str
        """
        return self._conference_code

    @conference_code.setter
    def conference_code(self, conference_code):
        """Sets the conference_code of this TSPAccount1.

        Conference code: numeric value, length is less than 16.  # noqa: E501

        :param conference_code: The conference_code of this TSPAccount1.  # noqa: E501
        :type: str
        """
        if conference_code is None:
            raise ValueError("Invalid value for `conference_code`, must not be `None`")  # noqa: E501

        self._conference_code = conference_code

    @property
    def dial_in_numbers(self):
        """Gets the dial_in_numbers of this TSPAccount1.  # noqa: E501

        List of dial in numbers.  # noqa: E501

        :return: The dial_in_numbers of this TSPAccount1.  # noqa: E501
        :rtype: list[UsersuserIdtsptspIdDialInNumbers]
        """
        return self._dial_in_numbers

    @dial_in_numbers.setter
    def dial_in_numbers(self, dial_in_numbers):
        """Sets the dial_in_numbers of this TSPAccount1.

        List of dial in numbers.  # noqa: E501

        :param dial_in_numbers: The dial_in_numbers of this TSPAccount1.  # noqa: E501
        :type: list[UsersuserIdtsptspIdDialInNumbers]
        """

        self._dial_in_numbers = dial_in_numbers

    @property
    def leader_pin(self):
        """Gets the leader_pin of this TSPAccount1.  # noqa: E501

        Leader PIN: numeric value, length is less than 16.  # noqa: E501

        :return: The leader_pin of this TSPAccount1.  # noqa: E501
        :rtype: str
        """
        return self._leader_pin

    @leader_pin.setter
    def leader_pin(self, leader_pin):
        """Sets the leader_pin of this TSPAccount1.

        Leader PIN: numeric value, length is less than 16.  # noqa: E501

        :param leader_pin: The leader_pin of this TSPAccount1.  # noqa: E501
        :type: str
        """
        if leader_pin is None:
            raise ValueError("Invalid value for `leader_pin`, must not be `None`")  # noqa: E501

        self._leader_pin = leader_pin

    @property
    def tsp_bridge(self):
        """Gets the tsp_bridge of this TSPAccount1.  # noqa: E501

        Telephony bridge  # noqa: E501

        :return: The tsp_bridge of this TSPAccount1.  # noqa: E501
        :rtype: str
        """
        return self._tsp_bridge

    @tsp_bridge.setter
    def tsp_bridge(self, tsp_bridge):
        """Sets the tsp_bridge of this TSPAccount1.

        Telephony bridge  # noqa: E501

        :param tsp_bridge: The tsp_bridge of this TSPAccount1.  # noqa: E501
        :type: str
        """
        allowed_values = ["US_TSP_TB", "EU_TSP_TB"]  # noqa: E501
        if tsp_bridge not in allowed_values:
            raise ValueError(
                "Invalid value for `tsp_bridge` ({0}), must be one of {1}"  # noqa: E501
                .format(tsp_bridge, allowed_values)
            )

        self._tsp_bridge = tsp_bridge

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
        if issubclass(TSPAccount1, dict):
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
        if not isinstance(other, TSPAccount1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
