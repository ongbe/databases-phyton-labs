"""

"""

import unittest
from unittest import TestCase
from dataset.files.AutoResizeableFile import AutoResizeableFile
from dataset.files.FilePackingListener import FilePackingListener


class AutoResizeableFile_test(TestCase, FilePackingListener):
    def setUp(self):
        self._file = None
        exception = Exception()
        raised = False
        try:
            self._file = AutoResizeableFile()
        except IOError, exc:
            exception = exc
            raised = True
        self.assertFalse(raised, exception.message)
        self.assertTrue(self._file.isOpened(), ".isOpened returned False")
        
        
    def tearDown(self):
        self._file.close()
        
        
    def testFileStringOperations(self):
        self.assertTrue(self._file.position() == 0, ".position() returned not-null value")
        self.assertTrue(self._file.write("Hello") == 5, ".write() returned not-5 value")
        self.assertTrue(self._file.position() == 5, ".position() returned not-5 value")
        self.assertTrue(self._file.size() == 5, ".size() returned not-5 value")
        self._file.setPosition(2)
        self._file.write("y, he")
        self.assertEqual("Hey, hello", self._file.readAll(), ".write('y, he', 0) error")
        self._file.setPosition(2)
        self._file.write("llo", 1)
        self.assertEquals("Hello, hello", self._file.readAll(), ".write('llo', 1) error")
        self.assertRaises(TypeError, self._file.setPosition, "hello")
        self._file.setPosition(self._file.size())
        
        
    def testPacking(self):
        self._file.addPackingListener(self) 
        self._file.write("Hello, my name is Andriy")
        self._file.write("I'm studying in KPI")
        self._file.removeRange(0, 24)
        self._file.pack()
        self.assertEqual(self._file.validRanges(), [(0, 19)], "Valid ranges error")
        self.assertEqual(self._file.readAll(), "I'm studying in KPI", ".readAll() error after packing")       
        
        
    def filePackedEvent(self, packingInfoList):
        pass
    

if __name__ == "__main__":
    import sys;
    sys.argv = ['', 'AutoResizeableFile_test.setUp']
    unittest.main()