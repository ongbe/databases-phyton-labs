"""

"""

from PyQt4 import QtCore, QtGui
from gui.interfaces.SearchResultsDialogUI import Ui_SearchResultsDialog

class SearchResultsDialog(QtGui.QDialog):
    """
    
    """
    def __init__(self, mainWindow):
        """
        
        """
        QtGui.QDialog.__init__(self, mainWindow)
        self._mainWindow = mainWindow
        self._ui = Ui_SearchResultsDialog()
        self._ui.setupUi(self)
        QtCore.QObject.connect(self._ui.pushButton, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
                               
                               
    def okButtonClicked(self):
        """
        
        """
        self.hide()
        
        
    def showResults(self, model):
        """
        
        """
        self._ui.tableView.setModel(model)
        self.show()