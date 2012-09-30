"""
    Module for showing search result dialog class
"""

from PyQt4 import QtCore, QtGui
from gui.interfaces.SearchResultsDialogUI import Ui_SearchResultsDialog

class SearchResultsDialog(QtGui.QDialog):
    """
        Showing search results dialog class
    """
    def __init__(self, mainWindow):
        """
            Default constructor.
            'mainWindow' - MainWindow object reference
        """
        QtGui.QDialog.__init__(self, mainWindow)
        self._mainWindow = mainWindow
        self._ui = Ui_SearchResultsDialog()
        self._ui.setupUi(self)
        QtCore.QObject.connect(self._ui.pushButton, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
                               
                               
    def okButtonClicked(self):
        """
            A slot for OK button "clicked()" signal
        Returns None
        """
        self.hide()
        
        
    def showResults(self, model):
        """
            Called by MainWindow object for showing search results.
            'model' - QAbstractTableModel object reference
        """
        self._ui.tableView.setModel(model)
        self.show()