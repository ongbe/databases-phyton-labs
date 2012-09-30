"""
    Module for main window
"""

from PyQt4 import QtCore, QtGui
from gui.AbstractTableController import AbstractTableController
from gui.interfaces.MainWindowUI import Ui_MainWindow
from dataset.files.RangesList import RangesList
from gui.SearchDialog import SearchDialog
from gui.SearchResultsDialog import SearchResultsDialog
from gui.ModifyingFieldDialog import ModifyingFieldDialog

class MainWindow(QtGui.QMainWindow):
    """
        Main window class
    """
    def __init__(self, controller):
        """
            Default constructor.
            'controller' - an AbstractTableController object
        """
        if not isinstance(controller, AbstractTableController):
            raise TypeError("Controller must be an 'AbstractTableController' type", 
                            {"raisingObject": self, "controller": controller})
        QtGui.QMainWindow.__init__(self)
        self.rowsPerPage = 100
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._visibleRowsRanges = RangesList(0, 0)
        self._searchDialog = SearchDialog(self)
        self._searchResultsDialog = SearchResultsDialog(self)
        self._modifyingFieldDialog = ModifyingFieldDialog(self)
        self._setFileAndTableOperationsEnabled(False)
        QtCore.QObject.connect(self._ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openFileAction)
        QtCore.QObject.connect(self._ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFileAction)
        QtCore.QObject.connect(self._ui.actionClose, QtCore.SIGNAL("triggered()"), self.closeFileAction)
        QtCore.QObject.connect(self._ui.pagesTabs, QtCore.SIGNAL("currentChanged(int)"), self.activeTabChanged)
        QtCore.QObject.connect(self._ui.actionInsert, QtCore.SIGNAL("triggered()"), self.insertNewRowAction)
        QtCore.QObject.connect(self._ui.actionRemove, QtCore.SIGNAL("triggered()"), self.removeRowAction)
        QtCore.QObject.connect(self._ui.actionSearch, QtCore.SIGNAL("triggered()"), self.searchRowAction)
        QtCore.QObject.connect(self._ui.tableView, QtCore.SIGNAL("doubleClicked(const QModelIndex &)"), self.tableViewDbClickEvent)
        
        
    def openFileAction(self):
        """
            Slot for File->Open item triggered() signal
        Returns None
        """
        filePath = QtGui.QFileDialog.getOpenFileName(parent = self, caption = QtCore.QString("Open table..."),
                                          filter = QtCore.QString("CSV files (*.csv)"))
        if filePath == None or len(filePath) == 0:
            return
        result = self._controller.openTable(filePath)
        if not result.isOk():
            QtGui.QMessageBox.about(self, "Error...", result.message())
            return
        model = result.data()
        self._ui.tableView.setModel(model)
        self._visibleRowsRanges.clear()
        self._visibleRowsRanges.add(0, model.rowCount())
        self._distributeToPages()
        self._selectPage(0)
        self._setFileAndTableOperationsEnabled(True)
        
        
    def saveFileAction(self):
        """
            Slot for File->Save item triggered() signal
        Returns None
        """
        self._controller.save()
        
        
    def closeFileAction(self):
        """
            Slot for File->Close item triggered() signal
        Returns None
        """
        self._controller.save()
        self._controller.close()
        self._ui.pagesTabs.clear()
        self._ui.tableView.setModel(None)
        
        
    def activeTabChanged(self, index):
        """
            Slot for File->Open item triggered() signal
        Returns None
        """
        self._selectPage(index)
        
        
    def insertNewRowAction(self):
        """
            Slot for pages QTabView object currentChanged(int) signal
        Returns None
        """
        result = self._controller.insertRow(self._ui.tableView.currentIndex().row())
        if not result.isOk():
            QtGui.QMessageBox.about(self, "Error...", result.message())
            return
        index = self._visibleRowsRanges.ranges()[0][1]
        self._visibleRowsRanges.add(index, index + 1)
        self._distributeToPages()
        self._selectPage(self._ui.pagesTabs.currentIndex())
        
        
    def removeRowAction(self):
        """
            Slot for Table->Remove row item triggered() signal
        Returns None
        """
        result = self._controller.removeRowAction(self._ui.tableView.currentIndex().row())
        if not result.isOk():
            QtGui.QMessageBox.about(self, "Error...", result.message())
            return
        self._distributeToPages()
        self._selectPage(self._ui.pagesTabs.currentIndex())
        
    
    def tableViewDbClickEvent(self, ARG):
        """
            Slot for QTableView object doubleClicked(const QModelIndex &) signal
        Returns None
        """
        self._modifyingFieldDialog.show()
        self._modifyingFieldDialog.focusToEdit()
    
        
    def searchRowAction(self):
        """
            Slot for Table->Search for... item triggered() signal
        Returns None
        """
        self._searchDialog.show()
        
        
    def searchFor(self, columnKey, key):
        """
            Called by SearchDialog object for searching data.
        Returns None
            'keyColumn' - zero-based column index
            'key' - string-convertable object to search
        """
        result = self._controller.searchRows(columnKey, key)
        if not result.isOk():
            QtGui.QMessageBox.about(self, "Error...", result.message())
            return
        self._searchResultsDialog.showResults(result.data())
        
        
    def modifyCurrentField(self, value):
        """
            Called by ModifyingFieldDialog object for changing
        currently selected field. Returns None
            'value' - new field value
        """
        index = self._ui.tableView.currentIndex()
        result = self._controller.modifyField(index.row(), index.column(), value)
        if not result.isOk():
            QtGui.QMessageBox.about(self, "Error...", result.message())
            return
        newRow = index.row()
        newColumn = (index.column() + 1) % self.currentModel().columnCount()
        if newColumn == 0:
            newRow = (index.row() + 1) % self.currentModel().rowCount()
            if newRow == 0:
                newRow = self.currentModel().rowCount() - 1
        self._ui.tableView.setCurrentIndex(self.currentModel().createIndex(newRow, newColumn))       
        
        
    def currentModel(self):
        """
            Returns currently associated with controller model
        """
        if self._controller == None:
            return None
        return self._controller.model()
        
        
    def _distributeToPages(self):
        model = self._controller.model()
        pages = (model.rowCount() + self.rowsPerPage - 1) / self.rowsPerPage
        for i in xrange(pages, self._ui.pagesTabs.count()):
            self._ui.pagesTabs.removeTab(i)
        for i in xrange(self._ui.pagesTabs.count(), pages):
            tab = QtGui.QWidget()
            tab.setObjectName(QtCore.QString("Tab_" + str(i + 1))) 
            self._ui.pagesTabs.addTab(tab, QtCore.QString(str(i + 1)))
            
            
    def _selectPage(self, page):
        model = self._controller.model()
        if model == None:
            return
        rangeToShow = (page * self.rowsPerPage, min((page + 1) * self.rowsPerPage, model.rowCount())) 
        for item in self._visibleRowsRanges.ranges():
            for i in xrange(item[0], item[1]):
                if i < rangeToShow[0] or i >= rangeToShow[1]:
                    self._ui.tableView.hideRow(i)
        self._visibleRowsRanges.clear()
        for i in xrange(rangeToShow[0], rangeToShow[1]):
            self._ui.tableView.showRow(i)
        self._visibleRowsRanges.add(rangeToShow[0], rangeToShow[1])
        self._ui.tableView.setCurrentIndex(self._controller.model().createIndex(rangeToShow[0], 0))
        
        
    def _setFileAndTableOperationsEnabled(self, enabled):
        self._ui.actionClose.setEnabled(enabled)
        self._ui.actionSave.setEnabled(enabled)
        self._ui.actionRemove.setEnabled(enabled)
        self._ui.actionSearch.setEnabled(enabled)
        self._ui.actionInsert.setEnabled(enabled)
        if not enabled:
            self._searchDialog.hide()
            self._searchResultsDialog.hide()
            self._modifyingFieldDialog.hide()
        
