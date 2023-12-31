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

class UpdateAUser(object):
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
        'cms_user_id': 'str',
        'company': 'str',
        'custom_attributes': 'list[UsersuserIdCustomAttributes]',
        'dept': 'str',
        'first_name': 'str',
        'group_id': 'str',
        'host_key': 'str',
        'job_title': 'str',
        'language': 'str',
        'last_name': 'str',
        'location': 'str',
        'manager': 'str',
        'phone_country': 'str',
        'phone_number': 'str',
        'phone_numbers': 'list[UsersuserIdPhoneNumbers]',
        'pmi': 'int',
        'pronouns': 'str',
        'pronouns_option': 'int',
        'timezone': 'str',
        'type': 'int',
        'use_pmi': 'bool',
        'vanity_name': 'str',
        'display_name': 'str',
        'zoom_one_type': 'int',
        'plan_united_type': 'str',
        'feature': 'UsersuserIdFeature',
        'about_me': 'str',
        'linkedin_url': 'str'
    }

    attribute_map = {
        'cms_user_id': 'cms_user_id',
        'company': 'company',
        'custom_attributes': 'custom_attributes',
        'dept': 'dept',
        'first_name': 'first_name',
        'group_id': 'group_id',
        'host_key': 'host_key',
        'job_title': 'job_title',
        'language': 'language',
        'last_name': 'last_name',
        'location': 'location',
        'manager': 'manager',
        'phone_country': 'phone_country',
        'phone_number': 'phone_number',
        'phone_numbers': 'phone_numbers',
        'pmi': 'pmi',
        'pronouns': 'pronouns',
        'pronouns_option': 'pronouns_option',
        'timezone': 'timezone',
        'type': 'type',
        'use_pmi': 'use_pmi',
        'vanity_name': 'vanity_name',
        'display_name': 'display_name',
        'zoom_one_type': 'zoom_one_type',
        'plan_united_type': 'plan_united_type',
        'feature': 'feature',
        'about_me': 'about_me',
        'linkedin_url': 'linkedin_url'
    }

    def __init__(self, cms_user_id=None, company=None, custom_attributes=None, dept=None, first_name=None, group_id=None, host_key=None, job_title=None, language=None, last_name=None, location=None, manager=None, phone_country=None, phone_number=None, phone_numbers=None, pmi=None, pronouns=None, pronouns_option=None, timezone=None, type=None, use_pmi=False, vanity_name=None, display_name=None, zoom_one_type=None, plan_united_type=None, feature=None, about_me=None, linkedin_url=None):  # noqa: E501
        """UpdateAUser - a model defined in Swagger"""  # noqa: E501
        self._cms_user_id = None
        self._company = None
        self._custom_attributes = None
        self._dept = None
        self._first_name = None
        self._group_id = None
        self._host_key = None
        self._job_title = None
        self._language = None
        self._last_name = None
        self._location = None
        self._manager = None
        self._phone_country = None
        self._phone_number = None
        self._phone_numbers = None
        self._pmi = None
        self._pronouns = None
        self._pronouns_option = None
        self._timezone = None
        self._type = None
        self._use_pmi = None
        self._vanity_name = None
        self._display_name = None
        self._zoom_one_type = None
        self._plan_united_type = None
        self._feature = None
        self._about_me = None
        self._linkedin_url = None
        self.discriminator = None
        if cms_user_id is not None:
            self.cms_user_id = cms_user_id
        if company is not None:
            self.company = company
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if dept is not None:
            self.dept = dept
        if first_name is not None:
            self.first_name = first_name
        if group_id is not None:
            self.group_id = group_id
        if host_key is not None:
            self.host_key = host_key
        if job_title is not None:
            self.job_title = job_title
        if language is not None:
            self.language = language
        if last_name is not None:
            self.last_name = last_name
        if location is not None:
            self.location = location
        if manager is not None:
            self.manager = manager
        if phone_country is not None:
            self.phone_country = phone_country
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if pmi is not None:
            self.pmi = pmi
        if pronouns is not None:
            self.pronouns = pronouns
        if pronouns_option is not None:
            self.pronouns_option = pronouns_option
        if timezone is not None:
            self.timezone = timezone
        if type is not None:
            self.type = type
        if use_pmi is not None:
            self.use_pmi = use_pmi
        if vanity_name is not None:
            self.vanity_name = vanity_name
        if display_name is not None:
            self.display_name = display_name
        if zoom_one_type is not None:
            self.zoom_one_type = zoom_one_type
        if plan_united_type is not None:
            self.plan_united_type = plan_united_type
        if feature is not None:
            self.feature = feature
        if about_me is not None:
            self.about_me = about_me
        if linkedin_url is not None:
            self.linkedin_url = linkedin_url

    @property
    def cms_user_id(self):
        """Gets the cms_user_id of this UpdateAUser.  # noqa: E501

        The Kaltura user ID.  # noqa: E501

        :return: The cms_user_id of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._cms_user_id

    @cms_user_id.setter
    def cms_user_id(self, cms_user_id):
        """Sets the cms_user_id of this UpdateAUser.

        The Kaltura user ID.  # noqa: E501

        :param cms_user_id: The cms_user_id of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._cms_user_id = cms_user_id

    @property
    def company(self):
        """Gets the company of this UpdateAUser.  # noqa: E501

        The user's company.  # noqa: E501

        :return: The company of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UpdateAUser.

        The user's company.  # noqa: E501

        :param company: The company of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this UpdateAUser.  # noqa: E501

        The user's assigned custom attributes.  # noqa: E501

        :return: The custom_attributes of this UpdateAUser.  # noqa: E501
        :rtype: list[UsersuserIdCustomAttributes]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this UpdateAUser.

        The user's assigned custom attributes.  # noqa: E501

        :param custom_attributes: The custom_attributes of this UpdateAUser.  # noqa: E501
        :type: list[UsersuserIdCustomAttributes]
        """

        self._custom_attributes = custom_attributes

    @property
    def dept(self):
        """Gets the dept of this UpdateAUser.  # noqa: E501

        The user's assigned department.  # noqa: E501

        :return: The dept of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this UpdateAUser.

        The user's assigned department.  # noqa: E501

        :param dept: The dept of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._dept = dept

    @property
    def first_name(self):
        """Gets the first_name of this UpdateAUser.  # noqa: E501

        The user's first name. This value cannot contain more than five Chinese characters.  # noqa: E501

        :return: The first_name of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateAUser.

        The user's first name. This value cannot contain more than five Chinese characters.  # noqa: E501

        :param first_name: The first_name of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def group_id(self):
        """Gets the group_id of this UpdateAUser.  # noqa: E501

        Provide the unique identifier of the group that you would like to add a [pending user](https://support.zoom.us/hc/en-us/articles/201363183-Managing-users#h_13c87a2a-ecd6-40ad-be61-a9935e660edb) to. Retrieve the value of this field from the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.  # noqa: E501

        :return: The group_id of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateAUser.

        Provide the unique identifier of the group that you would like to add a [pending user](https://support.zoom.us/hc/en-us/articles/201363183-Managing-users#h_13c87a2a-ecd6-40ad-be61-a9935e660edb) to. Retrieve the value of this field from the [**List groups**](/docs/api-reference/zoom-api/methods#operation/groups) API.  # noqa: E501

        :param group_id: The group_id of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def host_key(self):
        """Gets the host_key of this UpdateAUser.  # noqa: E501

        The user's host key.  # noqa: E501

        :return: The host_key of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._host_key

    @host_key.setter
    def host_key(self, host_key):
        """Sets the host_key of this UpdateAUser.

        The user's host key.  # noqa: E501

        :param host_key: The host_key of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._host_key = host_key

    @property
    def job_title(self):
        """Gets the job_title of this UpdateAUser.  # noqa: E501

        The user's job title.  # noqa: E501

        :return: The job_title of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this UpdateAUser.

        The user's job title.  # noqa: E501

        :param job_title: The job_title of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def language(self):
        """Gets the language of this UpdateAUser.  # noqa: E501

        The user's language.  # noqa: E501

        :return: The language of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateAUser.

        The user's language.  # noqa: E501

        :param language: The language of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def last_name(self):
        """Gets the last_name of this UpdateAUser.  # noqa: E501

        The user's last name. This value cannot contain more than five Chinese characters.  # noqa: E501

        :return: The last_name of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateAUser.

        The user's last name. This value cannot contain more than five Chinese characters.  # noqa: E501

        :param last_name: The last_name of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def location(self):
        """Gets the location of this UpdateAUser.  # noqa: E501

        The user's location.  # noqa: E501

        :return: The location of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UpdateAUser.

        The user's location.  # noqa: E501

        :param location: The location of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def manager(self):
        """Gets the manager of this UpdateAUser.  # noqa: E501

        The user's assigned manager.  # noqa: E501

        :return: The manager of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this UpdateAUser.

        The user's assigned manager.  # noqa: E501

        :param manager: The manager of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def phone_country(self):
        """Gets the phone_country of this UpdateAUser.  # noqa: E501

        **Note** This field has been **deprecated** and will not be supported in the future. Use the `country` field of the `phone_numbers` object to select the phone number country.   The user's phone number [country ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :return: The phone_country of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_country

    @phone_country.setter
    def phone_country(self, phone_country):
        """Sets the phone_country of this UpdateAUser.

        **Note** This field has been **deprecated** and will not be supported in the future. Use the `country` field of the `phone_numbers` object to select the phone number country.   The user's phone number [country ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :param phone_country: The phone_country of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._phone_country = phone_country

    @property
    def phone_number(self):
        """Gets the phone_number of this UpdateAUser.  # noqa: E501

        **Note** This field has been **deprecated** and will not be supported in the future. Instead, use the `phone_numbers` field to assign phone numbers to a user.   The user's phone number. To update a phone number, you must also provide the `phone_country` field.  # noqa: E501

        :return: The phone_number of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this UpdateAUser.

        **Note** This field has been **deprecated** and will not be supported in the future. Instead, use the `phone_numbers` field to assign phone numbers to a user.   The user's phone number. To update a phone number, you must also provide the `phone_country` field.  # noqa: E501

        :param phone_number: The phone_number of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this UpdateAUser.  # noqa: E501

        Information about the user's assigned phone numbers.  # noqa: E501

        :return: The phone_numbers of this UpdateAUser.  # noqa: E501
        :rtype: list[UsersuserIdPhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this UpdateAUser.

        Information about the user's assigned phone numbers.  # noqa: E501

        :param phone_numbers: The phone_numbers of this UpdateAUser.  # noqa: E501
        :type: list[UsersuserIdPhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def pmi(self):
        """Gets the pmi of this UpdateAUser.  # noqa: E501

        The user's [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi).  # noqa: E501

        :return: The pmi of this UpdateAUser.  # noqa: E501
        :rtype: int
        """
        return self._pmi

    @pmi.setter
    def pmi(self, pmi):
        """Sets the pmi of this UpdateAUser.

        The user's [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi).  # noqa: E501

        :param pmi: The pmi of this UpdateAUser.  # noqa: E501
        :type: int
        """

        self._pmi = pmi

    @property
    def pronouns(self):
        """Gets the pronouns of this UpdateAUser.  # noqa: E501

        The user's pronouns.  # noqa: E501

        :return: The pronouns of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._pronouns

    @pronouns.setter
    def pronouns(self, pronouns):
        """Sets the pronouns of this UpdateAUser.

        The user's pronouns.  # noqa: E501

        :param pronouns: The pronouns of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._pronouns = pronouns

    @property
    def pronouns_option(self):
        """Gets the pronouns_option of this UpdateAUser.  # noqa: E501

        The user's display pronouns setting.  * `1` - Ask the user every time they join meetings and webinars.  * `2` - Always display pronouns in meetings and webinars.  * `3` - Do not display pronouns in meetings and webinars.  # noqa: E501

        :return: The pronouns_option of this UpdateAUser.  # noqa: E501
        :rtype: int
        """
        return self._pronouns_option

    @pronouns_option.setter
    def pronouns_option(self, pronouns_option):
        """Sets the pronouns_option of this UpdateAUser.

        The user's display pronouns setting.  * `1` - Ask the user every time they join meetings and webinars.  * `2` - Always display pronouns in meetings and webinars.  * `3` - Do not display pronouns in meetings and webinars.  # noqa: E501

        :param pronouns_option: The pronouns_option of this UpdateAUser.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if pronouns_option not in allowed_values:
            raise ValueError(
                "Invalid value for `pronouns_option` ({0}), must be one of {1}"  # noqa: E501
                .format(pronouns_option, allowed_values)
            )

        self._pronouns_option = pronouns_option

    @property
    def timezone(self):
        """Gets the timezone of this UpdateAUser.  # noqa: E501

        The user's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones)  # noqa: E501

        :return: The timezone of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UpdateAUser.

        The user's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones)  # noqa: E501

        :param timezone: The timezone of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this UpdateAUser.  # noqa: E501

        The type of [user](https://support.zoom.us/hc/en-us/articles/201363173-Zoom-user-types-roles).  * `1` - Basic.  * `2` - Licensed.  * `4` - No Meetings License.  * `99` - None. You can only set this value if the user was created using the `ssoCreate` value for `action` parameter in the [**Create users**](/docs/api-reference/zoom-api/methods#operation/userCreate) API.  # noqa: E501

        :return: The type of this UpdateAUser.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateAUser.

        The type of [user](https://support.zoom.us/hc/en-us/articles/201363173-Zoom-user-types-roles).  * `1` - Basic.  * `2` - Licensed.  * `4` - No Meetings License.  * `99` - None. You can only set this value if the user was created using the `ssoCreate` value for `action` parameter in the [**Create users**](/docs/api-reference/zoom-api/methods#operation/userCreate) API.  # noqa: E501

        :param type: The type of this UpdateAUser.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 99]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def use_pmi(self):
        """Gets the use_pmi of this UpdateAUser.  # noqa: E501

        Whether to use a [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) for instant meetings.  # noqa: E501

        :return: The use_pmi of this UpdateAUser.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi

    @use_pmi.setter
    def use_pmi(self, use_pmi):
        """Sets the use_pmi of this UpdateAUser.

        Whether to use a [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) for instant meetings.  # noqa: E501

        :param use_pmi: The use_pmi of this UpdateAUser.  # noqa: E501
        :type: bool
        """

        self._use_pmi = use_pmi

    @property
    def vanity_name(self):
        """Gets the vanity_name of this UpdateAUser.  # noqa: E501

        The user's personal meeting room name.  # noqa: E501

        :return: The vanity_name of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._vanity_name

    @vanity_name.setter
    def vanity_name(self, vanity_name):
        """Sets the vanity_name of this UpdateAUser.

        The user's personal meeting room name.  # noqa: E501

        :param vanity_name: The vanity_name of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._vanity_name = vanity_name

    @property
    def display_name(self):
        """Gets the display_name of this UpdateAUser.  # noqa: E501

        The user's display name. This value cannot contain more than ten Chinese characters.  # noqa: E501

        :return: The display_name of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateAUser.

        The user's display name. This value cannot contain more than ten Chinese characters.  # noqa: E501

        :param display_name: The display_name of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def zoom_one_type(self):
        """Gets the zoom_one_type of this UpdateAUser.  # noqa: E501

        The Zoom One plan option.   `0` - Turn off Zoom One license.    `16` - Zoom One Business Plus with US/CA Unlimited.    `32` - Zoom One Business Plus with UK/IR Unlimited.    `64` - Zoom One Business Plus with AU/NZ Unlimited.    `128` - Zoom One Business Plus with Japan Unlimited.    `33554432` - Zoom One Business Plus with Global Select.    `134217728` - Zoom One Enterprise Premier with US/CA Unlimited.    `1073741824` - Zoom One Enterprise Premier with AU/NZ Unlimited.    `536870912` - Zoom One Enterprise Premier with UK/IR Unlimited.    `268435456` - Zoom One Enterprise Premier with Japan Unlimited.     The Zoom One plan option for Gov accounts:    `0` - Turn off Zoom One license.    `16` - Zoom One Business Plus.     The Zoom One plan option for Education accounts:    `0` - Turn off Zoom One license.    `18014398509481984` - Zoom One for Education School and Campus.    `72057594037927936` - Zoom One for Education Enterprise Essentials.    `576460752303423488` - Zoom One for Education Enterprise Student.    `144115188075855872` - Zoom One for Education Enterprise Plus.    `137438953472` - Zoom One for Education School and Campus Plus with US/CA Unlimited.    `1099511627776` -Zoom One for Education School and Campus Plus with AU/NZ Unlimited.    `549755813888` - Zoom One for Education School and Campus Plus with UK/IR Unlimited.    `274877906944` - Zoom One for Education School and Campus Plus with Japan Unlimited.    `2199023255552` - Zoom One for Education School and Campus Plus with Global Select.    `4294967296` - Zoom One for Education Enterprise Premier with US/CA Unlimited.    `34359738368` - Zoom One for Education Enterprise Premier with AU/NZ Unlimited.    `17179869184` -Zoom One for Education Enterprise Premier with UK/IR Unlimited.    `8589934592` - Zoom One for Education Enterprise Premier with with Japan Unlimited.    `68719476736` - Zoom One for Education Enterprise Premier with Global Select.  # noqa: E501

        :return: The zoom_one_type of this UpdateAUser.  # noqa: E501
        :rtype: int
        """
        return self._zoom_one_type

    @zoom_one_type.setter
    def zoom_one_type(self, zoom_one_type):
        """Sets the zoom_one_type of this UpdateAUser.

        The Zoom One plan option.   `0` - Turn off Zoom One license.    `16` - Zoom One Business Plus with US/CA Unlimited.    `32` - Zoom One Business Plus with UK/IR Unlimited.    `64` - Zoom One Business Plus with AU/NZ Unlimited.    `128` - Zoom One Business Plus with Japan Unlimited.    `33554432` - Zoom One Business Plus with Global Select.    `134217728` - Zoom One Enterprise Premier with US/CA Unlimited.    `1073741824` - Zoom One Enterprise Premier with AU/NZ Unlimited.    `536870912` - Zoom One Enterprise Premier with UK/IR Unlimited.    `268435456` - Zoom One Enterprise Premier with Japan Unlimited.     The Zoom One plan option for Gov accounts:    `0` - Turn off Zoom One license.    `16` - Zoom One Business Plus.     The Zoom One plan option for Education accounts:    `0` - Turn off Zoom One license.    `18014398509481984` - Zoom One for Education School and Campus.    `72057594037927936` - Zoom One for Education Enterprise Essentials.    `576460752303423488` - Zoom One for Education Enterprise Student.    `144115188075855872` - Zoom One for Education Enterprise Plus.    `137438953472` - Zoom One for Education School and Campus Plus with US/CA Unlimited.    `1099511627776` -Zoom One for Education School and Campus Plus with AU/NZ Unlimited.    `549755813888` - Zoom One for Education School and Campus Plus with UK/IR Unlimited.    `274877906944` - Zoom One for Education School and Campus Plus with Japan Unlimited.    `2199023255552` - Zoom One for Education School and Campus Plus with Global Select.    `4294967296` - Zoom One for Education Enterprise Premier with US/CA Unlimited.    `34359738368` - Zoom One for Education Enterprise Premier with AU/NZ Unlimited.    `17179869184` -Zoom One for Education Enterprise Premier with UK/IR Unlimited.    `8589934592` - Zoom One for Education Enterprise Premier with with Japan Unlimited.    `68719476736` - Zoom One for Education Enterprise Premier with Global Select.  # noqa: E501

        :param zoom_one_type: The zoom_one_type of this UpdateAUser.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 16, 32, 64, 128, 33554432]  # noqa: E501
        if zoom_one_type not in allowed_values:
            raise ValueError(
                "Invalid value for `zoom_one_type` ({0}), must be one of {1}"  # noqa: E501
                .format(zoom_one_type, allowed_values)
            )

        self._zoom_one_type = zoom_one_type

    @property
    def plan_united_type(self):
        """Gets the plan_united_type of this UpdateAUser.  # noqa: E501

        The Zoom United type and license.  * `1` - Zoom United Pro-United with US/CA Unlimited.  * `2` - Zoom United Pro-United with UK/IR Unlimited.  * `4` - Zoom United Pro-United with AU/NZ Unlimited.  * `8` - Zoom United Pro-United with Global Select.  * `16` - Zoom United Pro-United with Zoom Phone Pro.  * `32` - Zoom United Biz-United with US/CA Unlimited.  * `64` - Zoom United Biz-United with UK/IR Unlimited.  * `128` - Zoom United Biz-United with AU/NZ Unlimited.  * `256` - Zoom United Biz-United with Global Select.  * `512` - Zoom United Biz-United with Zoom Phone Pro.  * `1024` - Zoom United Ent-United with US/CA Unlimited.  * `2048` - Zoom United Ent-United with UK/IR Unlimited.  * `4096` - Zoom United Ent-United with AU/NZ Unlimited.  * `8192` - Zoom United Ent-United with Global Select.  * `16384` - Zoom United Ent-United with Zoom Phone Pro.  * `32768` - Zoom United Pro-United with JP Unlimited.  * `65536` - Zoom United Biz-United with JP Unlimited.  * `131072` - Zoom United Ent-United with JP Unlimited.  * `none` - Turn off Zoom United type.  # noqa: E501

        :return: The plan_united_type of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._plan_united_type

    @plan_united_type.setter
    def plan_united_type(self, plan_united_type):
        """Sets the plan_united_type of this UpdateAUser.

        The Zoom United type and license.  * `1` - Zoom United Pro-United with US/CA Unlimited.  * `2` - Zoom United Pro-United with UK/IR Unlimited.  * `4` - Zoom United Pro-United with AU/NZ Unlimited.  * `8` - Zoom United Pro-United with Global Select.  * `16` - Zoom United Pro-United with Zoom Phone Pro.  * `32` - Zoom United Biz-United with US/CA Unlimited.  * `64` - Zoom United Biz-United with UK/IR Unlimited.  * `128` - Zoom United Biz-United with AU/NZ Unlimited.  * `256` - Zoom United Biz-United with Global Select.  * `512` - Zoom United Biz-United with Zoom Phone Pro.  * `1024` - Zoom United Ent-United with US/CA Unlimited.  * `2048` - Zoom United Ent-United with UK/IR Unlimited.  * `4096` - Zoom United Ent-United with AU/NZ Unlimited.  * `8192` - Zoom United Ent-United with Global Select.  * `16384` - Zoom United Ent-United with Zoom Phone Pro.  * `32768` - Zoom United Pro-United with JP Unlimited.  * `65536` - Zoom United Biz-United with JP Unlimited.  * `131072` - Zoom United Ent-United with JP Unlimited.  * `none` - Turn off Zoom United type.  # noqa: E501

        :param plan_united_type: The plan_united_type of this UpdateAUser.  # noqa: E501
        :type: str
        """
        allowed_values = ["1", "2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "none"]  # noqa: E501
        if plan_united_type not in allowed_values:
            raise ValueError(
                "Invalid value for `plan_united_type` ({0}), must be one of {1}"  # noqa: E501
                .format(plan_united_type, allowed_values)
            )

        self._plan_united_type = plan_united_type

    @property
    def feature(self):
        """Gets the feature of this UpdateAUser.  # noqa: E501


        :return: The feature of this UpdateAUser.  # noqa: E501
        :rtype: UsersuserIdFeature
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this UpdateAUser.


        :param feature: The feature of this UpdateAUser.  # noqa: E501
        :type: UsersuserIdFeature
        """

        self._feature = feature

    @property
    def about_me(self):
        """Gets the about_me of this UpdateAUser.  # noqa: E501

        The user's self-introduction. Hyperlinks or HTML code not allowed in this field.  # noqa: E501

        :return: The about_me of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._about_me

    @about_me.setter
    def about_me(self, about_me):
        """Sets the about_me of this UpdateAUser.

        The user's self-introduction. Hyperlinks or HTML code not allowed in this field.  # noqa: E501

        :param about_me: The about_me of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._about_me = about_me

    @property
    def linkedin_url(self):
        """Gets the linkedin_url of this UpdateAUser.  # noqa: E501

        The user's LinkedIn link. The URL must contain `linkedin.com`.  # noqa: E501

        :return: The linkedin_url of this UpdateAUser.  # noqa: E501
        :rtype: str
        """
        return self._linkedin_url

    @linkedin_url.setter
    def linkedin_url(self, linkedin_url):
        """Sets the linkedin_url of this UpdateAUser.

        The user's LinkedIn link. The URL must contain `linkedin.com`.  # noqa: E501

        :param linkedin_url: The linkedin_url of this UpdateAUser.  # noqa: E501
        :type: str
        """

        self._linkedin_url = linkedin_url

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
        if issubclass(UpdateAUser, dict):
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
        if not isinstance(other, UpdateAUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
