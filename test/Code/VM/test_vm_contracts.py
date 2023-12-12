import unittest
from phantasma_py.VM import Contracts

class TestContractsEnum(unittest.TestCase):

    def test_enum_members(self):
        expected_contracts = {
            "GasContractName": "gas",
            "BlockContractName": "block",
            "StakeContractName": "stake",
            "SwapContractName": "swap",
            "AccountContractName": "account",
            "ConsensusContractName": "consensus",
            "GovernanceContractName": "governance",
            "StorageContractName": "storage",
            "ValidatorContractName": "validator",
            "InteropContractName": "interop",
            "ExchangeContractName": "exchange",
            "PrivacyContractName": "privacy",
            "RelayContractName": "relay",
            "RankingContractName": "ranking"
        }

        for contract_name, contract_value in expected_contracts.items():
            with self.subTest(contract_name=contract_name):
                self.assertTrue(hasattr(Contracts, contract_name))
                self.assertEqual(getattr(Contracts, contract_name).value, contract_value)

if __name__ == '__main__':
    unittest.main()