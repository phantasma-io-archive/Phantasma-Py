from datetime import datetime
import binascii
from ecpy.curves import Curve, Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.eddsa import EDDSA
import hashlib

from ..Types.Extensions import PBinaryWriter

from ..VM.ScriptBuilder import ScriptBuilder


class Transaction():

    '''
    The Transaction object implements all the basic methods needed to build a Phantasma Transaction string
    and sign it with HEX PK in order to broadcast to the Phantasma Blockchain.

    Args:
        nexusName (str): mainnet (production) or testnet (testing).
        chainName (str): chain name (main).
        script (str): script to execute.
        expiration (int): expiration timestamp.
        payload (str): payload message.

    Attributes:
        nexusName (str): mainnet (production) or testnet (testing).
        chainName (str): chain name (main).
        script (str): script to execute.
        expiration (int): expiration timestamp.
        payload (str): payload message.
        signatures (list): list of signatures, at least one is needed to broadcast tx.
    '''

    nexusName: str = None
    chainName: str = None
    script: str = None
    expiration: int = None
    payload: str = None
    hash: str = None

    signatures = []

    def __init__(
            self,
            nexusName: str,
            chainName: str,
            script: str,
            expiration: int,
            payload: str = 'PHANPY-1.0') -> None:

        if expiration is None:
            now = datetime.now()
            expiration = int(datetime.timestamp(now)) + 1000

        self.nexusName = nexusName
        self.chainName = chainName
        self.script = script
        self.expiration = expiration
        self.payload = payload
        self.signatures = []

    def sign(self, pk: int) -> None:
        '''Sign the transaction with HEX PK of the Sender's Address.

        Args:
            pk (int): HEX private key. Example: 0x411d7dabb39b455aadc49897e2fa13234585116d4f5eee198105f33f8f62d0b8

        Returns:
            None (The generated signature is added to the signatures list)
        '''
        signature = self.getSign(self.toString(False), pk)
        self.signatures.insert(0, signature)

    def toString(self, withSignature: bool) -> str:
        '''By using a ScriptBuilder object this method generates the needed string to broadcast the tx to
        the Phanstasma Blockchain.

        Args:
            withSignature (bool): flags that indicates if need to attach signatures or not to the end result.

        Returns:
            toString (str): Transaction object as string.
        '''

        num = self.expiration
        a = (num & 0xff000000) >> 24
        b = (num & 0x00ff0000) >> 16
        c = (num & 0x0000ff00) >> 8
        d = num & 0x000000ff

        expirationBytes = [d, c, b, a]

        sb = ScriptBuilder()
        sb.EmitVarString(self.nexusName)
        sb.EmitVarString(self.chainName)
        sb.EmitVarInt(int(len(self.script) / 2))
        sb.AppendHexEncoded(self.script)
        sb.EmitBytes(expirationBytes)
        sb.EmitVarString(self.payload)

        if (withSignature):
            sb.EmitVarInt(len(self.signatures))
            for s in self.signatures:
                sb.AppendByte(1)
                sig = s.decode("utf-8").upper()
                sb.EmitVarInt(int(len(sig) / 2))
                sb.AppendHexEncoded(sig)

        return sb.data

    def getSign(self, msgHex: str, pk: int) -> bytes:
        '''Method that given a message to sign & HEX private key returns the signature needed.

        Args:
           msgHex (str): Message to sign as Hex String.
           pk (int): HEX private key. Example: 0x411d7dabb39b455aadc49897e2fa13234585116d4f5eee198105f33f8f62d0b8

        Returns:
            getSign (bytes): Signature as bytes.
        '''
        hexBytes = binascii.unhexlify(msgHex)
        hexPk = int(pk)

        cv = Curve.get_curve('Ed25519')
        pv_key = ECPrivateKey(hexPk, cv)
        signer = EDDSA(hashlib.sha512)

        sig = signer.sign(hexBytes, pv_key)
        sig = binascii.hexlify(sig)

        return(sig)
    
    def to_byte_array(self, with_signature):
        writer = PBinaryWriter()
        writer.write_string(self.nexusName)
        writer.write_string(self.chainName)
        writer.append_hex_encoded(self.script)
        writer.write_date_time(self.expiration)
        writer.append_hex_encoded(self.payload)
        if with_signature:
            writer.write_var_int(len(self.signatures))
            for sig in self.signatures:
                writer.write_signature(sig)

        return writer.to_uint8_array()
    

    def get_hash(self):
        # Convert the transaction to a string representation (without the signature)
        transaction_str = self.toString(False)

        # Compute SHA256 hash of the string
        hash_obj = hashlib.sha256(transaction_str.encode())

        # Convert the hash to a hexadecimal string and reverse it
        self.hash = hash_obj.hexdigest()[::-1]

        return self.hash
    
    def to_string(self, with_signature):
        parts = []

        # Append the nexus name and chain name
        parts.append(self.nexus_name)
        parts.append(self.chain_name)

        # Append the script (length and hex encoded)
        parts.append(str(len(self.script) // 2))
        parts.append(self.script)

        # Convert the expiration date to a timestamp and append
        expiration_timestamp = int(self.expiration.timestamp())
        parts.append(str(expiration_timestamp))

        # Append the payload (length and hex encoded)
        parts.append(str(len(self.payload) // 2))
        parts.append(self.payload)

        if with_signature:
            # Append the number of signatures
            parts.append(str(len(self.signatures)))
            for sig in self.signatures:
                # You need to adapt this part based on the structure of your Signature object in Python
                parts.append(str(sig.kind))
                parts.append(str(len(sig.bytes) // 2))
                parts.append(binascii.hexlify(sig.bytes).decode())

        return ''.join(parts)
