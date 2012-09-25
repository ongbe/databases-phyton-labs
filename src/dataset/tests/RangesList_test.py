"""

"""
import unittest
from dataset.files.RangesList import RangesList


class RangesList_test(unittest.TestCase):
    def setUp(self):
        self._list = RangesList(0, 0)
        
        
    def tearDown(self):
        self._list.clear()


    def testUnion(self):
        self._list.add(1, 4)
        self._list.add(2, 5)
        self._list.add(0, 2)
        self._list.add(5, 7)
        self.assertEqual(self._list.size(), 1, ".size() error")
        self.assertEqual(self._list.ranges(), [(0, 7)], "Ranges union result error")
        self._list.add(8, 12)
        self._list.add(14, 16)
        self._list.add(15, 17)
        self._list.add(19, 24)
        self.assertEqual(self._list.size(), 4, ".size() error")
        self.assertEqual(self._list.ranges(), [(0, 7), (8, 12), (14, 17), (19, 24)], "Ranges union result error")
    
    def testSpliting(self):
        self._list.add(0, 7)
        self._list.add(8, 12)
        self._list.add(14, 17)
        self._list.add(19, 24)
        self._list.remove(2, 5)
        self._list.remove(6, 13)
        self._list.remove(14, 24)
        self.assertEqual(self._list.size(), 2, ".size() error")
        self.assertEquals(self._list.ranges(), [(0, 2), (5, 6)], "Ranges splitting result error")


if __name__ == "__main__":
    import sys;
    sys.argv = ["", "RangesList_test.setUp"]
    unittest.main()