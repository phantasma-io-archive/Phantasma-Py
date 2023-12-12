from abc import ABC, abstractmethod
from typing import List
from .SignatureKind import SignatureKind
from ..Types import Address
from ..Types.Extensions import PBinaryReader, PBinaryWriter

class Signature(ABC):
    @property
    @abstractmethod
    def Bytes(self) -> bytes:
        pass

    @property
    @abstractmethod
    def Kind(self) -> SignatureKind:
        pass

    @abstractmethod
    def SerializeData(self, writer: PBinaryWriter):
        pass

    @abstractmethod
    def UnserializeData(self, reader: PBinaryReader):
        pass

    @abstractmethod
    def VerifyMultiple(self, message: bytes, addresses: List[Address]) -> bool:
        pass

    def Verify(self, message: bytes, address: Address) -> bool:
        return self.VerifyMultiple(message, [address])

    def ToByteArray(self) -> bytes:
        stream = bytearray(64)
        writer = PBinaryWriter(stream)
        self.SerializeData(writer)
        return bytes(stream)