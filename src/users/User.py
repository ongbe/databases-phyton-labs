"""

"""
from users.UserRights import UserRights
from PyQt4 import QtCore

class User(QtCore.QObject):
    """
    
    """
    def __init__(self, login, password, rights = UserRights()):
        """
        
        """
        QtCore.QObject.__init__(self)
        self.setLogin(login)
        self.setPassword(password)
        self.setRights(rights)
        
        
    def login(self):
        """
        
        """
        return self._login
    
    
    def password(self):
        """
        
        """
        return self._password
    
    
    def rights(self):
        """
        
        """
        return self._rights
    
    
    def setLogin(self, login):
        """
        
        """
        self._login = self._validateString(login)
        
        
    def setRights(self, rights):
        """
        
        """
        if not isinstance(rights, UserRights):
            raise TypeError("Value must have 'UserRights' type", {"raisingObject": self, "value": rights})
        self._rights = rights
        
        
    def setPassword(self, password):
        """
        
        """
        self._password = self._validateString(password)
        
        
    def _validateString(self, string):
        try:
            return str(string)
        except (TypeError, AttributeError, ValueError):
            raise TypeError("Value must be a string!", {"raisingObject": self, "value": string})