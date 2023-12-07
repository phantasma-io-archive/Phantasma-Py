import binascii

class Base16:
    @staticmethod
    def encode(string: str) -> str:
        if not string:
            return ""
        return binascii.hexlify(string.encode()).decode()

    @staticmethod
    def encode_uint8_array(array: bytearray) -> str:
        if not array:
            return ""
        return binascii.hexlify(array).decode().upper()

    @staticmethod
    def decode(hex_string: str) -> str:
        if not hex_string or len(hex_string) % 2 != 0:
            return ""
        return binascii.unhexlify(hex_string).decode()

    @staticmethod
    def decode_uint8_array(hex_string: str) -> bytearray:
        if not hex_string or len(hex_string) % 2 != 0:
            return bytearray()
        return bytearray(binascii.unhexlify(hex_string))
