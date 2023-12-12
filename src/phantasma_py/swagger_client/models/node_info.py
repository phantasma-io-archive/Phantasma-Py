# coding: utf-8

"""
    Phantasma API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NodeInfo(object):
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
        'protocol_version': 'NodeInfoProtocolVersion',
        'id': 'str',
        'listen_addr': 'str',
        'network': 'str',
        'version': 'str',
        'channels': 'str',
        'moniker': 'str',
        'other': 'NodeInfoOther'
    }

    attribute_map = {
        'protocol_version': 'protocolVersion',
        'id': 'id',
        'listen_addr': 'listenAddr',
        'network': 'network',
        'version': 'version',
        'channels': 'channels',
        'moniker': 'moniker',
        'other': 'other'
    }

    def __init__(self, protocol_version=None, id=None, listen_addr=None, network=None, version=None, channels=None, moniker=None, other=None):  # noqa: E501
        """NodeInfo - a model defined in Swagger"""  # noqa: E501
        self._protocol_version = None
        self._id = None
        self._listen_addr = None
        self._network = None
        self._version = None
        self._channels = None
        self._moniker = None
        self._other = None
        self.discriminator = None
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if id is not None:
            self.id = id
        if listen_addr is not None:
            self.listen_addr = listen_addr
        if network is not None:
            self.network = network
        if version is not None:
            self.version = version
        if channels is not None:
            self.channels = channels
        if moniker is not None:
            self.moniker = moniker
        if other is not None:
            self.other = other

    @property
    def protocol_version(self):
        """Gets the protocol_version of this NodeInfo.  # noqa: E501


        :return: The protocol_version of this NodeInfo.  # noqa: E501
        :rtype: NodeInfoProtocolVersion
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this NodeInfo.


        :param protocol_version: The protocol_version of this NodeInfo.  # noqa: E501
        :type: NodeInfoProtocolVersion
        """

        self._protocol_version = protocol_version

    @property
    def id(self):
        """Gets the id of this NodeInfo.  # noqa: E501


        :return: The id of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeInfo.


        :param id: The id of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def listen_addr(self):
        """Gets the listen_addr of this NodeInfo.  # noqa: E501


        :return: The listen_addr of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._listen_addr

    @listen_addr.setter
    def listen_addr(self, listen_addr):
        """Sets the listen_addr of this NodeInfo.


        :param listen_addr: The listen_addr of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._listen_addr = listen_addr

    @property
    def network(self):
        """Gets the network of this NodeInfo.  # noqa: E501


        :return: The network of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NodeInfo.


        :param network: The network of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def version(self):
        """Gets the version of this NodeInfo.  # noqa: E501


        :return: The version of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodeInfo.


        :param version: The version of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def channels(self):
        """Gets the channels of this NodeInfo.  # noqa: E501


        :return: The channels of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this NodeInfo.


        :param channels: The channels of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._channels = channels

    @property
    def moniker(self):
        """Gets the moniker of this NodeInfo.  # noqa: E501


        :return: The moniker of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._moniker

    @moniker.setter
    def moniker(self, moniker):
        """Sets the moniker of this NodeInfo.


        :param moniker: The moniker of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._moniker = moniker

    @property
    def other(self):
        """Gets the other of this NodeInfo.  # noqa: E501


        :return: The other of this NodeInfo.  # noqa: E501
        :rtype: NodeInfoOther
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this NodeInfo.


        :param other: The other of this NodeInfo.  # noqa: E501
        :type: NodeInfoOther
        """

        self._other = other

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
        if issubclass(NodeInfo, dict):
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
        if not isinstance(other, NodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other