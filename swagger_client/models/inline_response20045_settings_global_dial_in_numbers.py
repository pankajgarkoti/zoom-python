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

class InlineResponse20045SettingsGlobalDialInNumbers(object):
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
        'city': 'str',
        'country': 'str',
        'country_name': 'str',
        'number': 'str',
        'type': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country',
        'country_name': 'country_name',
        'number': 'number',
        'type': 'type'
    }

    def __init__(self, city=None, country=None, country_name=None, number=None, type=None):  # noqa: E501
        """InlineResponse20045SettingsGlobalDialInNumbers - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._country = None
        self._country_name = None
        self._number = None
        self._type = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if country_name is not None:
            self.country_name = country_name
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type

    @property
    def city(self):
        """Gets the city of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501

        City of the number, if any. For example, Chicago.  # noqa: E501

        :return: The city of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InlineResponse20045SettingsGlobalDialInNumbers.

        City of the number, if any. For example, Chicago.  # noqa: E501

        :param city: The city of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501

        Country code. For example, BR.  # noqa: E501

        :return: The country of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse20045SettingsGlobalDialInNumbers.

        Country code. For example, BR.  # noqa: E501

        :param country: The country of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_name(self):
        """Gets the country_name of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501

        Full name of country. For example, Brazil.  # noqa: E501

        :return: The country_name of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this InlineResponse20045SettingsGlobalDialInNumbers.

        Full name of country. For example, Brazil.  # noqa: E501

        :param country_name: The country_name of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def number(self):
        """Gets the number of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501

        Phone number. For example, +1 2332357613.  # noqa: E501

        :return: The number of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse20045SettingsGlobalDialInNumbers.

        Phone number. For example, +1 2332357613.  # noqa: E501

        :param number: The number of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def type(self):
        """Gets the type of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501

        Type of number.   # noqa: E501

        :return: The type of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20045SettingsGlobalDialInNumbers.

        Type of number.   # noqa: E501

        :param type: The type of this InlineResponse20045SettingsGlobalDialInNumbers.  # noqa: E501
        :type: str
        """
        allowed_values = ["toll", "tollfree"]  # noqa: E501
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
        if issubclass(InlineResponse20045SettingsGlobalDialInNumbers, dict):
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
        if not isinstance(other, InlineResponse20045SettingsGlobalDialInNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
