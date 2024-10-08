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

class JsonSchema(object):
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
        'items': 'object',
        'properties': 'object',
        'description': 'str',
        'required': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'items': 'items',
        'properties': 'properties',
        'description': 'description',
        'required': 'required'
    }

    def __init__(self, type=None, items=None, properties=None, description=None, required=None):  # noqa: E501
        """JsonSchema - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._items = None
        self._properties = None
        self._description = None
        self._required = None
        self.discriminator = None
        self.type = type
        if items is not None:
            self.items = items
        if properties is not None:
            self.properties = properties
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required

    @property
    def type(self):
        """Gets the type of this JsonSchema.  # noqa: E501

        This is the type of output you'd like.  `string`, `number`, `integer`, `boolean` are the primitive types and should be obvious.  `array` and `object` are more interesting and quite powerful. They allow you to define nested structures.  For `array`, you can define the schema of the items in the array using the `items` property.  For `object`, you can define the properties of the object using the `properties` property.  # noqa: E501

        :return: The type of this JsonSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JsonSchema.

        This is the type of output you'd like.  `string`, `number`, `integer`, `boolean` are the primitive types and should be obvious.  `array` and `object` are more interesting and quite powerful. They allow you to define nested structures.  For `array`, you can define the schema of the items in the array using the `items` property.  For `object`, you can define the properties of the object using the `properties` property.  # noqa: E501

        :param type: The type of this JsonSchema.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "integer", "boolean", "array", "object"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def items(self):
        """Gets the items of this JsonSchema.  # noqa: E501

        This is required if the type is \"array\". This is the schema of the items in the array.  This is of type JsonSchema. However, Swagger doesn't support circular references.  # noqa: E501

        :return: The items of this JsonSchema.  # noqa: E501
        :rtype: object
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this JsonSchema.

        This is required if the type is \"array\". This is the schema of the items in the array.  This is of type JsonSchema. However, Swagger doesn't support circular references.  # noqa: E501

        :param items: The items of this JsonSchema.  # noqa: E501
        :type: object
        """

        self._items = items

    @property
    def properties(self):
        """Gets the properties of this JsonSchema.  # noqa: E501

        This is required if the type is \"object\". This specifies the properties of the object.  This is a map of string to JsonSchema. However, Swagger doesn't support circular references.  # noqa: E501

        :return: The properties of this JsonSchema.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JsonSchema.

        This is required if the type is \"object\". This specifies the properties of the object.  This is a map of string to JsonSchema. However, Swagger doesn't support circular references.  # noqa: E501

        :param properties: The properties of this JsonSchema.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def description(self):
        """Gets the description of this JsonSchema.  # noqa: E501

        This is the description to help the model understand what it needs to output.  # noqa: E501

        :return: The description of this JsonSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonSchema.

        This is the description to help the model understand what it needs to output.  # noqa: E501

        :param description: The description of this JsonSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this JsonSchema.  # noqa: E501

        This is a list of properties that are required.  This only makes sense if the type is \"object\".  # noqa: E501

        :return: The required of this JsonSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this JsonSchema.

        This is a list of properties that are required.  This only makes sense if the type is \"object\".  # noqa: E501

        :param required: The required of this JsonSchema.  # noqa: E501
        :type: list[str]
        """

        self._required = required

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
        if issubclass(JsonSchema, dict):
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
        if not isinstance(other, JsonSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
