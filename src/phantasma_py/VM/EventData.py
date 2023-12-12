import struct
import base64

from .Decoder import Decoder

def decode_vm_object(str):
    dec = Decoder(str)
    return dec.read_vm_object()

def get_token_event_data(str):
    dec = Decoder(str)
    return {
        'symbol': dec.read_string(),
        'value': dec.read_bigint_accurate(),
        'chainName': dec.read_string()
    }

def get_chain_value_event_data(str):
    dec = Decoder(str)
    return {
        'name': dec.read_string(),
        'value': dec.read_bigint()
    }

def get_transaction_settle_event_data(str):
    dec = Decoder(str)
    return {
        'hash': dec.read_byte(),
        'platform': dec.read_string(),
        'chain': dec.read_string()
    }

def get_gas_event_data(str):
    dec = Decoder(str)
    return {
        'address': dec.read_byte(),
        'price': dec.read_bigint(),
        'amount': dec.read_bigint(),
        'endAmount': 0 if dec.is_end() else dec.read_bigint()
    }

def get_infusion_event_data(str):
    dec = Decoder(str)
    return {
        'baseSymbol': dec.read_string(),
        'TokenID': dec.read_bigint_accurate(),
        'InfusedSymbol': dec.read_string(),
        'InfusedValue': dec.read_bigint_accurate(),
        'ChainName': dec.read_string()
    }

def get_market_event_data(str):
    dec = Decoder(str)
    return {
        'baseSymbol': dec.read_string(),
        'quoteSymbol': dec.read_string(),
        'id': dec.read_bigint_accurate(),
        'amount': dec.read_bigint()
    }

def get_string(str):
    return Decoder(str).read_string()