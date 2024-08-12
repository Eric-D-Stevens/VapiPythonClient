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

class PerplexityAIModel(object):
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
        'messages': 'list[OpenAIMessage]',
        'tools': 'list[OneOfPerplexityAIModelToolsItems]',
        'tool_ids': 'list[str]',
        'provider': 'str',
        'model': 'str',
        'temperature': 'float',
        'knowledge_base': 'AllOfPerplexityAIModelKnowledgeBase',
        'max_tokens': 'float',
        'emotion_recognition_enabled': 'bool',
        'num_fast_turns': 'float'
    }

    attribute_map = {
        'messages': 'messages',
        'tools': 'tools',
        'tool_ids': 'toolIds',
        'provider': 'provider',
        'model': 'model',
        'temperature': 'temperature',
        'knowledge_base': 'knowledgeBase',
        'max_tokens': 'maxTokens',
        'emotion_recognition_enabled': 'emotionRecognitionEnabled',
        'num_fast_turns': 'numFastTurns'
    }

    def __init__(self, messages=None, tools=None, tool_ids=None, provider=None, model=None, temperature=None, knowledge_base=None, max_tokens=None, emotion_recognition_enabled=None, num_fast_turns=None):  # noqa: E501
        """PerplexityAIModel - a model defined in Swagger"""  # noqa: E501
        self._messages = None
        self._tools = None
        self._tool_ids = None
        self._provider = None
        self._model = None
        self._temperature = None
        self._knowledge_base = None
        self._max_tokens = None
        self._emotion_recognition_enabled = None
        self._num_fast_turns = None
        self.discriminator = None
        if messages is not None:
            self.messages = messages
        if tools is not None:
            self.tools = tools
        if tool_ids is not None:
            self.tool_ids = tool_ids
        self.provider = provider
        self.model = model
        if temperature is not None:
            self.temperature = temperature
        if knowledge_base is not None:
            self.knowledge_base = knowledge_base
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if emotion_recognition_enabled is not None:
            self.emotion_recognition_enabled = emotion_recognition_enabled
        if num_fast_turns is not None:
            self.num_fast_turns = num_fast_turns

    @property
    def messages(self):
        """Gets the messages of this PerplexityAIModel.  # noqa: E501

        This is the starting state for the conversation.  # noqa: E501

        :return: The messages of this PerplexityAIModel.  # noqa: E501
        :rtype: list[OpenAIMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this PerplexityAIModel.

        This is the starting state for the conversation.  # noqa: E501

        :param messages: The messages of this PerplexityAIModel.  # noqa: E501
        :type: list[OpenAIMessage]
        """

        self._messages = messages

    @property
    def tools(self):
        """Gets the tools of this PerplexityAIModel.  # noqa: E501

        These are the tools that the assistant can use during the call. To use existing tools, use `toolIds`.  Both `tools` and `toolIds` can be used together.  # noqa: E501

        :return: The tools of this PerplexityAIModel.  # noqa: E501
        :rtype: list[OneOfPerplexityAIModelToolsItems]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this PerplexityAIModel.

        These are the tools that the assistant can use during the call. To use existing tools, use `toolIds`.  Both `tools` and `toolIds` can be used together.  # noqa: E501

        :param tools: The tools of this PerplexityAIModel.  # noqa: E501
        :type: list[OneOfPerplexityAIModelToolsItems]
        """

        self._tools = tools

    @property
    def tool_ids(self):
        """Gets the tool_ids of this PerplexityAIModel.  # noqa: E501

        These are the tools that the assistant can use during the call. To use transient tools, use `tools`.  Both `tools` and `toolIds` can be used together.  # noqa: E501

        :return: The tool_ids of this PerplexityAIModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tool_ids

    @tool_ids.setter
    def tool_ids(self, tool_ids):
        """Sets the tool_ids of this PerplexityAIModel.

        These are the tools that the assistant can use during the call. To use transient tools, use `tools`.  Both `tools` and `toolIds` can be used together.  # noqa: E501

        :param tool_ids: The tool_ids of this PerplexityAIModel.  # noqa: E501
        :type: list[str]
        """

        self._tool_ids = tool_ids

    @property
    def provider(self):
        """Gets the provider of this PerplexityAIModel.  # noqa: E501


        :return: The provider of this PerplexityAIModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this PerplexityAIModel.


        :param provider: The provider of this PerplexityAIModel.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["perplexity-ai"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def model(self):
        """Gets the model of this PerplexityAIModel.  # noqa: E501

        This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b  # noqa: E501

        :return: The model of this PerplexityAIModel.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PerplexityAIModel.

        This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b  # noqa: E501

        :param model: The model of this PerplexityAIModel.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def temperature(self):
        """Gets the temperature of this PerplexityAIModel.  # noqa: E501

        This is the temperature that will be used for calls. Default is 0 to leverage caching for lower latency.  # noqa: E501

        :return: The temperature of this PerplexityAIModel.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this PerplexityAIModel.

        This is the temperature that will be used for calls. Default is 0 to leverage caching for lower latency.  # noqa: E501

        :param temperature: The temperature of this PerplexityAIModel.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def knowledge_base(self):
        """Gets the knowledge_base of this PerplexityAIModel.  # noqa: E501

        These are the options for the knowledge base.  # noqa: E501

        :return: The knowledge_base of this PerplexityAIModel.  # noqa: E501
        :rtype: AllOfPerplexityAIModelKnowledgeBase
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base):
        """Sets the knowledge_base of this PerplexityAIModel.

        These are the options for the knowledge base.  # noqa: E501

        :param knowledge_base: The knowledge_base of this PerplexityAIModel.  # noqa: E501
        :type: AllOfPerplexityAIModelKnowledgeBase
        """

        self._knowledge_base = knowledge_base

    @property
    def max_tokens(self):
        """Gets the max_tokens of this PerplexityAIModel.  # noqa: E501

        This is the max number of tokens that the assistant will be allowed to generate in each turn of the conversation. Default is 250.  # noqa: E501

        :return: The max_tokens of this PerplexityAIModel.  # noqa: E501
        :rtype: float
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """Sets the max_tokens of this PerplexityAIModel.

        This is the max number of tokens that the assistant will be allowed to generate in each turn of the conversation. Default is 250.  # noqa: E501

        :param max_tokens: The max_tokens of this PerplexityAIModel.  # noqa: E501
        :type: float
        """

        self._max_tokens = max_tokens

    @property
    def emotion_recognition_enabled(self):
        """Gets the emotion_recognition_enabled of this PerplexityAIModel.  # noqa: E501

        This determines whether we detect user's emotion while they speak and send it as an additional info to model.  Default `false` because the model is usually are good at understanding the user's emotion from text.  @default false  # noqa: E501

        :return: The emotion_recognition_enabled of this PerplexityAIModel.  # noqa: E501
        :rtype: bool
        """
        return self._emotion_recognition_enabled

    @emotion_recognition_enabled.setter
    def emotion_recognition_enabled(self, emotion_recognition_enabled):
        """Sets the emotion_recognition_enabled of this PerplexityAIModel.

        This determines whether we detect user's emotion while they speak and send it as an additional info to model.  Default `false` because the model is usually are good at understanding the user's emotion from text.  @default false  # noqa: E501

        :param emotion_recognition_enabled: The emotion_recognition_enabled of this PerplexityAIModel.  # noqa: E501
        :type: bool
        """

        self._emotion_recognition_enabled = emotion_recognition_enabled

    @property
    def num_fast_turns(self):
        """Gets the num_fast_turns of this PerplexityAIModel.  # noqa: E501

        This sets how many turns at the start of the conversation to use a smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if provider is openai.  Default is 0.  @default 0  # noqa: E501

        :return: The num_fast_turns of this PerplexityAIModel.  # noqa: E501
        :rtype: float
        """
        return self._num_fast_turns

    @num_fast_turns.setter
    def num_fast_turns(self, num_fast_turns):
        """Sets the num_fast_turns of this PerplexityAIModel.

        This sets how many turns at the start of the conversation to use a smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if provider is openai.  Default is 0.  @default 0  # noqa: E501

        :param num_fast_turns: The num_fast_turns of this PerplexityAIModel.  # noqa: E501
        :type: float
        """

        self._num_fast_turns = num_fast_turns

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
        if issubclass(PerplexityAIModel, dict):
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
        if not isinstance(other, PerplexityAIModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
