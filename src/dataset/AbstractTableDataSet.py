"""

"""
from dataset.TableDataSetListener import TableDataSetListener

class AbstractTableDataSet(object):
    """
        Provides interface for any data set, which can be represented as a table.
        This class has to be always inherited by subclasses. 
        Not all methods have to be implemented, but not implemented methods must be never called.
        Each method informs all observers if needed and does nothing more. 
        Rows/columns indexes are zero-related. 
        Any accessing to out-of-range indexes attempts will cause exception raising.  
    """
    
    def __init__(self):
        self._listeners = []
        
    def addListener(self, listener):
        if not isinstance(listener, TableDataSetListener):
            raise TypeError() 
        if not listener in self._listeners:    
            self._listeners.append(listener)
        
    def removeListener(self, listener):
        if not isinstance(listener, TableDataSetListener):
            raise TypeError()     
        if not listener in self._listeners:
            return
        del self._listeners[self._listeners.index(listener)]

    def rows(self):
        pass
    
    def columns(self):
        pass
    
    def titles(self):
        pass
    
    def setTitles(self, * titles):
        for listener in self._listeners:
            listener.titlesChangedEvent(self, titles)
    
    def currentRow(self):
        pass
    
    def setCurrentRow(self, rowIndex):
        pass
    
    def currentColumn(self):
        pass
    
    def setCurrentColumn(self, columnIndex):
        pass
    
    def fieldData(self, rowIndex = -1, columnIndex = -1):
        pass
    
    def setFieldData(self, rowIndex = -1, columnIndex = -1, fieldData = None):
        for listener in self._listeners:
            listener.fieldDataChangedEvent(self, rowIndex, columnIndex, fieldData)
    
    def rowData(self, rowIndex = -1):
        pass
    
    def setRowData(self, rowIndex = -1, * rowData):
        for listener in self._listeners:
            listener.fieldDataChangedEvent(self, rowIndex, rowData)
    
    def addRow(self, * rowData):
        for listener in self._listeners:
            listener.rowAddedEvent(self, rowData)
    
    def addColumn(self, columnLabel = "", defaultFillingValue = None):
        for listener in self._listeners:
            listener.columnAddedEvent(self, columnLabel, defaultFillingValue)
    
    def removeRow(self, rowIndex = -1):
        for listener in self._listeners:
            listener.rowRemovedEvent(self, rowIndex)
    
    def removeColumn(self, columnIndex = -1):
        for listener in self._listeners:
            listener.columnRemovedEvent(self, columnIndex)
        
        
    
    