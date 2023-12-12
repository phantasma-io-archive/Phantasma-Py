from .Extensions import PBinaryWriter
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature
from typing import List

class Ed25519Signature:
    def __init__(self, bytes=None):
        self.bytes = bytes
        self.kind = "Ed25519"  # assuming SignatureKind is an enum or similar in Python

    def verify(self, message: bytes, address) -> bool:
        return self.verify_multiple(message, [address])

    def verify_multiple(self, message: bytes, addresses: List) -> bool:
        for address in addresses:
            if not address.is_user:
                continue
            public_key_bytes = address.to_byte_array()[2:]
            public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_key_bytes)
            try:
                public_key.verify(self.bytes, message)
                return True
            except InvalidSignature:
                continue
        return False

    def serialize_data(self, writer) -> None:
        writer.write_byte_array(self.bytes)

    def unserialize_data(self, reader) -> None:
        self.bytes = reader.read_byte_array()

    def to_byte_array(self) -> bytes:
        # Assuming PBinaryWriter is implemented in Python
        writer = PBinaryWriter()
        self.serialize_data(writer)
        return writer.to_bytes()

    @staticmethod
    def generate(keypair, message: bytes):
        private_key = ed25519.Ed25519PrivateKey.from_private_bytes(keypair.private_key)
        signature = private_key.sign(message)
        return Ed25519Signature(signature)
