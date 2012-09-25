"""

"""
from PyQt4 import QtCore

class RangeShiftingInfo(QtCore.QObject):
    """
    
    """
    
    def __init__(self, oldRange, shiftingValue):
        """
        
        """
        QtCore.QObject.__init__(self)
        typeError = TypeError("Range must be a 2-elements sequence of integers!", 
                            {"raiseObject": self, "range": oldRange})
        if not isinstance(oldRange, tuple) or len(oldRange) != 2:
            raise typeError
        try:
            shiftingValue = int(shiftingValue)
            oldRange = ( int(oldRange[0]), int(oldRange[1]) )
        except (AttributeError, TypeError, ValueError):
            raise typeError
        self._oldRange = oldRange
        self._shiftingValue = shiftingValue
        
    def oldRange(self):
        """
        
        """
        return self._oldRange
    
    def shiftingValue(self):
        """
        
        """
        return self._shiftingValue
            