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

class ServerMessageHang(object):
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
        'phone_number': 'object',
        'customer': 'object',
        'call': 'object',
        'artifact': 'object',
        'timestamp': 'str'
    }

    attribute_map = {
        'type': 'type',
        'phone_number': 'phoneNumber',
        'customer': 'customer',
        'call': 'call',
        'artifact': 'artifact',
        'timestamp': 'timestamp'
    }

    def __init__(self, type=None, phone_number=None, customer=None, call=None, artifact=None, timestamp=None):  # noqa: E501
        """ServerMessageHang - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._phone_number = None
        self._customer = None
        self._call = None
        self._artifact = None
        self._timestamp = None
        self.discriminator = None
        self.type = type
        if phone_number is not None:
            self.phone_number = phone_number
        self.customer = customer
        self.call = call
        if artifact is not None:
            self.artifact = artifact
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this ServerMessageHang.  # noqa: E501

        This is the type of the message. \"hang\" is sent when the assistant is hanging due to a delay. The delay can be caused by many factors, such as: - the model is too slow to respond - the voice is too slow to respond - the tool call is still waiting for a response from your server - etc.  # noqa: E501

        :return: The type of this ServerMessageHang.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerMessageHang.

        This is the type of the message. \"hang\" is sent when the assistant is hanging due to a delay. The delay can be caused by many factors, such as: - the model is too slow to respond - the voice is too slow to respond - the tool call is still waiting for a response from your server - etc.  # noqa: E501

        :param type: The type of this ServerMessageHang.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["hang"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def phone_number(self):
        """Gets the phone_number of this ServerMessageHang.  # noqa: E501

        The phone number associated with the call. This either directly matches `call.phoneNumber` or is expanded from `call.phoneNumberId`.  # noqa: E501

        :return: The phone_number of this ServerMessageHang.  # noqa: E501
        :rtype: object
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ServerMessageHang.

        The phone number associated with the call. This either directly matches `call.phoneNumber` or is expanded from `call.phoneNumberId`.  # noqa: E501

        :param phone_number: The phone_number of this ServerMessageHang.  # noqa: E501
        :type: object
        """

        self._phone_number = phone_number

    @property
    def customer(self):
        """Gets the customer of this ServerMessageHang.  # noqa: E501

        The customer associated with the call. This either directly matches `call.customer` or is expanded from `call.customerId`.  # noqa: E501

        :return: The customer of this ServerMessageHang.  # noqa: E501
        :rtype: object
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ServerMessageHang.

        The customer associated with the call. This either directly matches `call.customer` or is expanded from `call.customerId`.  # noqa: E501

        :param customer: The customer of this ServerMessageHang.  # noqa: E501
        :type: object
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def call(self):
        """Gets the call of this ServerMessageHang.  # noqa: E501

        This is the main `call` object of the call.  # noqa: E501

        :return: The call of this ServerMessageHang.  # noqa: E501
        :rtype: object
        """
        return self._call

    @call.setter
    def call(self, call):
        """Sets the call of this ServerMessageHang.

        This is the main `call` object of the call.  # noqa: E501

        :param call: The call of this ServerMessageHang.  # noqa: E501
        :type: object
        """
        if call is None:
            raise ValueError("Invalid value for `call`, must not be `None`")  # noqa: E501

        self._call = call

    @property
    def artifact(self):
        """Gets the artifact of this ServerMessageHang.  # noqa: E501

        These are the live artifacts of the call.  # noqa: E501

        :return: The artifact of this ServerMessageHang.  # noqa: E501
        :rtype: object
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this ServerMessageHang.

        These are the live artifacts of the call.  # noqa: E501

        :param artifact: The artifact of this ServerMessageHang.  # noqa: E501
        :type: object
        """

        self._artifact = artifact

    @property
    def timestamp(self):
        """Gets the timestamp of this ServerMessageHang.  # noqa: E501

        This is the timestamp of the message.  # noqa: E501

        :return: The timestamp of this ServerMessageHang.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ServerMessageHang.

        This is the timestamp of the message.  # noqa: E501

        :param timestamp: The timestamp of this ServerMessageHang.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(ServerMessageHang, dict):
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
        if not isinstance(other, ServerMessageHang):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
