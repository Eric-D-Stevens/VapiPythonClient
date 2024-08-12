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

class KnowledgeBase(object):
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
        'top_k': 'float',
        'file_ids': 'list[str]'
    }

    attribute_map = {
        'provider': 'provider',
        'top_k': 'topK',
        'file_ids': 'fileIds'
    }

    def __init__(self, provider=None, top_k=None, file_ids=None):  # noqa: E501
        """KnowledgeBase - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._top_k = None
        self._file_ids = None
        self.discriminator = None
        self.provider = provider
        if top_k is not None:
            self.top_k = top_k
        self.file_ids = file_ids

    @property
    def provider(self):
        """Gets the provider of this KnowledgeBase.  # noqa: E501


        :return: The provider of this KnowledgeBase.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this KnowledgeBase.


        :param provider: The provider of this KnowledgeBase.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["canonical"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def top_k(self):
        """Gets the top_k of this KnowledgeBase.  # noqa: E501


        :return: The top_k of this KnowledgeBase.  # noqa: E501
        :rtype: float
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """Sets the top_k of this KnowledgeBase.


        :param top_k: The top_k of this KnowledgeBase.  # noqa: E501
        :type: float
        """

        self._top_k = top_k

    @property
    def file_ids(self):
        """Gets the file_ids of this KnowledgeBase.  # noqa: E501


        :return: The file_ids of this KnowledgeBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this KnowledgeBase.


        :param file_ids: The file_ids of this KnowledgeBase.  # noqa: E501
        :type: list[str]
        """
        if file_ids is None:
            raise ValueError("Invalid value for `file_ids`, must not be `None`")  # noqa: E501

        self._file_ids = file_ids

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
        if issubclass(KnowledgeBase, dict):
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
        if not isinstance(other, KnowledgeBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
