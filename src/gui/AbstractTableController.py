"""

"""

from PyQt4 import QtCore

class AbstractTableController(QtCore.QObject):
    """
    
    """
    def __init__(self):
        """
        
        """
        QtCore.QObject.__init__(self)
        
        
    def userLoggedIn(self, user):
        """
        
        """
        pass
    
    
    def openTable(self, tablePath):
        """
        
        """
        pass
        
        
    def insertRow(self, rowIndex):
        """
        
        """
        pass
        
        
    def removeRowAction(self, rowIndex):
        """
        
        """
        pass
    
    
    def searchRows(self, keyColumn, key):
        """
        
        """
        pass
    
    
    def modifyField(self, row, column, data):
        """
        
        """
        pass
    
    
    def start(self, loginFilePath):
        """
        
        """
        pass
    
    
    def model(self):
        """
        
        """
        pass
    
    
    def save(self):
        """
        
        """
        pass
    
    
    def close(self):
        """
        
        """
        pass