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

class InlineResponse2002InSession(object):
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
        'custom_data_center_regions': 'bool',
        'data_center_regions': 'list[str]',
        'unchecked_data_center_regions': 'list[str]',
        'p2p_connetion': 'bool',
        'p2p_ports': 'bool',
        'ports_range': 'str',
        'dscp_audio': 'int',
        'dscp_marking': 'bool',
        'dscp_video': 'int',
        'dscp_dual': 'bool',
        'subsession': 'bool'
    }

    attribute_map = {
        'custom_data_center_regions': 'custom_data_center_regions',
        'data_center_regions': 'data_center_regions',
        'unchecked_data_center_regions': 'unchecked_data_center_regions',
        'p2p_connetion': 'p2p_connetion',
        'p2p_ports': 'p2p_ports',
        'ports_range': 'ports_range',
        'dscp_audio': 'dscp_audio',
        'dscp_marking': 'dscp_marking',
        'dscp_video': 'dscp_video',
        'dscp_dual': 'dscp_dual',
        'subsession': 'subsession'
    }

    def __init__(self, custom_data_center_regions=None, data_center_regions=None, unchecked_data_center_regions=None, p2p_connetion=None, p2p_ports=None, ports_range='', dscp_audio=56, dscp_marking=None, dscp_video=40, dscp_dual=None, subsession=None):  # noqa: E501
        """InlineResponse2002InSession - a model defined in Swagger"""  # noqa: E501
        self._custom_data_center_regions = None
        self._data_center_regions = None
        self._unchecked_data_center_regions = None
        self._p2p_connetion = None
        self._p2p_ports = None
        self._ports_range = None
        self._dscp_audio = None
        self._dscp_marking = None
        self._dscp_video = None
        self._dscp_dual = None
        self._subsession = None
        self.discriminator = None
        if custom_data_center_regions is not None:
            self.custom_data_center_regions = custom_data_center_regions
        if data_center_regions is not None:
            self.data_center_regions = data_center_regions
        if unchecked_data_center_regions is not None:
            self.unchecked_data_center_regions = unchecked_data_center_regions
        if p2p_connetion is not None:
            self.p2p_connetion = p2p_connetion
        if p2p_ports is not None:
            self.p2p_ports = p2p_ports
        if ports_range is not None:
            self.ports_range = ports_range
        if dscp_audio is not None:
            self.dscp_audio = dscp_audio
        if dscp_marking is not None:
            self.dscp_marking = dscp_marking
        if dscp_video is not None:
            self.dscp_video = dscp_video
        if dscp_dual is not None:
            self.dscp_dual = dscp_dual
        if subsession is not None:
            self.subsession = subsession

    @property
    def custom_data_center_regions(self):
        """Gets the custom_data_center_regions of this InlineResponse2002InSession.  # noqa: E501

        Whether custom [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-meetings-webinars) are in use.  * `true` - Users can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting real-time meeting traffic. The data center regions can be provided in the `data_center_regions` field.  * `false` - Only the default data center regions.  # noqa: E501

        :return: The custom_data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._custom_data_center_regions

    @custom_data_center_regions.setter
    def custom_data_center_regions(self, custom_data_center_regions):
        """Sets the custom_data_center_regions of this InlineResponse2002InSession.

        Whether custom [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-meetings-webinars) are in use.  * `true` - Users can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting real-time meeting traffic. The data center regions can be provided in the `data_center_regions` field.  * `false` - Only the default data center regions.  # noqa: E501

        :param custom_data_center_regions: The custom_data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._custom_data_center_regions = custom_data_center_regions

    @property
    def data_center_regions(self):
        """Gets the data_center_regions of this InlineResponse2002InSession.  # noqa: E501

        If the value of `custom_data_center_regions` is `true`, a comma-separated list of the selected custom [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list).  * `AU` - Australia. * `LA` - Latin America.  * `CA` - Canada.  * `CN` - China.  * `DE` - Germany.  * `HK` - Hong Kong SAR.  * `IN` - India.  * `IE` - Ireland.  * `TY` - Japan.  * `MX` - Mexico.  * `NL` - Netherlands.  * `SG` - Singapore.  * `US` - United States.  # noqa: E501

        :return: The data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_center_regions

    @data_center_regions.setter
    def data_center_regions(self, data_center_regions):
        """Sets the data_center_regions of this InlineResponse2002InSession.

        If the value of `custom_data_center_regions` is `true`, a comma-separated list of the selected custom [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list).  * `AU` - Australia. * `LA` - Latin America.  * `CA` - Canada.  * `CN` - China.  * `DE` - Germany.  * `HK` - Hong Kong SAR.  * `IN` - India.  * `IE` - Ireland.  * `TY` - Japan.  * `MX` - Mexico.  * `NL` - Netherlands.  * `SG` - Singapore.  * `US` - United States.  # noqa: E501

        :param data_center_regions: The data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AU", "LA", "CA", "CN", "DE", "HK", "IN", "IE", "TY", "MX", "NL", "SG", "US"]  # noqa: E501
        if not set(data_center_regions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `data_center_regions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(data_center_regions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._data_center_regions = data_center_regions

    @property
    def unchecked_data_center_regions(self):
        """Gets the unchecked_data_center_regions of this InlineResponse2002InSession.  # noqa: E501

        If the value of `custom_data_center_regions` is `true`, a comma-separated list the [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list) that are **not** selected.  * `EU` - Europe.  * `HK` - Hong Kong.  * `AU` - Australia.  * `IN` - India.  * `LA` - Latin America.  * `TY` - Tokyo.  * `CN` - China.  * `US` - United States.  * `CA` - Canada.  # noqa: E501

        :return: The unchecked_data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._unchecked_data_center_regions

    @unchecked_data_center_regions.setter
    def unchecked_data_center_regions(self, unchecked_data_center_regions):
        """Sets the unchecked_data_center_regions of this InlineResponse2002InSession.

        If the value of `custom_data_center_regions` is `true`, a comma-separated list the [data center regions](https://support.zoom.us/hc/en-us/articles/360059254691-Datacenter-abbreviation-list) that are **not** selected.  * `EU` - Europe.  * `HK` - Hong Kong.  * `AU` - Australia.  * `IN` - India.  * `LA` - Latin America.  * `TY` - Tokyo.  * `CN` - China.  * `US` - United States.  * `CA` - Canada.  # noqa: E501

        :param unchecked_data_center_regions: The unchecked_data_center_regions of this InlineResponse2002InSession.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["EU", "HK", "AU", "IN", "TY", "CN", "US", "CA", "DE", "NL", "LA"]  # noqa: E501
        if not set(unchecked_data_center_regions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `unchecked_data_center_regions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(unchecked_data_center_regions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._unchecked_data_center_regions = unchecked_data_center_regions

    @property
    def p2p_connetion(self):
        """Gets the p2p_connetion of this InlineResponse2002InSession.  # noqa: E501

        Whether to enable the [**Peer to Peer connection while only 2 people are in a meeting**](https://support.zoom.us/hc/en-us/articles/360061410851-Enabling-Peer-to-Peer-connection-for-2-people-in-a-meeting) setting.  # noqa: E501

        :return: The p2p_connetion of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._p2p_connetion

    @p2p_connetion.setter
    def p2p_connetion(self, p2p_connetion):
        """Sets the p2p_connetion of this InlineResponse2002InSession.

        Whether to enable the [**Peer to Peer connection while only 2 people are in a meeting**](https://support.zoom.us/hc/en-us/articles/360061410851-Enabling-Peer-to-Peer-connection-for-2-people-in-a-meeting) setting.  # noqa: E501

        :param p2p_connetion: The p2p_connetion of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._p2p_connetion = p2p_connetion

    @property
    def p2p_ports(self):
        """Gets the p2p_ports of this InlineResponse2002InSession.  # noqa: E501

        Whether to enable the **Listening ports range** setting.  # noqa: E501

        :return: The p2p_ports of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._p2p_ports

    @p2p_ports.setter
    def p2p_ports(self, p2p_ports):
        """Sets the p2p_ports of this InlineResponse2002InSession.

        Whether to enable the **Listening ports range** setting.  # noqa: E501

        :param p2p_ports: The p2p_ports of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._p2p_ports = p2p_ports

    @property
    def ports_range(self):
        """Gets the ports_range of this InlineResponse2002InSession.  # noqa: E501

        When the `p2p_ports` value is `true`, the value is a semi-colon list of the peer to peer listening ports range, between `1` to `65535`. This value defaults to an empty string.  # noqa: E501

        :return: The ports_range of this InlineResponse2002InSession.  # noqa: E501
        :rtype: str
        """
        return self._ports_range

    @ports_range.setter
    def ports_range(self, ports_range):
        """Sets the ports_range of this InlineResponse2002InSession.

        When the `p2p_ports` value is `true`, the value is a semi-colon list of the peer to peer listening ports range, between `1` to `65535`. This value defaults to an empty string.  # noqa: E501

        :param ports_range: The ports_range of this InlineResponse2002InSession.  # noqa: E501
        :type: str
        """

        self._ports_range = ports_range

    @property
    def dscp_audio(self):
        """Gets the dscp_audio of this InlineResponse2002InSession.  # noqa: E501

        The DSCP audio marking value. This value defaults to `56`.  # noqa: E501

        :return: The dscp_audio of this InlineResponse2002InSession.  # noqa: E501
        :rtype: int
        """
        return self._dscp_audio

    @dscp_audio.setter
    def dscp_audio(self, dscp_audio):
        """Sets the dscp_audio of this InlineResponse2002InSession.

        The DSCP audio marking value. This value defaults to `56`.  # noqa: E501

        :param dscp_audio: The dscp_audio of this InlineResponse2002InSession.  # noqa: E501
        :type: int
        """

        self._dscp_audio = dscp_audio

    @property
    def dscp_marking(self):
        """Gets the dscp_marking of this InlineResponse2002InSession.  # noqa: E501

        Whether to enable [differentiated services code point (DSCP)](https://en.wikipedia.org/wiki/Differentiated_services) marking.  # noqa: E501

        :return: The dscp_marking of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._dscp_marking

    @dscp_marking.setter
    def dscp_marking(self, dscp_marking):
        """Sets the dscp_marking of this InlineResponse2002InSession.

        Whether to enable [differentiated services code point (DSCP)](https://en.wikipedia.org/wiki/Differentiated_services) marking.  # noqa: E501

        :param dscp_marking: The dscp_marking of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._dscp_marking = dscp_marking

    @property
    def dscp_video(self):
        """Gets the dscp_video of this InlineResponse2002InSession.  # noqa: E501

        The DSCP video marking value. This value defaults to `40`.  # noqa: E501

        :return: The dscp_video of this InlineResponse2002InSession.  # noqa: E501
        :rtype: int
        """
        return self._dscp_video

    @dscp_video.setter
    def dscp_video(self, dscp_video):
        """Sets the dscp_video of this InlineResponse2002InSession.

        The DSCP video marking value. This value defaults to `40`.  # noqa: E501

        :param dscp_video: The dscp_video of this InlineResponse2002InSession.  # noqa: E501
        :type: int
        """

        self._dscp_video = dscp_video

    @property
    def dscp_dual(self):
        """Gets the dscp_dual of this InlineResponse2002InSession.  # noqa: E501

        Whether to use the differentiated services code point classifiers ('dscp_video', 'dscp_audio') in the dual way (incoming and outgoing).  # noqa: E501

        :return: The dscp_dual of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._dscp_dual

    @dscp_dual.setter
    def dscp_dual(self, dscp_dual):
        """Sets the dscp_dual of this InlineResponse2002InSession.

        Whether to use the differentiated services code point classifiers ('dscp_video', 'dscp_audio') in the dual way (incoming and outgoing).  # noqa: E501

        :param dscp_dual: The dscp_dual of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._dscp_dual = dscp_dual

    @property
    def subsession(self):
        """Gets the subsession of this InlineResponse2002InSession.  # noqa: E501

        Allow host to split meeting participants into separate, smaller rooms.  # noqa: E501

        :return: The subsession of this InlineResponse2002InSession.  # noqa: E501
        :rtype: bool
        """
        return self._subsession

    @subsession.setter
    def subsession(self, subsession):
        """Sets the subsession of this InlineResponse2002InSession.

        Allow host to split meeting participants into separate, smaller rooms.  # noqa: E501

        :param subsession: The subsession of this InlineResponse2002InSession.  # noqa: E501
        :type: bool
        """

        self._subsession = subsession

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
        if issubclass(InlineResponse2002InSession, dict):
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
        if not isinstance(other, InlineResponse2002InSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
