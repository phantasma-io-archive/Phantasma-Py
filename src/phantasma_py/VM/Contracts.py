from enum import IntEnum

class Contracts(IntEnum):
    GasContractName = "gas"
    BlockContractName = "block"
    StakeContractName = "stake"
    SwapContractName = "swap"
    AccountContractName = "account"
    ConsensusContractName = "consensus"
    GovernanceContractName = "governance"
    StorageContractName = "storage"
    ValidatorContractName = "validator"
    InteropContractName = "interop"
    ExchangeContractName = "exchange"
    PrivacyContractName = "privacy"
    RelayContractName = "relay"
    RankingContractName = "ranking"