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

class InlineResponse20069OperationLogs(object):
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
        'action': 'str',
        'category_type': 'str',
        'operation_detail': 'str',
        'operator': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'action': 'action',
        'category_type': 'category_type',
        'operation_detail': 'operation_detail',
        'operator': 'operator',
        'time': 'time'
    }

    def __init__(self, action=None, category_type=None, operation_detail=None, operator=None, time=None):  # noqa: E501
        """InlineResponse20069OperationLogs - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._category_type = None
        self._operation_detail = None
        self._operator = None
        self._time = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if category_type is not None:
            self.category_type = category_type
        if operation_detail is not None:
            self.operation_detail = operation_detail
        if operator is not None:
            self.operator = operator
        if time is not None:
            self.time = time

    @property
    def action(self):
        """Gets the action of this InlineResponse20069OperationLogs.  # noqa: E501

        Action  # noqa: E501

        :return: The action of this InlineResponse20069OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InlineResponse20069OperationLogs.

        Action  # noqa: E501

        :param action: The action of this InlineResponse20069OperationLogs.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def category_type(self):
        """Gets the category_type of this InlineResponse20069OperationLogs.  # noqa: E501

        Category type  # noqa: E501

        :return: The category_type of this InlineResponse20069OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this InlineResponse20069OperationLogs.

        Category type  # noqa: E501

        :param category_type: The category_type of this InlineResponse20069OperationLogs.  # noqa: E501
        :type: str
        """

        self._category_type = category_type

    @property
    def operation_detail(self):
        """Gets the operation_detail of this InlineResponse20069OperationLogs.  # noqa: E501

        Operation detail  # noqa: E501

        :return: The operation_detail of this InlineResponse20069OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._operation_detail

    @operation_detail.setter
    def operation_detail(self, operation_detail):
        """Sets the operation_detail of this InlineResponse20069OperationLogs.

        Operation detail  # noqa: E501

        :param operation_detail: The operation_detail of this InlineResponse20069OperationLogs.  # noqa: E501
        :type: str
        """

        self._operation_detail = operation_detail

    @property
    def operator(self):
        """Gets the operator of this InlineResponse20069OperationLogs.  # noqa: E501

        The user who performed the operation.  # noqa: E501

        :return: The operator of this InlineResponse20069OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this InlineResponse20069OperationLogs.

        The user who performed the operation.  # noqa: E501

        :param operator: The operator of this InlineResponse20069OperationLogs.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def time(self):
        """Gets the time of this InlineResponse20069OperationLogs.  # noqa: E501

        The time at which the operation was performed.  # noqa: E501

        :return: The time of this InlineResponse20069OperationLogs.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20069OperationLogs.

        The time at which the operation was performed.  # noqa: E501

        :param time: The time of this InlineResponse20069OperationLogs.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if issubclass(InlineResponse20069OperationLogs, dict):
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
        if not isinstance(other, InlineResponse20069OperationLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
