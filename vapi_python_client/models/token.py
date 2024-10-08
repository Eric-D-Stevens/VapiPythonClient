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

class Token(object):
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
        'tag': 'str',
        'id': 'str',
        'org_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'value': 'str',
        'name': 'str',
        'restrictions': 'AllOfTokenRestrictions'
    }

    attribute_map = {
        'tag': 'tag',
        'id': 'id',
        'org_id': 'orgId',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'value': 'value',
        'name': 'name',
        'restrictions': 'restrictions'
    }

    def __init__(self, tag=None, id=None, org_id=None, created_at=None, updated_at=None, value=None, name=None, restrictions=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._id = None
        self._org_id = None
        self._created_at = None
        self._updated_at = None
        self._value = None
        self._name = None
        self._restrictions = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        self.id = id
        self.org_id = org_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.value = value
        if name is not None:
            self.name = name
        if restrictions is not None:
            self.restrictions = restrictions

    @property
    def tag(self):
        """Gets the tag of this Token.  # noqa: E501

        This is the tag for the token. It represents its scope.  # noqa: E501

        :return: The tag of this Token.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Token.

        This is the tag for the token. It represents its scope.  # noqa: E501

        :param tag: The tag of this Token.  # noqa: E501
        :type: str
        """
        allowed_values = ["private", "public"]  # noqa: E501
        if tag not in allowed_values:
            raise ValueError(
                "Invalid value for `tag` ({0}), must be one of {1}"  # noqa: E501
                .format(tag, allowed_values)
            )

        self._tag = tag

    @property
    def id(self):
        """Gets the id of this Token.  # noqa: E501

        This is the unique identifier for the token.  # noqa: E501

        :return: The id of this Token.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Token.

        This is the unique identifier for the token.  # noqa: E501

        :param id: The id of this Token.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this Token.  # noqa: E501

        This is unique identifier for the org that this token belongs to.  # noqa: E501

        :return: The org_id of this Token.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Token.

        This is unique identifier for the org that this token belongs to.  # noqa: E501

        :param org_id: The org_id of this Token.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def created_at(self):
        """Gets the created_at of this Token.  # noqa: E501

        This is the ISO 8601 date-time string of when the token was created.  # noqa: E501

        :return: The created_at of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Token.

        This is the ISO 8601 date-time string of when the token was created.  # noqa: E501

        :param created_at: The created_at of this Token.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Token.  # noqa: E501

        This is the ISO 8601 date-time string of when the token was last updated.  # noqa: E501

        :return: The updated_at of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Token.

        This is the ISO 8601 date-time string of when the token was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Token.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this Token.  # noqa: E501

        This is the token key.  # noqa: E501

        :return: The value of this Token.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Token.

        This is the token key.  # noqa: E501

        :param value: The value of this Token.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def name(self):
        """Gets the name of this Token.  # noqa: E501

        This is the name of the token. This is just for your own reference.  # noqa: E501

        :return: The name of this Token.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Token.

        This is the name of the token. This is just for your own reference.  # noqa: E501

        :param name: The name of this Token.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def restrictions(self):
        """Gets the restrictions of this Token.  # noqa: E501

        This are the restrictions for the token.  # noqa: E501

        :return: The restrictions of this Token.  # noqa: E501
        :rtype: AllOfTokenRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this Token.

        This are the restrictions for the token.  # noqa: E501

        :param restrictions: The restrictions of this Token.  # noqa: E501
        :type: AllOfTokenRestrictions
        """

        self._restrictions = restrictions

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
        if issubclass(Token, dict):
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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
