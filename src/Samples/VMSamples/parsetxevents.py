import json
import requests
import sys

sys.path.append('../../Libs')
from VM import EventDecoder

sys.path.append('../../Bindings')
from Phantasma import PhantasmaAPI

def parseEventTx(txhash):
    #PRODUCTION RPC URL
    PHAN_API_URL = "http://207.148.17.86:7077/rpc"

    api = PhantasmaAPI(PHAN_API_URL)
    tx = api.getTransaction(txhash)

    #print("RAW TX DATA", tx)
    if 'result' in tx:
        for event in tx['events']:
            if "Gas" not in event["kind"]:

                print("EVENT:", event["contract"], event["kind"], event["data"])

                dec = EventDecoder(event["data"])
                tokensymbol = dec.readString()
                nft_id_or_tokenamount = dec.readBigIntAccurate()
                chain = dec.readString()

                print("DECODED DATA:", tokensymbol, nft_id_or_tokenamount, chain, "\n")


if __name__ == '__main__':

    # EXAMPLE TX WITH FT
    print("############## FT TX ############## ")
    parseEventTx(
        "2C55319B7B8A57B31CA41EA8517E5A970A6C20885ED2B85053137B8393BB03AA")
    print("############## FT TX ############## ")

    # EXAMPLE TX WITH NFT
    print("############## FT TX ############## ")
    parseEventTx(
        "9DA4489D589E4B8FA3AB46FBA25ED0086EF4808DC4EC8C888FC3B4D3715BAE07")
    print("############## FT TX ############## ")
