import unittest

from phantasma_py.VM import VMObject, VMType


class TestVMObject(unittest.TestCase):
    def test_string(self):
        myTestString = "MyString"
        vmObject = VMObject.FromObject(myTestString)
        result = vmObject.AsString()
        self.assertEqual(myTestString, result)
        #self.assertEqual(True, False)  # add assertion here

    def test_number(self):
        myTestNumber = 100
        vmObject = VMObject.FromObject(myTestNumber)
        result = vmObject.AsNumber()
        self.assertEqual(myTestNumber, result)
        #self.assertEqual(True, False)  # add assertion here

    def test_boolean(self):
        myTestBool = True
        vmObject = VMObject.FromObject(myTestBool)
        result = vmObject.AsBool()
        self.assertEqual(myTestBool, result)

    def test_array(self):
        myTestArray = ["myTestBool", "myTestString"]
        vmObject = VMObject.FromArray(myTestArray)
        #result = vmObject.AsArray(VMType.String)
        #self.assertEqual(myTestArray, result)

if __name__ == '__main__':
    unittest.main()
