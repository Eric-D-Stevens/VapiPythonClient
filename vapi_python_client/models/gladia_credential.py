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

class GladiaCredential(object):
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
        'api_key': 'str',
        'id': 'str',
        'org_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'provider': 'provider',
        'api_key': 'apiKey',
        'id': 'id',
        'org_id': 'orgId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, provider=None, api_key=None, id=None, org_id=None, created_at=None, updated_at=None):  # noqa: E501
        """GladiaCredential - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._api_key = None
        self._id = None
        self._org_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.provider = provider
        self.api_key = api_key
        self.id = id
        self.org_id = org_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def provider(self):
        """Gets the provider of this GladiaCredential.  # noqa: E501


        :return: The provider of this GladiaCredential.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this GladiaCredential.


        :param provider: The provider of this GladiaCredential.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["gladia"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def api_key(self):
        """Gets the api_key of this GladiaCredential.  # noqa: E501

        This is not returned in the API.  # noqa: E501

        :return: The api_key of this GladiaCredential.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this GladiaCredential.

        This is not returned in the API.  # noqa: E501

        :param api_key: The api_key of this GladiaCredential.  # noqa: E501
        :type: str
        """
        if api_key is None:
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def id(self):
        """Gets the id of this GladiaCredential.  # noqa: E501

        This is the unique identifier for the credential.  # noqa: E501

        :return: The id of this GladiaCredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GladiaCredential.

        This is the unique identifier for the credential.  # noqa: E501

        :param id: The id of this GladiaCredential.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this GladiaCredential.  # noqa: E501

        This is the unique identifier for the org that this credential belongs to.  # noqa: E501

        :return: The org_id of this GladiaCredential.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this GladiaCredential.

        This is the unique identifier for the org that this credential belongs to.  # noqa: E501

        :param org_id: The org_id of this GladiaCredential.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def created_at(self):
        """Gets the created_at of this GladiaCredential.  # noqa: E501

        This is the ISO 8601 date-time string of when the credential was created.  # noqa: E501

        :return: The created_at of this GladiaCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GladiaCredential.

        This is the ISO 8601 date-time string of when the credential was created.  # noqa: E501

        :param created_at: The created_at of this GladiaCredential.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GladiaCredential.  # noqa: E501

        This is the ISO 8601 date-time string of when the assistant was last updated.  # noqa: E501

        :return: The updated_at of this GladiaCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GladiaCredential.

        This is the ISO 8601 date-time string of when the assistant was last updated.  # noqa: E501

        :param updated_at: The updated_at of this GladiaCredential.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(GladiaCredential, dict):
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
        if not isinstance(other, GladiaCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
