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

class CreateDtmfToolDTO(object):
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
        '_async': 'bool',
        'messages': 'list[OneOfCreateDtmfToolDTOMessagesItems]',
        'type': 'str',
        'function': 'AllOfCreateDtmfToolDTOFunction',
        'server': 'AllOfCreateDtmfToolDTOServer'
    }

    attribute_map = {
        '_async': 'async',
        'messages': 'messages',
        'type': 'type',
        'function': 'function',
        'server': 'server'
    }

    def __init__(self, _async=None, messages=None, type=None, function=None, server=None):  # noqa: E501
        """CreateDtmfToolDTO - a model defined in Swagger"""  # noqa: E501
        self.__async = None
        self._messages = None
        self._type = None
        self._function = None
        self._server = None
        self.discriminator = None
        if _async is not None:
            self._async = _async
        if messages is not None:
            self.messages = messages
        self.type = type
        if function is not None:
            self.function = function
        if server is not None:
            self.server = server

    @property
    def _async(self):
        """Gets the _async of this CreateDtmfToolDTO.  # noqa: E501

        This determines if the tool is async.  If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.  If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.  Defaults to synchronous (`false`).  # noqa: E501

        :return: The _async of this CreateDtmfToolDTO.  # noqa: E501
        :rtype: bool
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        """Sets the _async of this CreateDtmfToolDTO.

        This determines if the tool is async.  If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.  If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.  Defaults to synchronous (`false`).  # noqa: E501

        :param _async: The _async of this CreateDtmfToolDTO.  # noqa: E501
        :type: bool
        """

        self.__async = _async

    @property
    def messages(self):
        """Gets the messages of this CreateDtmfToolDTO.  # noqa: E501

        These are the messages that will be spoken to the user as the tool is running.  For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.  # noqa: E501

        :return: The messages of this CreateDtmfToolDTO.  # noqa: E501
        :rtype: list[OneOfCreateDtmfToolDTOMessagesItems]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this CreateDtmfToolDTO.

        These are the messages that will be spoken to the user as the tool is running.  For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.  # noqa: E501

        :param messages: The messages of this CreateDtmfToolDTO.  # noqa: E501
        :type: list[OneOfCreateDtmfToolDTOMessagesItems]
        """

        self._messages = messages

    @property
    def type(self):
        """Gets the type of this CreateDtmfToolDTO.  # noqa: E501

        The type of tool. \"dtmf\" for DTMF tool.  # noqa: E501

        :return: The type of this CreateDtmfToolDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDtmfToolDTO.

        The type of tool. \"dtmf\" for DTMF tool.  # noqa: E501

        :param type: The type of this CreateDtmfToolDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["dtmf"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def function(self):
        """Gets the function of this CreateDtmfToolDTO.  # noqa: E501

        This is the function definition of the tool.  For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.  An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument \"reason\". Then, in `messages` array, you can have many \"request-complete\" messages. One of these messages will be triggered if the `messages[].conditions` matches the \"reason\" argument.  # noqa: E501

        :return: The function of this CreateDtmfToolDTO.  # noqa: E501
        :rtype: AllOfCreateDtmfToolDTOFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this CreateDtmfToolDTO.

        This is the function definition of the tool.  For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.  An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument \"reason\". Then, in `messages` array, you can have many \"request-complete\" messages. One of these messages will be triggered if the `messages[].conditions` matches the \"reason\" argument.  # noqa: E501

        :param function: The function of this CreateDtmfToolDTO.  # noqa: E501
        :type: AllOfCreateDtmfToolDTOFunction
        """

        self._function = function

    @property
    def server(self):
        """Gets the server of this CreateDtmfToolDTO.  # noqa: E501

        This is the server that will be hit when this tool is requested by the model.  All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.  This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.  # noqa: E501

        :return: The server of this CreateDtmfToolDTO.  # noqa: E501
        :rtype: AllOfCreateDtmfToolDTOServer
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateDtmfToolDTO.

        This is the server that will be hit when this tool is requested by the model.  All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.  This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.  # noqa: E501

        :param server: The server of this CreateDtmfToolDTO.  # noqa: E501
        :type: AllOfCreateDtmfToolDTOServer
        """

        self._server = server

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
        if issubclass(CreateDtmfToolDTO, dict):
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
        if not isinstance(other, CreateDtmfToolDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
