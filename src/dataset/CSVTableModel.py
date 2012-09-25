"""

"""
import os

from dataset.AbstractTableDataSet import AbstractTableDataSet
from dataset.exceptions.IndexOutOfRangeException import IndexOutOfRangeException

class CSVTableDataSet(AbstractTableDataSet):
    """
    
    """
    def __init__(self, filePath = None):
        """
        
        """
        AbstractTableDataSet.__init__(self)
        self._rows = 0
        self._columns = 0
        self._titles = []
        self._currentRow = 0
        self._currentColumn = 0
        
    def __del__(self):
        pass
        
    def rows(self):
        return self._rows
    
    def columns(self):
        return self._columns
    
    def titles(self):
        return self._titles
    
    def setTitles(self, * titles):
        columnIndex = 0
        for title in titles[0 : min(len(titles), len(self._titles))]:
            self._titles[columnIndex] = title
            ++columnIndex
        AbstractTableDataSet.setTitles(self, tuple(self._titles))
    
    def currentRow(self):
        return self._currentRow
    
    def setCurrentRow(self, rowIndex):
        if self._isRowIndexValid(rowIndex):
            self._currentRow = rowIndex
        else:
            raise IndexOutOfRangeException(self)
    
    def currentColumn(self):
        return self._currentColumn
    
    def setCurrentColumn(self, columnIndex):
        if self._isColumnIndexValid(columnIndex):
            self._currentColumn = columnIndex
        else:
            raise IndexOutOfRangeException(self)
    
    def fieldData(self, rowIndex = -1, columnIndex = -1):
        pass
    
    def setFieldData(self, rowIndex = -1, columnIndex = -1, fieldData = None):
        
        AbstractTableDataSet.setFieldData(self, rowIndex, columnIndex, fieldData)
    
    def rowData(self, rowIndex = -1):
        pass
    
    def setRowData(self, rowIndex = -1, * rowData):
        
        AbstractTableDataSet.setRowData(self, rowIndex, tuple(rowData))
    
    def addRow(self, * rowData):
        
        ++self._rows
        AbstractTableDataSet.addRow(self, tuple(rowData[0:self._columns]))
    
    def addColumn(self, columnLabel = "", defaultFillingValue = None):
        
        ++self._columns
        AbstractTableDataSet.addColumn(self, columnLabel, defaultFillingValue)
    
    def removeRow(self, rowIndex = -1):
        if rowIndex == -1:
            rowIndex = self._rows - 1
        if not self._isRowIndexValid(rowIndex):
            raise IndexOutOfRangeException(self)
        # add code here
        --self._rows
        if self._currentRow >= self._rows:
            self._currentRow = self._rows - 1
        AbstractTableDataSet.removeRow(self, rowIndex)
    
    def removeColumn(self, columnIndex = -1):
        if columnIndex == -1:
            columnIndex = self._columns - 1
        if not self._isColumnIndexValid(columnIndex):
            raise IndexOutOfRangeException(self);
        # add code here
        del self._titles[columnIndex]
        --self.columns()
        if self._currentColumn >= self._columns:
            self._currentColumn = self._columns - 1
        AbstractTableDataSet.removeColumn(self, columnIndex)
    
    def _isRowIndexValid(self, rowIndex):
        return rowIndex >= 0 and rowIndex < self._rows
    
    def _isColumnIndexValid(self, columnIndex):
        return columnIndex >= 0 and columnIndex < self._columns
        
        