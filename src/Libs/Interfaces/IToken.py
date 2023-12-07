from enum import Enum
from typing import NamedTuple, ByteString

from Types import Address

# Assuming Address and ContractInterface are defined elsewhere in your code
# from address import Address
# from contract_interface import ContractInterface

class TokenFlags(Enum):
    None_ = 0
    Transferable = 1 << 0
    Fungible = 1 << 1
    Finite = 1 << 2
    Divisible = 1 << 3
    Fuel = 1 << 4
    Stakable = 1 << 5
    Fiat = 1 << 6
    Swappable = 1 << 7
    Burnable = 1 << 8
    Mintable = 1 << 9

class TokenSeriesMode(Enum):
    Unique = 0
    Duplicated = 1

class IToken(NamedTuple):
    Name: str
    Symbol: str
    Owner: Address
    Flags: TokenFlags
    MaxSupply: int  # BigInteger in Python can be represented as int
    Decimals: int
    Script: ByteString
    ABI: ContractInterface

# Example Usage
# token = IToken(Name="MyToken", Symbol="MTK", Owner=address, Flags=TokenFlags.Fungible, MaxSupply=1000000, Decimals=2, Script=b'your_script', ABI=contract_interface)
