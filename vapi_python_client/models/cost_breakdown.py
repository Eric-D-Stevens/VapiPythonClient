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

class CostBreakdown(object):
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
        'transport': 'float',
        'stt': 'float',
        'llm': 'float',
        'tts': 'float',
        'vapi': 'float',
        'total': 'float',
        'llm_prompt_tokens': 'float',
        'llm_completion_tokens': 'float',
        'tts_characters': 'float',
        'analysis_cost_breakdown': 'AllOfCostBreakdownAnalysisCostBreakdown'
    }

    attribute_map = {
        'transport': 'transport',
        'stt': 'stt',
        'llm': 'llm',
        'tts': 'tts',
        'vapi': 'vapi',
        'total': 'total',
        'llm_prompt_tokens': 'llmPromptTokens',
        'llm_completion_tokens': 'llmCompletionTokens',
        'tts_characters': 'ttsCharacters',
        'analysis_cost_breakdown': 'analysisCostBreakdown'
    }

    def __init__(self, transport=None, stt=None, llm=None, tts=None, vapi=None, total=None, llm_prompt_tokens=None, llm_completion_tokens=None, tts_characters=None, analysis_cost_breakdown=None):  # noqa: E501
        """CostBreakdown - a model defined in Swagger"""  # noqa: E501
        self._transport = None
        self._stt = None
        self._llm = None
        self._tts = None
        self._vapi = None
        self._total = None
        self._llm_prompt_tokens = None
        self._llm_completion_tokens = None
        self._tts_characters = None
        self._analysis_cost_breakdown = None
        self.discriminator = None
        if transport is not None:
            self.transport = transport
        if stt is not None:
            self.stt = stt
        if llm is not None:
            self.llm = llm
        if tts is not None:
            self.tts = tts
        if vapi is not None:
            self.vapi = vapi
        if total is not None:
            self.total = total
        if llm_prompt_tokens is not None:
            self.llm_prompt_tokens = llm_prompt_tokens
        if llm_completion_tokens is not None:
            self.llm_completion_tokens = llm_completion_tokens
        if tts_characters is not None:
            self.tts_characters = tts_characters
        if analysis_cost_breakdown is not None:
            self.analysis_cost_breakdown = analysis_cost_breakdown

    @property
    def transport(self):
        """Gets the transport of this CostBreakdown.  # noqa: E501

        This is the cost of the transport provider, like Twilio or Vonage.  # noqa: E501

        :return: The transport of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this CostBreakdown.

        This is the cost of the transport provider, like Twilio or Vonage.  # noqa: E501

        :param transport: The transport of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._transport = transport

    @property
    def stt(self):
        """Gets the stt of this CostBreakdown.  # noqa: E501

        This is the cost of the speech-to-text service.  # noqa: E501

        :return: The stt of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._stt

    @stt.setter
    def stt(self, stt):
        """Sets the stt of this CostBreakdown.

        This is the cost of the speech-to-text service.  # noqa: E501

        :param stt: The stt of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._stt = stt

    @property
    def llm(self):
        """Gets the llm of this CostBreakdown.  # noqa: E501

        This is the cost of the language model.  # noqa: E501

        :return: The llm of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._llm

    @llm.setter
    def llm(self, llm):
        """Sets the llm of this CostBreakdown.

        This is the cost of the language model.  # noqa: E501

        :param llm: The llm of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._llm = llm

    @property
    def tts(self):
        """Gets the tts of this CostBreakdown.  # noqa: E501

        This is the cost of the text-to-speech service.  # noqa: E501

        :return: The tts of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._tts

    @tts.setter
    def tts(self, tts):
        """Sets the tts of this CostBreakdown.

        This is the cost of the text-to-speech service.  # noqa: E501

        :param tts: The tts of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._tts = tts

    @property
    def vapi(self):
        """Gets the vapi of this CostBreakdown.  # noqa: E501

        This is the cost of Vapi.  # noqa: E501

        :return: The vapi of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._vapi

    @vapi.setter
    def vapi(self, vapi):
        """Sets the vapi of this CostBreakdown.

        This is the cost of Vapi.  # noqa: E501

        :param vapi: The vapi of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._vapi = vapi

    @property
    def total(self):
        """Gets the total of this CostBreakdown.  # noqa: E501

        This is the total cost of the call.  # noqa: E501

        :return: The total of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CostBreakdown.

        This is the total cost of the call.  # noqa: E501

        :param total: The total of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def llm_prompt_tokens(self):
        """Gets the llm_prompt_tokens of this CostBreakdown.  # noqa: E501

        This is the LLM prompt tokens used for the call.  # noqa: E501

        :return: The llm_prompt_tokens of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._llm_prompt_tokens

    @llm_prompt_tokens.setter
    def llm_prompt_tokens(self, llm_prompt_tokens):
        """Sets the llm_prompt_tokens of this CostBreakdown.

        This is the LLM prompt tokens used for the call.  # noqa: E501

        :param llm_prompt_tokens: The llm_prompt_tokens of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._llm_prompt_tokens = llm_prompt_tokens

    @property
    def llm_completion_tokens(self):
        """Gets the llm_completion_tokens of this CostBreakdown.  # noqa: E501

        This is the LLM completion tokens used for the call.  # noqa: E501

        :return: The llm_completion_tokens of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._llm_completion_tokens

    @llm_completion_tokens.setter
    def llm_completion_tokens(self, llm_completion_tokens):
        """Sets the llm_completion_tokens of this CostBreakdown.

        This is the LLM completion tokens used for the call.  # noqa: E501

        :param llm_completion_tokens: The llm_completion_tokens of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._llm_completion_tokens = llm_completion_tokens

    @property
    def tts_characters(self):
        """Gets the tts_characters of this CostBreakdown.  # noqa: E501

        This is the TTS characters used for the call.  # noqa: E501

        :return: The tts_characters of this CostBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._tts_characters

    @tts_characters.setter
    def tts_characters(self, tts_characters):
        """Sets the tts_characters of this CostBreakdown.

        This is the TTS characters used for the call.  # noqa: E501

        :param tts_characters: The tts_characters of this CostBreakdown.  # noqa: E501
        :type: float
        """

        self._tts_characters = tts_characters

    @property
    def analysis_cost_breakdown(self):
        """Gets the analysis_cost_breakdown of this CostBreakdown.  # noqa: E501

        This is the cost of the analysis.  # noqa: E501

        :return: The analysis_cost_breakdown of this CostBreakdown.  # noqa: E501
        :rtype: AllOfCostBreakdownAnalysisCostBreakdown
        """
        return self._analysis_cost_breakdown

    @analysis_cost_breakdown.setter
    def analysis_cost_breakdown(self, analysis_cost_breakdown):
        """Sets the analysis_cost_breakdown of this CostBreakdown.

        This is the cost of the analysis.  # noqa: E501

        :param analysis_cost_breakdown: The analysis_cost_breakdown of this CostBreakdown.  # noqa: E501
        :type: AllOfCostBreakdownAnalysisCostBreakdown
        """

        self._analysis_cost_breakdown = analysis_cost_breakdown

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
        if issubclass(CostBreakdown, dict):
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
        if not isinstance(other, CostBreakdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
