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

class SipPhonesBody(object):
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
        'authorization_name': 'str',
        'domain': 'str',
        'password': 'str',
        'proxy_server': 'str',
        'proxy_server2': 'str',
        'proxy_server3': 'str',
        'register_server': 'str',
        'register_server2': 'str',
        'register_server3': 'str',
        'registration_expire_time': 'int',
        'transport_protocol': 'str',
        'transport_protocol2': 'str',
        'transport_protocol3': 'str',
        'user_email': 'str',
        'user_name': 'str',
        'voice_mail': 'str'
    }

    attribute_map = {
        'authorization_name': 'authorization_name',
        'domain': 'domain',
        'password': 'password',
        'proxy_server': 'proxy_server',
        'proxy_server2': 'proxy_server2',
        'proxy_server3': 'proxy_server3',
        'register_server': 'register_server',
        'register_server2': 'register_server2',
        'register_server3': 'register_server3',
        'registration_expire_time': 'registration_expire_time',
        'transport_protocol': 'transport_protocol',
        'transport_protocol2': 'transport_protocol2',
        'transport_protocol3': 'transport_protocol3',
        'user_email': 'user_email',
        'user_name': 'user_name',
        'voice_mail': 'voice_mail'
    }

    def __init__(self, authorization_name=None, domain=None, password=None, proxy_server=None, proxy_server2=None, proxy_server3=None, register_server=None, register_server2=None, register_server3=None, registration_expire_time=60, transport_protocol=None, transport_protocol2=None, transport_protocol3=None, user_email=None, user_name=None, voice_mail=None):  # noqa: E501
        """SipPhonesBody - a model defined in Swagger"""  # noqa: E501
        self._authorization_name = None
        self._domain = None
        self._password = None
        self._proxy_server = None
        self._proxy_server2 = None
        self._proxy_server3 = None
        self._register_server = None
        self._register_server2 = None
        self._register_server3 = None
        self._registration_expire_time = None
        self._transport_protocol = None
        self._transport_protocol2 = None
        self._transport_protocol3 = None
        self._user_email = None
        self._user_name = None
        self._voice_mail = None
        self.discriminator = None
        self.authorization_name = authorization_name
        self.domain = domain
        self.password = password
        self.proxy_server = proxy_server
        if proxy_server2 is not None:
            self.proxy_server2 = proxy_server2
        if proxy_server3 is not None:
            self.proxy_server3 = proxy_server3
        self.register_server = register_server
        if register_server2 is not None:
            self.register_server2 = register_server2
        if register_server3 is not None:
            self.register_server3 = register_server3
        if registration_expire_time is not None:
            self.registration_expire_time = registration_expire_time
        if transport_protocol is not None:
            self.transport_protocol = transport_protocol
        if transport_protocol2 is not None:
            self.transport_protocol2 = transport_protocol2
        if transport_protocol3 is not None:
            self.transport_protocol3 = transport_protocol3
        self.user_email = user_email
        self.user_name = user_name
        self.voice_mail = voice_mail

    @property
    def authorization_name(self):
        """Gets the authorization_name of this SipPhonesBody.  # noqa: E501

        The authorization name of the user that is registered for SIP phone.  # noqa: E501

        :return: The authorization_name of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._authorization_name

    @authorization_name.setter
    def authorization_name(self, authorization_name):
        """Sets the authorization_name of this SipPhonesBody.

        The authorization name of the user that is registered for SIP phone.  # noqa: E501

        :param authorization_name: The authorization_name of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if authorization_name is None:
            raise ValueError("Invalid value for `authorization_name`, must not be `None`")  # noqa: E501

        self._authorization_name = authorization_name

    @property
    def domain(self):
        """Gets the domain of this SipPhonesBody.  # noqa: E501

        The name or IP address of your provider's SIP domain (example: CDC.WEB).   # noqa: E501

        :return: The domain of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SipPhonesBody.

        The name or IP address of your provider's SIP domain (example: CDC.WEB).   # noqa: E501

        :param domain: The domain of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def password(self):
        """Gets the password of this SipPhonesBody.  # noqa: E501

        The password generated for the user in the SIP account.  # noqa: E501

        :return: The password of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SipPhonesBody.

        The password generated for the user in the SIP account.  # noqa: E501

        :param password: The password of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def proxy_server(self):
        """Gets the proxy_server of this SipPhonesBody.  # noqa: E501

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.  # noqa: E501

        :return: The proxy_server of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._proxy_server

    @proxy_server.setter
    def proxy_server(self, proxy_server):
        """Sets the proxy_server of this SipPhonesBody.

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.  # noqa: E501

        :param proxy_server: The proxy_server of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if proxy_server is None:
            raise ValueError("Invalid value for `proxy_server`, must not be `None`")  # noqa: E501

        self._proxy_server = proxy_server

    @property
    def proxy_server2(self):
        """Gets the proxy_server2 of this SipPhonesBody.  # noqa: E501

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.  # noqa: E501

        :return: The proxy_server2 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._proxy_server2

    @proxy_server2.setter
    def proxy_server2(self, proxy_server2):
        """Sets the proxy_server2 of this SipPhonesBody.

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.  # noqa: E501

        :param proxy_server2: The proxy_server2 of this SipPhonesBody.  # noqa: E501
        :type: str
        """

        self._proxy_server2 = proxy_server2

    @property
    def proxy_server3(self):
        """Gets the proxy_server3 of this SipPhonesBody.  # noqa: E501

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.  # noqa: E501

        :return: The proxy_server3 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._proxy_server3

    @proxy_server3.setter
    def proxy_server3(self, proxy_server3):
        """Sets the proxy_server3 of this SipPhonesBody.

        The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.  # noqa: E501

        :param proxy_server3: The proxy_server3 of this SipPhonesBody.  # noqa: E501
        :type: str
        """

        self._proxy_server3 = proxy_server3

    @property
    def register_server(self):
        """Gets the register_server of this SipPhonesBody.  # noqa: E501

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :return: The register_server of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._register_server

    @register_server.setter
    def register_server(self, register_server):
        """Sets the register_server of this SipPhonesBody.

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :param register_server: The register_server of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if register_server is None:
            raise ValueError("Invalid value for `register_server`, must not be `None`")  # noqa: E501

        self._register_server = register_server

    @property
    def register_server2(self):
        """Gets the register_server2 of this SipPhonesBody.  # noqa: E501

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :return: The register_server2 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._register_server2

    @register_server2.setter
    def register_server2(self, register_server2):
        """Sets the register_server2 of this SipPhonesBody.

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :param register_server2: The register_server2 of this SipPhonesBody.  # noqa: E501
        :type: str
        """

        self._register_server2 = register_server2

    @property
    def register_server3(self):
        """Gets the register_server3 of this SipPhonesBody.  # noqa: E501

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :return: The register_server3 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._register_server3

    @register_server3.setter
    def register_server3(self, register_server3):
        """Sets the register_server3 of this SipPhonesBody.

        The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.  # noqa: E501

        :param register_server3: The register_server3 of this SipPhonesBody.  # noqa: E501
        :type: str
        """

        self._register_server3 = register_server3

    @property
    def registration_expire_time(self):
        """Gets the registration_expire_time of this SipPhonesBody.  # noqa: E501

        The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.  # noqa: E501

        :return: The registration_expire_time of this SipPhonesBody.  # noqa: E501
        :rtype: int
        """
        return self._registration_expire_time

    @registration_expire_time.setter
    def registration_expire_time(self, registration_expire_time):
        """Sets the registration_expire_time of this SipPhonesBody.

        The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.  # noqa: E501

        :param registration_expire_time: The registration_expire_time of this SipPhonesBody.  # noqa: E501
        :type: int
        """

        self._registration_expire_time = registration_expire_time

    @property
    def transport_protocol(self):
        """Gets the transport_protocol of this SipPhonesBody.  # noqa: E501

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :return: The transport_protocol of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._transport_protocol

    @transport_protocol.setter
    def transport_protocol(self, transport_protocol):
        """Sets the transport_protocol of this SipPhonesBody.

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :param transport_protocol: The transport_protocol of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["UDP", "TCP", "TLS", "AUTO"]  # noqa: E501
        if transport_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_protocol, allowed_values)
            )

        self._transport_protocol = transport_protocol

    @property
    def transport_protocol2(self):
        """Gets the transport_protocol2 of this SipPhonesBody.  # noqa: E501

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :return: The transport_protocol2 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._transport_protocol2

    @transport_protocol2.setter
    def transport_protocol2(self, transport_protocol2):
        """Sets the transport_protocol2 of this SipPhonesBody.

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :param transport_protocol2: The transport_protocol2 of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["UDP", "TCP", "TLS", "AUTO"]  # noqa: E501
        if transport_protocol2 not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_protocol2` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_protocol2, allowed_values)
            )

        self._transport_protocol2 = transport_protocol2

    @property
    def transport_protocol3(self):
        """Gets the transport_protocol3 of this SipPhonesBody.  # noqa: E501

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :return: The transport_protocol3 of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._transport_protocol3

    @transport_protocol3.setter
    def transport_protocol3(self, transport_protocol3):
        """Sets the transport_protocol3 of this SipPhonesBody.

        Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.  # noqa: E501

        :param transport_protocol3: The transport_protocol3 of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["UDP", "TCP", "TLS", "AUTO"]  # noqa: E501
        if transport_protocol3 not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_protocol3` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_protocol3, allowed_values)
            )

        self._transport_protocol3 = transport_protocol3

    @property
    def user_email(self):
        """Gets the user_email of this SipPhonesBody.  # noqa: E501

        The email address of the user to associate with the SIP Phone. Can add `.win`, `.mac`, `.android`, `.ipad`, `.iphone`, `.linux`, `.pc`, `.mobile`, `.pad` at the end of the email (for example, `user@example.com.mac`) to add accounts for different platforms for the same user.  # noqa: E501

        :return: The user_email of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this SipPhonesBody.

        The email address of the user to associate with the SIP Phone. Can add `.win`, `.mac`, `.android`, `.ipad`, `.iphone`, `.linux`, `.pc`, `.mobile`, `.pad` at the end of the email (for example, `user@example.com.mac`) to add accounts for different platforms for the same user.  # noqa: E501

        :param user_email: The user_email of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_name(self):
        """Gets the user_name of this SipPhonesBody.  # noqa: E501

        The phone number associated with the user in the SIP account.  # noqa: E501

        :return: The user_name of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SipPhonesBody.

        The phone number associated with the user in the SIP account.  # noqa: E501

        :param user_name: The user_name of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def voice_mail(self):
        """Gets the voice_mail of this SipPhonesBody.  # noqa: E501

        The number to dial for checking voicemail.  # noqa: E501

        :return: The voice_mail of this SipPhonesBody.  # noqa: E501
        :rtype: str
        """
        return self._voice_mail

    @voice_mail.setter
    def voice_mail(self, voice_mail):
        """Sets the voice_mail of this SipPhonesBody.

        The number to dial for checking voicemail.  # noqa: E501

        :param voice_mail: The voice_mail of this SipPhonesBody.  # noqa: E501
        :type: str
        """
        if voice_mail is None:
            raise ValueError("Invalid value for `voice_mail`, must not be `None`")  # noqa: E501

        self._voice_mail = voice_mail

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
        if issubclass(SipPhonesBody, dict):
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
        if not isinstance(other, SipPhonesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
