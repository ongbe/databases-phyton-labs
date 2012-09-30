"""
    A module for FilePackingListener class
"""
from PyQt4 import QtCore

class FilePackingListener(QtCore.QObject):
    """
        Is an analog for Java or C# interface. In fact, it is
    an abstract class, that declares a contract for file packing
    event listeners
    """
    def __init__(self):
        """
            Default constructor. Must be invoked in derived classes
        """
        QtCore.QObject.__init__(self)
    
    def filePackedEvent(self, packingInfoList):
        """
            Is invoked when file packing event happens
            'packingInfoList' - a list of RangeShiftingInfo objects
        """
        pass