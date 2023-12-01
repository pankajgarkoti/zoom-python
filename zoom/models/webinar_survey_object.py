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

class WebinarSurveyObject(object):
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
        'custom_survey': 'WebinarSurveyObjectCustomSurvey',
        'show_in_the_browser': 'bool',
        'show_in_the_follow_up_email': 'bool',
        'third_party_survey': 'str'
    }

    attribute_map = {
        'custom_survey': 'custom_survey',
        'show_in_the_browser': 'show_in_the_browser',
        'show_in_the_follow_up_email': 'show_in_the_follow_up_email',
        'third_party_survey': 'third_party_survey'
    }

    def __init__(self, custom_survey=None, show_in_the_browser=True, show_in_the_follow_up_email=False, third_party_survey=None):  # noqa: E501
        """WebinarSurveyObject - a model defined in Swagger"""  # noqa: E501
        self._custom_survey = None
        self._show_in_the_browser = None
        self._show_in_the_follow_up_email = None
        self._third_party_survey = None
        self.discriminator = None
        if custom_survey is not None:
            self.custom_survey = custom_survey
        if show_in_the_browser is not None:
            self.show_in_the_browser = show_in_the_browser
        if show_in_the_follow_up_email is not None:
            self.show_in_the_follow_up_email = show_in_the_follow_up_email
        if third_party_survey is not None:
            self.third_party_survey = third_party_survey

    @property
    def custom_survey(self):
        """Gets the custom_survey of this WebinarSurveyObject.  # noqa: E501


        :return: The custom_survey of this WebinarSurveyObject.  # noqa: E501
        :rtype: WebinarSurveyObjectCustomSurvey
        """
        return self._custom_survey

    @custom_survey.setter
    def custom_survey(self, custom_survey):
        """Sets the custom_survey of this WebinarSurveyObject.


        :param custom_survey: The custom_survey of this WebinarSurveyObject.  # noqa: E501
        :type: WebinarSurveyObjectCustomSurvey
        """

        self._custom_survey = custom_survey

    @property
    def show_in_the_browser(self):
        """Gets the show_in_the_browser of this WebinarSurveyObject.  # noqa: E501

        Whether the **Show in the browser when the webinar ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.  # noqa: E501

        :return: The show_in_the_browser of this WebinarSurveyObject.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_the_browser

    @show_in_the_browser.setter
    def show_in_the_browser(self, show_in_the_browser):
        """Sets the show_in_the_browser of this WebinarSurveyObject.

        Whether the **Show in the browser when the webinar ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.  # noqa: E501

        :param show_in_the_browser: The show_in_the_browser of this WebinarSurveyObject.  # noqa: E501
        :type: bool
        """

        self._show_in_the_browser = show_in_the_browser

    @property
    def show_in_the_follow_up_email(self):
        """Gets the show_in_the_follow_up_email of this WebinarSurveyObject.  # noqa: E501

        Whether the **Show the link on the follow-up email** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `false`.  # noqa: E501

        :return: The show_in_the_follow_up_email of this WebinarSurveyObject.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_the_follow_up_email

    @show_in_the_follow_up_email.setter
    def show_in_the_follow_up_email(self, show_in_the_follow_up_email):
        """Sets the show_in_the_follow_up_email of this WebinarSurveyObject.

        Whether the **Show the link on the follow-up email** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `false`.  # noqa: E501

        :param show_in_the_follow_up_email: The show_in_the_follow_up_email of this WebinarSurveyObject.  # noqa: E501
        :type: bool
        """

        self._show_in_the_follow_up_email = show_in_the_follow_up_email

    @property
    def third_party_survey(self):
        """Gets the third_party_survey of this WebinarSurveyObject.  # noqa: E501

        The link to the third party webinar survey.  # noqa: E501

        :return: The third_party_survey of this WebinarSurveyObject.  # noqa: E501
        :rtype: str
        """
        return self._third_party_survey

    @third_party_survey.setter
    def third_party_survey(self, third_party_survey):
        """Sets the third_party_survey of this WebinarSurveyObject.

        The link to the third party webinar survey.  # noqa: E501

        :param third_party_survey: The third_party_survey of this WebinarSurveyObject.  # noqa: E501
        :type: str
        """

        self._third_party_survey = third_party_survey

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
        if issubclass(WebinarSurveyObject, dict):
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
        if not isinstance(other, WebinarSurveyObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other