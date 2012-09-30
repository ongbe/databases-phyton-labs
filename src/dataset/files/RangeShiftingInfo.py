"""
    Contains an auxiliary class for file packing events processing 
"""
from PyQt4 import QtCore

class RangeShiftingInfo(QtCore.QObject):
    """
        Class for storing all needed information about 1 file 
    section shifting
    """
    
    def __init__(self, oldRange, shiftingValue):
        """
            Default constructor.
            'oldRange' - old section constrains (a 2-integers tuple, 
        oldRange[1] - excludly) 
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
            Returns old file section constrains
        """
        return self._oldRange
    
    def shiftingValue(self):
        """
            Returns section shifting value
        """
        return self._shiftingValue
            