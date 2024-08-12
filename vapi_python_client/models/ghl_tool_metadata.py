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

class GhlToolMetadata(object):
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
        'workflow_id': 'str',
        'location_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflowId',
        'location_id': 'locationId'
    }

    def __init__(self, workflow_id=None, location_id=None):  # noqa: E501
        """GhlToolMetadata - a model defined in Swagger"""  # noqa: E501
        self._workflow_id = None
        self._location_id = None
        self.discriminator = None
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if location_id is not None:
            self.location_id = location_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this GhlToolMetadata.  # noqa: E501


        :return: The workflow_id of this GhlToolMetadata.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this GhlToolMetadata.


        :param workflow_id: The workflow_id of this GhlToolMetadata.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def location_id(self):
        """Gets the location_id of this GhlToolMetadata.  # noqa: E501


        :return: The location_id of this GhlToolMetadata.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GhlToolMetadata.


        :param location_id: The location_id of this GhlToolMetadata.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

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
        if issubclass(GhlToolMetadata, dict):
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
        if not isinstance(other, GhlToolMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
