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

class GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation(object):
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
        'language_item_pair_list': 'GroupsgroupIdsettingsInMeetingAutoGeneratedTranslationLanguageItemPairList',
        'enable': 'bool'
    }

    attribute_map = {
        'language_item_pair_list': 'language_item_pairList',
        'enable': 'enable'
    }

    def __init__(self, language_item_pair_list=None, enable=None):  # noqa: E501
        """GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation - a model defined in Swagger"""  # noqa: E501
        self._language_item_pair_list = None
        self._enable = None
        self.discriminator = None
        if language_item_pair_list is not None:
            self.language_item_pair_list = language_item_pair_list
        if enable is not None:
            self.enable = enable

    @property
    def language_item_pair_list(self):
        """Gets the language_item_pair_list of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501


        :return: The language_item_pair_list of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501
        :rtype: GroupsgroupIdsettingsInMeetingAutoGeneratedTranslationLanguageItemPairList
        """
        return self._language_item_pair_list

    @language_item_pair_list.setter
    def language_item_pair_list(self, language_item_pair_list):
        """Sets the language_item_pair_list of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.


        :param language_item_pair_list: The language_item_pair_list of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501
        :type: GroupsgroupIdsettingsInMeetingAutoGeneratedTranslationLanguageItemPairList
        """

        self._language_item_pair_list = language_item_pair_list

    @property
    def enable(self):
        """Gets the enable of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501

        Whether to allow users to enable automated translated captions in these language pairs in meetings.  # noqa: E501

        :return: The enable of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.

        Whether to allow users to enable automated translated captions in these language pairs in meetings.  # noqa: E501

        :param enable: The enable of this GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if issubclass(GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation, dict):
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
        if not isinstance(other, GroupsgroupIdsettingsInMeetingAutoGeneratedTranslation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
