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

class InlineResponse2002Security(object):
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
        'admin_change_name_pic': 'bool',
        'admin_change_user_info': 'bool',
        'user_modifiable_info_by_admin': 'list[str]',
        'signin_with_sso': 'InlineResponse2002SecuritySigninWithSso',
        'hide_billing_info': 'bool',
        'import_photos_from_devices': 'bool',
        'password_requirement': 'InlineResponse2002SecurityPasswordRequirement',
        'sign_again_period_for_inactivity_on_client': 'int',
        'sign_again_period_for_inactivity_on_web': 'int',
        'sign_in_with_two_factor_auth': 'str',
        'sign_in_with_two_factor_auth_groups': 'list[str]',
        'sign_in_with_two_factor_auth_roles': 'list[str]'
    }

    attribute_map = {
        'admin_change_name_pic': 'admin_change_name_pic',
        'admin_change_user_info': 'admin_change_user_info',
        'user_modifiable_info_by_admin': 'user_modifiable_info_by_admin',
        'signin_with_sso': 'signin_with_sso',
        'hide_billing_info': 'hide_billing_info',
        'import_photos_from_devices': 'import_photos_from_devices',
        'password_requirement': 'password_requirement',
        'sign_again_period_for_inactivity_on_client': 'sign_again_period_for_inactivity_on_client',
        'sign_again_period_for_inactivity_on_web': 'sign_again_period_for_inactivity_on_web',
        'sign_in_with_two_factor_auth': 'sign_in_with_two_factor_auth',
        'sign_in_with_two_factor_auth_groups': 'sign_in_with_two_factor_auth_groups',
        'sign_in_with_two_factor_auth_roles': 'sign_in_with_two_factor_auth_roles'
    }

    def __init__(self, admin_change_name_pic=None, admin_change_user_info=None, user_modifiable_info_by_admin=None, signin_with_sso=None, hide_billing_info=None, import_photos_from_devices=None, password_requirement=None, sign_again_period_for_inactivity_on_client=None, sign_again_period_for_inactivity_on_web=None, sign_in_with_two_factor_auth=None, sign_in_with_two_factor_auth_groups=None, sign_in_with_two_factor_auth_roles=None):  # noqa: E501
        """InlineResponse2002Security - a model defined in Swagger"""  # noqa: E501
        self._admin_change_name_pic = None
        self._admin_change_user_info = None
        self._user_modifiable_info_by_admin = None
        self._signin_with_sso = None
        self._hide_billing_info = None
        self._import_photos_from_devices = None
        self._password_requirement = None
        self._sign_again_period_for_inactivity_on_client = None
        self._sign_again_period_for_inactivity_on_web = None
        self._sign_in_with_two_factor_auth = None
        self._sign_in_with_two_factor_auth_groups = None
        self._sign_in_with_two_factor_auth_roles = None
        self.discriminator = None
        if admin_change_name_pic is not None:
            self.admin_change_name_pic = admin_change_name_pic
        if admin_change_user_info is not None:
            self.admin_change_user_info = admin_change_user_info
        if user_modifiable_info_by_admin is not None:
            self.user_modifiable_info_by_admin = user_modifiable_info_by_admin
        if signin_with_sso is not None:
            self.signin_with_sso = signin_with_sso
        if hide_billing_info is not None:
            self.hide_billing_info = hide_billing_info
        if import_photos_from_devices is not None:
            self.import_photos_from_devices = import_photos_from_devices
        if password_requirement is not None:
            self.password_requirement = password_requirement
        if sign_again_period_for_inactivity_on_client is not None:
            self.sign_again_period_for_inactivity_on_client = sign_again_period_for_inactivity_on_client
        if sign_again_period_for_inactivity_on_web is not None:
            self.sign_again_period_for_inactivity_on_web = sign_again_period_for_inactivity_on_web
        if sign_in_with_two_factor_auth is not None:
            self.sign_in_with_two_factor_auth = sign_in_with_two_factor_auth
        if sign_in_with_two_factor_auth_groups is not None:
            self.sign_in_with_two_factor_auth_groups = sign_in_with_two_factor_auth_groups
        if sign_in_with_two_factor_auth_roles is not None:
            self.sign_in_with_two_factor_auth_roles = sign_in_with_two_factor_auth_roles

    @property
    def admin_change_name_pic(self):
        """Gets the admin_change_name_pic of this InlineResponse2002Security.  # noqa: E501

        Whether to only allow account administrators to change a user's picture.  # noqa: E501

        :return: The admin_change_name_pic of this InlineResponse2002Security.  # noqa: E501
        :rtype: bool
        """
        return self._admin_change_name_pic

    @admin_change_name_pic.setter
    def admin_change_name_pic(self, admin_change_name_pic):
        """Sets the admin_change_name_pic of this InlineResponse2002Security.

        Whether to only allow account administrators to change a user's picture.  # noqa: E501

        :param admin_change_name_pic: The admin_change_name_pic of this InlineResponse2002Security.  # noqa: E501
        :type: bool
        """

        self._admin_change_name_pic = admin_change_name_pic

    @property
    def admin_change_user_info(self):
        """Gets the admin_change_user_info of this InlineResponse2002Security.  # noqa: E501

        Whether to only allow account administrators to change a user's information.  # noqa: E501

        :return: The admin_change_user_info of this InlineResponse2002Security.  # noqa: E501
        :rtype: bool
        """
        return self._admin_change_user_info

    @admin_change_user_info.setter
    def admin_change_user_info(self, admin_change_user_info):
        """Sets the admin_change_user_info of this InlineResponse2002Security.

        Whether to only allow account administrators to change a user's information.  # noqa: E501

        :param admin_change_user_info: The admin_change_user_info of this InlineResponse2002Security.  # noqa: E501
        :type: bool
        """

        self._admin_change_user_info = admin_change_user_info

    @property
    def user_modifiable_info_by_admin(self):
        """Gets the user_modifiable_info_by_admin of this InlineResponse2002Security.  # noqa: E501

        If the `admin_change_user_info` value is `true`, the list of the types of user information that only the account administrators can modify.  * `name`  * `profile_picture`  * `sign_in_email`  * `host_key`  # noqa: E501

        :return: The user_modifiable_info_by_admin of this InlineResponse2002Security.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_modifiable_info_by_admin

    @user_modifiable_info_by_admin.setter
    def user_modifiable_info_by_admin(self, user_modifiable_info_by_admin):
        """Sets the user_modifiable_info_by_admin of this InlineResponse2002Security.

        If the `admin_change_user_info` value is `true`, the list of the types of user information that only the account administrators can modify.  * `name`  * `profile_picture`  * `sign_in_email`  * `host_key`  # noqa: E501

        :param user_modifiable_info_by_admin: The user_modifiable_info_by_admin of this InlineResponse2002Security.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["name", "profile_picture", "sign_in_email", "host_key"]  # noqa: E501
        if not set(user_modifiable_info_by_admin).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `user_modifiable_info_by_admin` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(user_modifiable_info_by_admin) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._user_modifiable_info_by_admin = user_modifiable_info_by_admin

    @property
    def signin_with_sso(self):
        """Gets the signin_with_sso of this InlineResponse2002Security.  # noqa: E501


        :return: The signin_with_sso of this InlineResponse2002Security.  # noqa: E501
        :rtype: InlineResponse2002SecuritySigninWithSso
        """
        return self._signin_with_sso

    @signin_with_sso.setter
    def signin_with_sso(self, signin_with_sso):
        """Sets the signin_with_sso of this InlineResponse2002Security.


        :param signin_with_sso: The signin_with_sso of this InlineResponse2002Security.  # noqa: E501
        :type: InlineResponse2002SecuritySigninWithSso
        """

        self._signin_with_sso = signin_with_sso

    @property
    def hide_billing_info(self):
        """Gets the hide_billing_info of this InlineResponse2002Security.  # noqa: E501

        Hide billing information.  # noqa: E501

        :return: The hide_billing_info of this InlineResponse2002Security.  # noqa: E501
        :rtype: bool
        """
        return self._hide_billing_info

    @hide_billing_info.setter
    def hide_billing_info(self, hide_billing_info):
        """Sets the hide_billing_info of this InlineResponse2002Security.

        Hide billing information.  # noqa: E501

        :param hide_billing_info: The hide_billing_info of this InlineResponse2002Security.  # noqa: E501
        :type: bool
        """

        self._hide_billing_info = hide_billing_info

    @property
    def import_photos_from_devices(self):
        """Gets the import_photos_from_devices of this InlineResponse2002Security.  # noqa: E501

        Allow users to import photos from a photo library on a  device.  # noqa: E501

        :return: The import_photos_from_devices of this InlineResponse2002Security.  # noqa: E501
        :rtype: bool
        """
        return self._import_photos_from_devices

    @import_photos_from_devices.setter
    def import_photos_from_devices(self, import_photos_from_devices):
        """Sets the import_photos_from_devices of this InlineResponse2002Security.

        Allow users to import photos from a photo library on a  device.  # noqa: E501

        :param import_photos_from_devices: The import_photos_from_devices of this InlineResponse2002Security.  # noqa: E501
        :type: bool
        """

        self._import_photos_from_devices = import_photos_from_devices

    @property
    def password_requirement(self):
        """Gets the password_requirement of this InlineResponse2002Security.  # noqa: E501


        :return: The password_requirement of this InlineResponse2002Security.  # noqa: E501
        :rtype: InlineResponse2002SecurityPasswordRequirement
        """
        return self._password_requirement

    @password_requirement.setter
    def password_requirement(self, password_requirement):
        """Sets the password_requirement of this InlineResponse2002Security.


        :param password_requirement: The password_requirement of this InlineResponse2002Security.  # noqa: E501
        :type: InlineResponse2002SecurityPasswordRequirement
        """

        self._password_requirement = password_requirement

    @property
    def sign_again_period_for_inactivity_on_client(self):
        """Gets the sign_again_period_for_inactivity_on_client of this InlineResponse2002Security.  # noqa: E501

        Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Client app after a set amount of time.       If this setting is disabled, the value of this field will be `0`. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom client.     `5` - 5 minutes.     `10` - 10 minutes.     `15` - 15 minutes.     `30` - 30 minutes.     `45` - 45 minutes.     `60` - 60 .     `90` - 90 minutes.     `120` - 120 minutes.   # noqa: E501

        :return: The sign_again_period_for_inactivity_on_client of this InlineResponse2002Security.  # noqa: E501
        :rtype: int
        """
        return self._sign_again_period_for_inactivity_on_client

    @sign_again_period_for_inactivity_on_client.setter
    def sign_again_period_for_inactivity_on_client(self, sign_again_period_for_inactivity_on_client):
        """Sets the sign_again_period_for_inactivity_on_client of this InlineResponse2002Security.

        Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Client app after a set amount of time.       If this setting is disabled, the value of this field will be `0`. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom client.     `5` - 5 minutes.     `10` - 10 minutes.     `15` - 15 minutes.     `30` - 30 minutes.     `45` - 45 minutes.     `60` - 60 .     `90` - 90 minutes.     `120` - 120 minutes.   # noqa: E501

        :param sign_again_period_for_inactivity_on_client: The sign_again_period_for_inactivity_on_client of this InlineResponse2002Security.  # noqa: E501
        :type: int
        """

        self._sign_again_period_for_inactivity_on_client = sign_again_period_for_inactivity_on_client

    @property
    def sign_again_period_for_inactivity_on_web(self):
        """Gets the sign_again_period_for_inactivity_on_web of this InlineResponse2002Security.  # noqa: E501

        Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Web Portal after a set amount of time.       If this setting is disabled, the value of this field will be `0`. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom Web Portal.     `5` - 5 minutes.     `10` - 10 minutes.     `15` - 15 minutes.     `30` - 30 minutes.     `60` - 60 minutes.     `120` - 120 minutes.      # noqa: E501

        :return: The sign_again_period_for_inactivity_on_web of this InlineResponse2002Security.  # noqa: E501
        :rtype: int
        """
        return self._sign_again_period_for_inactivity_on_web

    @sign_again_period_for_inactivity_on_web.setter
    def sign_again_period_for_inactivity_on_web(self, sign_again_period_for_inactivity_on_web):
        """Sets the sign_again_period_for_inactivity_on_web of this InlineResponse2002Security.

        Settings for User Sign In interval requirements after a period of inactivity. If enabled, this setting forces automatic logout of users in Zoom Web Portal after a set amount of time.       If this setting is disabled, the value of this field will be `0`. If the setting is enabled, the value of this field will indicate the **period of inactivity** in minutes, after which an inactive user will be automatically logged out of the Zoom Web Portal.     `5` - 5 minutes.     `10` - 10 minutes.     `15` - 15 minutes.     `30` - 30 minutes.     `60` - 60 minutes.     `120` - 120 minutes.      # noqa: E501

        :param sign_again_period_for_inactivity_on_web: The sign_again_period_for_inactivity_on_web of this InlineResponse2002Security.  # noqa: E501
        :type: int
        """

        self._sign_again_period_for_inactivity_on_web = sign_again_period_for_inactivity_on_web

    @property
    def sign_in_with_two_factor_auth(self):
        """Gets the sign_in_with_two_factor_auth of this InlineResponse2002Security.  # noqa: E501

        Settings for 2FA( [two factor authentication](https://support.zoom.us/hc/en-us/articles/360038247071) ). `all` - Two factor authentication will be enabled for all users in the account.     `none` - Two factor authentication is disabled.     `group` - Two factor authentication will be enabled for users belonging to specific groups. If 2FA is enabled for certain groups, the group IDs of the group(s) will be provided in the `sign_in_with_two_factor_auth_groups` field.     `role` - Two factor authentication will be enabled only for users assigned with specific roles in the account. If 2FA is enabled for specific roles, the role IDs will be provided in the `sign_in_with_two_factor_auth_roles` field.   # noqa: E501

        :return: The sign_in_with_two_factor_auth of this InlineResponse2002Security.  # noqa: E501
        :rtype: str
        """
        return self._sign_in_with_two_factor_auth

    @sign_in_with_two_factor_auth.setter
    def sign_in_with_two_factor_auth(self, sign_in_with_two_factor_auth):
        """Sets the sign_in_with_two_factor_auth of this InlineResponse2002Security.

        Settings for 2FA( [two factor authentication](https://support.zoom.us/hc/en-us/articles/360038247071) ). `all` - Two factor authentication will be enabled for all users in the account.     `none` - Two factor authentication is disabled.     `group` - Two factor authentication will be enabled for users belonging to specific groups. If 2FA is enabled for certain groups, the group IDs of the group(s) will be provided in the `sign_in_with_two_factor_auth_groups` field.     `role` - Two factor authentication will be enabled only for users assigned with specific roles in the account. If 2FA is enabled for specific roles, the role IDs will be provided in the `sign_in_with_two_factor_auth_roles` field.   # noqa: E501

        :param sign_in_with_two_factor_auth: The sign_in_with_two_factor_auth of this InlineResponse2002Security.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "group", "role", "none"]  # noqa: E501
        if sign_in_with_two_factor_auth not in allowed_values:
            raise ValueError(
                "Invalid value for `sign_in_with_two_factor_auth` ({0}), must be one of {1}"  # noqa: E501
                .format(sign_in_with_two_factor_auth, allowed_values)
            )

        self._sign_in_with_two_factor_auth = sign_in_with_two_factor_auth

    @property
    def sign_in_with_two_factor_auth_groups(self):
        """Gets the sign_in_with_two_factor_auth_groups of this InlineResponse2002Security.  # noqa: E501

        This field contains group IDs of groups that have 2FA enabled. This field is only returned if the value of `sign_in_with_two_factor_auth` is `group`  # noqa: E501

        :return: The sign_in_with_two_factor_auth_groups of this InlineResponse2002Security.  # noqa: E501
        :rtype: list[str]
        """
        return self._sign_in_with_two_factor_auth_groups

    @sign_in_with_two_factor_auth_groups.setter
    def sign_in_with_two_factor_auth_groups(self, sign_in_with_two_factor_auth_groups):
        """Sets the sign_in_with_two_factor_auth_groups of this InlineResponse2002Security.

        This field contains group IDs of groups that have 2FA enabled. This field is only returned if the value of `sign_in_with_two_factor_auth` is `group`  # noqa: E501

        :param sign_in_with_two_factor_auth_groups: The sign_in_with_two_factor_auth_groups of this InlineResponse2002Security.  # noqa: E501
        :type: list[str]
        """

        self._sign_in_with_two_factor_auth_groups = sign_in_with_two_factor_auth_groups

    @property
    def sign_in_with_two_factor_auth_roles(self):
        """Gets the sign_in_with_two_factor_auth_roles of this InlineResponse2002Security.  # noqa: E501

        This field contains role IDs of roles that have 2FA enabled. This field is only returned if the value of `sign_in_with_two_factor_auth` is `role`.  # noqa: E501

        :return: The sign_in_with_two_factor_auth_roles of this InlineResponse2002Security.  # noqa: E501
        :rtype: list[str]
        """
        return self._sign_in_with_two_factor_auth_roles

    @sign_in_with_two_factor_auth_roles.setter
    def sign_in_with_two_factor_auth_roles(self, sign_in_with_two_factor_auth_roles):
        """Sets the sign_in_with_two_factor_auth_roles of this InlineResponse2002Security.

        This field contains role IDs of roles that have 2FA enabled. This field is only returned if the value of `sign_in_with_two_factor_auth` is `role`.  # noqa: E501

        :param sign_in_with_two_factor_auth_roles: The sign_in_with_two_factor_auth_roles of this InlineResponse2002Security.  # noqa: E501
        :type: list[str]
        """

        self._sign_in_with_two_factor_auth_roles = sign_in_with_two_factor_auth_roles

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
        if issubclass(InlineResponse2002Security, dict):
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
        if not isinstance(other, InlineResponse2002Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
