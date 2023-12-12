import unittest

from phantasma_py.Types import PhantasmaKeys, Address
from phantasma_py.VM import ScriptBuilder

class TestScriptBuilder(unittest.TestCase):
    def test_scriptbuilder_callcontract(self):
        myScriptShouldBe = "0D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D0004055374616B6503000D0004057374616B652D00012E010B"
        keys = PhantasmaKeys.from_wif("L5UEVHBjujaR1721aZM5Zm5ayjDyamMZS9W35RE9Y9giRkdf3dVx")
        testSB = ScriptBuilder()
        testSB.CallContract("stake", "Stake", [keys.Address.Text, keys.Address.Text])
        script = testSB.EndScript()
        self.assertEqual(script, myScriptShouldBe)  # add assertion here

    def test_scriptbuilder_callcontract_complex(self):
        myScriptShouldBe = "0D000302085203000D000302102703000D0004044E554C4C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D000408416C6C6F7747617303000D0004036761732D00012E010D000408313030303030303003000D000404534F554C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D00041652756E74696D652E5472616E73666572546F6B656E7307000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D0004085370656E6447617303000D0004036761732D00012E010B"
        keys = PhantasmaKeys.from_wif("L5UEVHBjujaR1721aZM5Zm5ayjDyamMZS9W35RE9Y9giRkdf3dVx")
        amount = 10000000
        testSB = ScriptBuilder()
        testSB = testSB.AllowGas(keys.Address.Text, Address.NullText, 10000, 21000)
        testSB = testSB.CallInterop("Runtime.TransferTokens", [keys.Address.Text, keys.Address.Text, "SOUL", str(amount) ])
        testSB = testSB.SpendGas(keys.Address.Text)
        script = testSB.EndScript()
        self.assertEqual(myScriptShouldBe, script )  # add assertion here´
        self.assertEqual(len(myScriptShouldBe), len(script) )  # add assertion here´

    def test_scriptbuilder_callinterop(self):
        myScriptShouldBe = "0D000408313030303030303003000D000404534F554C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D00042F50324B464579466576705166536157384734566A536D6857555A585234517247395951523148624D7054554370434C03000D00041652756E74696D652E5472616E73666572546F6B656E7307000B"
        keys = PhantasmaKeys.from_wif("L5UEVHBjujaR1721aZM5Zm5ayjDyamMZS9W35RE9Y9giRkdf3dVx")
        amount = 10000000
        testSB = ScriptBuilder()
        testSB.CallInterop("Runtime.TransferTokens", [keys.Address.Text, keys.Address.Text, "SOUL", str(amount)])
        script = testSB.EndScript()
        self.assertEqual(myScriptShouldBe, script)
        self.assertEqual(len(myScriptShouldBe), len(script))  # add assertion here´



if __name__ == '__main__':
    unittest.main()
