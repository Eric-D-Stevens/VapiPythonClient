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

class NeetsVoice(object):
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
        'input_preprocessing_enabled': 'bool',
        'input_reformatting_enabled': 'bool',
        'input_min_characters': 'float',
        'input_punctuation_boundaries': 'list[str]',
        'filler_injection_enabled': 'bool',
        'provider': 'str',
        'voice_id': 'OneOfNeetsVoiceVoiceId'
    }

    attribute_map = {
        'input_preprocessing_enabled': 'inputPreprocessingEnabled',
        'input_reformatting_enabled': 'inputReformattingEnabled',
        'input_min_characters': 'inputMinCharacters',
        'input_punctuation_boundaries': 'inputPunctuationBoundaries',
        'filler_injection_enabled': 'fillerInjectionEnabled',
        'provider': 'provider',
        'voice_id': 'voiceId'
    }

    def __init__(self, input_preprocessing_enabled=None, input_reformatting_enabled=None, input_min_characters=None, input_punctuation_boundaries=None, filler_injection_enabled=None, provider=None, voice_id=None):  # noqa: E501
        """NeetsVoice - a model defined in Swagger"""  # noqa: E501
        self._input_preprocessing_enabled = None
        self._input_reformatting_enabled = None
        self._input_min_characters = None
        self._input_punctuation_boundaries = None
        self._filler_injection_enabled = None
        self._provider = None
        self._voice_id = None
        self.discriminator = None
        if input_preprocessing_enabled is not None:
            self.input_preprocessing_enabled = input_preprocessing_enabled
        if input_reformatting_enabled is not None:
            self.input_reformatting_enabled = input_reformatting_enabled
        if input_min_characters is not None:
            self.input_min_characters = input_min_characters
        if input_punctuation_boundaries is not None:
            self.input_punctuation_boundaries = input_punctuation_boundaries
        if filler_injection_enabled is not None:
            self.filler_injection_enabled = filler_injection_enabled
        self.provider = provider
        self.voice_id = voice_id

    @property
    def input_preprocessing_enabled(self):
        """Gets the input_preprocessing_enabled of this NeetsVoice.  # noqa: E501

        This determines whether the model output is preprocessed into chunks before being sent to the voice provider.  Default `true` because voice generation sounds better with chunking (and reformatting them).  To send every token from the model output directly to the voice provider and rely on the voice provider's audio generation logic, set this to `false`.  If disabled, vapi-provided audio control tokens like <flush /> will not work.  # noqa: E501

        :return: The input_preprocessing_enabled of this NeetsVoice.  # noqa: E501
        :rtype: bool
        """
        return self._input_preprocessing_enabled

    @input_preprocessing_enabled.setter
    def input_preprocessing_enabled(self, input_preprocessing_enabled):
        """Sets the input_preprocessing_enabled of this NeetsVoice.

        This determines whether the model output is preprocessed into chunks before being sent to the voice provider.  Default `true` because voice generation sounds better with chunking (and reformatting them).  To send every token from the model output directly to the voice provider and rely on the voice provider's audio generation logic, set this to `false`.  If disabled, vapi-provided audio control tokens like <flush /> will not work.  # noqa: E501

        :param input_preprocessing_enabled: The input_preprocessing_enabled of this NeetsVoice.  # noqa: E501
        :type: bool
        """

        self._input_preprocessing_enabled = input_preprocessing_enabled

    @property
    def input_reformatting_enabled(self):
        """Gets the input_reformatting_enabled of this NeetsVoice.  # noqa: E501

        This determines whether the chunk is reformatted before being sent to the voice provider. Many things are reformatted including phone numbers, emails and addresses to improve their enunciation.  Default `true` because voice generation sounds better with reformatting.  To disable chunk reformatting, set this to `false`.  To disable chunking completely, set `inputPreprocessingEnabled` to `false`.  # noqa: E501

        :return: The input_reformatting_enabled of this NeetsVoice.  # noqa: E501
        :rtype: bool
        """
        return self._input_reformatting_enabled

    @input_reformatting_enabled.setter
    def input_reformatting_enabled(self, input_reformatting_enabled):
        """Sets the input_reformatting_enabled of this NeetsVoice.

        This determines whether the chunk is reformatted before being sent to the voice provider. Many things are reformatted including phone numbers, emails and addresses to improve their enunciation.  Default `true` because voice generation sounds better with reformatting.  To disable chunk reformatting, set this to `false`.  To disable chunking completely, set `inputPreprocessingEnabled` to `false`.  # noqa: E501

        :param input_reformatting_enabled: The input_reformatting_enabled of this NeetsVoice.  # noqa: E501
        :type: bool
        """

        self._input_reformatting_enabled = input_reformatting_enabled

    @property
    def input_min_characters(self):
        """Gets the input_min_characters of this NeetsVoice.  # noqa: E501

        This is the minimum number of characters before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults to 30.  Increasing this value might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, increasing might be a good idea if you want to give voice provider bigger chunks so it can pronounce them better.  Decreasing this value might decrease latency but might also decrease quality if the voice provider struggles to pronounce the text correctly.  # noqa: E501

        :return: The input_min_characters of this NeetsVoice.  # noqa: E501
        :rtype: float
        """
        return self._input_min_characters

    @input_min_characters.setter
    def input_min_characters(self, input_min_characters):
        """Sets the input_min_characters of this NeetsVoice.

        This is the minimum number of characters before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults to 30.  Increasing this value might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, increasing might be a good idea if you want to give voice provider bigger chunks so it can pronounce them better.  Decreasing this value might decrease latency but might also decrease quality if the voice provider struggles to pronounce the text correctly.  # noqa: E501

        :param input_min_characters: The input_min_characters of this NeetsVoice.  # noqa: E501
        :type: float
        """

        self._input_min_characters = input_min_characters

    @property
    def input_punctuation_boundaries(self):
        """Gets the input_punctuation_boundaries of this NeetsVoice.  # noqa: E501

        These are the punctuations that are considered valid boundaries before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults are chosen differently for each provider.  Constraining the delimiters might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, constraining might be a good idea if you want to give voice provider longer chunks so it can sound less disjointed across chunks. Eg. ['.'].  # noqa: E501

        :return: The input_punctuation_boundaries of this NeetsVoice.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_punctuation_boundaries

    @input_punctuation_boundaries.setter
    def input_punctuation_boundaries(self, input_punctuation_boundaries):
        """Sets the input_punctuation_boundaries of this NeetsVoice.

        These are the punctuations that are considered valid boundaries before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults are chosen differently for each provider.  Constraining the delimiters might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, constraining might be a good idea if you want to give voice provider longer chunks so it can sound less disjointed across chunks. Eg. ['.'].  # noqa: E501

        :param input_punctuation_boundaries: The input_punctuation_boundaries of this NeetsVoice.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["。", "，", ".", "!", "?", ";", ")", "،", "۔", "।", "॥", "|", "||", ",", ":"]  # noqa: E501
        if not set(input_punctuation_boundaries).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `input_punctuation_boundaries` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(input_punctuation_boundaries) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._input_punctuation_boundaries = input_punctuation_boundaries

    @property
    def filler_injection_enabled(self):
        """Gets the filler_injection_enabled of this NeetsVoice.  # noqa: E501

        This determines whether fillers are injected into the model output before inputting it into the voice provider.  Default `false` because you can achieve better results with prompting the model.  # noqa: E501

        :return: The filler_injection_enabled of this NeetsVoice.  # noqa: E501
        :rtype: bool
        """
        return self._filler_injection_enabled

    @filler_injection_enabled.setter
    def filler_injection_enabled(self, filler_injection_enabled):
        """Sets the filler_injection_enabled of this NeetsVoice.

        This determines whether fillers are injected into the model output before inputting it into the voice provider.  Default `false` because you can achieve better results with prompting the model.  # noqa: E501

        :param filler_injection_enabled: The filler_injection_enabled of this NeetsVoice.  # noqa: E501
        :type: bool
        """

        self._filler_injection_enabled = filler_injection_enabled

    @property
    def provider(self):
        """Gets the provider of this NeetsVoice.  # noqa: E501

        This is the voice provider that will be used.  # noqa: E501

        :return: The provider of this NeetsVoice.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this NeetsVoice.

        This is the voice provider that will be used.  # noqa: E501

        :param provider: The provider of this NeetsVoice.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["neets"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def voice_id(self):
        """Gets the voice_id of this NeetsVoice.  # noqa: E501

        This is the provider-specific ID that will be used.  # noqa: E501

        :return: The voice_id of this NeetsVoice.  # noqa: E501
        :rtype: OneOfNeetsVoiceVoiceId
        """
        return self._voice_id

    @voice_id.setter
    def voice_id(self, voice_id):
        """Sets the voice_id of this NeetsVoice.

        This is the provider-specific ID that will be used.  # noqa: E501

        :param voice_id: The voice_id of this NeetsVoice.  # noqa: E501
        :type: OneOfNeetsVoiceVoiceId
        """
        if voice_id is None:
            raise ValueError("Invalid value for `voice_id`, must not be `None`")  # noqa: E501

        self._voice_id = voice_id

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
        if issubclass(NeetsVoice, dict):
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
        if not isinstance(other, NeetsVoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
