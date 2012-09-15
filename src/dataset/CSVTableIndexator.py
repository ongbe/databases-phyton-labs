"""

"""
from dataset.TableDataSetListener import TableDataSetListener
from dataset.CSVTableDataSet import CSVTableDataSet


class CSVTableIndexator(TableDataSetListener):
    """
    
    """

    def __init__(self, csvDataSet):
        """
        
        """
        if not isinstance(csvDataSet, CSVTableDataSet):
            raise TypeError()
        self._dataSet = csvDataSet;