import base64
import hashlib
from ..Interfaces.IKeyPair import IKeyPair
import base58
from . import Address, Ed25519Signature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
import os

class PhantasmaKeys:
    PrivateKeyLength = 32
    PublicKey = None

    def __init__(self, private_key: bytes):
        if len(private_key) == 64:
            private_key = private_key[:32]

        if len(private_key) != self.PrivateKeyLength:
            raise ValueError(f"PrivateKey should have length {self.PrivateKeyLength}")

        self._private_key = private_key
        self._private_key_obj = ed25519.Ed25519PrivateKey.from_private_bytes(self._private_key)
        self._public_key = self._private_key_obj.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        
        self.PublicKey = self._public_key
        #if ( hasattr(Address, 'FromKey') ):
        self.Address = Address.FromKey(self._public_key)
        #Address.FromMyKey()  # Implement Address class

    def __str__(self):
        return self.Address.Text

    @staticmethod
    def generate():
        private_key = os.urandom(PhantasmaKeys.PrivateKeyLength)
        return PhantasmaKeys(private_key)

    @staticmethod
    def from_wif(wif: str):

        if not wif:
            raise ValueError("WIF required")

        # Decode the WIF string
        data = base58.b58decode(wif)

        # Perform checks on the decoded data
        if len(data) == 38:
            data = data[:-4]  # Remove the last 4 bytes (checksum)

        if len(data) != 34 or data[0] != 0x80 or data[-1] != 0x01:
            raise ValueError("Invalid WIF format")

        private_key = data[1:33]  # Extract the private key
        return PhantasmaKeys(private_key)

    def to_wif(self):
        # Step 1: Prepend 0x80 to the private key
        extended_private_key = b'\x80' + self._private_key

        # Step 2: Append 0x01 as a suffix
        extended_private_key = extended_private_key + b'\x01'

        # Step 3: Perform SHA-256 hash twice
        first_sha256 = hashlib.sha256(extended_private_key).digest()
        second_sha256 = hashlib.sha256(first_sha256).digest()

        # Step 4: Append the first 4 bytes of the double SHA-256 hash as a checksum
        checksum = second_sha256[:4]
        wif_bytes = extended_private_key + checksum

        # Step 5: Encode the result using base58 encoding
        wif_string = base58.b58encode(wif_bytes)

        return wif_string.decode('utf-8')

    def sign(self, message: bytes):
    # Return an Ed25519Signature object
        return Ed25519Signature.generate(self, message)