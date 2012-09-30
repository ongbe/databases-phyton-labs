"""
    Contains an AbstractTableController implementing class
for *.CSV files tables
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
        Implements AbstractTableController class for *.CSV files tables
    """
    def __init__(self):
        """
            Default constructor
        """
        AbstractTableController.__init__(self)
        self._user = None
        self._userRights = UserRights()
        self._model = None
        self._application = None
        self._mainWindow = None
        
        
    def start(self, loginFilePath):
        """
            Reimplemented from AbstractTableController
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
            Reimplemented from AbstractTableController
        """
        if user == None or (user.login() == "" and user.password() == ""):
            self._application.exit()
            return
        self._user = user
        self._userRights = user.rights()
        self._mainWindow.setVisible(True)       
    
    
    def openTable(self, tablePath):
        """
            Reimplemented from AbstractTableController
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
            Reimplemented from AbstractTableController
        """
        if self._user == None or not self._userRights.rowsAddingPermited():
            return OperationResult(False, None, "Rights error: not permited!")
        try:
            self._model.insertRow(rowIndex)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True)
                
        
    def removeRow(self, rowIndex):
        """
            Reimplemented from AbstractTableController
        """
        if self._user == None or not self._userRights.rowsRemovingPermited():
            return OperationResult(False, None, "Rights error: not permited!")
        try:
            self._model.removeRow(rowIndex)
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
        return OperationResult(True)
    
    
    def searchRows(self, keyColumn, key):
        """
            Reimplemented from AbstractTableController
        """
        try:
            return OperationResult(True, self._model.search(keyColumn, key))
        except Exception, exception:
            return OperationResult(False, None, "Model error: " + exception.message)
            
    
    def modifyField(self, row, column, data):
        """
            Reimplemented from AbstractTableController
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
            Reimplemented from AbstractTableController
        """
        return self._model
    
    
    def save(self):
        """
            Reimplemented from AbstractTableController
        """
        self._model.save()
        return OperationResult(True)
        
        
    def close(self):
        """
            Reimplemented from AbstractTableController
        """
        self._model = None
        return OperationResult(True)