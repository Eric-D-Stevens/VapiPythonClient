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

class InlineResponse2012(object):
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
    }

    attribute_map = {
    }

    discriminator_value_class_map = {
            'dtmf'.lower(): '#/components/schemas/DtmfTool',
            'endCall'.lower(): '#/components/schemas/EndCallTool',
            'function'.lower(): '#/components/schemas/FunctionTool',
            'ghl'.lower(): '#/components/schemas/GhlTool',
            'make'.lower(): '#/components/schemas/MakeTool',
            'transferCall'.lower(): '#/components/schemas/TransferCallTool',
            'MakeTool'.lower(): 'make',
            'FunctionTool'.lower(): 'function',
            'DtmfTool'.lower(): 'dtmf',
            'TransferCallTool'.lower(): 'transferCall',
            'EndCallTool'.lower(): 'endCall',
            'GhlTool'.lower(): 'ghl',
    }

    def __init__(self):  # noqa: E501
        """InlineResponse2012 - a model defined in Swagger"""  # noqa: E501
        self.discriminator = 'type'

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(InlineResponse2012, dict):
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
        if not isinstance(other, InlineResponse2012):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
