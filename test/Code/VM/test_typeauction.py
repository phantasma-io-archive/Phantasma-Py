import unittest
from phantasma_py.VM import TypeAuction  # Replace 'your_module' with the name of the module where Opcode is defined

class TestTypeAuctionEnum(unittest.TestCase):

    def test_typeauction_values(self):
        expected_opcodes = {
            "Fixed": 0,
            "Classic": 1,
            "Reserve": 2,
            "Dutch": 3,
        }

        for opcode_name, opcode_value in expected_opcodes.items():
            with self.subTest(opcode_name=opcode_name):
                self.assertTrue(hasattr(TypeAuction, opcode_name))
                self.assertEqual(getattr(TypeAuction, opcode_name), opcode_value)

if __name__ == '__main__':
    unittest.main()