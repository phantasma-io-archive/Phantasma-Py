import struct
import io
from typing import Union

class PBinaryReader:
    def __init__(self, arg1: Union[bytes, bytearray]):
        self.reader = io.BytesIO(arg1)

    @property
    def length(self) -> int:
        current_pos = self.reader.tell()
        self.reader.seek(0, io.SEEK_END)
        length = self.reader.tell()
        self.reader.seek(current_pos, io.SEEK_SET)
        return length

    @property
    def position(self) -> int:
        return self.reader.tell()

    @position.setter
    def position(self, value: int):
        self.reader.seek(value, io.SEEK_SET)

    @property
    def is_end_of_stream(self) -> bool:
        return self.reader.tell() == self.length

    def read_boolean(self) -> bool:
        return struct.unpack('?', self.reader.read(1))[0]

    def read_byte(self) -> int:
        return struct.unpack('B', self.reader.read(1))[0]

    def read_bytes(self, bytes_to_read: int) -> bytes:
        return self.reader.read(bytes_to_read)

    def read_signed_byte(self) -> int:
        return struct.unpack('b', self.reader.read(1))[0]

    def read_short(self) -> int:
        return struct.unpack('<h', self.reader.read(2))[0]

    def read_unsigned_short(self) -> int:
        return struct.unpack('<H', self.reader.read(2))[0]

    def read_int(self) -> int:
        return struct.unpack('<i', self.reader.read(4))[0]

    def read_unsigned_int(self) -> int:
        return struct.unpack('<I', self.reader.read(4))[0]

    def read_long_string(self) -> str:
        length = self.read_var_int()
        return self.read_string_bytes(length)

    def read_long(self) -> int:
        return struct.unpack('<q', self.reader.read(8))[0]

    def read_unsigned_long_string(self) -> str:
        return str(self.read_unsigned_long())

    def read_unsigned_long(self) -> int:
        return struct.unpack('<Q', self.reader.read(8))[0]

    def read_float(self) -> float:
        return struct.unpack('<f', self.reader.read(4))[0]

    def read_double(self) -> float:
        return struct.unpack('<d', self.reader.read(8))[0]

    def read_char(self, encoding: str) -> str:
        return self.reader.read(1).decode(encoding)

    def read_chars(self, characters_to_read: int, encoding: str) -> str:
        return self.reader.read(characters_to_read).decode(encoding)

    def read_big_integer(self) -> int:
        """
        Read a BigInteger. Assumes the BigInteger is unsigned and little-endian encoded.
        """
        length = self.read_var_int()
        if length == 0:
            return 0

        bytes_ = self.read_bytes(length)
        return int.from_bytes(bytes_, byteorder='little', signed=False)

    def read_big_integer_accurate(self) -> str:
        """
        Read a BigInteger accurately as a string.
        """
        length = self.read_var_int()
        if length == 0:
            return "0"

        bytes_ = self.read_bytes(length)
        return str(int.from_bytes(bytes_, byteorder='little', signed=False))

    def read_var_int(self) -> int:
        """
        Read a variable length integer.
        """
        first_byte = self.read_byte()
        if first_byte == 0xfd:
            return struct.unpack('<H', self.read_bytes(2))[0]
        elif first_byte == 0xfe:
            return struct.unpack('<I', self.read_bytes(4))[0]
        elif first_byte == 0xff:
            return struct.unpack('<Q', self.read_bytes(8))[0]
        else:
            return first_byte

    def read_timestamp(self) -> int:
        """
        Read a timestamp. Assumes the timestamp is a 32-bit Unix timestamp.
        """
        bytes_ = self.read_bytes(4)
        return int.from_bytes(bytes_, byteorder='little', signed=False)

    def read_vm_object(self):
        """
        Read a VM object. Implementation depends on the VM's specification.
        """
        # Placeholder for reading a VM object based on your VM's specification.
        pass

    def read_string_bytes(self, num_bytes: int) -> str:
        return self.reader.read(num_bytes).decode()

    # You would need to implement other methods (like readBigInteger, readSignature, etc.) 
    # based on your application logic and the availability of related Python libraries or classes.

# Note: This implementation assumes certain classes and methods are defined elsewhere, like Signature, Timestamp, etc.
