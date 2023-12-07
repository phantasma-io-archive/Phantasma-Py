# Assuming PBinaryReader and PBinaryWriter are already defined
# from your previous code or another source

from enum import IntEnum


class SignatureKind(IntEnum):
    None_ = 0
    Ed25519 = 1
    ECDSA = 2