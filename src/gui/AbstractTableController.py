"""
    Contains a class for unified table data controllers
"""

from PyQt4 import QtCore

class AbstractTableController(QtCore.QObject):
    """
        An abstract class for unified table data controllers
    """
    def __init__(self):
        """
            Default constructor. Must be invoked in derived classes
        """
        QtCore.QObject.__init__(self)
        
        
    def userLoggedIn(self, user):
        """
            Called when user had logged in. Returns None
            'user' - User object reference
        """
        pass
    
    
    def openTable(self, tablePath):
        """
            Called when a table must be loaded (in any way). Returns
        OperationResult object with 'data' field refered to QAbstractTableModel
            'tablePath' - implementation depended value for table identifying
        """
        pass
        
        
    def insertRow(self, rowIndex):
        """
            Called for new row insertion. Returns OperationResult object
        'rowIndex' - zero-based row index
        """
        pass
        
        
    def removeRow(self, rowIndex):
        """
            Called for row removing. Returns OperationResult object
            'rowIndex' - zero-based row index
        """
        pass
    
    
    def searchRows(self, keyColumn, key):
        """
            Called for searching rows that have the same string value in 
        'keyColumn' as 'key'. Returns OperationResult object with 'data' field 
        refered to CSVTableModel object, representing search results.
            'keyColumn' - zero-based column index
            'key' - string-convertable object to search
        """
        pass
    
    
    def modifyField(self, row, column, data):
        """
            Called for changing specified field data. Returns
        OperationResult object
            'row' - zero-based row index
            'column' - zero-based column index
            'data' - string-convertable object
        """
        pass
    
    
    def start(self, loginFilePath):
        """
            Called for starting controller work. Returns None
        """
        pass
    
    
    def model(self):
        """
            Returns an QAbstractTableModel associated with controller 
        """
        pass
    
    
    def save(self):
        """
            Called for saving model. Returns OperationResult object
        """
        pass
    
    
    def close(self):
        """
            Called for closing model. Returns OperationResult object
        """
        pass