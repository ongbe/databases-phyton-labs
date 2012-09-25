""""

"""

import os
import struct
from PyQt4 import QtCore
from dataset.files.RangesList import RangesList
from dataset.files.FilePackingListener import FilePackingListener
from dataset.files.RangeShiftingInfo import RangeShiftingInfo

"""

"""
class AutoResizeableFile(QtCore.QObject):
    """
    
    """
    def __init__(self, filePath = None):
        QtCore.QObject.__init__(self)
        self._isTemporary = False;
        if filePath == None:
            filePath = os.tempnam()
            self._isTemporary = True
        self._file = QtCore.QFile(filePath)
        if not self._file.open(QtCore.QIODevice.ReadWrite):
            raise IOError("File can't be opened!",
                          {"raisingObject": self, "path": filePath, "error": self._file.error()})
        self._validRanges = RangesList(0, self._file.size())
        self._packingListeners = []
        
        
    def __del__(self):
        """
        
        """
        self.close()
               
                  
    def close(self):
        """
        
        """
        if self._file.isOpen():
            self.flush()
            self._file.close()
            if self._isTemporary:
                self._file.remove()
                
                
    def path(self):
        """
        
        """
        return self._file.fileName()
                        
                          
    def position(self):
        """
        
        """
        return self._file.pos()
    
    
    def size(self):
        """
        
        """
        return self._file.size()
    
    def validRanges(self):
        """
        
        """
        return self._validRanges.ranges()
    
    
    def isOpened(self):
        """
        
        """
        return self._file.isOpen()
    
    
    def endOfFile(self):
        """
        
        """
        return self.position() >= self.size()
    
    
    def setPosition(self, position):
        """
        
        """
        position = self._validateInteger(position)
        if not self._file.seek(position):
            raise IOError("Seeking position failed", 
                             {"raiseObject": self, "position": position, "error": self._file.error()})
        return self.position()
    
    
    def erase(self):
        """
        
        """
        self._file.resize(0)
        self.setPosition(0)
        self._validRanges.clear()
    
    
    def addPackingListener(self, listener):
        """
        
        """
        if not isinstance(listener, FilePackingListener):
            raise TypeError("Listener must has a 'FilePackingListener' type!",
                            {"raisingObject": self})
        self._packingListeners.append(listener)
        
        
    def removePackingListener(self, listener):
        """
        
        """
        if not isinstance(listener, FilePackingListener):
            raise TypeError("Listener must has a 'FilePackingListener' type!",
                            {"raisingObject": self})
        if not (listener in self._packingListeners):
            return
        del self._packingListeners[self._packingListeners.index(listener)]
        
        
    def realPositionFor(self, validPosition):
        """
        
        """
        ranges = self._validRanges.ranges()
        lastRangeIndex, currentSum = 0, 0
        rangeFound = False
        for lastRangeIndex in xrange(0, len(ranges)):
            currentRange = ranges[lastRangeIndex]
            if currentSum <= validPosition < currentSum + (currentRange[1] - currentRange[0]):
                rangeFound = True
                break
            else:
                currentSum += (currentRange[1] - currentRange[0])
        if not rangeFound:
            if currentSum == validPosition:
                return  validPosition 
            else:
                raise IndexError("Position is too large", {"raisingObject": self, 
                                                           "value": validPosition})
        lastEnumeratedRange = ranges[lastRangeIndex]
        neededDelta = validPosition - currentSum
        return lastEnumeratedRange[0] + neededDelta
    
        
    def readLine(self):
        """
        
        """
        data = str(self._file.readLine())
        return data.strip()
    
    
    def read(self, size = -1):
        """
        
        """
        size = self._validateInteger(size)
        if size == -1:
            size = self._file.size() - self.position()
        oldPosition = self.position()   
        data = str(self._file.read(size))
        return data
    
    
    def readAll(self):
        """
        
        """
        oldPosition = self.position()
        self.setPosition(0)
        data = self.read()
        self.setPosition(oldPosition)
        return data
    
    
    def readInteger(self):
        """
        
        """
        oldPosition = self.position()
        string = self.read(4)
        if len(string) != 4:
            self._file.seek(oldPosition)
            raise EOFError("Can't read needed amount of bytes!",
                           {"raiseObject": self, "position": oldPosition, "fileSize": self._file.size()})
        return struct.unpack("i", string)[0]
    
    
    def write(self, string, eraseFirstSymbols = 0):
        """
        
        """
        eraseFirstSymbols = self._validateInteger(eraseFirstSymbols)
        string = str(string)
        stringLength = len(string)
        eraseFirstSymbols = min(eraseFirstSymbols, self._file.size() - self.position())
        additionalSpace = stringLength - eraseFirstSymbols
        start= self.position() + eraseFirstSymbols
        newStart = start + additionalSpace
        oldPosition = self.position()
        self._shift(start, -1, newStart)
        written = self._file.writeData(string)
        self.setPosition(oldPosition + written)
        rangeToAdd = (oldPosition, oldPosition + stringLength)
        shiftingValue = newStart - start
        self._shiftValidRanges(start, shiftingValue)
        self._validRanges.add(rangeToAdd[0], rangeToAdd[1])
        return written
        
        
    def writeLine(self, string, eraseFirstSymbols = 0):
        """
        
        """
        string = str(string) + '\n'
        return self.write(string, eraseFirstSymbols)
        
    
    def writeInteger(self, value, eraseOld = False):
        """
        
        """
        value = self._validateInteger(value)
        eraseFirstSymbols = 0
        if eraseOld:
            eraseFirstSymbols = 4
        return self.write(struct.pack("i", value), eraseFirstSymbols)
    
    
    def flush(self):
        """
        
        """
        self.pack()
        self._file.flush()
        
        
    def pack(self):
        """
        
        """
        if self._validRanges.size() == 0:
            self.setPosition(0)
            self._file.resize(0)
            return
        shiftingInfos = []
        currentValidSize = 0
        totalShifting = 0
        for validRange in self._validRanges.ranges():
            shiftValue = currentValidSize - validRange[0]
            totalShifting += shiftValue
            if (validRange[0] != validRange[1]) and (totalShifting != 0):
                shiftingInfos.append(RangeShiftingInfo(validRange, totalShifting))
            self._shift(validRange[0], validRange[1], currentValidSize)
            currentValidSize += validRange[1] - validRange[0]
        self._file.resize(currentValidSize)
        if len(shiftingInfos) != 0:
            for listener in self._packingListeners:
                listener.filePackedEvent(shiftingInfos)
        self._validRanges.clear()
        self._validRanges.add(0, currentValidSize)
                        
    
    def removeRange(self, startPosition, endPosition):
        """
        
        """
        self._validRanges.remove(startPosition, endPosition)
        invalidSpacePercentage = (1 - (float(self._validRanges.size()) / float(self._file.size()))) * 100.0
        if invalidSpacePercentage > 25.0 or self._validRanges.size() >= 64:
            self.pack() 
        
    
    def _shift(self, start, end, newStart):
        if newStart == start:
            return
        if end == -1:
            end = self._file.size();
        start, end = min(start, end), max(start, end)
        oldPosition = self.position()
        self.setPosition(start)
        data = self.read(end - start)
        if newStart > self._file.size():
            self._file.resize(newStart)
        self.setPosition(newStart)
        self._file.writeData(data)
        self.setPosition(oldPosition)
        
    
    def _shiftValidRanges(self, fileStartPosition, shiftingValue):
        ranges = self._validRanges.ranges()
        firstShiftingRangeIndex = -1
        for i in xrange(0, len(ranges)):
            if ranges[i][0] <= fileStartPosition <= ranges[i][1]:
                firstShiftingRangeIndex = i
                break
        if firstShiftingRangeIndex == -1:
            return
        else:
            firstShiftingRange = ranges[firstShiftingRangeIndex]
            splitedRanges = [(firstShiftingRange[0], fileStartPosition), 
                             (fileStartPosition, firstShiftingRange[1])]
            self._validRanges.remove(splitedRanges[1][0], ranges[len(ranges) - 1][1])
            shiftingRanges = [(splitedRanges[1][0], splitedRanges[1][1])]
            for i in xrange(firstShiftingRangeIndex + 1, len(ranges)):
                if ranges[i][0] != ranges[i][1]:
                    shiftingRanges.append(ranges[i])
            shiftingInfos = []
            for item in shiftingRanges:
                self._validRanges.add(item[0] + shiftingValue, item[1] + shiftingValue)
                if (item[0] != item[1]) and (shiftingValue != 0):
                    shiftingInfos.append(RangeShiftingInfo(item, shiftingValue))
            if len(shiftingInfos) != 0:
                for listener in self._packingListeners:
                    listener.filePackedEvent(shiftingInfos)
                    
    
    def _validateInteger(self, value):
        try:
            return int(value)
        except (TypeError, AttributeError, ValueError):
            raise TypeError("Value mast be an integer", {"raisingObject": self, "value": value})
            
            