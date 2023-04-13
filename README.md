# Phantasma Py

## Python SimpleWallet Sample app

This is a simple wallet sample that needs to be connected to a RPC node. By default it uses the localhost:7077/rpc endpoint, but you can switch to your own URL.

To run the sample app, follow these steps:

1. Install "requests" module (Run "pip install requests" on command line inside app folder)

2. Run the sample app!

## Python VM Samples

The VM Module implements the following classes EventDecoder, ScriptBuilder and Transaction in order to provide support to:

- Decode TX events data.
  Examples:
  /Python/Samples/VMSamples/parsetxevents.py

- Create Scripts, Transactions and Sign them using HEX Private Key.
  Examples:
  /Python/Samples/VMSamples/transferFungible.py
  /Python/Samples/VMSamples/transferNonFungible.py
