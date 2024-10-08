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

class CreateToolCallBlockDTO(object):
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
        'messages': 'list[OneOfCreateToolCallBlockDTOMessagesItems]',
        'input_schema': 'AllOfCreateToolCallBlockDTOInputSchema',
        'output_schema': 'AllOfCreateToolCallBlockDTOOutputSchema',
        'type': 'str',
        'tool': 'OneOfCreateToolCallBlockDTOTool',
        'tool_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'messages': 'messages',
        'input_schema': 'inputSchema',
        'output_schema': 'outputSchema',
        'type': 'type',
        'tool': 'tool',
        'tool_id': 'toolId',
        'name': 'name'
    }

    def __init__(self, messages=None, input_schema=None, output_schema=None, type=None, tool=None, tool_id=None, name=None):  # noqa: E501
        """CreateToolCallBlockDTO - a model defined in Swagger"""  # noqa: E501
        self._messages = None
        self._input_schema = None
        self._output_schema = None
        self._type = None
        self._tool = None
        self._tool_id = None
        self._name = None
        self.discriminator = None
        if messages is not None:
            self.messages = messages
        if input_schema is not None:
            self.input_schema = input_schema
        if output_schema is not None:
            self.output_schema = output_schema
        self.type = type
        if tool is not None:
            self.tool = tool
        if tool_id is not None:
            self.tool_id = tool_id
        if name is not None:
            self.name = name

    @property
    def messages(self):
        """Gets the messages of this CreateToolCallBlockDTO.  # noqa: E501

        These are the pre-configured messages that will be spoken to the user while the block is running.  # noqa: E501

        :return: The messages of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: list[OneOfCreateToolCallBlockDTOMessagesItems]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this CreateToolCallBlockDTO.

        These are the pre-configured messages that will be spoken to the user while the block is running.  # noqa: E501

        :param messages: The messages of this CreateToolCallBlockDTO.  # noqa: E501
        :type: list[OneOfCreateToolCallBlockDTOMessagesItems]
        """

        self._messages = messages

    @property
    def input_schema(self):
        """Gets the input_schema of this CreateToolCallBlockDTO.  # noqa: E501

        This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`  These are accessible as variables: - ({{input.propertyName}}) in context of the block execution (step) - ({{stepName.input.propertyName}}) in context of the workflow  # noqa: E501

        :return: The input_schema of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: AllOfCreateToolCallBlockDTOInputSchema
        """
        return self._input_schema

    @input_schema.setter
    def input_schema(self, input_schema):
        """Sets the input_schema of this CreateToolCallBlockDTO.

        This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`  These are accessible as variables: - ({{input.propertyName}}) in context of the block execution (step) - ({{stepName.input.propertyName}}) in context of the workflow  # noqa: E501

        :param input_schema: The input_schema of this CreateToolCallBlockDTO.  # noqa: E501
        :type: AllOfCreateToolCallBlockDTOInputSchema
        """

        self._input_schema = input_schema

    @property
    def output_schema(self):
        """Gets the output_schema of this CreateToolCallBlockDTO.  # noqa: E501

        This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).  These are accessible as variables: - ({{output.propertyName}}) in context of the block execution (step) - ({{stepName.output.propertyName}}) in context of the workflow  # noqa: E501

        :return: The output_schema of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: AllOfCreateToolCallBlockDTOOutputSchema
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema):
        """Sets the output_schema of this CreateToolCallBlockDTO.

        This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).  These are accessible as variables: - ({{output.propertyName}}) in context of the block execution (step) - ({{stepName.output.propertyName}}) in context of the workflow  # noqa: E501

        :param output_schema: The output_schema of this CreateToolCallBlockDTO.  # noqa: E501
        :type: AllOfCreateToolCallBlockDTOOutputSchema
        """

        self._output_schema = output_schema

    @property
    def type(self):
        """Gets the type of this CreateToolCallBlockDTO.  # noqa: E501

        This block makes a tool call.  # noqa: E501

        :return: The type of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateToolCallBlockDTO.

        This block makes a tool call.  # noqa: E501

        :param type: The type of this CreateToolCallBlockDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["tool-call"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def tool(self):
        """Gets the tool of this CreateToolCallBlockDTO.  # noqa: E501

        This is the tool that the block will call. To use an existing tool, use `toolId`.  # noqa: E501

        :return: The tool of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: OneOfCreateToolCallBlockDTOTool
        """
        return self._tool

    @tool.setter
    def tool(self, tool):
        """Sets the tool of this CreateToolCallBlockDTO.

        This is the tool that the block will call. To use an existing tool, use `toolId`.  # noqa: E501

        :param tool: The tool of this CreateToolCallBlockDTO.  # noqa: E501
        :type: OneOfCreateToolCallBlockDTOTool
        """

        self._tool = tool

    @property
    def tool_id(self):
        """Gets the tool_id of this CreateToolCallBlockDTO.  # noqa: E501

        This is the id of the tool that the block will call. To use a transient tool, use `tool`.  # noqa: E501

        :return: The tool_id of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: str
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this CreateToolCallBlockDTO.

        This is the id of the tool that the block will call. To use a transient tool, use `tool`.  # noqa: E501

        :param tool_id: The tool_id of this CreateToolCallBlockDTO.  # noqa: E501
        :type: str
        """

        self._tool_id = tool_id

    @property
    def name(self):
        """Gets the name of this CreateToolCallBlockDTO.  # noqa: E501

        This is the name of the block. This is just for your reference.  # noqa: E501

        :return: The name of this CreateToolCallBlockDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateToolCallBlockDTO.

        This is the name of the block. This is just for your reference.  # noqa: E501

        :param name: The name of this CreateToolCallBlockDTO.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(CreateToolCallBlockDTO, dict):
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
        if not isinstance(other, CreateToolCallBlockDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
