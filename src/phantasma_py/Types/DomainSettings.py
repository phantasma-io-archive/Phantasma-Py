
class StakeReward:
    def __init__(self, staker, date):
        self.staker = staker
        self.date = date

class DomainSettings:
    LatestKnownProtocol = 18
    Phantasma20Protocol = 7
    Phantasma30Protocol = 8
    MaxTxPerBlock = 1024
    MaxOracleEntriesPerBlock = 5120
    MaxEventsPerBlock = 2048
    MaxEventsPerTx = 8096
    MaxTriggerLoop = 5
    MAX_TOKEN_DECIMALS = 18
    DefaultMinimumGasFee = 100000
    InitialValidatorCount = 4
    FuelTokenSymbol = 'KCAL'
    FuelTokenName = 'Phantasma Energy'
    FuelTokenDecimals = 10
    NexusMainnet = 'mainnet'
    NexusTestnet = 'testnet'
    StakingTokenSymbol = 'SOUL'
    StakingTokenName = 'Phantasma Stake'
    StakingTokenDecimals = 8
    FiatTokenSymbol = 'USD'
    FiatTokenName = 'Dollars'
    FiatTokenDecimals = 8
    RewardTokenSymbol = 'CROWN'
    RewardTokenName = 'Phantasma Crown'
    LiquidityTokenSymbol = 'LP'
    LiquidityTokenName = 'Phantasma Liquidity'
    LiquidityTokenDecimals = 8
    FuelPerContractDeployTag = 'nexus.contract.cost'
    FuelPerTokenDeployTag = 'nexus.token.cost'
    FuelPerOrganizationDeployTag = 'nexus.organization.cost'
    SystemTokens = [
        FuelTokenSymbol,
        StakingTokenSymbol,
        FiatTokenSymbol,
        RewardTokenSymbol,
        LiquidityTokenSymbol,
    ]
    RootChainName = 'main'
    ValidatorsOrganizationName = 'validators'
    MastersOrganizationName = 'masters'
    StakersOrganizationName = 'stakers'
    PhantomForceOrganizationName = 'phantom_force'
    PlatformName = 'phantasma'
    ArchiveMinSize = 64
    ArchiveMaxSize = 104857600
    InfusionName = 'infusion'
    NameMaxLength = 255
    UrlMaxLength = 2048
    ArgsMax = 64
    AddressMaxSize = 34
    ScriptMaxSize = 32767
