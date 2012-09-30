"""
    Module for changing field dialog class
"""

from PyQt4 import QtCore, QtGui
from gui.interfaces.ModifyFieldDialogUI import Ui_ModifyingFieldDialog

class ModifyingFieldDialog(QtGui.QDialog):
    """
        Changing field dialog class
    """
    def __init__(self, mainWindow):
        """
            Default constructor
            'mainWindow' - MainWindow object reference
        """
        QtGui.QDialog.__init__(self, mainWindow)
        self._mainWindow = mainWindow
        self._ui = Ui_ModifyingFieldDialog()
        self._ui.setupUi(self)
        QtCore.QObject.connect(self._ui.okButton, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
        QtCore.QObject.connect(self._ui.cancelButton, QtCore.SIGNAL("clicked()"), self.cancelButtonClicked)
        
        
    def okButtonClicked(self):
        """
            A slot for OK button "clicked()" signal
        Returns None
        """
        self._mainWindow.modifyCurrentField(self._ui.valueEdit.text())
        self.focusToEdit()
        
        
    def focusToEdit(self):
        """
            Puts edit box in focus and makes it's text selected.
        Returns None
        """
        self._ui.valueEdit.setSelection(0, self._ui.valueEdit.text().length())
        self._ui.valueEdit.setFocus()
    
    
    def cancelButtonClicked(self):
        """
            A slot for CANCEL button "clicked()" signal
        Returns None
        """
        self.hide()