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

class AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages(object):
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
        'enable': 'bool',
        'giphy_content_rating': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'giphy_content_rating': 'giphy_content_rating'
    }

    def __init__(self, enable=None, giphy_content_rating=None):  # noqa: E501
        """AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._giphy_content_rating = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if giphy_content_rating is not None:
            self.giphy_content_rating = giphy_content_rating

    @property
    def enable(self):
        """Gets the enable of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501

        Whether to allow users to search GIF images from GIPHY when they compose messages.  # noqa: E501

        :return: The enable of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.

        Whether to allow users to search GIF images from GIPHY when they compose messages.  # noqa: E501

        :param enable: The enable of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def giphy_content_rating(self):
        """Gets the giphy_content_rating of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501

        Set the GIPHY content rating. This feature is only available for Zoom Client v5.11.0 or later.  # noqa: E501

        :return: The giphy_content_rating of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501
        :rtype: int
        """
        return self._giphy_content_rating

    @giphy_content_rating.setter
    def giphy_content_rating(self, giphy_content_rating):
        """Sets the giphy_content_rating of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.

        Set the GIPHY content rating. This feature is only available for Zoom Client v5.11.0 or later.  # noqa: E501

        :param giphy_content_rating: The giphy_content_rating of this AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if giphy_content_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `giphy_content_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(giphy_content_rating, allowed_values)
            )

        self._giphy_content_rating = giphy_content_rating

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
        if issubclass(AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other