from enum import IntEnum

class AddressKind(IntEnum):
    Invalid = 0
    User = 1
    System = 2
    Interop = 3