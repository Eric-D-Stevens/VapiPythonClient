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

class ToolCallResultMessage(object):
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
        'role': 'str',
        'tool_call_id': 'str',
        'name': 'str',
        'result': 'str',
        'time': 'float',
        'seconds_from_start': 'float'
    }

    attribute_map = {
        'role': 'role',
        'tool_call_id': 'toolCallId',
        'name': 'name',
        'result': 'result',
        'time': 'time',
        'seconds_from_start': 'secondsFromStart'
    }

    def __init__(self, role=None, tool_call_id=None, name=None, result=None, time=None, seconds_from_start=None):  # noqa: E501
        """ToolCallResultMessage - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._tool_call_id = None
        self._name = None
        self._result = None
        self._time = None
        self._seconds_from_start = None
        self.discriminator = None
        self.role = role
        self.tool_call_id = tool_call_id
        self.name = name
        self.result = result
        self.time = time
        self.seconds_from_start = seconds_from_start

    @property
    def role(self):
        """Gets the role of this ToolCallResultMessage.  # noqa: E501

        The role of the tool call result in the conversation.  # noqa: E501

        :return: The role of this ToolCallResultMessage.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ToolCallResultMessage.

        The role of the tool call result in the conversation.  # noqa: E501

        :param role: The role of this ToolCallResultMessage.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def tool_call_id(self):
        """Gets the tool_call_id of this ToolCallResultMessage.  # noqa: E501

        The ID of the tool call.  # noqa: E501

        :return: The tool_call_id of this ToolCallResultMessage.  # noqa: E501
        :rtype: str
        """
        return self._tool_call_id

    @tool_call_id.setter
    def tool_call_id(self, tool_call_id):
        """Sets the tool_call_id of this ToolCallResultMessage.

        The ID of the tool call.  # noqa: E501

        :param tool_call_id: The tool_call_id of this ToolCallResultMessage.  # noqa: E501
        :type: str
        """
        if tool_call_id is None:
            raise ValueError("Invalid value for `tool_call_id`, must not be `None`")  # noqa: E501

        self._tool_call_id = tool_call_id

    @property
    def name(self):
        """Gets the name of this ToolCallResultMessage.  # noqa: E501

        The name of the tool that returned the result.  # noqa: E501

        :return: The name of this ToolCallResultMessage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ToolCallResultMessage.

        The name of the tool that returned the result.  # noqa: E501

        :param name: The name of this ToolCallResultMessage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def result(self):
        """Gets the result of this ToolCallResultMessage.  # noqa: E501

        The result of the tool call in JSON format.  # noqa: E501

        :return: The result of this ToolCallResultMessage.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ToolCallResultMessage.

        The result of the tool call in JSON format.  # noqa: E501

        :param result: The result of this ToolCallResultMessage.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def time(self):
        """Gets the time of this ToolCallResultMessage.  # noqa: E501

        The timestamp when the message was sent.  # noqa: E501

        :return: The time of this ToolCallResultMessage.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ToolCallResultMessage.

        The timestamp when the message was sent.  # noqa: E501

        :param time: The time of this ToolCallResultMessage.  # noqa: E501
        :type: float
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def seconds_from_start(self):
        """Gets the seconds_from_start of this ToolCallResultMessage.  # noqa: E501

        The number of seconds from the start of the conversation.  # noqa: E501

        :return: The seconds_from_start of this ToolCallResultMessage.  # noqa: E501
        :rtype: float
        """
        return self._seconds_from_start

    @seconds_from_start.setter
    def seconds_from_start(self, seconds_from_start):
        """Sets the seconds_from_start of this ToolCallResultMessage.

        The number of seconds from the start of the conversation.  # noqa: E501

        :param seconds_from_start: The seconds_from_start of this ToolCallResultMessage.  # noqa: E501
        :type: float
        """
        if seconds_from_start is None:
            raise ValueError("Invalid value for `seconds_from_start`, must not be `None`")  # noqa: E501

        self._seconds_from_start = seconds_from_start

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
        if issubclass(ToolCallResultMessage, dict):
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
        if not isinstance(other, ToolCallResultMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
