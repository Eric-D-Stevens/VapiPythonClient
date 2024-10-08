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

class AzureOpenAICredential(object):
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
        'region': 'str',
        'models': 'list[str]',
        'open_ai_key': 'str',
        'id': 'str',
        'org_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'open_ai_endpoint': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'region': 'region',
        'models': 'models',
        'open_ai_key': 'openAIKey',
        'id': 'id',
        'org_id': 'orgId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'open_ai_endpoint': 'openAIEndpoint'
    }

    def __init__(self, provider=None, region=None, models=None, open_ai_key=None, id=None, org_id=None, created_at=None, updated_at=None, open_ai_endpoint=None):  # noqa: E501
        """AzureOpenAICredential - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._region = None
        self._models = None
        self._open_ai_key = None
        self._id = None
        self._org_id = None
        self._created_at = None
        self._updated_at = None
        self._open_ai_endpoint = None
        self.discriminator = None
        self.provider = provider
        self.region = region
        self.models = models
        self.open_ai_key = open_ai_key
        self.id = id
        self.org_id = org_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.open_ai_endpoint = open_ai_endpoint

    @property
    def provider(self):
        """Gets the provider of this AzureOpenAICredential.  # noqa: E501


        :return: The provider of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AzureOpenAICredential.


        :param provider: The provider of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["azure-openai"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this AzureOpenAICredential.  # noqa: E501


        :return: The region of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AzureOpenAICredential.


        :param region: The region of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501
        allowed_values = ["australia", "canada", "eastus2", "eastus", "france", "india", "japan", "northcentralus", "norway", "southcentralus", "sweden", "switzerland", "uk", "westus", "westus3"]  # noqa: E501
        if region not in allowed_values:
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def models(self):
        """Gets the models of this AzureOpenAICredential.  # noqa: E501


        :return: The models of this AzureOpenAICredential.  # noqa: E501
        :rtype: list[str]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this AzureOpenAICredential.


        :param models: The models of this AzureOpenAICredential.  # noqa: E501
        :type: list[str]
        """
        if models is None:
            raise ValueError("Invalid value for `models`, must not be `None`")  # noqa: E501
        allowed_values = ["gpt-4o-2024-05-13", "gpt-4-turbo-2024-04-09", "gpt-4-0125-preview", "gpt-4-1106-preview", "gpt-4-0613", "gpt-35-turbo-0125", "gpt-35-turbo-1106"]  # noqa: E501
        if not set(models).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `models` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(models) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._models = models

    @property
    def open_ai_key(self):
        """Gets the open_ai_key of this AzureOpenAICredential.  # noqa: E501

        This is not returned in the API.  # noqa: E501

        :return: The open_ai_key of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._open_ai_key

    @open_ai_key.setter
    def open_ai_key(self, open_ai_key):
        """Sets the open_ai_key of this AzureOpenAICredential.

        This is not returned in the API.  # noqa: E501

        :param open_ai_key: The open_ai_key of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if open_ai_key is None:
            raise ValueError("Invalid value for `open_ai_key`, must not be `None`")  # noqa: E501

        self._open_ai_key = open_ai_key

    @property
    def id(self):
        """Gets the id of this AzureOpenAICredential.  # noqa: E501

        This is the unique identifier for the credential.  # noqa: E501

        :return: The id of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureOpenAICredential.

        This is the unique identifier for the credential.  # noqa: E501

        :param id: The id of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this AzureOpenAICredential.  # noqa: E501

        This is the unique identifier for the org that this credential belongs to.  # noqa: E501

        :return: The org_id of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this AzureOpenAICredential.

        This is the unique identifier for the org that this credential belongs to.  # noqa: E501

        :param org_id: The org_id of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def created_at(self):
        """Gets the created_at of this AzureOpenAICredential.  # noqa: E501

        This is the ISO 8601 date-time string of when the credential was created.  # noqa: E501

        :return: The created_at of this AzureOpenAICredential.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AzureOpenAICredential.

        This is the ISO 8601 date-time string of when the credential was created.  # noqa: E501

        :param created_at: The created_at of this AzureOpenAICredential.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AzureOpenAICredential.  # noqa: E501

        This is the ISO 8601 date-time string of when the assistant was last updated.  # noqa: E501

        :return: The updated_at of this AzureOpenAICredential.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AzureOpenAICredential.

        This is the ISO 8601 date-time string of when the assistant was last updated.  # noqa: E501

        :param updated_at: The updated_at of this AzureOpenAICredential.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def open_ai_endpoint(self):
        """Gets the open_ai_endpoint of this AzureOpenAICredential.  # noqa: E501


        :return: The open_ai_endpoint of this AzureOpenAICredential.  # noqa: E501
        :rtype: str
        """
        return self._open_ai_endpoint

    @open_ai_endpoint.setter
    def open_ai_endpoint(self, open_ai_endpoint):
        """Sets the open_ai_endpoint of this AzureOpenAICredential.


        :param open_ai_endpoint: The open_ai_endpoint of this AzureOpenAICredential.  # noqa: E501
        :type: str
        """
        if open_ai_endpoint is None:
            raise ValueError("Invalid value for `open_ai_endpoint`, must not be `None`")  # noqa: E501

        self._open_ai_endpoint = open_ai_endpoint

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
        if issubclass(AzureOpenAICredential, dict):
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
        if not isinstance(other, AzureOpenAICredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
