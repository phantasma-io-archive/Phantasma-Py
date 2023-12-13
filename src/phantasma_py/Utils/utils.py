import binascii
import base64

from phantasma_py.Types import Address

def hex_to_byte_array(hex_string):
    return bytearray.fromhex(hex_string)

def hex_to_buffer(hex_string):
    return bytes.fromhex(hex_string)

def buffer_to_hex(buffer):
    return binascii.hexlify(buffer).decode('utf-8')

def reverse_hex(hex_string):
    return hex_string[::-1]

def decode_base16(hex_string):
    return bytearray.fromhex(hex_string).decode()

def encode_base16(string):
    return binascii.hexlify(string.encode()).decode('utf-8').upper()

def uint8_array_to_string(array):
    return ''.join(chr(b) for b in array)

def string_to_uint8_array(string):
    return bytearray(string, 'utf-8')

def hex_string_to_uint8_array(hex_string):
    return bytearray.fromhex(hex_string)

def hex_string_to_bytes(hex_string):
    return bytearray.fromhex(hex_string)

def get_difficulty(transaction_hash):
    bytes = hex_string_to_bytes(transaction_hash)
    bytes.reverse()
    result = 0

    for byte in bytes:
        for j in range(8):
            if byte & (1 << j):
                result = 1 + (len(bytes) - 1 - result) * 8 + j
                return 256 - result

    return 256 - result


def number_to_byte_array(num, size=None):
    if size is None:
        size = (num.bit_length() + 7) // 8
    return num.to_bytes(size, byteorder='little')

def big_int_to_byte_array(bigint):
    hex_string = bigint.to_bytes((bigint.bit_length() + 7) // 8, 'big').hex()
    return bytearray.fromhex(hex_string)

def hex2ascii(hex_string):
    return bytearray.fromhex(hex_string).decode()

def int2buffer(i):
    return i.to_bytes((i.bit_length() + 7) // 8, 'big')


def get_address_from_public_key(public_key):
    # Decode the public key from Base16 (hex) to bytes
    pub_key_bytes = base64.b16decode(public_key.upper())

    # Create a new bytes array and set the first two elements
    addr_array = bytearray(34)
    addr_array[0] = 1

    # Copy 32 bytes from the public key to addr_array, starting from the 3rd position
    addr_array[2:34] = pub_key_bytes[:32]

    return Address.FromPublicKey(addr_array)