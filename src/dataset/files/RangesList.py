"""
    A module with a class for ranges operations
"""

from PyQt4 import QtCore

class RangesList(QtCore.QObject):
    """
        Represents a list of ranges and determines different
    operations with stored ranges
    """
    
    def __init__(self, * initialRange):
        """
            Default constructor.
            'initialRange' - 2 integers that represent initial range
        """   
        QtCore.QObject.__init__(self)   
        self._rangeList = None
        try:
            self._rangeList = [ self._validateRange(initialRange) ]
            if self._rangeList[0][0] == self._rangeList[0][1]:
                self._rangeList = []
        except:
            raise
        
    
    def ranges(self):
        """
            Return a copy of ranges list, stored in the object
        """
        return list(self._rangeList)
    
    def rangeLength(self, rangeIndex):
        """
            Returns length of specified range in the list
            'rangeIndex' - index of range
        """
        typeError = TypeError("Index must be an integer!", {"raiseObject": self, "index": rangeIndex})
        try:
            rangeIndex = int(rangeIndex)
            item = self._rangeList[rangeIndex]
            return item[1] - item[0]
        except (TypeError, AttributeError):
            raise typeError
        except IndexError:
            raise IndexError("Index is out of range!", {"raisingObject": self, "index": rangeIndex})
    
    
    def totalRangesLength(self):
        """
            Returns total length of all ranges stored in the list
        """
        total = 0
        for item in self._rangeList:
            total += item[1] - item[0]
        return total 
    
    
    def size(self):
        """
            Returns ranges amount in the list 
        """
        return len(self._rangeList)
    
    
    def clear(self):
        """
            Clears the list. Returns None
        """
        self._rangeList = []
    
   
    def add(self, * rangeToAdd):
        """
            Adds a new range and performs union operation if needed.
        Returns None
        """
        try:
            rangeToAdd = self._validateRange(rangeToAdd)
        except:
            raise
        if rangeToAdd[0] == rangeToAdd[1]:
            return
        if len(self._rangeList) == 0:
            self._rangeList = [rangeToAdd]
            return
        coveredSlice = self._getCoveredIndexesSlice(rangeToAdd)
        if len(coveredSlice) == 0:
            if rangeToAdd[1] < self._rangeList[0][0]:
                self._rangeList.insert(0, rangeToAdd)
            else:
                self._rangeList.append(rangeToAdd)
            return
        rangesSlice = self._rangeList[coveredSlice[0]:coveredSlice[1]]
        rangesSlice.append(rangeToAdd)
        joinedRange = reduce(lambda first, second: ( min(first[0], second[0]), max(first[1], second[1]) ),
               rangesSlice)
        self._rangeList[coveredSlice[0]:coveredSlice[1]] = [joinedRange]
            
            
    def remove(self, * rangeToRemove):
        """
            Removes a range and performs spliting operation if needed
        """
        try:
            rangeToRemove = self._validateRange(rangeToRemove)
        except:
            raise
        if rangeToRemove[0] == rangeToRemove[1]:
            return 
        rangeToRemove = ( max(rangeToRemove[0], self._rangeList[0][0]), 
                          min(rangeToRemove[1], self._rangeList[len(self._rangeList)-1][1]) )
        coveredSlice = self._getCoveredIndexesSlice(rangeToRemove)
        if len(coveredSlice) == 0:
            return
        if rangeToRemove[0] <= self._rangeList[coveredSlice[0]][0]:
            if rangeToRemove[1] >= self._rangeList[coveredSlice[1] - 1][1]:
                del self._rangeList[coveredSlice[0]:coveredSlice[1]]
                return
        splitedRanges = []
        if self._rangeList[coveredSlice[0]][0] <= rangeToRemove[0]:
            splitedRanges.append( (self._rangeList[coveredSlice[0]][0], rangeToRemove[0]) )
        if self._rangeList[coveredSlice[1] - 1][1] >= rangeToRemove[1]:
            splitedRanges.append( (rangeToRemove[1], self._rangeList[coveredSlice[1] - 1][1]) )
        rangesToAdd = []
        for item in splitedRanges:
            if item[0] != item[1]:
                rangesToAdd.append(item)
        self._rangeList[coveredSlice[0]:coveredSlice[1]] = rangesToAdd                
        
    
    def _validateRange(self, rangeToValidate):
        typeError = TypeError("A range must be a 2-elements sequence of integers!", 
                            {"raiseObject": self, "range": rangeToValidate})
        if rangeToValidate == None or len(rangeToValidate) != 2:
            raise typeError
        result = None
        try:
            left = int(rangeToValidate[0])
            right = int(rangeToValidate[1])
            result = ( min(left, right), max(left, right) )
        except (AttributeError, TypeError, ValueError):
            raise typeError
        return result
    
    def _getCoveredIndexesSlice(self, masterRange):
        leftIndex, rightIndex = len(self._rangeList) + 1, 0
        for i in xrange(0, len(self._rangeList)):
            masterLeft, masterRight = masterRange[0], masterRange[1]
            currentLeft, currentRight = self._rangeList[i]
            contains = False or (masterLeft <= currentLeft <= masterRight)
            contains = contains or (masterLeft <= currentRight <= masterRight)
            contains = contains or (currentLeft <= masterLeft <= currentRight)
            contains = contains or (currentLeft <= masterRight <= currentRight) 
            if contains:
                if i < leftIndex:
                    leftIndex = i
                if i + 1 > rightIndex:
                    rightIndex = i + 1
        if leftIndex > rightIndex:
            return ()
        return (leftIndex, rightIndex)
            
            
        
        
            