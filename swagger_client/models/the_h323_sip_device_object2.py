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

class TheH323SIPDeviceObject2(object):
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
        'encryption': 'str',
        'ip': 'str',
        'name': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'encryption': 'encryption',
        'ip': 'ip',
        'name': 'name',
        'protocol': 'protocol'
    }

    def __init__(self, encryption=None, ip=None, name=None, protocol=None):  # noqa: E501
        """TheH323SIPDeviceObject2 - a model defined in Swagger"""  # noqa: E501
        self._encryption = None
        self._ip = None
        self._name = None
        self._protocol = None
        self.discriminator = None
        self.encryption = encryption
        self.ip = ip
        self.name = name
        self.protocol = protocol

    @property
    def encryption(self):
        """Gets the encryption of this TheH323SIPDeviceObject2.  # noqa: E501

        Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.  # noqa: E501

        :return: The encryption of this TheH323SIPDeviceObject2.  # noqa: E501
        :rtype: str
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this TheH323SIPDeviceObject2.

        Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.  # noqa: E501

        :param encryption: The encryption of this TheH323SIPDeviceObject2.  # noqa: E501
        :type: str
        """
        if encryption is None:
            raise ValueError("Invalid value for `encryption`, must not be `None`")  # noqa: E501
        allowed_values = ["auto", "yes", "no"]  # noqa: E501
        if encryption not in allowed_values:
            raise ValueError(
                "Invalid value for `encryption` ({0}), must be one of {1}"  # noqa: E501
                .format(encryption, allowed_values)
            )

        self._encryption = encryption

    @property
    def ip(self):
        """Gets the ip of this TheH323SIPDeviceObject2.  # noqa: E501

        Device IP.  # noqa: E501

        :return: The ip of this TheH323SIPDeviceObject2.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TheH323SIPDeviceObject2.

        Device IP.  # noqa: E501

        :param ip: The ip of this TheH323SIPDeviceObject2.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this TheH323SIPDeviceObject2.  # noqa: E501

        Device name.  # noqa: E501

        :return: The name of this TheH323SIPDeviceObject2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TheH323SIPDeviceObject2.

        Device name.  # noqa: E501

        :param name: The name of this TheH323SIPDeviceObject2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this TheH323SIPDeviceObject2.  # noqa: E501

        Device protocol:    `H.323` - H.323.    `SIP` - SIP.  # noqa: E501

        :return: The protocol of this TheH323SIPDeviceObject2.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TheH323SIPDeviceObject2.

        Device protocol:    `H.323` - H.323.    `SIP` - SIP.  # noqa: E501

        :param protocol: The protocol of this TheH323SIPDeviceObject2.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["H.323", "SIP"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

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
        if issubclass(TheH323SIPDeviceObject2, dict):
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
        if not isinstance(other, TheH323SIPDeviceObject2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other