"""
    Module for representing operation result class
"""

from PyQt4 import QtCore

class OperationResult(QtCore.QObject):
    """
        Represents result of operation
    """
    def __init__(self, isOk, data = None, message = "OK"):
        """
            Default constructor
            'isOk' - True, if operation succeed, False - otherwise
            'data' - any user-defined data
            'massage' - user-friendly text message
        """
        QtCore.QObject.__init__(self)
        self._isOk = isOk
        self._message = message
        self._data = data
        
        
    def isOk(self):
        """
            Returns operation success status
        """
        return self._isOk
    
    
    def message(self):
        """
            Returns user-friendly message
        """
        return self._message
    
    
    def data(self):
        """
            Returns user-defined data
        """
        return self._data
    
    
    def setOk(self, isOk = True):
        """
            Sets operation success status. Returns None
        """
        self._isOk = isOk
        
        
    def setMessage(self, message):
        """
             Sets user-friendly message. Returns None
        """
        self._message = message
        
        
    def setData(self, data):
        """
            Sets user-defined data. Returns None
        """
        self._data = data