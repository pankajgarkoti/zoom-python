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

class AccountsaccountIdsettingsTsp(object):
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
        'call_out': 'bool',
        'call_out_countries': 'list[str]',
        'display_toll_free_numbers': 'bool',
        'show_international_numbers_link': 'bool'
    }

    attribute_map = {
        'call_out': 'call_out',
        'call_out_countries': 'call_out_countries',
        'display_toll_free_numbers': 'display_toll_free_numbers',
        'show_international_numbers_link': 'show_international_numbers_link'
    }

    def __init__(self, call_out=None, call_out_countries=None, display_toll_free_numbers=None, show_international_numbers_link=None):  # noqa: E501
        """AccountsaccountIdsettingsTsp - a model defined in Swagger"""  # noqa: E501
        self._call_out = None
        self._call_out_countries = None
        self._display_toll_free_numbers = None
        self._show_international_numbers_link = None
        self.discriminator = None
        if call_out is not None:
            self.call_out = call_out
        if call_out_countries is not None:
            self.call_out_countries = call_out_countries
        if display_toll_free_numbers is not None:
            self.display_toll_free_numbers = display_toll_free_numbers
        if show_international_numbers_link is not None:
            self.show_international_numbers_link = show_international_numbers_link

    @property
    def call_out(self):
        """Gets the call_out of this AccountsaccountIdsettingsTsp.  # noqa: E501

        Call Out  # noqa: E501

        :return: The call_out of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :rtype: bool
        """
        return self._call_out

    @call_out.setter
    def call_out(self, call_out):
        """Sets the call_out of this AccountsaccountIdsettingsTsp.

        Call Out  # noqa: E501

        :param call_out: The call_out of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :type: bool
        """

        self._call_out = call_out

    @property
    def call_out_countries(self):
        """Gets the call_out_countries of this AccountsaccountIdsettingsTsp.  # noqa: E501

        Call Out Countries/Regions  # noqa: E501

        :return: The call_out_countries of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :rtype: list[str]
        """
        return self._call_out_countries

    @call_out_countries.setter
    def call_out_countries(self, call_out_countries):
        """Sets the call_out_countries of this AccountsaccountIdsettingsTsp.

        Call Out Countries/Regions  # noqa: E501

        :param call_out_countries: The call_out_countries of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :type: list[str]
        """

        self._call_out_countries = call_out_countries

    @property
    def display_toll_free_numbers(self):
        """Gets the display_toll_free_numbers of this AccountsaccountIdsettingsTsp.  # noqa: E501

        Display toll-free numbers  # noqa: E501

        :return: The display_toll_free_numbers of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :rtype: bool
        """
        return self._display_toll_free_numbers

    @display_toll_free_numbers.setter
    def display_toll_free_numbers(self, display_toll_free_numbers):
        """Sets the display_toll_free_numbers of this AccountsaccountIdsettingsTsp.

        Display toll-free numbers  # noqa: E501

        :param display_toll_free_numbers: The display_toll_free_numbers of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :type: bool
        """

        self._display_toll_free_numbers = display_toll_free_numbers

    @property
    def show_international_numbers_link(self):
        """Gets the show_international_numbers_link of this AccountsaccountIdsettingsTsp.  # noqa: E501

        Show international numbers link on the invitation email  # noqa: E501

        :return: The show_international_numbers_link of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :rtype: bool
        """
        return self._show_international_numbers_link

    @show_international_numbers_link.setter
    def show_international_numbers_link(self, show_international_numbers_link):
        """Sets the show_international_numbers_link of this AccountsaccountIdsettingsTsp.

        Show international numbers link on the invitation email  # noqa: E501

        :param show_international_numbers_link: The show_international_numbers_link of this AccountsaccountIdsettingsTsp.  # noqa: E501
        :type: bool
        """

        self._show_international_numbers_link = show_international_numbers_link

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
        if issubclass(AccountsaccountIdsettingsTsp, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsTsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other