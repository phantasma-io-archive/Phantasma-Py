from enum import Enum
from typing import NamedTuple

# Assuming ContractInterface is defined elsewhere in your Python code
# from contract_interface import ContractInterface

class NativeContractKind(Enum):
    Gas = 0
    Block = 1
    Stake = 2
    Swap = 3
    Account = 4
    Consensus = 5
    Governance = 6
    Storage = 7
    Validator = 8
    Interop = 9
    Exchange = 10
    Privacy = 11
    Relay = 12
    Ranking = 13
    Market = 14
    Friends = 15
    Mail = 16
    Sale = 17
    Unknown = 18

class IContract(NamedTuple):
    Name: str
    #ABI: ContractInterface

# Example Usage
# contract = IContract(Name="MyContract", ABI=contract_interface)
