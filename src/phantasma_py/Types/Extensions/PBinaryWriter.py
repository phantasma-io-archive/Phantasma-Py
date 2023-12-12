import struct
from datetime import datetime
from typing import Union, List

from ...Interfaces import Signature, SignatureKind

# Assuming Signature and SignatureKind are already defined in your Python project

class PBinaryWriter:
    def __init__(self, arg1: Union[None, bytearray, bytes] = None):
        if arg1 is None:
            self._buffer = bytearray()
        elif isinstance(arg1, (bytearray, bytes)):
            self._buffer = bytearray(arg1)
        else:
            raise TypeError("Invalid argument type")

    @property
    def length(self) -> int:
        return len(self._buffer)

    @property
    def position(self) -> int:
        return len(self._buffer)

    def write_boolean(self, value: bool) -> None:
        self._buffer += struct.pack('?', value)

    def write_byte(self, value: int) -> None:
        self._buffer += struct.pack('B', value)

    def write_signed_byte(self, value: int) -> None:
        self._buffer += struct.pack('b', value)

    def write_short(self, value: int) -> None:
        self._buffer += struct.pack('<h', value)

    def write_unsigned_short(self, value: int) -> None:
        self._buffer += struct.pack('<H', value)

    def write_int(self, value: int) -> None:
        self._buffer += struct.pack('<i', value)

    def write_unsigned_int(self, value: int) -> None:
        self._buffer += struct.pack('<I', value)

    def write_long(self, value: Union[str, int]) -> None:
        self._buffer += struct.pack('<q', int(value))

    def write_unsigned_long(self, value: Union[str, int]) -> None:
        self._buffer += struct.pack('<Q', int(value))

    def write_float(self, value: float) -> None:
        self._buffer += struct.pack('<f', value)

    def write_double(self, value: float) -> None:
        self._buffer += struct.pack('<d', value)

    # ... more methods ...

    def to_byte_array(self) -> bytearray:
        return self._buffer

    def write_var_int(self, value: int) -> None:
        if value < 0:
            raise ValueError("negative value invalid")
        if value < 0xfd:
            self.write_byte(value)
        elif value <= 0xffff:
            self.write_byte(0xfd)
            self.write_unsigned_short(value)
        elif value <= 0xffffffff:
            self.write_byte(0xfe)
            self.write_unsigned_int(value)
        else:
            self.write_byte(0xff)
            self.write_unsigned_long(value)

    def write_chars(self, characters: Union[str, List[int]], encoding: str) -> None:
        if isinstance(characters, str):
            self._buffer += characters.encode(encoding)
        elif isinstance(characters, list):
            for char in characters:
                self._buffer += struct.pack('c', char.to_bytes(1, 'little'))

    def clear(self) -> None:
        self._buffer.clear()

    def to_uint8_array(self) -> bytes:
        return bytes(self._buffer)

    def append_bytes(self, bytes_: List[int]) -> None:
        for byte in bytes_:
            if byte is not None and byte != float('nan'):
                self.write_byte(byte)

    def write_enum(self, value: int) -> None:
        bytes_ = [(value >> (8 * i)) & 0xff for i in range(4)]
        self.append_bytes(bytes_)

    def write_bytes(self, bytes_: List[int]) -> None:
        for byte in bytes_:
            self.write_byte(byte)

    def write_timestamp(self, timestamp: datetime) -> None:
        unix_time = int(timestamp.timestamp())
        self.write_unsigned_int(unix_time)

    def write_date_time(self, date_time: datetime) -> None:
        unix_time = int(date_time.timestamp())
        self.write_unsigned_int(unix_time)

    def raw_string(self, value: str) -> List[int]:
        return [ord(char) for char in value]

    def write_byte_array(self, bytes_: Union[List[int], bytes, bytearray]) -> None:
        if isinstance(bytes_, (bytes, bytearray)):
            bytes_ = list(bytes_)
        self.write_var_int(len(bytes_))
        self.write_bytes(bytes_)

    def write_string(self, text: str) -> None:
        bytes_ = self.raw_string(text)
        self.write_var_int(len(bytes_))
        self.write_bytes(bytes_)

    def emit_uint32(self, value: int) -> None:
        bytes_ = [(value >> (8 * i)) & 0xff for i in range(4)]
        self.append_bytes(bytes_)

    def write_big_integer(self, value: int) -> None:
        self.write_big_integer_string(str(value))

    def write_big_integer_string(self, value: str) -> None:
        if value == "0":
            bytes_ = [0]
        elif value.startswith("-"):
            raise ValueError("Unsigned bigint serialization not supported")
        else:
            hex_str = hex(int(value))[2:]
            if len(hex_str) % 2:
                hex_str = '0' + hex_str
            bytes_ = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]
            bytes_.append(0)  # add sign at the end
        self.write_byte_array(bytes_)

    def write_signature(self, signature: Signature) -> None:
        if signature is None:
            self.write_byte(SignatureKind.None_.value)
        else:
            self.write_byte(signature.Kind.value)
            signature.SerializeData(self)

    def append_hex_encoded(self, hex_string: str) -> None:
        local_encoded = bytes.fromhex(hex_string)
        self.write_var_int(len(local_encoded))
        self.append_bytes(list(local_encoded))
