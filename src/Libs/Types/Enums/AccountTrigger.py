from enum import Enum


class AccountTrigger(Enum):
    OnMint = 0
    OnBurn = 1
    OnSend = 2
    OnReceive = 3
    OnWitness = 4
    OnUpgrade = 5
    OnMigrate = 6
    OnKill = 7