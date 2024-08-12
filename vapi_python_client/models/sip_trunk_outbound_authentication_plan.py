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

class SipTrunkOutboundAuthenticationPlan(object):
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
        'auth_password': 'str',
        'auth_username': 'str',
        'sip_register_plan': 'AllOfSipTrunkOutboundAuthenticationPlanSipRegisterPlan'
    }

    attribute_map = {
        'auth_password': 'authPassword',
        'auth_username': 'authUsername',
        'sip_register_plan': 'sipRegisterPlan'
    }

    def __init__(self, auth_password=None, auth_username=None, sip_register_plan=None):  # noqa: E501
        """SipTrunkOutboundAuthenticationPlan - a model defined in Swagger"""  # noqa: E501
        self._auth_password = None
        self._auth_username = None
        self._sip_register_plan = None
        self.discriminator = None
        if auth_password is not None:
            self.auth_password = auth_password
        if auth_username is not None:
            self.auth_username = auth_username
        if sip_register_plan is not None:
            self.sip_register_plan = sip_register_plan

    @property
    def auth_password(self):
        """Gets the auth_password of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501

        This is not returned in the API.  # noqa: E501

        :return: The auth_password of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :rtype: str
        """
        return self._auth_password

    @auth_password.setter
    def auth_password(self, auth_password):
        """Sets the auth_password of this SipTrunkOutboundAuthenticationPlan.

        This is not returned in the API.  # noqa: E501

        :param auth_password: The auth_password of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :type: str
        """

        self._auth_password = auth_password

    @property
    def auth_username(self):
        """Gets the auth_username of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501


        :return: The auth_username of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :rtype: str
        """
        return self._auth_username

    @auth_username.setter
    def auth_username(self, auth_username):
        """Sets the auth_username of this SipTrunkOutboundAuthenticationPlan.


        :param auth_username: The auth_username of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :type: str
        """

        self._auth_username = auth_username

    @property
    def sip_register_plan(self):
        """Gets the sip_register_plan of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501

        This can be used to configure the SIP register if required by the SIP trunk.  # noqa: E501

        :return: The sip_register_plan of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :rtype: AllOfSipTrunkOutboundAuthenticationPlanSipRegisterPlan
        """
        return self._sip_register_plan

    @sip_register_plan.setter
    def sip_register_plan(self, sip_register_plan):
        """Sets the sip_register_plan of this SipTrunkOutboundAuthenticationPlan.

        This can be used to configure the SIP register if required by the SIP trunk.  # noqa: E501

        :param sip_register_plan: The sip_register_plan of this SipTrunkOutboundAuthenticationPlan.  # noqa: E501
        :type: AllOfSipTrunkOutboundAuthenticationPlanSipRegisterPlan
        """

        self._sip_register_plan = sip_register_plan

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
        if issubclass(SipTrunkOutboundAuthenticationPlan, dict):
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
        if not isinstance(other, SipTrunkOutboundAuthenticationPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
