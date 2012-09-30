"""
    Module for users list storing class 
"""
from dataset.files.AutoResizeableFile import AutoResizeableFile
from users.UserRights import UserRights
from users.User import User
from PyQt4 import QtCore


class UsersList(QtCore.QObject):
    """
        Users list storing class 
    """
    def __init__(self, filePath):
        """
            Default constructor.
            'filePath' - path to the file with users authentification data
            File format:
        <login1>-<password1>: [add][,remove][,modify]
        <login2>-<password2>: [add][,remove][,modify]
            ................................
        <loginN>-<passwordN>: [add][,remove][,modify]
            Empty passwords are valid, empty logins - invalid
        """
        QtCore.QObject.__init__(self)
        try:
            with open(filePath) as testingObject:
                pass
        except IOError, exception:
            exception.message = "Users file doesn't exist"
            raise exception
        usersFile = AutoResizeableFile(filePath)
        self._users = []
        while not usersFile.endOfFile():
            string = usersFile.readLine()
            if len(string) == 0:
                continue
            invalidFormatError = ValueError("Invalid file format!", {"raisingObject": self, "filePath": filePath, "string": string})
            parts = string.split(":")
            if len(parts) != 2:
                raise invalidFormatError
            loginPassword, rightsString = parts
            parts = loginPassword.split("-")
            if len(parts) != 2:
                raise invalidFormatError
            login, password = parts
            rights = UserRights()
            for right in rightsString.split(","):
                right = right.strip()
                if right == "add":
                    rights.setRowsAddingPermited(True)
                elif right == "remove":
                    rights.setRowsRemovingPermition(True)
                elif right == "modify":
                    rights.setFieldsModifyingPermited(True)
            self._users.append(User(login.strip(), password.strip(), rights))
            
            
    def get(self, login):
        """
            Returns User object reference with specified login
        or None if such user was not found.
            'login' - user login
        """
        for user in self._users:
            if user.login() == login:
                return user
        return None
                    
            