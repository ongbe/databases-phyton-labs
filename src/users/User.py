"""
    Module for User class
"""
from users.UserRights import UserRights
from PyQt4 import QtCore

class User(QtCore.QObject):
    """
        User representing class
    """
    def __init__(self, login, password, rights = UserRights()):
        """
            Default constructor.
            'login' - user login
            'password' - user password
            'rights' - UserRight object reference
        """
        QtCore.QObject.__init__(self)
        self.setLogin(login)
        self.setPassword(password)
        self.setRights(rights)
        
        
    def login(self):
        """
            Returns users's login
        """
        return self._login
    
    
    def password(self):
        """
            Returns users's password
        """
        return self._password
    
    
    def rights(self):
        """
            Returns users's rights (UserRights object reference)
        """
        return self._rights
    
    
    def setLogin(self, login):
        """
            Sets users's login. Returns None
            'login' - new user's login
        """
        self._login = self._validateString(login)
        
        
    def setRights(self, rights):
        """
            Sets users's rights. Returns None
            'rights' - new user's rights (UserRights object reference)
        """
        if not isinstance(rights, UserRights):
            raise TypeError("Value must have 'UserRights' type", {"raisingObject": self, "value": rights})
        self._rights = rights
        
        
    def setPassword(self, password):
        """
            Sets users's password. Returns None
            'password' - new user's password
        """
        self._password = self._validateString(password)
        
        
    def _validateString(self, string):
        try:
            return str(string)
        except (TypeError, AttributeError, ValueError):
            raise TypeError("Value must be a string!", {"raisingObject": self, "value": string})