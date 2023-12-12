#from Types import PhantasmaKeys
from .Enums import AddressKind
from .Serialization import Serialization
import base58
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from typing import Union

class Address:
    NullText = "NULL"
    LengthInBytes = 34
    MaxPlatformNameLength = 10
    NullPublicKey = bytes([0] * LengthInBytes)
    Null = None  # This will be initialized after the class definition

    _keyToTextCache = {}

    def __init__(self, public_key: bytes):
        if len(public_key) != Address.LengthInBytes:
            raise ValueError(f"publicKey length must be {Address.LengthInBytes}, it was {len(public_key)}")
        self._bytes = public_key[0:Address.LengthInBytes]
        self._text = None

    @staticmethod
    def FromKey(key):
        bytes = bytearray()
        bytes.extend([ AddressKind.User])
        if len(key) == 32:
            bytes.extend([0] * 1) 
            bytes.extend(key)
        elif len(key) == 33:
            #bytes.extend([0] * 1) 
            bytes.extend(key[1:])
        elif len(key) == 64:
            #bytes.extend([0] * 1) 
            bytes.extend(key[:32])
        else:
            raise ValueError(f'Invalid public key length: {len(key)}')
        return Address(bytes)

    def Kind(self):
        if self.IsNull():
            return AddressKind.System
        elif self._bytes[0] >= 3:
            return AddressKind.Interop
        else:
            return self._bytes[0]

    def IsSystem(self) -> bool:
        return self.Kind == AddressKind.System

    def IsInterop(self) -> bool:
        return self.Kind == AddressKind.Interop

    def IsUser(self) -> bool:
        return self.Kind == AddressKind.User
    
    def IsNull(self):
        if self._bytes is None or len(self._bytes) == 0:
            return True

        for i in range(1, len(self._bytes)):
            if self._bytes[i] != 0:
                return False

        return True

    @property
    def Text(self):
        if self.IsNull():
            return Address.NullText

        if not self._text:
            #if self._bytes in self._keyToTextCache:
            #    print("here3")
            #    self._text = self._keyToTextCache[self._bytes]

            if not self._text:
                prefix = 'P' 
                if self.IsNull():
                    prefix = 'S'
                elif self._bytes[0] >= 3:
                    prefix = 'X'
                base58_text = base58.b58encode(self._bytes).decode('utf-8')
                self._text = prefix + base58_text
                #self._keyToTextCache[self._bytes] = self._text

        return self._text
    
    @staticmethod
    def FromPublicKey(public_key: bytes):
        public_key = public_key[:Address.LengthInBytes]
        return Address(public_key)

    @staticmethod
    def FromText(text: str):
        return Address.Parse(text)

    @staticmethod
    def Parse(text: str):
        if text is None:
            return Address.Null

        if text == Address.NullText:
            return Address.Null

        prefix = text[0]
        text = text[1:]
        bytes_ = base58.b58decode(text)
        addr = Address(bytes_)

        if prefix == "P" and addr.Kind() != AddressKind.User:
            raise ValueError("Invalid address prefix. Expected 'P'")
        elif prefix == "S" and addr.Kind() != AddressKind.System:
            raise ValueError("Invalid address prefix. Expected 'S'")
        elif prefix == "X" and addr.Kind() < AddressKind.Interop:
            raise ValueError("Invalid address prefix. Expected 'X'")

        return addr

    @staticmethod
    def IsValidAddress(text: str) -> bool:
        try:
            Address.FromText(text)
            return True
        except:
            return False

    @staticmethod
    def FromHash(input):
        if isinstance(input, str):
            bytes_input = input.encode()
        else:
            bytes_input = input

        hash = hashlib.sha256(bytes_input).digest()
        address_bytes = bytearray(Address.LengthInBytes)
        address_bytes[0] = AddressKind.User
        address_bytes[2:34] = hash[:32]
        return Address(bytes(address_bytes))

    @staticmethod
    def FromWif(wif):
        # Assuming `get_private_key_from_wif` function is implemented to extract the private key from WIF
        private_key = get_private_key_from_wif(wif)
        public_key = private_key.public_key().public_bytes(
            encoding=Serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        address_hex = b'\x01\x00' + public_key
        return Address.FromBytes(address_hex)

    @staticmethod
    def FromBytes(bytes):
        return Address(bytes)

    def compareTo(self, other):
        return (self._bytes > other._bytes) - (self._bytes < other._bytes)

    def equals(self, other):
        return isinstance(other, Address) and self._bytes == other._bytes

    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        if self.is_null():
            return self.NullText

        return self.Text;

    def to_byte_array(self):
        return self._bytes

    def serialize_data(self, writer):
        # Assuming PBinaryWriter is implemented
        writer.write_byte_array(self._bytes)

    def unserialize_data(self, reader):
        # Assuming PBinaryReader is implemented
        self._bytes = reader.read_byte_array()
        self._text = None

    def is_null(self):
        return self._bytes == bytearray(self.LengthInBytes)