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

class TalkscriberTranscriber(object):
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
        'provider': 'str',
        'model': 'str',
        'language': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'model': 'model',
        'language': 'language'
    }

    def __init__(self, provider=None, model=None, language=None):  # noqa: E501
        """TalkscriberTranscriber - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._model = None
        self._language = None
        self.discriminator = None
        self.provider = provider
        if model is not None:
            self.model = model
        if language is not None:
            self.language = language

    @property
    def provider(self):
        """Gets the provider of this TalkscriberTranscriber.  # noqa: E501

        This is the transcription provider that will be used.  # noqa: E501

        :return: The provider of this TalkscriberTranscriber.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this TalkscriberTranscriber.

        This is the transcription provider that will be used.  # noqa: E501

        :param provider: The provider of this TalkscriberTranscriber.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["talkscriber"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def model(self):
        """Gets the model of this TalkscriberTranscriber.  # noqa: E501

        This is the model that will be used for the transcription.  # noqa: E501

        :return: The model of this TalkscriberTranscriber.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TalkscriberTranscriber.

        This is the model that will be used for the transcription.  # noqa: E501

        :param model: The model of this TalkscriberTranscriber.  # noqa: E501
        :type: str
        """
        allowed_values = ["whisper"]  # noqa: E501
        if model not in allowed_values:
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"  # noqa: E501
                .format(model, allowed_values)
            )

        self._model = model

    @property
    def language(self):
        """Gets the language of this TalkscriberTranscriber.  # noqa: E501

        This is the language that will be set for the transcription. The list of languages Whisper supports can be found here: https://github.com/openai/whisper/blob/main/whisper/tokenizer.py  # noqa: E501

        :return: The language of this TalkscriberTranscriber.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TalkscriberTranscriber.

        This is the language that will be set for the transcription. The list of languages Whisper supports can be found here: https://github.com/openai/whisper/blob/main/whisper/tokenizer.py  # noqa: E501

        :param language: The language of this TalkscriberTranscriber.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "zh", "de", "es", "ru", "ko", "fr", "ja", "pt", "tr", "pl", "ca", "nl", "ar", "sv", "it", "id", "hi", "fi", "vi", "he", "uk", "el", "ms", "cs", "ro", "da", "hu", "ta", "no", "th", "ur", "hr", "bg", "lt", "la", "mi", "ml", "cy", "sk", "te", "fa", "lv", "bn", "sr", "az", "sl", "kn", "et", "mk", "br", "eu", "is", "hy", "ne", "mn", "bs", "kk", "sq", "sw", "gl", "mr", "pa", "si", "km", "sn", "yo", "so", "af", "oc", "ka", "be", "tg", "sd", "gu", "am", "yi", "lo", "uz", "fo", "ht", "ps", "tk", "nn", "mt", "sa", "lb", "my", "bo", "tl", "mg", "as", "tt", "haw", "ln", "ha", "ba", "jw", "su", "yue"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

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
        if issubclass(TalkscriberTranscriber, dict):
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
        if not isinstance(other, TalkscriberTranscriber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
