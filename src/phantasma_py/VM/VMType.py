from enum import IntEnum

class VMType(IntEnum):
    NONE = 0
    Struct = 1
    Bytes = 2
    Number = 3
    String = 4
    Timestamp = 5
    Bool = 6
    Enum = 7
    Object = 8
