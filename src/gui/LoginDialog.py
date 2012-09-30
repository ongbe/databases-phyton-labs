"""
    Module for log-in dialog
"""

from PyQt4 import QtGui, QtCore
from gui.interfaces.LoginDialogUI import Ui_loginDialog
from users.UsersList import UsersList
from users.User import User

class LoginDialog(QtGui.QDialog):
    """
        Log-in dialog class
    """
    def __init__(self, loginsFilePath):
        """
            Default constructor.
            'loginsFilePath' - path to the file with users data
        """
        QtGui.QDialog.__init__(self)
        self._ui = Ui_loginDialog()
        self._ui.setupUi(self)
        self._usersList = UsersList(loginsFilePath)
        QtCore.QObject.connect(self._ui.okButton, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
        QtCore.QObject.connect(self._ui.cancelButton, QtCore.SIGNAL("clicked()"), self.cancelButtonClicked)
        QtCore.QObject.connect(self, QtCore.SIGNAL("rejected()"), self.cancelButtonClicked)
        
    
    def okButtonClicked(self):
        """
            A slot for OK button "clicked()" signal
        """
        login = self._ui.loginEdit.text()
        password = self._ui.passwordEdit.text()
        user = self._usersList.get(login)
        if user == None or password != user.password():
            QtGui.QMessageBox.about(self, "Error...", "No such login-password pair was found!")
        else:
            self.hide()
            self.emit(QtCore.SIGNAL("userLoggedIn(QObject)"), user)
       
    
    def cancelButtonClicked(self):
        """
            A slot for CANCEL button "clicked()" signal
        """
        self.hide()
        self.emit(QtCore.SIGNAL("userLoggedIn(QObject)"), User("", ""))