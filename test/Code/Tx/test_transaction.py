import unittest
from phantasma_py.Tx import Transaction  # Replace with your actual import path
import binascii

class TestTransaction(unittest.TestCase):

    def setUp(self):
        # Set up a transaction instance and other necessary variables for testing
        self.nexus_name = "testnet"
        self.chain_name = "main"
        self.script = "01020304"  # Example script in hex
        self.expiration = 1654123456  # Example timestamp
        self.payload = "PHANPY-1.0"
        self.transaction = Transaction(self.nexus_name, self.chain_name, self.script, self.expiration, self.payload)

    def test_sign(self):
        # Test the sign method
        pk = 0x411d7dabb39b455aadc49897e2fa13234585116d4f5eee198105f33f8f62d0b8
        self.transaction.sign(pk)
        self.assertGreater(len(self.transaction.signatures), 0, "Signing failed")

    def test_to_string(self):
        # Test the to_string method
        transaction_string = self.transaction.toString(False)
        self.assertIsInstance(transaction_string, str, "to_string method did not return a string")

    def test_get_hash(self):
        # Test the get_hash method
        transaction_hash = self.transaction.get_hash()
        self.assertEqual(len(transaction_hash), 64, "Hash length is incorrect")

    # Add more test methods for other Transaction methods

if __name__ == '__main__':
    unittest.main()
