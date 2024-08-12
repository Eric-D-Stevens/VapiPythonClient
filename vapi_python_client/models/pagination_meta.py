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

class PaginationMeta(object):
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
        'items_per_page': 'float',
        'total_items': 'float',
        'current_page': 'float'
    }

    attribute_map = {
        'items_per_page': 'itemsPerPage',
        'total_items': 'totalItems',
        'current_page': 'currentPage'
    }

    def __init__(self, items_per_page=None, total_items=None, current_page=None):  # noqa: E501
        """PaginationMeta - a model defined in Swagger"""  # noqa: E501
        self._items_per_page = None
        self._total_items = None
        self._current_page = None
        self.discriminator = None
        self.items_per_page = items_per_page
        self.total_items = total_items
        self.current_page = current_page

    @property
    def items_per_page(self):
        """Gets the items_per_page of this PaginationMeta.  # noqa: E501


        :return: The items_per_page of this PaginationMeta.  # noqa: E501
        :rtype: float
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this PaginationMeta.


        :param items_per_page: The items_per_page of this PaginationMeta.  # noqa: E501
        :type: float
        """
        if items_per_page is None:
            raise ValueError("Invalid value for `items_per_page`, must not be `None`")  # noqa: E501

        self._items_per_page = items_per_page

    @property
    def total_items(self):
        """Gets the total_items of this PaginationMeta.  # noqa: E501


        :return: The total_items of this PaginationMeta.  # noqa: E501
        :rtype: float
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this PaginationMeta.


        :param total_items: The total_items of this PaginationMeta.  # noqa: E501
        :type: float
        """
        if total_items is None:
            raise ValueError("Invalid value for `total_items`, must not be `None`")  # noqa: E501

        self._total_items = total_items

    @property
    def current_page(self):
        """Gets the current_page of this PaginationMeta.  # noqa: E501


        :return: The current_page of this PaginationMeta.  # noqa: E501
        :rtype: float
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this PaginationMeta.


        :param current_page: The current_page of this PaginationMeta.  # noqa: E501
        :type: float
        """
        if current_page is None:
            raise ValueError("Invalid value for `current_page`, must not be `None`")  # noqa: E501

        self._current_page = current_page

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
        if issubclass(PaginationMeta, dict):
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
        if not isinstance(other, PaginationMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
