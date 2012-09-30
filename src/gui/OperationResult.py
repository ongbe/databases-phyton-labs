"""

"""

from PyQt4 import QtCore

class OperationResult(QtCore.QObject):
    """
    
    """
    def __init__(self, isOk, data = None, message = "OK"):
        """
        
        """
        QtCore.QObject.__init__(self)
        self._isOk = isOk
        self._message = message
        self._data = data
        
        
    def isOk(self):
        """
        
        """
        return self._isOk
    
    
    def message(self):
        """
        
        """
        return self._message
    
    
    def data(self):
        """
        
        """
        return self._data
    
    
    def setOk(self, isOk = True):
        """
        
        """
        self._isOk = isOk
        
        
    def setMessage(self, message):
        """
        
        """
        self._message = message
        
        
    def setData(self, data):
        """
        
        """
        self._data = data