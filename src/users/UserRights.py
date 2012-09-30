"""
    Module for user rights class
"""
from PyQt4 import QtCore

class UserRights(QtCore.QObject):
    """
        User rights class
    """
    def __init__(self, fieldsModifyingPermited = False, rowsAddingPermited = False, rowsRemovingPermited = False):
        """
            Default constructor
            'fieldsModifyingPermited' - True, if changing fields is permited
            'rowsAddingPermited' - True, if new rows adding is permited
            'rowsRemovingPermited' - True, if rows removing is permited
        """
        QtCore.QObject.__init__(self)
        self.setFieldsModifyingPermited(fieldsModifyingPermited)
        self.setRowsAddingPermited(rowsAddingPermited)
        self.setRowsRemovingPermition(rowsRemovingPermited)
        
    
    def rowsRemovingPermited(self):
        """
            Returns changing fields permition status
        """
        return self._rowsRemovingPermited
    
    
    def rowsAddingPermited(self):
        """
            Returns rows adding permition status
        """
        return self._rowsAddingPermited
    
    
    def fieldsModifyingPermited(self):
        """
            Returns rows removing permition status
        """
        return self._fieldsModifyingPermited
    
    
    def setRowsRemovingPermition(self, permited):
        """
            Sets rows removing permition status. Returns None
            'permited' - new rows removing permition status
        """
        self._rowsRemovingPermited = bool(permited)
        
        
    def setRowsAddingPermited(self, permited):
        """
            Sets adding rows permition status. Returns None
            'permited' - new rows permition status
        """
        self._rowsAddingPermited = bool(permited)
        
        
    def setFieldsModifyingPermited(self, permited):
        """
            Sets fields changing permition status. Returns None
            'permited' - new fields changing permition
        """
        self._fieldsModifyingPermited = bool(permited)
        
        
    