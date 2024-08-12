# coding: utf-8

"""
    Vapi API

    API for building voice assistants  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SipTrunkGateway(object):
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
        'ip': 'str',
        'port': 'float',
        'netmask': 'float',
        'inbound_enabled': 'bool',
        'outbound_enabled': 'bool',
        'outbound_protocol': 'str',
        'options_ping_enabled': 'bool'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'netmask': 'netmask',
        'inbound_enabled': 'inboundEnabled',
        'outbound_enabled': 'outboundEnabled',
        'outbound_protocol': 'outboundProtocol',
        'options_ping_enabled': 'optionsPingEnabled'
    }

    def __init__(self, ip=None, port=None, netmask=None, inbound_enabled=None, outbound_enabled=None, outbound_protocol=None, options_ping_enabled=None):  # noqa: E501
        """SipTrunkGateway - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._port = None
        self._netmask = None
        self._inbound_enabled = None
        self._outbound_enabled = None
        self._outbound_protocol = None
        self._options_ping_enabled = None
        self.discriminator = None
        self.ip = ip
        self.port = port
        if netmask is not None:
            self.netmask = netmask
        if inbound_enabled is not None:
            self.inbound_enabled = inbound_enabled
        if outbound_enabled is not None:
            self.outbound_enabled = outbound_enabled
        if outbound_protocol is not None:
            self.outbound_protocol = outbound_protocol
        if options_ping_enabled is not None:
            self.options_ping_enabled = options_ping_enabled

    @property
    def ip(self):
        """Gets the ip of this SipTrunkGateway.  # noqa: E501

        This is the IPv4 address of the gateway.  # noqa: E501

        :return: The ip of this SipTrunkGateway.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SipTrunkGateway.

        This is the IPv4 address of the gateway.  # noqa: E501

        :param ip: The ip of this SipTrunkGateway.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this SipTrunkGateway.  # noqa: E501

        This is the port number of the gateway. Default is 5060.  @default 5060  # noqa: E501

        :return: The port of this SipTrunkGateway.  # noqa: E501
        :rtype: float
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SipTrunkGateway.

        This is the port number of the gateway. Default is 5060.  @default 5060  # noqa: E501

        :param port: The port of this SipTrunkGateway.  # noqa: E501
        :type: float
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def netmask(self):
        """Gets the netmask of this SipTrunkGateway.  # noqa: E501

        This is the netmask of the gateway.  # noqa: E501

        :return: The netmask of this SipTrunkGateway.  # noqa: E501
        :rtype: float
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this SipTrunkGateway.

        This is the netmask of the gateway.  # noqa: E501

        :param netmask: The netmask of this SipTrunkGateway.  # noqa: E501
        :type: float
        """

        self._netmask = netmask

    @property
    def inbound_enabled(self):
        """Gets the inbound_enabled of this SipTrunkGateway.  # noqa: E501

        This is whether inbound calls are allowed from this gateway. Default is true.  @default true  # noqa: E501

        :return: The inbound_enabled of this SipTrunkGateway.  # noqa: E501
        :rtype: bool
        """
        return self._inbound_enabled

    @inbound_enabled.setter
    def inbound_enabled(self, inbound_enabled):
        """Sets the inbound_enabled of this SipTrunkGateway.

        This is whether inbound calls are allowed from this gateway. Default is true.  @default true  # noqa: E501

        :param inbound_enabled: The inbound_enabled of this SipTrunkGateway.  # noqa: E501
        :type: bool
        """

        self._inbound_enabled = inbound_enabled

    @property
    def outbound_enabled(self):
        """Gets the outbound_enabled of this SipTrunkGateway.  # noqa: E501

        This is whether outbound calls should be sent to this gateway. Default is true.  @default true  # noqa: E501

        :return: The outbound_enabled of this SipTrunkGateway.  # noqa: E501
        :rtype: bool
        """
        return self._outbound_enabled

    @outbound_enabled.setter
    def outbound_enabled(self, outbound_enabled):
        """Sets the outbound_enabled of this SipTrunkGateway.

        This is whether outbound calls should be sent to this gateway. Default is true.  @default true  # noqa: E501

        :param outbound_enabled: The outbound_enabled of this SipTrunkGateway.  # noqa: E501
        :type: bool
        """

        self._outbound_enabled = outbound_enabled

    @property
    def outbound_protocol(self):
        """Gets the outbound_protocol of this SipTrunkGateway.  # noqa: E501

        This is the protocol to use for SIP signaling outbound calls. Default is udp.  @default udp  # noqa: E501

        :return: The outbound_protocol of this SipTrunkGateway.  # noqa: E501
        :rtype: str
        """
        return self._outbound_protocol

    @outbound_protocol.setter
    def outbound_protocol(self, outbound_protocol):
        """Sets the outbound_protocol of this SipTrunkGateway.

        This is the protocol to use for SIP signaling outbound calls. Default is udp.  @default udp  # noqa: E501

        :param outbound_protocol: The outbound_protocol of this SipTrunkGateway.  # noqa: E501
        :type: str
        """
        allowed_values = ["tls/srtp", "tcp", "tls", "udp"]  # noqa: E501
        if outbound_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `outbound_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(outbound_protocol, allowed_values)
            )

        self._outbound_protocol = outbound_protocol

    @property
    def options_ping_enabled(self):
        """Gets the options_ping_enabled of this SipTrunkGateway.  # noqa: E501

        This is whether to send options ping to the gateway. This can be used to check if the gateway is reachable. Default is false.  This is useful for high availability setups where you want to check if the gateway is reachable before routing calls to it. Note, if no gateway for a trunk is reachable, outbound calls will be rejected.  @default false  # noqa: E501

        :return: The options_ping_enabled of this SipTrunkGateway.  # noqa: E501
        :rtype: bool
        """
        return self._options_ping_enabled

    @options_ping_enabled.setter
    def options_ping_enabled(self, options_ping_enabled):
        """Sets the options_ping_enabled of this SipTrunkGateway.

        This is whether to send options ping to the gateway. This can be used to check if the gateway is reachable. Default is false.  This is useful for high availability setups where you want to check if the gateway is reachable before routing calls to it. Note, if no gateway for a trunk is reachable, outbound calls will be rejected.  @default false  # noqa: E501

        :param options_ping_enabled: The options_ping_enabled of this SipTrunkGateway.  # noqa: E501
        :type: bool
        """

        self._options_ping_enabled = options_ping_enabled

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
        if issubclass(SipTrunkGateway, dict):
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
        if not isinstance(other, SipTrunkGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
