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

class InlineResponse20083Users(object):
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
        'user_created_at': 'datetime',
        'created_at': 'datetime',
        'custom_attributes': 'list[InlineResponse20083CustomAttributes]',
        'dept': 'str',
        'email': 'str',
        'employee_unique_id': 'str',
        'first_name': 'str',
        'group_ids': 'list[str]',
        'host_key': 'str',
        'id': 'str',
        'im_group_ids': 'list[str]',
        'last_client_version': 'str',
        'last_login_time': 'datetime',
        'last_name': 'str',
        'plan_united_type': 'str',
        'pmi': 'int',
        'role_id': 'str',
        'status': 'str',
        'timezone': 'str',
        'type': 'int',
        'verified': 'int',
        'display_name': 'str'
    }

    attribute_map = {
        'user_created_at': 'user_created_at',
        'created_at': 'created_at',
        'custom_attributes': 'custom_attributes',
        'dept': 'dept',
        'email': 'email',
        'employee_unique_id': 'employee_unique_id',
        'first_name': 'first_name',
        'group_ids': 'group_ids',
        'host_key': 'host_key',
        'id': 'id',
        'im_group_ids': 'im_group_ids',
        'last_client_version': 'last_client_version',
        'last_login_time': 'last_login_time',
        'last_name': 'last_name',
        'plan_united_type': 'plan_united_type',
        'pmi': 'pmi',
        'role_id': 'role_id',
        'status': 'status',
        'timezone': 'timezone',
        'type': 'type',
        'verified': 'verified',
        'display_name': 'display_name'
    }

    def __init__(self, user_created_at=None, created_at=None, custom_attributes=None, dept=None, email=None, employee_unique_id=None, first_name=None, group_ids=None, host_key=None, id=None, im_group_ids=None, last_client_version=None, last_login_time=None, last_name=None, plan_united_type=None, pmi=None, role_id=None, status=None, timezone=None, type=None, verified=None, display_name=None):  # noqa: E501
        """InlineResponse20083Users - a model defined in Swagger"""  # noqa: E501
        self._user_created_at = None
        self._created_at = None
        self._custom_attributes = None
        self._dept = None
        self._email = None
        self._employee_unique_id = None
        self._first_name = None
        self._group_ids = None
        self._host_key = None
        self._id = None
        self._im_group_ids = None
        self._last_client_version = None
        self._last_login_time = None
        self._last_name = None
        self._plan_united_type = None
        self._pmi = None
        self._role_id = None
        self._status = None
        self._timezone = None
        self._type = None
        self._verified = None
        self._display_name = None
        self.discriminator = None
        if user_created_at is not None:
            self.user_created_at = user_created_at
        if created_at is not None:
            self.created_at = created_at
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if dept is not None:
            self.dept = dept
        self.email = email
        if employee_unique_id is not None:
            self.employee_unique_id = employee_unique_id
        if first_name is not None:
            self.first_name = first_name
        if group_ids is not None:
            self.group_ids = group_ids
        if host_key is not None:
            self.host_key = host_key
        if id is not None:
            self.id = id
        if im_group_ids is not None:
            self.im_group_ids = im_group_ids
        if last_client_version is not None:
            self.last_client_version = last_client_version
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if last_name is not None:
            self.last_name = last_name
        if plan_united_type is not None:
            self.plan_united_type = plan_united_type
        if pmi is not None:
            self.pmi = pmi
        if role_id is not None:
            self.role_id = role_id
        if status is not None:
            self.status = status
        if timezone is not None:
            self.timezone = timezone
        self.type = type
        if verified is not None:
            self.verified = verified
        if display_name is not None:
            self.display_name = display_name

    @property
    def user_created_at(self):
        """Gets the user_created_at of this InlineResponse20083Users.  # noqa: E501

        The date and time when this user was created.  # noqa: E501

        :return: The user_created_at of this InlineResponse20083Users.  # noqa: E501
        :rtype: datetime
        """
        return self._user_created_at

    @user_created_at.setter
    def user_created_at(self, user_created_at):
        """Sets the user_created_at of this InlineResponse20083Users.

        The date and time when this user was created.  # noqa: E501

        :param user_created_at: The user_created_at of this InlineResponse20083Users.  # noqa: E501
        :type: datetime
        """

        self._user_created_at = user_created_at

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20083Users.  # noqa: E501

        The date and time when this user's latest login type was created.  # noqa: E501

        :return: The created_at of this InlineResponse20083Users.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20083Users.

        The date and time when this user's latest login type was created.  # noqa: E501

        :param created_at: The created_at of this InlineResponse20083Users.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this InlineResponse20083Users.  # noqa: E501

        Information about the user's custom attributes.  This field is **only** returned if users are assigned custom attributes and you provided the `custom_attributes` value for the `include_fields` query parameter in the API request.  # noqa: E501

        :return: The custom_attributes of this InlineResponse20083Users.  # noqa: E501
        :rtype: list[InlineResponse20083CustomAttributes]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this InlineResponse20083Users.

        Information about the user's custom attributes.  This field is **only** returned if users are assigned custom attributes and you provided the `custom_attributes` value for the `include_fields` query parameter in the API request.  # noqa: E501

        :param custom_attributes: The custom_attributes of this InlineResponse20083Users.  # noqa: E501
        :type: list[InlineResponse20083CustomAttributes]
        """

        self._custom_attributes = custom_attributes

    @property
    def dept(self):
        """Gets the dept of this InlineResponse20083Users.  # noqa: E501

        The user's department.  # noqa: E501

        :return: The dept of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this InlineResponse20083Users.

        The user's department.  # noqa: E501

        :param dept: The dept of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._dept = dept

    @property
    def email(self):
        """Gets the email of this InlineResponse20083Users.  # noqa: E501

        The user's email address.  # noqa: E501

        :return: The email of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20083Users.

        The user's email address.  # noqa: E501

        :param email: The email of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def employee_unique_id(self):
        """Gets the employee_unique_id of this InlineResponse20083Users.  # noqa: E501

        The employee's unique ID. The this field only returns when:  * SAML single sign-on (SSO) is enabled.  * The `login_type` value is `101` (SSO).  # noqa: E501

        :return: The employee_unique_id of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._employee_unique_id

    @employee_unique_id.setter
    def employee_unique_id(self, employee_unique_id):
        """Sets the employee_unique_id of this InlineResponse20083Users.

        The employee's unique ID. The this field only returns when:  * SAML single sign-on (SSO) is enabled.  * The `login_type` value is `101` (SSO).  # noqa: E501

        :param employee_unique_id: The employee_unique_id of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._employee_unique_id = employee_unique_id

    @property
    def first_name(self):
        """Gets the first_name of this InlineResponse20083Users.  # noqa: E501

        The user's first name.  # noqa: E501

        :return: The first_name of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineResponse20083Users.

        The user's first name.  # noqa: E501

        :param first_name: The first_name of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def group_ids(self):
        """Gets the group_ids of this InlineResponse20083Users.  # noqa: E501

        The IDs of groups where the user is a member.  # noqa: E501

        :return: The group_ids of this InlineResponse20083Users.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this InlineResponse20083Users.

        The IDs of groups where the user is a member.  # noqa: E501

        :param group_ids: The group_ids of this InlineResponse20083Users.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def host_key(self):
        """Gets the host_key of this InlineResponse20083Users.  # noqa: E501

        The user's [host key](https://support.zoom.us/hc/en-us/articles/205172555-Using-your-host-key).  This field is **only** returned if users are assigned a host key and you provided the `host_key` value for the `include_fields` query parameter in the API request.  # noqa: E501

        :return: The host_key of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._host_key

    @host_key.setter
    def host_key(self, host_key):
        """Sets the host_key of this InlineResponse20083Users.

        The user's [host key](https://support.zoom.us/hc/en-us/articles/205172555-Using-your-host-key).  This field is **only** returned if users are assigned a host key and you provided the `host_key` value for the `include_fields` query parameter in the API request.  # noqa: E501

        :param host_key: The host_key of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._host_key = host_key

    @property
    def id(self):
        """Gets the id of this InlineResponse20083Users.  # noqa: E501

        The user's ID.   The API does **not** return this value for users with the `pending` status.  # noqa: E501

        :return: The id of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20083Users.

        The user's ID.   The API does **not** return this value for users with the `pending` status.  # noqa: E501

        :param id: The id of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def im_group_ids(self):
        """Gets the im_group_ids of this InlineResponse20083Users.  # noqa: E501

        The IDs of IM directory groups where the user is a member.  # noqa: E501

        :return: The im_group_ids of this InlineResponse20083Users.  # noqa: E501
        :rtype: list[str]
        """
        return self._im_group_ids

    @im_group_ids.setter
    def im_group_ids(self, im_group_ids):
        """Sets the im_group_ids of this InlineResponse20083Users.

        The IDs of IM directory groups where the user is a member.  # noqa: E501

        :param im_group_ids: The im_group_ids of this InlineResponse20083Users.  # noqa: E501
        :type: list[str]
        """

        self._im_group_ids = im_group_ids

    @property
    def last_client_version(self):
        """Gets the last_client_version of this InlineResponse20083Users.  # noqa: E501

        The last client version that user used to log in.  # noqa: E501

        :return: The last_client_version of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._last_client_version

    @last_client_version.setter
    def last_client_version(self, last_client_version):
        """Sets the last_client_version of this InlineResponse20083Users.

        The last client version that user used to log in.  # noqa: E501

        :param last_client_version: The last_client_version of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._last_client_version = last_client_version

    @property
    def last_login_time(self):
        """Gets the last_login_time of this InlineResponse20083Users.  # noqa: E501

        The user's last login time. This field has a three-day buffer period.  For example, if user first logged in on `2020-01-01` and then logged out and logged in on `2020-01-02`, this value will still reflect the login time of `2020-01-01`. However, if the user logs in on `2020-01-04`, the value of this field will reflect the corresponding login time since it exceeds the three-day buffer period.  # noqa: E501

        :return: The last_login_time of this InlineResponse20083Users.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this InlineResponse20083Users.

        The user's last login time. This field has a three-day buffer period.  For example, if user first logged in on `2020-01-01` and then logged out and logged in on `2020-01-02`, this value will still reflect the login time of `2020-01-01`. However, if the user logs in on `2020-01-04`, the value of this field will reflect the corresponding login time since it exceeds the three-day buffer period.  # noqa: E501

        :param last_login_time: The last_login_time of this InlineResponse20083Users.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def last_name(self):
        """Gets the last_name of this InlineResponse20083Users.  # noqa: E501

        The user's last name.  # noqa: E501

        :return: The last_name of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InlineResponse20083Users.

        The user's last name.  # noqa: E501

        :param last_name: The last_name of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def plan_united_type(self):
        """Gets the plan_united_type of this InlineResponse20083Users.  # noqa: E501

        This field is returned if the user is enrolled in the [Zoom United](https://zoom.us/pricing/zoom-bundles) plan. The license option:  * `1` &mdash; Zoom United Pro-United with US/CA Unlimited.  * `2` &mdash; Zoom United Pro-United with UK/IR Unlimited.  * `4` &mdash; Zoom United Pro-United with AU/NZ Unlimited.  * `8` &mdash; Zoom United Pro-United with Global Select.  * `16` &mdash; Zoom United Pro-United with Zoom Phone Pro.  * `32` &mdash; Zoom United Biz-United with US/CA Unlimited.  * `64` &mdash; Zoom United Biz-United with UK/IR Unlimited.  * `128` &mdash; Zoom United Biz-United with AU/NZ Unlimited.  * `256` &mdash; Zoom United Biz-United with Global Select.  * `512` &mdash; Zoom United Biz-United with Zoom Phone Pro.  * `1024` &mdash; Zoom United Ent-United with US/CA Unlimited.  * `2048` &mdash; Zoom United Ent-United with UK/IR Unlimited.  * `4096` &mdash; Zoom United Ent-United with AU/NZ Unlimited.  * `8192` &mdash; Zoom United Ent-United with Global Select.  * `16384` &mdash; Zoom United Ent-United with Zoom Phone Pro.  * `32768` &mdash; Zoom United Pro-United with JP Unlimited.  * `65536` &mdash; Zoom United Biz-United with JP Unlimited.  * `131072` &mdash; Zoom United Ent-United with JP Unlimited.  # noqa: E501

        :return: The plan_united_type of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._plan_united_type

    @plan_united_type.setter
    def plan_united_type(self, plan_united_type):
        """Sets the plan_united_type of this InlineResponse20083Users.

        This field is returned if the user is enrolled in the [Zoom United](https://zoom.us/pricing/zoom-bundles) plan. The license option:  * `1` &mdash; Zoom United Pro-United with US/CA Unlimited.  * `2` &mdash; Zoom United Pro-United with UK/IR Unlimited.  * `4` &mdash; Zoom United Pro-United with AU/NZ Unlimited.  * `8` &mdash; Zoom United Pro-United with Global Select.  * `16` &mdash; Zoom United Pro-United with Zoom Phone Pro.  * `32` &mdash; Zoom United Biz-United with US/CA Unlimited.  * `64` &mdash; Zoom United Biz-United with UK/IR Unlimited.  * `128` &mdash; Zoom United Biz-United with AU/NZ Unlimited.  * `256` &mdash; Zoom United Biz-United with Global Select.  * `512` &mdash; Zoom United Biz-United with Zoom Phone Pro.  * `1024` &mdash; Zoom United Ent-United with US/CA Unlimited.  * `2048` &mdash; Zoom United Ent-United with UK/IR Unlimited.  * `4096` &mdash; Zoom United Ent-United with AU/NZ Unlimited.  * `8192` &mdash; Zoom United Ent-United with Global Select.  * `16384` &mdash; Zoom United Ent-United with Zoom Phone Pro.  * `32768` &mdash; Zoom United Pro-United with JP Unlimited.  * `65536` &mdash; Zoom United Biz-United with JP Unlimited.  * `131072` &mdash; Zoom United Ent-United with JP Unlimited.  # noqa: E501

        :param plan_united_type: The plan_united_type of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """
        allowed_values = ["1", "2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072"]  # noqa: E501
        if plan_united_type not in allowed_values:
            raise ValueError(
                "Invalid value for `plan_united_type` ({0}), must be one of {1}"  # noqa: E501
                .format(plan_united_type, allowed_values)
            )

        self._plan_united_type = plan_united_type

    @property
    def pmi(self):
        """Gets the pmi of this InlineResponse20083Users.  # noqa: E501

        The user's [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi)  # noqa: E501

        :return: The pmi of this InlineResponse20083Users.  # noqa: E501
        :rtype: int
        """
        return self._pmi

    @pmi.setter
    def pmi(self, pmi):
        """Sets the pmi of this InlineResponse20083Users.

        The user's [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi)  # noqa: E501

        :param pmi: The pmi of this InlineResponse20083Users.  # noqa: E501
        :type: int
        """

        self._pmi = pmi

    @property
    def role_id(self):
        """Gets the role_id of this InlineResponse20083Users.  # noqa: E501

        The unique ID of the user's assigned [role](/api-reference/zoom-api/methods#operation/roles).  # noqa: E501

        :return: The role_id of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this InlineResponse20083Users.

        The unique ID of the user's assigned [role](/api-reference/zoom-api/methods#operation/roles).  # noqa: E501

        :param role_id: The role_id of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def status(self):
        """Gets the status of this InlineResponse20083Users.  # noqa: E501

        The user's status.  * `active` - An active user.  * `inactive` - A deactivated user.  * `pending` - A pending user.  # noqa: E501

        :return: The status of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20083Users.

        The user's status.  * `active` - An active user.  * `inactive` - A deactivated user.  * `pending` - A pending user.  # noqa: E501

        :param status: The status of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def timezone(self):
        """Gets the timezone of this InlineResponse20083Users.  # noqa: E501

        The user's timezone.  # noqa: E501

        :return: The timezone of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InlineResponse20083Users.

        The user's timezone.  # noqa: E501

        :param timezone: The timezone of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this InlineResponse20083Users.  # noqa: E501

        The user's assigned plan type.  * `1` - Basic.  * `2` - Licensed.  * `4` - No Meeting License.  * `99` - None (this can only be set with `ssoCreate`).  # noqa: E501

        :return: The type of this InlineResponse20083Users.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20083Users.

        The user's assigned plan type.  * `1` - Basic.  * `2` - Licensed.  * `4` - No Meeting License.  * `99` - None (this can only be set with `ssoCreate`).  # noqa: E501

        :param type: The type of this InlineResponse20083Users.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 4, 99]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def verified(self):
        """Gets the verified of this InlineResponse20083Users.  # noqa: E501

        Display whether the user's email address for the Zoom account is verified.  * `1` - A verified user email.  * `0` - The user's email **not** verified.  # noqa: E501

        :return: The verified of this InlineResponse20083Users.  # noqa: E501
        :rtype: int
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this InlineResponse20083Users.

        Display whether the user's email address for the Zoom account is verified.  * `1` - A verified user email.  * `0` - The user's email **not** verified.  # noqa: E501

        :param verified: The verified of this InlineResponse20083Users.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 0]  # noqa: E501
        if verified not in allowed_values:
            raise ValueError(
                "Invalid value for `verified` ({0}), must be one of {1}"  # noqa: E501
                .format(verified, allowed_values)
            )

        self._verified = verified

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20083Users.  # noqa: E501

        The user's display name.  # noqa: E501

        :return: The display_name of this InlineResponse20083Users.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20083Users.

        The user's display name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20083Users.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if issubclass(InlineResponse20083Users, dict):
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
        if not isinstance(other, InlineResponse20083Users):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
