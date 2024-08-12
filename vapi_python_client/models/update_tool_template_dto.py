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

class UpdateToolTemplateDTO(object):
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
        'details': 'OneOfUpdateToolTemplateDTODetails',
        'provider_details': 'OneOfUpdateToolTemplateDTOProviderDetails',
        'metadata': 'ToolTemplateMetadata',
        'visibility': 'str',
        'type': 'str',
        'name': 'str',
        'provider': 'str'
    }

    attribute_map = {
        'details': 'details',
        'provider_details': 'providerDetails',
        'metadata': 'metadata',
        'visibility': 'visibility',
        'type': 'type',
        'name': 'name',
        'provider': 'provider'
    }

    def __init__(self, details=None, provider_details=None, metadata=None, visibility='private', type='tool', name=None, provider=None):  # noqa: E501
        """UpdateToolTemplateDTO - a model defined in Swagger"""  # noqa: E501
        self._details = None
        self._provider_details = None
        self._metadata = None
        self._visibility = None
        self._type = None
        self._name = None
        self._provider = None
        self.discriminator = None
        if details is not None:
            self.details = details
        if provider_details is not None:
            self.provider_details = provider_details
        if metadata is not None:
            self.metadata = metadata
        if visibility is not None:
            self.visibility = visibility
        self.type = type
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider

    @property
    def details(self):
        """Gets the details of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The details of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: OneOfUpdateToolTemplateDTODetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UpdateToolTemplateDTO.


        :param details: The details of this UpdateToolTemplateDTO.  # noqa: E501
        :type: OneOfUpdateToolTemplateDTODetails
        """

        self._details = details

    @property
    def provider_details(self):
        """Gets the provider_details of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The provider_details of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: OneOfUpdateToolTemplateDTOProviderDetails
        """
        return self._provider_details

    @provider_details.setter
    def provider_details(self, provider_details):
        """Sets the provider_details of this UpdateToolTemplateDTO.


        :param provider_details: The provider_details of this UpdateToolTemplateDTO.  # noqa: E501
        :type: OneOfUpdateToolTemplateDTOProviderDetails
        """

        self._provider_details = provider_details

    @property
    def metadata(self):
        """Gets the metadata of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The metadata of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: ToolTemplateMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateToolTemplateDTO.


        :param metadata: The metadata of this UpdateToolTemplateDTO.  # noqa: E501
        :type: ToolTemplateMetadata
        """

        self._metadata = metadata

    @property
    def visibility(self):
        """Gets the visibility of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The visibility of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this UpdateToolTemplateDTO.


        :param visibility: The visibility of this UpdateToolTemplateDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["public", "private"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def type(self):
        """Gets the type of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The type of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateToolTemplateDTO.


        :param type: The type of this UpdateToolTemplateDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["tool"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this UpdateToolTemplateDTO.  # noqa: E501

        The name of the template. This is just for your own reference.  # noqa: E501

        :return: The name of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateToolTemplateDTO.

        The name of the template. This is just for your own reference.  # noqa: E501

        :param name: The name of this UpdateToolTemplateDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this UpdateToolTemplateDTO.  # noqa: E501


        :return: The provider of this UpdateToolTemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UpdateToolTemplateDTO.


        :param provider: The provider of this UpdateToolTemplateDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["make", "gohighlevel", "function"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

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
        if issubclass(UpdateToolTemplateDTO, dict):
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
        if not isinstance(other, UpdateToolTemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
