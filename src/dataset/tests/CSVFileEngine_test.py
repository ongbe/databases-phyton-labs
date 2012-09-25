"""

"""

import unittest
from dataset.files.AutoResizeableFile import AutoResizeableFile
from dataset.csv.CSVFileEngine import CSVFileEngine

class CSVFileEngine_text(unittest.TestCase):
    def setUp(self):
        self._file = AutoResizeableFile()
        self._file.writeLine("T1;T02;T003")
        self._engine = CSVFileEngine(self._file)


    def tearDown(self):
        del self._file
        del self._engine


    def testEngineOperations(self):
        self.assertEqual(self._engine.columnCount(), 3, ".columnCount() return error")
        self.assertEqual(self._engine.rowCount(), 0, ".rowCount() return error")
        self.assertEqual(tuple(self._engine.titles()), ("T1", "T02", "T003"), ".titles() return error")
        self._engine.insertRow(0, ("a", "aaa", "aa"))
        self._engine.insertRow(1, ("bb", "aaa", "bbb"))
        self._engine.insertRow(0, ("ccc", "c", "bbb"))
        self._engine.insertRow(3, ("dddd", "eeeee", "aa"))
        self.assertEqual(self._engine.rowData(0), (0, "ccc", "c", "bbb"), ".rowData() return error")
        self.assertEqual(self._engine.rowData(1), (1, "a", "aaa", "aa"), ".rowData() return error")
        self.assertEqual(self._engine.rowData(2), (2, "bb", "aaa", "bbb"), ".rowData() return error")
        self.assertEqual(self._engine.rowData(3), (3, "dddd", "eeeee", "aa"), ".rowData() return error")
        self.assertEqual(self._engine.rowCount(), 4, ".rowCount() return error")
        self._engine.removeRow(1)
        self._engine.removeRow(2)
        self.assertEqual(self._engine.rowCount(), 2, ".rowCount() return error")
        self.assertEqual(self._engine.rowData(0), (0, "ccc", "c", "bbb"), ".rowData() return error")
        self.assertEqual(self._engine.rowData(1), (1, "bb", "aaa", "bbb"), ".rowData() return error")
        searchResult = self._engine.searchRows(2, "bbb")
        self.assertEqual(len(searchResult), 2, "Search result length error")
        self._engine.insertRow(0, ("a", "aaa", ""))
        self._engine.insertRow(1, ("bb", "aaa", "bbb"))
        self._engine.insertRow(2, ("ccc", "c", "bbb"))
        self._engine.insertRow(3, ("dddd", "eeeee", "aa"))
        self.assertEqual(self._engine.rowCount(), 6, ".rowCount() return error")
        self._engine.changeFieldData(0, 2, "CHANGED")
        self._engine.changeFieldData(2, 2, "0")
        self._engine.changeFieldData(5, 2, "GO")
        self._engine.changeFieldData(4, 0, "")
        self.assertEqual(self._engine.fieldData(0, 2), "CHANGED", ".fieldData() return error")
        self.assertEqual(self._engine.fieldData(2, 2), "0", ".fieldData() return error")
        self.assertEqual(self._engine.fieldData(5, 2), "GO", ".fieldData() return error")
        self.assertEqual(self._engine.fieldData(4, 0), "", ".fieldData() return error")
        searchResult = self._engine.searchRows(1, "aaa")
        self.assertEqual(len(searchResult), 3, "Search result length error")
        self._engine.insertRow(0, ("", "", ""))
        self._engine.changeFieldData(0, 0, "HI")
        self._engine.changeFieldData(0, 1, "HELLO")
        self._engine.changeFieldData(0, 2, "BYE")
        self.assertEqual(tuple(self._engine.rowData(0)), (0, "HI", "HELLO", "BYE"), ".rowData() return error")
        

if __name__ == "__main__":
    import sys;
    sys.argv = ["", "CSVFileEngine_text.testEngineOperations"]
    unittest.main()