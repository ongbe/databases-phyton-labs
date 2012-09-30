"""

"""

from PyQt4 import QtCore, QtGui
from dataset.files.AutoResizeableFile import AutoResizeableFile
from dataset.csv.CSVFileEngine import CSVFileEngine

"""

"""
class CSVTableModel(QtCore.QAbstractTableModel):
    """
    
    """
    def __init__ (self, filePath = None, engine = None):
        """
        
        """
        QtCore.QAbstractTableModel.__init__(self)
        self._engine = engine
        if self._engine == None:
            engineFile = AutoResizeableFile(filePath)
            self._engine = CSVFileEngine(engineFile)
            
    
    def rowCount(self, modelIndex = QtCore.QModelIndex()):
        """
        
        """
        return self._engine.rowCount()
    
    
    def columnCount(self, modelIndex = QtCore.QModelIndex()):
        """
        
        """
        return self._engine.columnCount()
    
    
    def data(self, index, role = QtCore.Qt.DisplayRole):
        """
        
        """
        index = self._validateQModelIndex(index) 
        if not index.isValid() or role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self._engine.fieldData(index.row(), index.column()))
    
    
    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        """
        
        """
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QVariant(self._engine.titles()[section])
            else:
                return  QtCore.QVariant(section + 1)
        return QtCore.QVariant()
    
    
    def insertRows(self, row, count, parent = QtCore.QModelIndex()):
        """
        
        """
        for i in xrange(row, row + count):
            self.insertRow(i)
        return True
    
    
    def insertRow(self, row, parent = QtCore.QModelIndex()):
        """
        
        """
        emptyData = []
        for i in xrange(0, self._engine.columnCount()):
            emptyData.append("")
        QtCore.QAbstractTableModel.beginInsertRows(self, parent, row, row)
        self._engine.insertRow(row, emptyData)
        QtCore.QAbstractTableModel.endInsertRows(self)
        return True
    
    
    def removeRowAction(self, row, parent = QtCore.QModelIndex()):
        """
        
        """
        QtCore.QAbstractTableModel.beginRemoveRows(self, parent, row, row)
        self._engine.removeRowAction(row)
        QtCore.QAbstractTableModel.endRemoveRows(self)
        return True
    
    
    def removeRows(self, row, count, parent = QtCore.QModelIndex()):
        """
        
        """
        
        for i in xrange(row, row + count):
            self.removeRowAction(row)
        return True
        
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        """
        
        """
        self._engine.changeFieldData(index.row(), index.column(), value)
        return True
    
    
    def search(self, keyColumn, key):
        """
        
        """
        return CSVTableModel(None, self._engine.searchRows(keyColumn, key))
        
        
    def flags(self, index):
        """
        
        """
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    
    
    def save(self):
        """
        
        """
        self._engine.flush()
            
    
    def _validateQModelIndex(self, index):
        if not isinstance(index, QtCore.QModelIndex):
            raise TypeError("Index must be have 'QModelIndex' type", 
                            {"raisingObject": self, "index": index})
        return index