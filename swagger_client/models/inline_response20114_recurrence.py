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

class InlineResponse20114Recurrence(object):
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
        'end_date_time': 'datetime',
        'end_times': 'int',
        'monthly_day': 'int',
        'monthly_week': 'int',
        'monthly_week_day': 'int',
        'repeat_interval': 'int',
        'type': 'int',
        'weekly_days': 'str'
    }

    attribute_map = {
        'end_date_time': 'end_date_time',
        'end_times': 'end_times',
        'monthly_day': 'monthly_day',
        'monthly_week': 'monthly_week',
        'monthly_week_day': 'monthly_week_day',
        'repeat_interval': 'repeat_interval',
        'type': 'type',
        'weekly_days': 'weekly_days'
    }

    def __init__(self, end_date_time=None, end_times=1, monthly_day=1, monthly_week=None, monthly_week_day=None, repeat_interval=None, type=None, weekly_days='1'):  # noqa: E501
        """InlineResponse20114Recurrence - a model defined in Swagger"""  # noqa: E501
        self._end_date_time = None
        self._end_times = None
        self._monthly_day = None
        self._monthly_week = None
        self._monthly_week_day = None
        self._repeat_interval = None
        self._type = None
        self._weekly_days = None
        self.discriminator = None
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if end_times is not None:
            self.end_times = end_times
        if monthly_day is not None:
            self.monthly_day = monthly_day
        if monthly_week is not None:
            self.monthly_week = monthly_week
        if monthly_week_day is not None:
            self.monthly_week_day = monthly_week_day
        if repeat_interval is not None:
            self.repeat_interval = repeat_interval
        self.type = type
        if weekly_days is not None:
            self.weekly_days = weekly_days

    @property
    def end_date_time(self):
        """Gets the end_date_time of this InlineResponse20114Recurrence.  # noqa: E501

        Select the final date when the meeting will recur before it is canceled. Should be in UTC time, such as 2017-11-25T12:00:00Z. Cannot be used with `end_times`.  # noqa: E501

        :return: The end_date_time of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this InlineResponse20114Recurrence.

        Select the final date when the meeting will recur before it is canceled. Should be in UTC time, such as 2017-11-25T12:00:00Z. Cannot be used with `end_times`.  # noqa: E501

        :param end_date_time: The end_date_time of this InlineResponse20114Recurrence.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def end_times(self):
        """Gets the end_times of this InlineResponse20114Recurrence.  # noqa: E501

        Select how many times the meeting should recur before it is canceled. The maximum number of recurring is 60. Cannot be used with `end_date_time`.  # noqa: E501

        :return: The end_times of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._end_times

    @end_times.setter
    def end_times(self, end_times):
        """Sets the end_times of this InlineResponse20114Recurrence.

        Select how many times the meeting should recur before it is canceled. The maximum number of recurring is 60. Cannot be used with `end_date_time`.  # noqa: E501

        :param end_times: The end_times of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """

        self._end_times = end_times

    @property
    def monthly_day(self):
        """Gets the monthly_day of this InlineResponse20114Recurrence.  # noqa: E501

        Use this field only if you're scheduling a recurring meeting of type `3` to state the day in a month when the meeting should recur. The value range is from 1 to 31.  For instance, if you would like the meeting to recur on 23rd of each month, provide `23` as this field's value and `1` as the `repeat_interval` field's value. Instead, to have the meeting recur every three months on 23rd of the month, change the value of the `repeat_interval` field to `3`.  # noqa: E501

        :return: The monthly_day of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._monthly_day

    @monthly_day.setter
    def monthly_day(self, monthly_day):
        """Sets the monthly_day of this InlineResponse20114Recurrence.

        Use this field only if you're scheduling a recurring meeting of type `3` to state the day in a month when the meeting should recur. The value range is from 1 to 31.  For instance, if you would like the meeting to recur on 23rd of each month, provide `23` as this field's value and `1` as the `repeat_interval` field's value. Instead, to have the meeting recur every three months on 23rd of the month, change the value of the `repeat_interval` field to `3`.  # noqa: E501

        :param monthly_day: The monthly_day of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """

        self._monthly_day = monthly_day

    @property
    def monthly_week(self):
        """Gets the monthly_week of this InlineResponse20114Recurrence.  # noqa: E501

        Use this field **only if you're scheduling a recurring meeting of type** `3` to state the week of the month when the meeting should recur. If you use this field, you must also use the `monthly_week_day` field to state the day of the week when the meeting should recur.     `-1` - Last week of the month.    `1` - First week of the month.    `2` - Second week of the month.    `3` - Third week of the month.    `4` - Fourth week of the month.  # noqa: E501

        :return: The monthly_week of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._monthly_week

    @monthly_week.setter
    def monthly_week(self, monthly_week):
        """Sets the monthly_week of this InlineResponse20114Recurrence.

        Use this field **only if you're scheduling a recurring meeting of type** `3` to state the week of the month when the meeting should recur. If you use this field, you must also use the `monthly_week_day` field to state the day of the week when the meeting should recur.     `-1` - Last week of the month.    `1` - First week of the month.    `2` - Second week of the month.    `3` - Third week of the month.    `4` - Fourth week of the month.  # noqa: E501

        :param monthly_week: The monthly_week of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 1, 2, 3, 4]  # noqa: E501
        if monthly_week not in allowed_values:
            raise ValueError(
                "Invalid value for `monthly_week` ({0}), must be one of {1}"  # noqa: E501
                .format(monthly_week, allowed_values)
            )

        self._monthly_week = monthly_week

    @property
    def monthly_week_day(self):
        """Gets the monthly_week_day of this InlineResponse20114Recurrence.  # noqa: E501

        Use this field **only if you're scheduling a recurring meeting of type** `3` to state a specific day in a week when the monthly meeting should recur. To use this field, you must also use the `monthly_week` field.       `1` - Sunday.    `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` - Thursday.    `6` - Friday.    `7` - Saturday.  # noqa: E501

        :return: The monthly_week_day of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._monthly_week_day

    @monthly_week_day.setter
    def monthly_week_day(self, monthly_week_day):
        """Sets the monthly_week_day of this InlineResponse20114Recurrence.

        Use this field **only if you're scheduling a recurring meeting of type** `3` to state a specific day in a week when the monthly meeting should recur. To use this field, you must also use the `monthly_week` field.       `1` - Sunday.    `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` - Thursday.    `6` - Friday.    `7` - Saturday.  # noqa: E501

        :param monthly_week_day: The monthly_week_day of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if monthly_week_day not in allowed_values:
            raise ValueError(
                "Invalid value for `monthly_week_day` ({0}), must be one of {1}"  # noqa: E501
                .format(monthly_week_day, allowed_values)
            )

        self._monthly_week_day = monthly_week_day

    @property
    def repeat_interval(self):
        """Gets the repeat_interval of this InlineResponse20114Recurrence.  # noqa: E501

        Define the interval for the meeting to recur. For instance, to schedule a meeting that recurs every two months, set this field's value to `2` and the value of the `type` parameter as `3`.   For a daily meeting, the maximum interval you can set is `90` days. For a weekly meeting the maximum interval that you can set is  of `12` weeks. For a monthly meeting, there is a maximum of `3` months.    # noqa: E501

        :return: The repeat_interval of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        """Sets the repeat_interval of this InlineResponse20114Recurrence.

        Define the interval for the meeting to recur. For instance, to schedule a meeting that recurs every two months, set this field's value to `2` and the value of the `type` parameter as `3`.   For a daily meeting, the maximum interval you can set is `90` days. For a weekly meeting the maximum interval that you can set is  of `12` weeks. For a monthly meeting, there is a maximum of `3` months.    # noqa: E501

        :param repeat_interval: The repeat_interval of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """

        self._repeat_interval = repeat_interval

    @property
    def type(self):
        """Gets the type of this InlineResponse20114Recurrence.  # noqa: E501

        Recurrence meeting types.  `1` - Daily.    `2` - Weekly.    `3` - Monthly.  # noqa: E501

        :return: The type of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20114Recurrence.

        Recurrence meeting types.  `1` - Daily.    `2` - Weekly.    `3` - Monthly.  # noqa: E501

        :param type: The type of this InlineResponse20114Recurrence.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def weekly_days(self):
        """Gets the weekly_days of this InlineResponse20114Recurrence.  # noqa: E501

        This field is required **if you're scheduling a recurring meeting of type** `2` to state the days of the week when the meeting should repeat.     This field's value could be a number between `1` to `7` in string format. For instance, if the meeting should recur on Sunday, provide `1` as this field's value.         **Note:** If you would like the meeting to occur on multiple days of a week, provide comma separated values for this field. For instance, if the meeting should recur on Sundays and Tuesdays, provide `1,3` as this field's value.       `1`  - Sunday.     `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` -  Thursday.    `6` - Friday.    `7` - Saturday.  # noqa: E501

        :return: The weekly_days of this InlineResponse20114Recurrence.  # noqa: E501
        :rtype: str
        """
        return self._weekly_days

    @weekly_days.setter
    def weekly_days(self, weekly_days):
        """Sets the weekly_days of this InlineResponse20114Recurrence.

        This field is required **if you're scheduling a recurring meeting of type** `2` to state the days of the week when the meeting should repeat.     This field's value could be a number between `1` to `7` in string format. For instance, if the meeting should recur on Sunday, provide `1` as this field's value.         **Note:** If you would like the meeting to occur on multiple days of a week, provide comma separated values for this field. For instance, if the meeting should recur on Sundays and Tuesdays, provide `1,3` as this field's value.       `1`  - Sunday.     `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` -  Thursday.    `6` - Friday.    `7` - Saturday.  # noqa: E501

        :param weekly_days: The weekly_days of this InlineResponse20114Recurrence.  # noqa: E501
        :type: str
        """
        allowed_values = ["1", "2", "3", "4", "5", "6", "7"]  # noqa: E501
        if weekly_days not in allowed_values:
            raise ValueError(
                "Invalid value for `weekly_days` ({0}), must be one of {1}"  # noqa: E501
                .format(weekly_days, allowed_values)
            )

        self._weekly_days = weekly_days

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
        if issubclass(InlineResponse20114Recurrence, dict):
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
        if not isinstance(other, InlineResponse20114Recurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
