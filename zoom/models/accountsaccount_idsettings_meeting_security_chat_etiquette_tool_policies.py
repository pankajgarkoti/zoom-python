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

class AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies(object):
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
        'description': 'str',
        'id': 'str',
        'is_locked': 'bool',
        'keywords': 'list[str]',
        'name': 'str',
        'regular_expression': 'str',
        'status': 'str',
        'trigger_action': 'int'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'is_locked': 'is_locked',
        'keywords': 'keywords',
        'name': 'name',
        'regular_expression': 'regular_expression',
        'status': 'status',
        'trigger_action': 'trigger_action'
    }

    def __init__(self, description=None, id=None, is_locked=False, keywords=None, name=None, regular_expression=None, status=None, trigger_action=None):  # noqa: E501
        """AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._id = None
        self._is_locked = None
        self._keywords = None
        self._name = None
        self._regular_expression = None
        self._status = None
        self._trigger_action = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_locked is not None:
            self.is_locked = is_locked
        if keywords is not None:
            self.keywords = keywords
        if name is not None:
            self.name = name
        if regular_expression is not None:
            self.regular_expression = regular_expression
        if status is not None:
            self.status = status
        if trigger_action is not None:
            self.trigger_action = trigger_action

    @property
    def description(self):
        """Gets the description of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The policy's description.  # noqa: E501

        :return: The description of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The policy's description.  # noqa: E501

        :param description: The description of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The policy ID.  # noqa: E501

        :return: The id of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The policy ID.  # noqa: E501

        :param id: The id of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_locked(self):
        """Gets the is_locked of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        Whether to lock the policy. When it is locked, users cannot update the policy. This value defaults to `false`.  # noqa: E501

        :return: The is_locked of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        Whether to lock the policy. When it is locked, users cannot update the policy. This value defaults to `false`.  # noqa: E501

        :param is_locked: The is_locked of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def keywords(self):
        """Gets the keywords of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        A list of defined rule keywords.  # noqa: E501

        :return: The keywords of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        A list of defined rule keywords.  # noqa: E501

        :param keywords: The keywords of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def name(self):
        """Gets the name of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The policy name.  # noqa: E501

        :return: The name of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The policy name.  # noqa: E501

        :param name: The name of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def regular_expression(self):
        """Gets the regular_expression of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The regular expression to match to the content of chat messages.  # noqa: E501

        :return: The regular_expression of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        """Sets the regular_expression of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The regular expression to match to the content of chat messages.  # noqa: E501

        :param regular_expression: The regular_expression of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: str
        """

        self._regular_expression = regular_expression

    @property
    def status(self):
        """Gets the status of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The policy's current status.  * `activated` - Activated.  * `deactivated` - Deactivated.  # noqa: E501

        :return: The status of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The policy's current status.  * `activated` - Activated.  * `deactivated` - Deactivated.  # noqa: E501

        :param status: The status of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: str
        """
        allowed_values = ["activated", "deactivated"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def trigger_action(self):
        """Gets the trigger_action of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501

        The policy's trigger action.  * `1` - Ask the user to confirm before they send the message.  * `2` - Block the user's message.  # noqa: E501

        :return: The trigger_action of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :rtype: int
        """
        return self._trigger_action

    @trigger_action.setter
    def trigger_action(self, trigger_action):
        """Sets the trigger_action of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.

        The policy's trigger action.  * `1` - Ask the user to confirm before they send the message.  * `2` - Block the user's message.  # noqa: E501

        :param trigger_action: The trigger_action of this AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if trigger_action not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_action` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_action, allowed_values)
            )

        self._trigger_action = trigger_action

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
        if issubclass(AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies, dict):
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
        if not isinstance(other, AccountsaccountIdsettingsMeetingSecurityChatEtiquetteToolPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
