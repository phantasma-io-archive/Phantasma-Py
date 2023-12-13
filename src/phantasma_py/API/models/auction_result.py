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

class AuctionResult(object):
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
        'creator_address': 'str',
        'chain_address': 'str',
        'start_date': 'int',
        'end_date': 'int',
        'base_symbol': 'str',
        'quote_symbol': 'str',
        'token_id': 'str',
        'price': 'str',
        'end_price': 'str',
        'extension_period': 'str',
        'type': 'str',
        'rom': 'str',
        'ram': 'str',
        'listing_fee': 'str',
        'current_winner': 'str'
    }

    attribute_map = {
        'creator_address': 'creatorAddress',
        'chain_address': 'chainAddress',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'base_symbol': 'baseSymbol',
        'quote_symbol': 'quoteSymbol',
        'token_id': 'tokenId',
        'price': 'price',
        'end_price': 'endPrice',
        'extension_period': 'extensionPeriod',
        'type': 'type',
        'rom': 'rom',
        'ram': 'ram',
        'listing_fee': 'listingFee',
        'current_winner': 'currentWinner'
    }

    def __init__(self, creator_address=None, chain_address=None, start_date=None, end_date=None, base_symbol=None, quote_symbol=None, token_id=None, price=None, end_price=None, extension_period=None, type=None, rom=None, ram=None, listing_fee=None, current_winner=None):  # noqa: E501
        """AuctionResult - a model defined in Swagger"""  # noqa: E501
        self._creator_address = None
        self._chain_address = None
        self._start_date = None
        self._end_date = None
        self._base_symbol = None
        self._quote_symbol = None
        self._token_id = None
        self._price = None
        self._end_price = None
        self._extension_period = None
        self._type = None
        self._rom = None
        self._ram = None
        self._listing_fee = None
        self._current_winner = None
        self.discriminator = None
        if creator_address is not None:
            self.creator_address = creator_address
        if chain_address is not None:
            self.chain_address = chain_address
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if base_symbol is not None:
            self.base_symbol = base_symbol
        if quote_symbol is not None:
            self.quote_symbol = quote_symbol
        if token_id is not None:
            self.token_id = token_id
        if price is not None:
            self.price = price
        if end_price is not None:
            self.end_price = end_price
        if extension_period is not None:
            self.extension_period = extension_period
        if type is not None:
            self.type = type
        if rom is not None:
            self.rom = rom
        if ram is not None:
            self.ram = ram
        if listing_fee is not None:
            self.listing_fee = listing_fee
        if current_winner is not None:
            self.current_winner = current_winner

    @property
    def creator_address(self):
        """Gets the creator_address of this AuctionResult.  # noqa: E501


        :return: The creator_address of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._creator_address

    @creator_address.setter
    def creator_address(self, creator_address):
        """Sets the creator_address of this AuctionResult.


        :param creator_address: The creator_address of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._creator_address = creator_address

    @property
    def chain_address(self):
        """Gets the chain_address of this AuctionResult.  # noqa: E501


        :return: The chain_address of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._chain_address

    @chain_address.setter
    def chain_address(self, chain_address):
        """Sets the chain_address of this AuctionResult.


        :param chain_address: The chain_address of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._chain_address = chain_address

    @property
    def start_date(self):
        """Gets the start_date of this AuctionResult.  # noqa: E501


        :return: The start_date of this AuctionResult.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AuctionResult.


        :param start_date: The start_date of this AuctionResult.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this AuctionResult.  # noqa: E501


        :return: The end_date of this AuctionResult.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AuctionResult.


        :param end_date: The end_date of this AuctionResult.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def base_symbol(self):
        """Gets the base_symbol of this AuctionResult.  # noqa: E501


        :return: The base_symbol of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._base_symbol

    @base_symbol.setter
    def base_symbol(self, base_symbol):
        """Sets the base_symbol of this AuctionResult.


        :param base_symbol: The base_symbol of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._base_symbol = base_symbol

    @property
    def quote_symbol(self):
        """Gets the quote_symbol of this AuctionResult.  # noqa: E501


        :return: The quote_symbol of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._quote_symbol

    @quote_symbol.setter
    def quote_symbol(self, quote_symbol):
        """Sets the quote_symbol of this AuctionResult.


        :param quote_symbol: The quote_symbol of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._quote_symbol = quote_symbol

    @property
    def token_id(self):
        """Gets the token_id of this AuctionResult.  # noqa: E501


        :return: The token_id of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this AuctionResult.


        :param token_id: The token_id of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def price(self):
        """Gets the price of this AuctionResult.  # noqa: E501


        :return: The price of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AuctionResult.


        :param price: The price of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def end_price(self):
        """Gets the end_price of this AuctionResult.  # noqa: E501


        :return: The end_price of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._end_price

    @end_price.setter
    def end_price(self, end_price):
        """Sets the end_price of this AuctionResult.


        :param end_price: The end_price of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._end_price = end_price

    @property
    def extension_period(self):
        """Gets the extension_period of this AuctionResult.  # noqa: E501


        :return: The extension_period of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._extension_period

    @extension_period.setter
    def extension_period(self, extension_period):
        """Sets the extension_period of this AuctionResult.


        :param extension_period: The extension_period of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._extension_period = extension_period

    @property
    def type(self):
        """Gets the type of this AuctionResult.  # noqa: E501


        :return: The type of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuctionResult.


        :param type: The type of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def rom(self):
        """Gets the rom of this AuctionResult.  # noqa: E501


        :return: The rom of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._rom

    @rom.setter
    def rom(self, rom):
        """Sets the rom of this AuctionResult.


        :param rom: The rom of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._rom = rom

    @property
    def ram(self):
        """Gets the ram of this AuctionResult.  # noqa: E501


        :return: The ram of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this AuctionResult.


        :param ram: The ram of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._ram = ram

    @property
    def listing_fee(self):
        """Gets the listing_fee of this AuctionResult.  # noqa: E501


        :return: The listing_fee of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._listing_fee

    @listing_fee.setter
    def listing_fee(self, listing_fee):
        """Sets the listing_fee of this AuctionResult.


        :param listing_fee: The listing_fee of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._listing_fee = listing_fee

    @property
    def current_winner(self):
        """Gets the current_winner of this AuctionResult.  # noqa: E501


        :return: The current_winner of this AuctionResult.  # noqa: E501
        :rtype: str
        """
        return self._current_winner

    @current_winner.setter
    def current_winner(self, current_winner):
        """Sets the current_winner of this AuctionResult.


        :param current_winner: The current_winner of this AuctionResult.  # noqa: E501
        :type: str
        """

        self._current_winner = current_winner

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
        if issubclass(AuctionResult, dict):
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
        if not isinstance(other, AuctionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other