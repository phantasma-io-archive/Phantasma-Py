import unittest
from phantasma_py.Types import Address, AddressKind, PhantasmaKeys  # Replace 'your_module' with the actual module name

class TestAddress(unittest.TestCase):

    def setUp(self):
        self.key = PhantasmaKeys.generate()  # Sample PhantasmaKeys instance for testing
        self.sample_public_key = self.key.Address._bytes  # Sample public key for testing
        self.sample_text = self.key.Address.Text  # Sample text for testing

    def test_init_valid_length(self):
        address = Address(self.sample_public_key)
        self.assertEqual(len(address._bytes), Address.LengthInBytes)

    def test_init_invalid_length(self):
        with self.assertRaises(ValueError):
            Address(b'\x01' * (Address.LengthInBytes - 1))

    def test_from_key(self):
        # Add your specific logic for testing FromKey method
        pass

    def test_from_public_key(self):
        address = Address.FromPublicKey(self.sample_public_key)
        self.assertIsInstance(address, Address)

    def test_from_text_valid(self):
        address = Address.FromText(self.key.Address.Text)
        self.assertIsInstance(address, Address)
        assert address.Text == self.key.Address.Text

    def test_from_text_invalid(self):
        with self.assertRaises(ValueError):
            Address.FromText("InvalidText")

    def test_parse_valid(self):
        address = Address.Parse(self.sample_text)
        self.assertIsInstance(address, Address)

    def test_parse_invalid(self):
        with self.assertRaises(ValueError):
            Address.Parse("InvalidText")

    def test_is_valid_address(self):
        self.assertTrue(Address.IsValidAddress(self.sample_text))
        self.assertFalse(Address.IsValidAddress("InvalidText"))

    # Add more tests for other methods like compareTo, equals, serialize_data, unserialize_data, etc.

if __name__ == '__main__':
    unittest.main()
