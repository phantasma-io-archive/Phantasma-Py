import sys

sys.path.append('../../Bindings')
from Phantasma import PhantasmaAPI

try:
    api = PhantasmaAPI("http://localhost:7077/rpc")
    response = api.getAccount("P2f7ZFuj6NfZ76ymNMnG3xRBT5hAMicDrQRHE4S7SoxEr")

    if 'balances' in response:
        print("Wallet Balances:")
        for bal in response['balances']:
            tokenSymbol = bal['symbol']
            tokenAmount = int(bal['amount']) / pow(10, int(bal['decimals']))

            print(tokenSymbol, tokenAmount)

except Exception as ex:
    print("error", ex)
