"""

"""
from PyQt4 import QtCore

class UserRights(QtCore.QObject):
    """
    
    """
    def __init__(self, fieldsModifyingPermited = False, rowsAddingPermited = False, rowsRemovingPermited = False):
        QtCore.QObject.__init__(self)
        self.setFieldsModifyingPermited(fieldsModifyingPermited)
        self.setRowsAddingPermited(rowsAddingPermited)
        self.setRowsRemovingPermition(rowsRemovingPermited)
        
    
    def rowsRemovingPermited(self):
        """
        
        """
        return self._rowsRemovingPermited
    
    
    def rowsAddingPermited(self):
        """
        
        """
        return self._rowsAddingPermited
    
    
    def fieldsModifyingPermited(self):
        """
        
        """
        return self._fieldsModifyingPermited
    
    
    def setRowsRemovingPermition(self, permited):
        """
        
        """
        self._rowsRemovingPermited = bool(permited)
        
        
    def setRowsAddingPermited(self, permited):
        """
        
        """
        self._rowsAddingPermited = bool(permited)
        
        
    def setFieldsModifyingPermited(self, permited):
        """
        
        """
        self._fieldsModifyingPermited = bool(permited)
        
        
    