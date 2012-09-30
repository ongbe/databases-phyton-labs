"""

"""

import sys
from PyQt4 import QtCore, QtGui
from gui.AbstractTableController import AbstractTableController
from gui.MainWindow import MainWindow
from gui.LoginDialog import LoginDialog
from gui.OperationResult import OperationResult
from dataset.csv.CSVTableModel import CSVTableModel
from users.UserRights import UserRights

class CSVTableController(AbstractTableController):
    """
    
    """
    def __init__(self):
        """
        
        """
        AbstractTableController.__init__(self)
        self._user = None
        self._userRights = UserRights()
        self._model = None
        self._application = None
        self._mainWindow = None
        
        
    def start(self, loginFilePath):
        """
        
        """
        self._application = QtGui.QApplication(sys.argv)
        self._mainWindow = MainWindow(self)
        self._mainWindow.setVisible(False)
        loginDialog = LoginDialog(loginFilePath)
        QtCore.QObject.connect(loginDialog, QtCore.SIGNAL("userLoggedIn(QObject)"), self.userLoggedIn)
        loginDialog.setModal(True)
        loginDialog.show()
        sys.exit(self._application.exec_())
        
        
    def userLoggedIn(self, user):
        """
        
        """
        if user == None or (user.login() == "" and user.password() == ""):
            self._application.exit()
            return
        self._user = user
        self._userRights = user.rights()
        self._mainWindow.setVisible(True)       
    
    
    def openTable(self, tablePath):
        """
        
        """
        try:
            with open(tablePath) as testingObject:
                pass
        except IOError, exception:
            return OperationResult(False, None, "File error: " + exception.message)
        try:
            self._model = CSVTableModel(tablePath)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True, self._model)
        
        
    def insertRow(self, rowIndex):
        """
        
        """
        if self._user == None or not self._userRights.rowsAddingPermited():
            return OperationResult(False, None, "Rights error: not permited!")
        try:
            self._model.insertRow(rowIndex)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True)
                
        
    def removeRowAction(self, rowIndex):
        """
        
        """
        if self._user == None or not self._userRights.rowsRemovingPermited():
            return OperationResult(False, None, "Rights error: not permited!")
        try:
            self._model.removeRowAction(rowIndex)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True)
    
    
    def searchRows(self, keyColumn, key):
        """
        
        """
        try:
            return OperationResult(True, self._model.search(keyColumn, key))
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
            
    
    def modifyField(self, row, column, data):
        """
        
        """
        if self._user == None or not self._userRights.fieldsModifyingPermited():
            return OperationResult(False, None, "Rights error: not permited!")
        try:
            self._model.setData(self._model.createIndex(row, column), data)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True)
    
    
    def model(self):
        """
        
        """
        return self._model
    
    
    def save(self):
        """
        
        """
        self._model.save()
        return OperationResult(True)
        
        
    def close(self):
        """
        
        """
        self._model = None
        return OperationResult(True)
    
    
c = CSVTableController()
c.start("login.txt")