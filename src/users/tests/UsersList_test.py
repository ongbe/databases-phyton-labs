"""

"""

import unittest
from dataset.files.AutoResizeableFile import AutoResizeableFile
from users.UsersList import UsersList


class UsersList_test(unittest.TestCase):
    def setUp(self):
        self._file = AutoResizeableFile()
        self._file.writeLine("staand-081194:add, remove, modify")
        self._file.writeLine("chess_master-chess:add, modify")
        self._file.writeLine("stamax-314159:")
        self._file.writeLine("dsz-dsz:remove")
        self._file.flush()
        
        
    def tearDown(self):
        self._file.close()


    def testParsing(self):
        users = UsersList(self._file.path())
        staand = users.get("staand")
        stamax = users.get("stamax")
        chess_master = users.get("chess_master")
        dsz = users.get("dsz")
        none = users.get("any_other")
        self.assertNotEqual(staand, None, "'staand' user is 'None'")
        self.assertNotEqual(stamax, None, "'stamax' user is 'None'")
        self.assertNotEqual(chess_master, None, "'chess_master' user is 'None'")
        self.assertNotEqual(dsz, None, "'dsz' user is 'None'")
        self.assertEqual(none, None, "'none' user is NOT 'None'")
        self.assertTrue(staand.login() == "staand" and staand.password() == "081194", "'staand' attributes error")
        self.assertTrue(chess_master.login() == "chess_master" and chess_master.password() == "chess", "'chess_master' attributes error")
        self.assertTrue(stamax.login() == "stamax" and stamax.password() == "314159", "'stamax' attributes error")
        self.assertTrue(dsz.login() == "dsz" and dsz.password() == "dsz", "'dsz' attributes error")
        rights = staand.rights()
        self.assertTrue(rights.fieldsModifyingPermited() and rights.rowsAddingPermited() and rights.rowsRemovingPermited(), 
                        "'staand' rights error")
        rights = stamax.rights()
        self.assertFalse(rights.fieldsModifyingPermited() or rights.rowsAddingPermited() or rights.rowsRemovingPermited(), 
                        "'stamax' rights error")
        rights = chess_master.rights()
        self.assertTrue(rights.fieldsModifyingPermited() and rights.rowsAddingPermited() and not rights.rowsRemovingPermited(), 
                        "'chess_master' rights error")
        rights = dsz.rights()
        self.assertTrue(not rights.fieldsModifyingPermited() and not rights.rowsAddingPermited() and rights.rowsRemovingPermited(), 
                        "'dsz' rights error")


if __name__ == "__main__":
    import sys;
    sys.argv = ['', 'UsersList_test.testParsing']
    unittest.main()