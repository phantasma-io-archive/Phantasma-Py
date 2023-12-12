import unittest
from phantasma_py.VM import Opcode  # Replace 'your_module' with the name of the module where Opcode is defined

class TestOpcodeEnum(unittest.TestCase):

    def test_opcode_values(self):
        expected_opcodes = {
            "NOP": 0,
            "MOVE": 1,
            "COPY": 2,
            # ... (list all other opcodes here)
            "DEBUG": 52,
            "SUBSTR": 53
        }

        for opcode_name, opcode_value in expected_opcodes.items():
            with self.subTest(opcode_name=opcode_name):
                self.assertTrue(hasattr(Opcode, opcode_name))
                self.assertEqual(getattr(Opcode, opcode_name), opcode_value)

if __name__ == '__main__':
    unittest.main()