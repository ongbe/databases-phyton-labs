"""
    Module with a class inherited from the QAbstractTableModel
using for unified tables representation
"""

from PyQt4 import QtCore, QtGui
from dataset.files.AutoResizeableFile import AutoResizeableFile
from dataset.csv.CSVFileEngine import CSVFileEngine


class CSVTableModel(QtCore.QAbstractTableModel):
    """
        A class for representing *.CSV files as QAbstractTableModel objects
    """
    def __init__ (self, filePath = None, engine = None):
        """
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e885f969ab78f931ae1f682f2ddb49dd970f87a6
            Default constructor.
            'filePath' - path to the *.CSV file.
            'engine' - reference to CSVFileEngine object.
        Used if the 'filePath' parameter has None value, ignored otherwise
<<<<<<< HEAD
=======
=======
        
>>>>>>> 44786a20d2b05b7d3d55e44a8ac9f7365e1efaa8
>>>>>>> e885f969ab78f931ae1f682f2ddb49dd970f87a6
        """
        QtCore.QAbstractTableModel.__init__(self)
        self._engine = engine
        if self._engine == None:
            engineFile = AutoResizeableFile(filePath)
            self._engine = CSVFileEngine(engineFile)
            
    
    def rowCount(self, modelIndex = QtCore.QModelIndex()):
        """
            Reimplemented from QAbstractTableModel class
        """
        return self._engine.rowCount()
    
    
    def columnCount(self, modelIndex = QtCore.QModelIndex()):
        """
            Reimplemented from QAbstractTableModel class
        """
        return self._engine.columnCount()
    
    
    def data(self, index, role = QtCore.Qt.DisplayRole):
        """
            Reimplemented from QAbstractTableModel class
        """
        index = self._validateQModelIndex(index) 
        if not index.isValid() or role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self._engine.fieldData(index.row(), index.column()))
    
    
    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        """
            Reimplemented from QAbstractTableModel class
        """
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QVariant(self._engine.titles()[section])
            else:
                return  QtCore.QVariant(section + 1)
        return QtCore.QVariant()
    
    
    def insertRows(self, row, count, parent = QtCore.QModelIndex()):
        """
            Reimplemented from QAbstractTableModel class
        """
        for i in xrange(row, row + count):
            self.insertRow(i)
        return True
    
    
    def insertRow(self, row, parent = QtCore.QModelIndex()):
        """
            Reimplemented from QAbstractTableModel class
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
            Reimplemented from QAbstractTableModel class
        """
        QtCore.QAbstractTableModel.beginRemoveRows(self, parent, row, row)
        self._engine.removeRowAction(row)
        QtCore.QAbstractTableModel.endRemoveRows(self)
        return True
    
    
    def removeRows(self, row, count, parent = QtCore.QModelIndex()):
        """
            Reimplemented from QAbstractTableModel class
        """
        
        for i in xrange(row, row + count):
            self.removeRowAction(row)
        return True
        
        
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        """
            Reimplemented from QAbstractTableModel class
        """
        self._engine.changeFieldData(index.row(), index.column(), value)
        return True
    
    
    def search(self, keyColumn, key):
        """
            Searches rows that have the same string value in 'keyColumn' as 'key'.
        Returns a CSVTableModel object, representing search results.
            'keyColumn' - zero-based column index
            'key' - string-convertable object to search
        """
        return CSVTableModel(None, self._engine.searchRows(keyColumn, key))
        
        
    def flags(self, index):
        """
            Reimplemented from QAbstractTableModel class
        """
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    
    
    def save(self):
        """
<<<<<<< HEAD
            Saves all changes made on the disk.
=======
<<<<<<< HEAD
            Saves all changes made on the disk.
=======
        
>>>>>>> 44786a20d2b05b7d3d55e44a8ac9f7365e1efaa8
>>>>>>> e885f969ab78f931ae1f682f2ddb49dd970f87a6
        """
        self._engine.flush()
            
    
    def _validateQModelIndex(self, index):
        if not isinstance(index, QtCore.QModelIndex):
            raise TypeError("Index must be have 'QModelIndex' type", 
                            {"raisingObject": self, "index": index})
        return index