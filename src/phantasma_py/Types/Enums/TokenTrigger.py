from enum import Enum


class TokenTrigger(Enum):
    OnMint = 0
    OnBurn = 1
    OnSend = 2
    OnReceive = 3
    OnInfuse = 4
    OnUpgrade = 5
    OnSeries = 6
    OnWrite = 7
    OnMigrate = 8
    OnKill = 9