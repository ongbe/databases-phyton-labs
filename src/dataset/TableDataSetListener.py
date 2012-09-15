""""
"""


class TableDataSetListener(object):
    """
    
    """
    
    def titlesChangedEvent(self, table, * titles): 
        pass
    
    def fieldDataChangedEvent(self, table, rowIndex, columnIndex, data):
        pass
    
    def rowDataChangedEvent(self, table, rowIndex, * data):
        pass
    
    def rowAddedEvent(self, table, * rowData):
        pass
    
    def columnAddedEvent(self, table, columnLabel, fillingValue):
        pass
    
    def rowRemovedEvent(self, table, rowIndex):
        pass
    
    def columnRemovedEvent(self, table, columnIndex):
        pass
    