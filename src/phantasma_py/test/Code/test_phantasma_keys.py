# coding: utf-8
import sys
import os
import unittest

#sys.path.append('../../../../')

from Types import Address
from Types import PhantasmaKeys


class TestPhantasmaKeys(unittest.TestCase):

    def testPhantasmaKeys(self):
        keys = PhantasmaKeys.from_wif("KxMn2TgXukYaNXx7tEdjh7qB2YaMgeuKy47j4rvKigHhBuZWeP3r")
        assert keys.to_wif() == "KxMn2TgXukYaNXx7tEdjh7qB2YaMgeuKy47j4rvKigHhBuZWeP3r"
        assert keys.Address.Text == "P2K9zmyFDNGN6n6hHiTUAz6jqn29s5G1SWLiXwCVQcpHcQb"

        keys = PhantasmaKeys.from_wif("L2sTuSzangXQCFxXFXJqfPAKJsstKvQdkGqP9J2VFkFRbEjd1Ez6")
        assert keys.to_wif() == "L2sTuSzangXQCFxXFXJqfPAKJsstKvQdkGqP9J2VFkFRbEjd1Ez6"
        assert keys.Address.Text == "P2K65RZhfxZhQcXKGgSPZL6c6hkygXipNxdeuW5FU531Bqc"
        pass


if __name__ == '__main__':
    unittest.main()
