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

class UserIdWebinarTemplatesBody(object):
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
        'webinar_id': 'int',
        'name': 'str',
        'save_recurrence': 'bool',
        'overwrite': 'bool'
    }

    attribute_map = {
        'webinar_id': 'webinar_id',
        'name': 'name',
        'save_recurrence': 'save_recurrence',
        'overwrite': 'overwrite'
    }

    def __init__(self, webinar_id=None, name=None, save_recurrence=False, overwrite=False):  # noqa: E501
        """UserIdWebinarTemplatesBody - a model defined in Swagger"""  # noqa: E501
        self._webinar_id = None
        self._name = None
        self._save_recurrence = None
        self._overwrite = None
        self.discriminator = None
        if webinar_id is not None:
            self.webinar_id = webinar_id
        if name is not None:
            self.name = name
        if save_recurrence is not None:
            self.save_recurrence = save_recurrence
        if overwrite is not None:
            self.overwrite = overwrite

    @property
    def webinar_id(self):
        """Gets the webinar_id of this UserIdWebinarTemplatesBody.  # noqa: E501

        The webinar ID in long (int64) format.  # noqa: E501

        :return: The webinar_id of this UserIdWebinarTemplatesBody.  # noqa: E501
        :rtype: int
        """
        return self._webinar_id

    @webinar_id.setter
    def webinar_id(self, webinar_id):
        """Sets the webinar_id of this UserIdWebinarTemplatesBody.

        The webinar ID in long (int64) format.  # noqa: E501

        :param webinar_id: The webinar_id of this UserIdWebinarTemplatesBody.  # noqa: E501
        :type: int
        """

        self._webinar_id = webinar_id

    @property
    def name(self):
        """Gets the name of this UserIdWebinarTemplatesBody.  # noqa: E501

        The webinar template's name.  # noqa: E501

        :return: The name of this UserIdWebinarTemplatesBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserIdWebinarTemplatesBody.

        The webinar template's name.  # noqa: E501

        :param name: The name of this UserIdWebinarTemplatesBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def save_recurrence(self):
        """Gets the save_recurrence of this UserIdWebinarTemplatesBody.  # noqa: E501

        If the field is set to true, the recurrence webinar template will be saved as the scheduled webinar.  # noqa: E501

        :return: The save_recurrence of this UserIdWebinarTemplatesBody.  # noqa: E501
        :rtype: bool
        """
        return self._save_recurrence

    @save_recurrence.setter
    def save_recurrence(self, save_recurrence):
        """Sets the save_recurrence of this UserIdWebinarTemplatesBody.

        If the field is set to true, the recurrence webinar template will be saved as the scheduled webinar.  # noqa: E501

        :param save_recurrence: The save_recurrence of this UserIdWebinarTemplatesBody.  # noqa: E501
        :type: bool
        """

        self._save_recurrence = save_recurrence

    @property
    def overwrite(self):
        """Gets the overwrite of this UserIdWebinarTemplatesBody.  # noqa: E501

        Overwrite an existing webinar template if the template is created from same existing webinar.  # noqa: E501

        :return: The overwrite of this UserIdWebinarTemplatesBody.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this UserIdWebinarTemplatesBody.

        Overwrite an existing webinar template if the template is created from same existing webinar.  # noqa: E501

        :param overwrite: The overwrite of this UserIdWebinarTemplatesBody.  # noqa: E501
        :type: bool
        """

        self._overwrite = overwrite

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
        if issubclass(UserIdWebinarTemplatesBody, dict):
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
        if not isinstance(other, UserIdWebinarTemplatesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other