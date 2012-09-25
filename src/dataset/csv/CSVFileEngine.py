"""

"""
from dataset.files.FilePackingListener import FilePackingListener
from dataset.files.AutoResizeableFile import AutoResizeableFile

class CSVFileEngine(FilePackingListener):
    """
    
    """
    def __init__(self, resizeableFile):
        """
        
        """
        FilePackingListener.__init__(self)
        self._file = resizeableFile
        self._fieldsIndexingFile = AutoResizeableFile()
        oldPosition = self._file.position()
        self._file.setPosition(0)
        self._titles = self._file.readLine().split(";")
        self._columnsCount = len(self._titles)
        self._rowsCount = 0
        while not self._file.endOfFile():
            left = self._file.position()
            string = self._file.readLine()
            if len(string) != 0:
                self._rowsCount += 1
                indexes = self._stringToFieldsIndexes(string, left)
                for index in indexes:
                    self._fieldsIndexingFile.writeInteger(index)
        self._orderIndexesFiles = []
        for i in xrange(0, self._columnsCount):
            self._orderIndexesFiles.append(None)
        self._file.addPackingListener(self)
        self._file.setPosition(oldPosition)
        
        
    def filePackedEvent(self, packingInfoList):
        """
        
        """
        oldPosition = self._fieldsIndexingFile.position()
        self._fieldsIndexingFile.pack()
        for position in xrange(0, self._fieldsIndexingFile.size(), 4):
            self._fieldsIndexingFile.setPosition(position)
            currentValue = self._fieldsIndexingFile.readInteger()
            for item in packingInfoList:
                oldRange = item.oldRange()
                if oldRange[0] <= currentValue <= oldRange[1]:
                    self._fieldsIndexingFile.setPosition(position)
                    self._fieldsIndexingFile.writeInteger(currentValue + item.shiftingValue(), True)
        self._fieldsIndexingFile.setPosition(oldPosition)
                    
    
    def rowCount(self):
        """
        
        """
        return self._rowsCount
    
    
    def columnCount(self):
        """
        
        """
        return self._columnsCount
    
    
    def titles(self):
        """
        
        """
        return self._titles
    
                  
    def rowData(self, row):
        """
        
        """
        row = self._validateRow(row)
        fieldsRanges = self._getRowFieldsRanges(row)
        data = self._readStrings(fieldsRanges)
        return tuple([row] + data)
    
    
    def fieldData(self, row, column):
        """
        
        """
        row = self._validateRow(row)
        column = self._validateColumn(column)
        fieldRange = self._getRowFieldsRanges(row)[column]
        return self._readStrings([fieldRange])[0]
    
    
    def changeFieldData(self, row, column, data):
        """
        
        """
        row = self._validateRow(row)
        column = self._validateColumn(column)
        self._removeFieldFromOrderFileIfPossible(row, column)
        rowFieldsRanges = self._getRowFieldsRanges(row)
        fieldRange = rowFieldsRanges[column]
        rowBeginIndex = rowFieldsRanges[0][0]
        oldPosition = self._file.position()
        self._file.setPosition(fieldRange[0])
        self._file.write(data, fieldRange[1] - fieldRange[0])
        self._file.setPosition(oldPosition)
        self._fieldsIndexingFile.setPosition(self._fieldsIndexingFile.realPositionFor(4 * row * (self._columnsCount + 1)))
        self._fieldsIndexingFile.writeInteger(rowBeginIndex, True)
        self._insertFieldIntoOrderFileIfPossible(row, column, data, self._rowsCount - 1)
        
        
    def insertRow(self, rowIndex, rowData):
        """
        
        """
        rowIndex = self._validateRow(rowIndex, self._rowsCount + 1)
        try:
            data = []
            for i in xrange(0, self._columnsCount):
                data.append(str(rowData[i]))
            rowData = data
        except (ValueError, TypeError, AttributeError, IndexError):
            raise ValueError("rowData must be a columnCount-size sequence of string-convertable values",
                             {"rowData": rowData, "raisingObject": self})
        for i in xrange(0, self._columnsCount):
            self._insertFieldIntoOrderFileIfPossible(rowIndex, i, rowData[i])
        string = ""
        oldPosition = self._file.position()
        for i in xrange(0, self._columnsCount):
            string = string + rowData[i]
            if i != self._columnsCount - 1:
                string += ';'
        insertPosition = self._file.size()
        if rowIndex != self._rowsCount:
            insertPosition = self._getRowFieldsRanges(rowIndex)[0][0]
        indexes = self._stringToFieldsIndexes(string, insertPosition)
        self._file.setPosition(insertPosition)
        self._file.writeLine(string)
        self._fieldsIndexingFile.setPosition(self._fieldsIndexingFile.size())
        if rowIndex != self._rowsCount:
            self._fieldsIndexingFile.setPosition( self._fieldsIndexingFile.realPositionFor(
                                                            4 * rowIndex * (self._columnsCount + 1)) )
        for index in indexes:
            self._fieldsIndexingFile.writeInteger(index)
        self._file.setPosition(oldPosition)
        self._rowsCount = self._rowsCount + 1
        
        
    def removeRow(self, row): 
        """
        
        """
        row = self._validateRow(row)
        for i in xrange(0, self._columnsCount):
            self._removeFieldFromOrderFileIfPossible(row, i)
        indexFileLeft = self._fieldsIndexingFile.realPositionFor(row * 4 * (self._columnsCount + 1))
        indexFileRight = indexFileLeft + 4*(self._columnsCount + 1)
        fileLeft, fileRight = self._getRowFieldsRanges(row)[0][0], 0
        if row == self._rowsCount - 1:
            fileRight = self._file.size()
        else:
            fileRight = self._getRowFieldsRanges(row + 1)[0][0]
        self._fieldsIndexingFile.removeRange(indexFileLeft, indexFileRight)  
        self._file.removeRange(fileLeft, fileRight)
        self._rowsCount = self._rowsCount - 1
        
        
    def searchRows(self, keyColumn, key):
        """
        
        """
        keyColumn = self._validateColumn(keyColumn)
        orderFile = self._createOrderFileIfNeeded(keyColumn)
        orderFile.setPosition(self._searchFieldPositionInOrderFile(keyColumn, key))
        result = []
        while not orderFile.endOfFile():
            rowIndex = orderFile.readInteger()
            rowData = self.rowData(rowIndex)
            if rowData[keyColumn + 1] == key:
                result.append(rowData)
            else:
                break
        return result
    
    
    def fieldsIndexes(self):
        result = []
        self._fieldsIndexingFile.pack()
        self._fieldsIndexingFile.setPosition(0)
        for i in xrange(0, self._rowsCount):
            rowIndexes = []
            for j in xrange(0, self._columnsCount):
                rowIndexes.append(self._fieldsIndexingFile.readInteger())
            result.append(tuple(rowIndexes))     
        return result           
        
    
    def _createOrderFileIfNeeded(self, column):
        if self._orderIndexesFiles[column] != None:
            return self._orderIndexesFiles[column]
        self._orderIndexesFiles[column] = AutoResizeableFile()
        for i in xrange(0, self._rowsCount):
            self._insertFieldIntoOrderFileIfPossible(i, column, self.fieldData(i, column), i)
        return self._orderIndexesFiles[column]
        
        
    def _removeFieldFromOrderFileIfPossible(self, row, column, rowsCount = -1):
        if self._orderIndexesFiles[column] == None:
            return
        if rowsCount == -1:
            rowsCount = self._rowsCount
        orderFile = self._orderIndexesFiles[column]
        oldPosition = orderFile.position()
        removingPosition = -1
        for i in xrange(0, rowsCount):
            realPosition = orderFile.realPositionFor(i * 4)
            orderFile.setPosition(realPosition)
            readValue = orderFile.readInteger()
            if readValue == row:
                removingPosition = realPosition
            elif readValue > row:
                orderFile.setPosition(realPosition)
                orderFile.writeInteger(readValue - 1, True)
        if removingPosition != -1:
            orderFile.removeRange(removingPosition, removingPosition + 4)
        orderFile.setPosition(oldPosition)
        
    
    def _insertFieldIntoOrderFileIfPossible(self, row, column, data, rowsCount = -1):
        if self._orderIndexesFiles[column] == None:
            return
        if rowsCount == -1:
            rowsCount = self._rowsCount
        orderFile = self._orderIndexesFiles[column]
        oldPosition = orderFile.position()
        insertPositon = self._searchFieldPositionInOrderFile(column, data, rowsCount)
        for i in xrange(0, rowsCount):
            realPosition = orderFile.realPositionFor(i * 4)
            orderFile.setPosition(realPosition)
            readValue = orderFile.readInteger()
            if readValue >= row:
                orderFile.setPosition(realPosition)
                orderFile.writeInteger(readValue + 1, True)
        orderFile.setPosition(insertPositon)
        orderFile.writeInteger(row)        
        orderFile.setPosition(oldPosition)
                
        
    def _searchFieldPositionInOrderFile(self, column, data, rowsCount = -1):
        if rowsCount == -1:
            rowsCount = self._rowsCount
        if rowsCount == 0:
            return 0
        orderFile = self._orderIndexesFiles[column]
        left, right = 0, rowsCount
        while left < right:
            middle = (left + right) / 2
            orderFile.setPosition(orderFile.realPositionFor(middle * 4))
            middleRowIndex = orderFile.readInteger()
            middleData = self.fieldData(middleRowIndex, column)
            if data <= middleData:
                right = middle
            else:
                left = middle + 1
        return orderFile.realPositionFor(right * 4)

    
    def _stringToFieldsIndexes(self, string, left):
        indexes = [left]
        fieldsCount = 0
        for stringIndex in xrange(0, len(string)):
            if string[stringIndex] == ';':
                fieldsCount += 1
                indexes.append(stringIndex + left)
                if fieldsCount == self._columnsCount - 1:
                    break
        indexes.append(left + len(string))
        return indexes

    
    def _getRowFieldsRanges(self, row):
        realPosition = self._fieldsIndexingFile.realPositionFor(4 * row * (self._columnsCount + 1))
        oldPosition = self._fieldsIndexingFile.position()
        self._fieldsIndexingFile.setPosition(realPosition)
        indexes = []
        for i in xrange(0, self._columnsCount + 1):
            indexes.append(self._fieldsIndexingFile.readInteger())
        result = []
        for i in xrange(0, len(indexes) - 1):
            if i == 0:
                result.append( (indexes[i], indexes[i+1]) )
            else:
                result.append( (indexes[i] + 1, indexes[i+1]) )
        self._fieldsIndexingFile.setPosition(oldPosition)
        return result
        
        
    def _readStrings(self, rangesList):
        oldPosition = self._file.position()
        result = []
        for item in rangesList:
            self._file.setPosition(item[0])
            result.append(self._file.read(item[1] - item[0]))
        self._file.setPosition(oldPosition)
        return result
    
    
    def _validateInteger(self, value):
        try:
            return int(value)
        except (TypeError, AttributeError, ValueError):
            raise TypeError("Value mast be an integer", {"raisingObject": self, "value": value})
        
    
    def _validateRow(self, row, limit = -1):
        if limit == -1:
            limit = self._rowsCount
        try:
            row = self._validateInteger(row)
        except TypeError, exception:
            exception.message = "Row index must be an integer"
            raise exception
        if row >= limit:
            raise IndexError("Row index is out-of-range", {"raisingObject": self, "index": row})
        return row
        
        
    def _validateColumn(self, column, limit = -1):
        if limit == -1:
            limit = self._columnsCount
        try:
            column = self._validateInteger(column)
        except TypeError, exception:
            exception.message = "Column index must be an integer"
            raise exception
        if column >= limit:
            raise IndexError("Column index is out-of-range", {"raisingObject": self, "index": column})
        return column
