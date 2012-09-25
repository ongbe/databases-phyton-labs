""""

"""

import unittest
from dataset.files.RangeShiftingInfo import RangeShiftingInfo


class RangeShiftingInfo_test(unittest.TestCase):
    def testInitAndGetters(self):
        info = RangeShiftingInfo((2, 5), 40)
        self.assertEqual(info.oldRange(), (2, 5), ".oldRange() return error")
        self.assertEqual(info.shiftingValue(), 40, ".shiftingValue() return error")


if __name__ == "__main__":
    import sys;
    sys.argv = ["", "RangesShiftingInfo_test.testInitAndGetters"]
    unittest.main()