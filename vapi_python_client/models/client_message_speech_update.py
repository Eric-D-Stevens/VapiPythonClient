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

class ClientMessageSpeechUpdate(object):
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
        'role': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'role': 'role'
    }

    def __init__(self, type=None, status=None, role=None):  # noqa: E501
        """ClientMessageSpeechUpdate - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._role = None
        self.discriminator = None
        self.type = type
        self.status = status
        self.role = role

    @property
    def type(self):
        """Gets the type of this ClientMessageSpeechUpdate.  # noqa: E501

        This is the type of the message. \"speech-update\" is sent whenever assistant or user start or stop speaking.  # noqa: E501

        :return: The type of this ClientMessageSpeechUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientMessageSpeechUpdate.

        This is the type of the message. \"speech-update\" is sent whenever assistant or user start or stop speaking.  # noqa: E501

        :param type: The type of this ClientMessageSpeechUpdate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["speech-update"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this ClientMessageSpeechUpdate.  # noqa: E501

        This is the status of the speech update.  # noqa: E501

        :return: The status of this ClientMessageSpeechUpdate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClientMessageSpeechUpdate.

        This is the status of the speech update.  # noqa: E501

        :param status: The status of this ClientMessageSpeechUpdate.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["started", "stopped"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def role(self):
        """Gets the role of this ClientMessageSpeechUpdate.  # noqa: E501

        This is the role which the speech update is for.  # noqa: E501

        :return: The role of this ClientMessageSpeechUpdate.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ClientMessageSpeechUpdate.

        This is the role which the speech update is for.  # noqa: E501

        :param role: The role of this ClientMessageSpeechUpdate.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["assistant", "user"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(ClientMessageSpeechUpdate, dict):
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
        if not isinstance(other, ClientMessageSpeechUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
