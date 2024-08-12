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

class TwilioVoicemailDetection(object):
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
        'voicemail_detection_types': 'list[str]',
        'enabled': 'bool',
        'machine_detection_timeout': 'float',
        'machine_detection_speech_threshold': 'float',
        'machine_detection_speech_end_threshold': 'float',
        'machine_detection_silence_timeout': 'float'
    }

    attribute_map = {
        'provider': 'provider',
        'voicemail_detection_types': 'voicemailDetectionTypes',
        'enabled': 'enabled',
        'machine_detection_timeout': 'machineDetectionTimeout',
        'machine_detection_speech_threshold': 'machineDetectionSpeechThreshold',
        'machine_detection_speech_end_threshold': 'machineDetectionSpeechEndThreshold',
        'machine_detection_silence_timeout': 'machineDetectionSilenceTimeout'
    }

    def __init__(self, provider=None, voicemail_detection_types=None, enabled=None, machine_detection_timeout=None, machine_detection_speech_threshold=None, machine_detection_speech_end_threshold=None, machine_detection_silence_timeout=None):  # noqa: E501
        """TwilioVoicemailDetection - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._voicemail_detection_types = None
        self._enabled = None
        self._machine_detection_timeout = None
        self._machine_detection_speech_threshold = None
        self._machine_detection_speech_end_threshold = None
        self._machine_detection_silence_timeout = None
        self.discriminator = None
        self.provider = provider
        if voicemail_detection_types is not None:
            self.voicemail_detection_types = voicemail_detection_types
        if enabled is not None:
            self.enabled = enabled
        if machine_detection_timeout is not None:
            self.machine_detection_timeout = machine_detection_timeout
        if machine_detection_speech_threshold is not None:
            self.machine_detection_speech_threshold = machine_detection_speech_threshold
        if machine_detection_speech_end_threshold is not None:
            self.machine_detection_speech_end_threshold = machine_detection_speech_end_threshold
        if machine_detection_silence_timeout is not None:
            self.machine_detection_silence_timeout = machine_detection_silence_timeout

    @property
    def provider(self):
        """Gets the provider of this TwilioVoicemailDetection.  # noqa: E501

        This is the provider to use for voicemail detection.  # noqa: E501

        :return: The provider of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this TwilioVoicemailDetection.

        This is the provider to use for voicemail detection.  # noqa: E501

        :param provider: The provider of this TwilioVoicemailDetection.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["twilio"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def voicemail_detection_types(self):
        """Gets the voicemail_detection_types of this TwilioVoicemailDetection.  # noqa: E501

        These are the AMD messages from Twilio that are considered as voicemail. Default is ['machine_end_beep', 'machine_end_silence'].  @default {Array} ['machine_end_beep', 'machine_end_silence']  # noqa: E501

        :return: The voicemail_detection_types of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: list[str]
        """
        return self._voicemail_detection_types

    @voicemail_detection_types.setter
    def voicemail_detection_types(self, voicemail_detection_types):
        """Sets the voicemail_detection_types of this TwilioVoicemailDetection.

        These are the AMD messages from Twilio that are considered as voicemail. Default is ['machine_end_beep', 'machine_end_silence'].  @default {Array} ['machine_end_beep', 'machine_end_silence']  # noqa: E501

        :param voicemail_detection_types: The voicemail_detection_types of this TwilioVoicemailDetection.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["machine_start", "human", "fax", "unknown", "machine_end_beep", "machine_end_silence", "machine_end_other"]  # noqa: E501
        if not set(voicemail_detection_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `voicemail_detection_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(voicemail_detection_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._voicemail_detection_types = voicemail_detection_types

    @property
    def enabled(self):
        """Gets the enabled of this TwilioVoicemailDetection.  # noqa: E501

        This sets whether the assistant should detect voicemail. Defaults to true.  @default true  # noqa: E501

        :return: The enabled of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TwilioVoicemailDetection.

        This sets whether the assistant should detect voicemail. Defaults to true.  @default true  # noqa: E501

        :param enabled: The enabled of this TwilioVoicemailDetection.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def machine_detection_timeout(self):
        """Gets the machine_detection_timeout of this TwilioVoicemailDetection.  # noqa: E501

        The number of seconds that Twilio should attempt to perform answering machine detection before timing out and returning AnsweredBy as unknown. Default is 30 seconds.  Increasing this value will provide the engine more time to make a determination. This can be useful when DetectMessageEnd is provided in the MachineDetection parameter and there is an expectation of long answering machine greetings that can exceed 30 seconds.  Decreasing this value will reduce the amount of time the engine has to make a determination. This can be particularly useful when the Enable option is provided in the MachineDetection parameter and you want to limit the time for initial detection.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 30  # noqa: E501

        :return: The machine_detection_timeout of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: float
        """
        return self._machine_detection_timeout

    @machine_detection_timeout.setter
    def machine_detection_timeout(self, machine_detection_timeout):
        """Sets the machine_detection_timeout of this TwilioVoicemailDetection.

        The number of seconds that Twilio should attempt to perform answering machine detection before timing out and returning AnsweredBy as unknown. Default is 30 seconds.  Increasing this value will provide the engine more time to make a determination. This can be useful when DetectMessageEnd is provided in the MachineDetection parameter and there is an expectation of long answering machine greetings that can exceed 30 seconds.  Decreasing this value will reduce the amount of time the engine has to make a determination. This can be particularly useful when the Enable option is provided in the MachineDetection parameter and you want to limit the time for initial detection.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 30  # noqa: E501

        :param machine_detection_timeout: The machine_detection_timeout of this TwilioVoicemailDetection.  # noqa: E501
        :type: float
        """

        self._machine_detection_timeout = machine_detection_timeout

    @property
    def machine_detection_speech_threshold(self):
        """Gets the machine_detection_speech_threshold of this TwilioVoicemailDetection.  # noqa: E501

        The number of milliseconds that is used as the measuring stick for the length of the speech activity. Durations lower than this value will be interpreted as a human, longer as a machine. Default is 2400 milliseconds.  Increasing this value will reduce the chance of a False Machine (detected machine, actually human) for a long human greeting (e.g., a business greeting) but increase the time it takes to detect a machine.  Decreasing this value will reduce the chances of a False Human (detected human, actually machine) for short voicemail greetings. The value of this parameter may need to be reduced by more than 1000ms to detect very short voicemail greetings. A reduction of that significance can result in increased False Machine detections. Adjusting the MachineDetectionSpeechEndThreshold is likely the better approach for short voicemails. Decreasing MachineDetectionSpeechThreshold will also reduce the time it takes to detect a machine.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 2400  # noqa: E501

        :return: The machine_detection_speech_threshold of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: float
        """
        return self._machine_detection_speech_threshold

    @machine_detection_speech_threshold.setter
    def machine_detection_speech_threshold(self, machine_detection_speech_threshold):
        """Sets the machine_detection_speech_threshold of this TwilioVoicemailDetection.

        The number of milliseconds that is used as the measuring stick for the length of the speech activity. Durations lower than this value will be interpreted as a human, longer as a machine. Default is 2400 milliseconds.  Increasing this value will reduce the chance of a False Machine (detected machine, actually human) for a long human greeting (e.g., a business greeting) but increase the time it takes to detect a machine.  Decreasing this value will reduce the chances of a False Human (detected human, actually machine) for short voicemail greetings. The value of this parameter may need to be reduced by more than 1000ms to detect very short voicemail greetings. A reduction of that significance can result in increased False Machine detections. Adjusting the MachineDetectionSpeechEndThreshold is likely the better approach for short voicemails. Decreasing MachineDetectionSpeechThreshold will also reduce the time it takes to detect a machine.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 2400  # noqa: E501

        :param machine_detection_speech_threshold: The machine_detection_speech_threshold of this TwilioVoicemailDetection.  # noqa: E501
        :type: float
        """

        self._machine_detection_speech_threshold = machine_detection_speech_threshold

    @property
    def machine_detection_speech_end_threshold(self):
        """Gets the machine_detection_speech_end_threshold of this TwilioVoicemailDetection.  # noqa: E501

        The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Default is 1200 milliseconds.  Increasing this value will typically be used to better address the short voicemail greeting scenarios. For short voicemails, there is typically 1000-2000ms of audio followed by 1200-2400ms of silence and then additional audio before the beep. Increasing the MachineDetectionSpeechEndThreshold to ~2500ms will treat the 1200-2400ms of silence as a gap in the greeting but not the end of the greeting and will result in a machine detection. The downsides of such a change include: - Increasing the delay for human detection by the amount you increase this parameter, e.g., a change of 1200ms to 2500ms increases human detection delay by 1300ms. - Cases where a human has two utterances separated by a period of silence (e.g. a \"Hello\", then 2000ms of silence, and another \"Hello\") may be interpreted as a machine.  Decreasing this value will result in faster human detection. The consequence is that it can lead to increased False Human (detected human, actually machine) detections because a silence gap in a voicemail greeting (not necessarily just in short voicemail scenarios) can be incorrectly interpreted as the end of speech.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 1200  # noqa: E501

        :return: The machine_detection_speech_end_threshold of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: float
        """
        return self._machine_detection_speech_end_threshold

    @machine_detection_speech_end_threshold.setter
    def machine_detection_speech_end_threshold(self, machine_detection_speech_end_threshold):
        """Sets the machine_detection_speech_end_threshold of this TwilioVoicemailDetection.

        The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Default is 1200 milliseconds.  Increasing this value will typically be used to better address the short voicemail greeting scenarios. For short voicemails, there is typically 1000-2000ms of audio followed by 1200-2400ms of silence and then additional audio before the beep. Increasing the MachineDetectionSpeechEndThreshold to ~2500ms will treat the 1200-2400ms of silence as a gap in the greeting but not the end of the greeting and will result in a machine detection. The downsides of such a change include: - Increasing the delay for human detection by the amount you increase this parameter, e.g., a change of 1200ms to 2500ms increases human detection delay by 1300ms. - Cases where a human has two utterances separated by a period of silence (e.g. a \"Hello\", then 2000ms of silence, and another \"Hello\") may be interpreted as a machine.  Decreasing this value will result in faster human detection. The consequence is that it can lead to increased False Human (detected human, actually machine) detections because a silence gap in a voicemail greeting (not necessarily just in short voicemail scenarios) can be incorrectly interpreted as the end of speech.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 1200  # noqa: E501

        :param machine_detection_speech_end_threshold: The machine_detection_speech_end_threshold of this TwilioVoicemailDetection.  # noqa: E501
        :type: float
        """

        self._machine_detection_speech_end_threshold = machine_detection_speech_end_threshold

    @property
    def machine_detection_silence_timeout(self):
        """Gets the machine_detection_silence_timeout of this TwilioVoicemailDetection.  # noqa: E501

        The number of milliseconds of initial silence after which an unknown AnsweredBy result will be returned. Default is 5000 milliseconds.  Increasing this value will result in waiting for a longer period of initial silence before returning an 'unknown' AMD result.  Decreasing this value will result in waiting for a shorter period of initial silence before returning an 'unknown' AMD result.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 5000  # noqa: E501

        :return: The machine_detection_silence_timeout of this TwilioVoicemailDetection.  # noqa: E501
        :rtype: float
        """
        return self._machine_detection_silence_timeout

    @machine_detection_silence_timeout.setter
    def machine_detection_silence_timeout(self, machine_detection_silence_timeout):
        """Sets the machine_detection_silence_timeout of this TwilioVoicemailDetection.

        The number of milliseconds of initial silence after which an unknown AnsweredBy result will be returned. Default is 5000 milliseconds.  Increasing this value will result in waiting for a longer period of initial silence before returning an 'unknown' AMD result.  Decreasing this value will result in waiting for a shorter period of initial silence before returning an 'unknown' AMD result.  Check the [Twilio docs](https://www.twilio.com/docs/voice/answering-machine-detection#optional-api-tuning-parameters) for more info.  @default 5000  # noqa: E501

        :param machine_detection_silence_timeout: The machine_detection_silence_timeout of this TwilioVoicemailDetection.  # noqa: E501
        :type: float
        """

        self._machine_detection_silence_timeout = machine_detection_silence_timeout

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
        if issubclass(TwilioVoicemailDetection, dict):
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
        if not isinstance(other, TwilioVoicemailDetection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
