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

class ServerMessageStatusUpdate(object):
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
        'type': 'str',
        'status': 'str',
        'ended_reason': 'str',
        'messages': 'list[OneOfServerMessageStatusUpdateMessagesItems]',
        'messages_open_ai_formatted': 'list[OpenAIMessage]',
        'destination': 'OneOfServerMessageStatusUpdateDestination',
        'phone_number': 'object',
        'customer': 'object',
        'call': 'object',
        'artifact': 'object',
        'timestamp': 'str',
        'transcript': 'str',
        'inbound_phone_call_debugging_artifacts': 'object'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'ended_reason': 'endedReason',
        'messages': 'messages',
        'messages_open_ai_formatted': 'messagesOpenAIFormatted',
        'destination': 'destination',
        'phone_number': 'phoneNumber',
        'customer': 'customer',
        'call': 'call',
        'artifact': 'artifact',
        'timestamp': 'timestamp',
        'transcript': 'transcript',
        'inbound_phone_call_debugging_artifacts': 'inboundPhoneCallDebuggingArtifacts'
    }

    def __init__(self, type=None, status=None, ended_reason=None, messages=None, messages_open_ai_formatted=None, destination=None, phone_number=None, customer=None, call=None, artifact=None, timestamp=None, transcript=None, inbound_phone_call_debugging_artifacts=None):  # noqa: E501
        """ServerMessageStatusUpdate - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._ended_reason = None
        self._messages = None
        self._messages_open_ai_formatted = None
        self._destination = None
        self._phone_number = None
        self._customer = None
        self._call = None
        self._artifact = None
        self._timestamp = None
        self._transcript = None
        self._inbound_phone_call_debugging_artifacts = None
        self.discriminator = None
        self.type = type
        self.status = status
        if ended_reason is not None:
            self.ended_reason = ended_reason
        if messages is not None:
            self.messages = messages
        if messages_open_ai_formatted is not None:
            self.messages_open_ai_formatted = messages_open_ai_formatted
        if destination is not None:
            self.destination = destination
        if phone_number is not None:
            self.phone_number = phone_number
        self.customer = customer
        self.call = call
        if artifact is not None:
            self.artifact = artifact
        if timestamp is not None:
            self.timestamp = timestamp
        if transcript is not None:
            self.transcript = transcript
        if inbound_phone_call_debugging_artifacts is not None:
            self.inbound_phone_call_debugging_artifacts = inbound_phone_call_debugging_artifacts

    @property
    def type(self):
        """Gets the type of this ServerMessageStatusUpdate.  # noqa: E501

        This is the type of the message. \"status-update\" is sent whenever the `call.status` changes.  # noqa: E501

        :return: The type of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerMessageStatusUpdate.

        This is the type of the message. \"status-update\" is sent whenever the `call.status` changes.  # noqa: E501

        :param type: The type of this ServerMessageStatusUpdate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["status-update"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this ServerMessageStatusUpdate.  # noqa: E501

        This is the status of the call.  # noqa: E501

        :return: The status of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServerMessageStatusUpdate.

        This is the status of the call.  # noqa: E501

        :param status: The status of this ServerMessageStatusUpdate.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["queued", "ringing", "in-progress", "forwarding", "ended"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def ended_reason(self):
        """Gets the ended_reason of this ServerMessageStatusUpdate.  # noqa: E501

        This is the reason the call ended. This is only sent if the status is \"ended\".  # noqa: E501

        :return: The ended_reason of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._ended_reason

    @ended_reason.setter
    def ended_reason(self, ended_reason):
        """Sets the ended_reason of this ServerMessageStatusUpdate.

        This is the reason the call ended. This is only sent if the status is \"ended\".  # noqa: E501

        :param ended_reason: The ended_reason of this ServerMessageStatusUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["assistant-error", "assistant-not-found", "db-error", "no-server-available", "pipeline-error-openai-llm-failed", "pipeline-error-azure-openai-llm-failed", "pipeline-error-groq-llm-failed", "pipeline-error-openai-voice-failed", "pipeline-error-cartesia-voice-failed", "pipeline-error-deepgram-transcriber-failed", "pipeline-error-deepgram-voice-failed", "pipeline-error-gladia-transcriber-failed", "pipeline-error-eleven-labs-voice-failed", "pipeline-error-playht-voice-failed", "pipeline-error-lmnt-voice-failed", "pipeline-error-azure-voice-failed", "pipeline-error-rime-ai-voice-failed", "pipeline-error-neets-voice-failed", "pipeline-no-available-model", "worker-shutdown", "twilio-failed-to-connect-call", "unknown-error", "vonage-disconnected", "vonage-failed-to-connect-call", "phone-call-provider-bypass-enabled-but-no-call-received", "vapi-error-phone-call-worker-setup-socket-error", "vapi-error-phone-call-worker-worker-setup-socket-timeout", "vapi-error-phone-call-worker-could-not-find-call", "vapi-error-phone-call-worker-call-never-connected", "vapi-error-web-call-worker-setup-failed", "assistant-not-invalid", "assistant-not-provided", "call-start-error-neither-assistant-nor-server-set", "assistant-request-failed", "assistant-request-returned-error", "assistant-request-returned-unspeakable-error", "assistant-request-returned-invalid-assistant", "assistant-request-returned-no-assistant", "assistant-request-returned-forwarding-phone-number", "assistant-ended-call", "assistant-said-end-call-phrase", "assistant-forwarded-call", "assistant-join-timed-out", "customer-busy", "customer-ended-call", "customer-did-not-answer", "customer-did-not-give-microphone-permission", "assistant-said-message-with-end-call-enabled", "exceeded-max-duration", "manually-canceled", "phone-call-provider-closed-websocket", "pipeline-error-anthropic-llm-failed", "pipeline-error-together-ai-llm-failed", "pipeline-error-anyscale-llm-failed", "pipeline-error-openrouter-llm-failed", "pipeline-error-perplexity-ai-llm-failed", "pipeline-error-deepinfra-llm-failed", "pipeline-error-runpod-llm-failed", "pipeline-error-custom-llm-llm-failed", "pipeline-error-eleven-labs-voice-not-found", "pipeline-error-eleven-labs-quota-exceeded", "pipeline-error-eleven-labs-unauthorized-access", "pipeline-error-eleven-labs-unauthorized-to-access-model", "pipeline-error-eleven-labs-professional-voices-only-for-creator-plus", "pipeline-error-eleven-labs-blocked-free-plan-and-requested-upgrade", "pipeline-error-eleven-labs-blocked-concurrent-requests-and-requested-upgrade", "pipeline-error-eleven-labs-blocked-using-instant-voice-clone-and-requested-upgrade", "pipeline-error-eleven-labs-system-busy-and-requested-upgrade", "pipeline-error-eleven-labs-voice-not-fine-tuned", "pipeline-error-eleven-labs-invalid-api-key", "pipeline-error-eleven-labs-invalid-voice-samples", "pipeline-error-eleven-labs-voice-disabled-by-owner", "pipeline-error-eleven-labs-blocked-account-in-probation", "pipeline-error-playht-request-timed-out", "pipeline-error-playht-invalid-voice", "pipeline-error-playht-unexpected-error", "pipeline-error-playht-out-of-credits", "pipeline-error-playht-rate-limit-exceeded", "pipeline-error-playht-502-gateway-error", "pipeline-error-playht-504-gateway-error", "pipeline-error-gladia-transcriber-failed", "silence-timed-out", "voicemail", "vonage-rejected"]  # noqa: E501
        if ended_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `ended_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(ended_reason, allowed_values)
            )

        self._ended_reason = ended_reason

    @property
    def messages(self):
        """Gets the messages of this ServerMessageStatusUpdate.  # noqa: E501

        These are the conversation messages of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :return: The messages of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: list[OneOfServerMessageStatusUpdateMessagesItems]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ServerMessageStatusUpdate.

        These are the conversation messages of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :param messages: The messages of this ServerMessageStatusUpdate.  # noqa: E501
        :type: list[OneOfServerMessageStatusUpdateMessagesItems]
        """

        self._messages = messages

    @property
    def messages_open_ai_formatted(self):
        """Gets the messages_open_ai_formatted of this ServerMessageStatusUpdate.  # noqa: E501

        These are the conversation messages of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :return: The messages_open_ai_formatted of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: list[OpenAIMessage]
        """
        return self._messages_open_ai_formatted

    @messages_open_ai_formatted.setter
    def messages_open_ai_formatted(self, messages_open_ai_formatted):
        """Sets the messages_open_ai_formatted of this ServerMessageStatusUpdate.

        These are the conversation messages of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :param messages_open_ai_formatted: The messages_open_ai_formatted of this ServerMessageStatusUpdate.  # noqa: E501
        :type: list[OpenAIMessage]
        """

        self._messages_open_ai_formatted = messages_open_ai_formatted

    @property
    def destination(self):
        """Gets the destination of this ServerMessageStatusUpdate.  # noqa: E501

        This is the destination the call is being transferred to. This is only sent if the status is \"forwarding\".  # noqa: E501

        :return: The destination of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: OneOfServerMessageStatusUpdateDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ServerMessageStatusUpdate.

        This is the destination the call is being transferred to. This is only sent if the status is \"forwarding\".  # noqa: E501

        :param destination: The destination of this ServerMessageStatusUpdate.  # noqa: E501
        :type: OneOfServerMessageStatusUpdateDestination
        """

        self._destination = destination

    @property
    def phone_number(self):
        """Gets the phone_number of this ServerMessageStatusUpdate.  # noqa: E501

        The phone number associated with the call. This either directly matches `call.phoneNumber` or is expanded from `call.phoneNumberId`.  # noqa: E501

        :return: The phone_number of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: object
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ServerMessageStatusUpdate.

        The phone number associated with the call. This either directly matches `call.phoneNumber` or is expanded from `call.phoneNumberId`.  # noqa: E501

        :param phone_number: The phone_number of this ServerMessageStatusUpdate.  # noqa: E501
        :type: object
        """

        self._phone_number = phone_number

    @property
    def customer(self):
        """Gets the customer of this ServerMessageStatusUpdate.  # noqa: E501

        The customer associated with the call. This either directly matches `call.customer` or is expanded from `call.customerId`.  # noqa: E501

        :return: The customer of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: object
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ServerMessageStatusUpdate.

        The customer associated with the call. This either directly matches `call.customer` or is expanded from `call.customerId`.  # noqa: E501

        :param customer: The customer of this ServerMessageStatusUpdate.  # noqa: E501
        :type: object
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def call(self):
        """Gets the call of this ServerMessageStatusUpdate.  # noqa: E501

        This is the main `call` object of the call.  # noqa: E501

        :return: The call of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: object
        """
        return self._call

    @call.setter
    def call(self, call):
        """Sets the call of this ServerMessageStatusUpdate.

        This is the main `call` object of the call.  # noqa: E501

        :param call: The call of this ServerMessageStatusUpdate.  # noqa: E501
        :type: object
        """
        if call is None:
            raise ValueError("Invalid value for `call`, must not be `None`")  # noqa: E501

        self._call = call

    @property
    def artifact(self):
        """Gets the artifact of this ServerMessageStatusUpdate.  # noqa: E501

        These are the live artifacts of the call.  # noqa: E501

        :return: The artifact of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: object
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this ServerMessageStatusUpdate.

        These are the live artifacts of the call.  # noqa: E501

        :param artifact: The artifact of this ServerMessageStatusUpdate.  # noqa: E501
        :type: object
        """

        self._artifact = artifact

    @property
    def timestamp(self):
        """Gets the timestamp of this ServerMessageStatusUpdate.  # noqa: E501

        This is the timestamp of the message.  # noqa: E501

        :return: The timestamp of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ServerMessageStatusUpdate.

        This is the timestamp of the message.  # noqa: E501

        :param timestamp: The timestamp of this ServerMessageStatusUpdate.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def transcript(self):
        """Gets the transcript of this ServerMessageStatusUpdate.  # noqa: E501

        This is the transcript of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :return: The transcript of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._transcript

    @transcript.setter
    def transcript(self, transcript):
        """Sets the transcript of this ServerMessageStatusUpdate.

        This is the transcript of the call. This is only sent if the status is \"forwarding\".  # noqa: E501

        :param transcript: The transcript of this ServerMessageStatusUpdate.  # noqa: E501
        :type: str
        """

        self._transcript = transcript

    @property
    def inbound_phone_call_debugging_artifacts(self):
        """Gets the inbound_phone_call_debugging_artifacts of this ServerMessageStatusUpdate.  # noqa: E501

        This is the inbound phone call debugging artifacts. This is only sent if the status is \"ended\" and there was an error accepting the inbound phone call.  This will include any errors related to the \"assistant-request\" if one was made.  # noqa: E501

        :return: The inbound_phone_call_debugging_artifacts of this ServerMessageStatusUpdate.  # noqa: E501
        :rtype: object
        """
        return self._inbound_phone_call_debugging_artifacts

    @inbound_phone_call_debugging_artifacts.setter
    def inbound_phone_call_debugging_artifacts(self, inbound_phone_call_debugging_artifacts):
        """Sets the inbound_phone_call_debugging_artifacts of this ServerMessageStatusUpdate.

        This is the inbound phone call debugging artifacts. This is only sent if the status is \"ended\" and there was an error accepting the inbound phone call.  This will include any errors related to the \"assistant-request\" if one was made.  # noqa: E501

        :param inbound_phone_call_debugging_artifacts: The inbound_phone_call_debugging_artifacts of this ServerMessageStatusUpdate.  # noqa: E501
        :type: object
        """

        self._inbound_phone_call_debugging_artifacts = inbound_phone_call_debugging_artifacts

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
        if issubclass(ServerMessageStatusUpdate, dict):
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
        if not isinstance(other, ServerMessageStatusUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
