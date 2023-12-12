from enum import IntEnum


class Opcode(IntEnum):
    NOP = 0
    # Register
    MOVE = 1
    COPY = 2
    PUSH = 3
    POP = 4
    SWAP = 5
    # Flow
    CALL = 6
    EXTCALL = 7
    JMP = 8
    JMPIF = 9
    JMPNOT = 10
    RET = 11
    THROW = 12
    # Data
    LOAD = 13
    CAST = 14
    CAT = 15
    RANGE = 16
    LEFT = 17
    RIGHT = 18
    SIZE = 19
    COUNT = 20
    # Logical
    NOT = 21
    AND = 22
    OR = 23
    XOR = 24
    EQUAL = 25
    LT = 26
    GT = 27
    LTE = 28
    GTE = 29
    # Numeric
    INC = 30
    DEC = 31
    SIGN = 32
    NEGATE = 33
    ABS = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    MOD = 39
    SHL = 40
    SHR = 41
    MIN = 42
    MAX = 43
    POW = 44
    # Context
    CTX = 45
    SWITCH = 46
    # Array
    PUT = 47
    GET = 48
    CLEAR = 49
    UNPACK = 50
    PACK = 51
    # Debugger
    DEBUG = 52
    # ADD
    SUBSTR = 53
