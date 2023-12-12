import unittest
from phantasma_py.VM import EventKind  # Replace 'your_module' with the name of the module where EventKind is defined

class TestEventKindEnum(unittest.TestCase):

    def test_enum_members(self):
        expected_events = {
            "Unknown": 0,
            "ChainCreate": 1,
            "TokenCreate": 2,
            "TokenSend": 3,
            "TokenReceive": 4,
            "TokenMint": 5,
            "TokenBurn": 6,
            "TokenStake": 7,
            "TokenClaim": 8,
            "AddressRegister": 9,
            "AddressLink": 10,
            "AddressUnlink": 11,
            "OrganizationCreate": 12,
            "OrganizationAdd": 13,
            "OrganizationRemove": 14,
            "GasEscrow": 15,
            "GasPayment": 16,
            "AddressUnregister": 17,
            "OrderCreated": 18,
            "OrderCancelled": 19,
            "OrderFilled": 20,
            "OrderClosed": 21,
            "FeedCreate": 22,
            "FeedUpdate": 23,
            "FileCreate": 24,
            "FileDelete": 25,
            "ValidatorPropose": 26,
            "ValidatorElect": 27,
            "ValidatorRemove": 28,
            "ValidatorSwitch": 29,
            "PackedNFT": 30,
            "ValueCreate": 31,
            "ValueUpdate": 32,
            "PollCreated": 33,
            "PollClosed": 34,
            "PollVote": 35,
            "ChannelCreate": 36,
            "ChannelRefill": 37,
            "ChannelSettle": 38,
            "LeaderboardCreate": 39,
            "LeaderboardInsert": 40,
            "LeaderboardReset": 41,
            "PlatformCreate": 42,
            "ChainSwap": 43,
            "ContractRegister": 44,
            "ContractDeploy": 45,
            "AddressMigration": 46,
            "ContractUpgrade": 47,
            "Log": 48,
            "Inflation": 49,
            "OrderBid": 59,
            "MasterClaim": 61,
            "Custom": 64
        }
        
        for event_name, event_value in expected_events.items():
            with self.subTest(event_name=event_name):
                self.assertTrue(hasattr(EventKind, event_name))
                self.assertEqual(getattr(EventKind, event_name).value, event_value)

if __name__ == '__main__':
    unittest.main()
