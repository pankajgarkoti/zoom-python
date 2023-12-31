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

class AccountsaccountIdsettingsSessionSecurity(object):
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
        'approved_or_denied_countries_or_regions': 'AccountsaccountIdsettingsSessionSecurityApprovedOrDeniedCountriesOrRegions'
    }

    attribute_map = {
        'approved_or_denied_countries_or_regions': 'approved_or_denied_countries_or_regions'
    }

    def __init__(self, approved_or_denied_countries_or_regions=None):  # noqa: E501
        """AccountsaccountIdsettingsSessionSecurity - a model defined in Swagger"""  # noqa: E501
        self._approved_or_denied_countries_or_regions = None
        self.discriminator = None
        if approved_or_denied_countries_or_regions is not None:
            self.approved_or_denied_countries_or_regions = approved_or_denied_countries_or_regions

    @property
    def approved_or_denied_countries_or_regions(self):
        """Gets the approved_or_denied_countries_or_regions of this AccountsaccountIdsettingsSessionSecurity.  # noqa: E501


        :return: The approved_or_denied_countries_or_regions of this AccountsaccountIdsettingsSessionSecurity.  # noqa: E501
        :rtype: AccountsaccountIdsettingsSessionSecurityApprovedOrDeniedCountriesOrRegions
        """
        return self._approved_or_denied_countries_or_regions

    @approved_or_denied_countries_or_regions.setter
    def approved_or_denied_countries_or_regions(self, approved_or_denied_countries_or_regions):
        """Sets the approved_or_denied_countries_or_regions of this AccountsaccountIdsettingsSessionSecurity.


        :param approved_or_denied_countries_or_regions: The approved_or_denied_countries_or_regions of this AccountsaccountIdsettingsSessionSecurity.  # noqa: E501
        :type: AccountsaccountIdsettingsSessionSecurityApprovedOrDeniedCountriesOrRegions
        """

        self._approved_or_denied_countries_or_regions = approved_or_denied_countries_or_regions

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
        if issubclass(AccountsaccountIdsettingsSessionSecurity, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsSessionSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
