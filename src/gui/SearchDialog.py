"""

"""

from PyQt4 import QtCore, QtGui
from gui.interfaces.SearchDialogUI import Ui_SearchDialog

class SearchDialog(QtGui.QDialog):
    """
    
    """
    
    def __init__(self, mainWindow):
        """
        
        """
        QtGui.QDialog.__init__(self, mainWindow)
        self._ui = Ui_SearchDialog()
        self._ui.setupUi(self)
        self._mainWindow = mainWindow
        QtCore.QObject.connect(self._ui.pushButton, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
        
    
    def show(self):
        """
        
        """
        QtGui.QDialog.show(self)
        model = self._mainWindow.currentModel()
        if model == None:
            return
        self._ui.keyColumnCombo.clear()
        for i in xrange(0, model.columnCount()):
            title = model.headerData(i, QtCore.Qt.Horizontal)
            self._ui.keyColumnCombo.insertItem(i, title.toString())      
            
            
    def okButtonClicked(self):
        """
        
        """
        self._mainWindow.searchFor(self._ui.keyColumnCombo.currentIndex(), self._ui.keyEdit.text())
        
        
        