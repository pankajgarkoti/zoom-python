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

class TSPAccountDialInNumbers(object):
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
        'code': 'str',
        'country_label': 'str',
        'number': 'str',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'country_label': 'country_label',
        'number': 'number',
        'type': 'type'
    }

    def __init__(self, code=None, country_label=None, number=None, type=None):  # noqa: E501
        """TSPAccountDialInNumbers - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._country_label = None
        self._number = None
        self._type = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if country_label is not None:
            self.country_label = country_label
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type

    @property
    def code(self):
        """Gets the code of this TSPAccountDialInNumbers.  # noqa: E501

        Country code.  # noqa: E501

        :return: The code of this TSPAccountDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TSPAccountDialInNumbers.

        Country code.  # noqa: E501

        :param code: The code of this TSPAccountDialInNumbers.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def country_label(self):
        """Gets the country_label of this TSPAccountDialInNumbers.  # noqa: E501

        Country Label, if passed, will display in place of code.  # noqa: E501

        :return: The country_label of this TSPAccountDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._country_label

    @country_label.setter
    def country_label(self, country_label):
        """Sets the country_label of this TSPAccountDialInNumbers.

        Country Label, if passed, will display in place of code.  # noqa: E501

        :param country_label: The country_label of this TSPAccountDialInNumbers.  # noqa: E501
        :type: str
        """

        self._country_label = country_label

    @property
    def number(self):
        """Gets the number of this TSPAccountDialInNumbers.  # noqa: E501

        Dial-in number: length is less than 16.  # noqa: E501

        :return: The number of this TSPAccountDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TSPAccountDialInNumbers.

        Dial-in number: length is less than 16.  # noqa: E501

        :param number: The number of this TSPAccountDialInNumbers.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def type(self):
        """Gets the type of this TSPAccountDialInNumbers.  # noqa: E501

        Dial-in number types:    `toll` - Toll number.    `tollfree` -Toll free number.      `media_link` - Media link phone number. This is used for PSTN integration instead of a paid bridge number.  # noqa: E501

        :return: The type of this TSPAccountDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TSPAccountDialInNumbers.

        Dial-in number types:    `toll` - Toll number.    `tollfree` -Toll free number.      `media_link` - Media link phone number. This is used for PSTN integration instead of a paid bridge number.  # noqa: E501

        :param type: The type of this TSPAccountDialInNumbers.  # noqa: E501
        :type: str
        """
        allowed_values = ["toll", "tollfree", "media_link"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(TSPAccountDialInNumbers, dict):
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
        if not isinstance(other, TSPAccountDialInNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
