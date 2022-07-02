from math import *

class CopyOfTable:
    def __init__(self, valuesList=[], text_wrapping=False, max_width=-1):
        self.Cell = []
        self.RowInfo = []
        self.WrapSheet = []
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.TOTAL_WIDTH_MINIMUM = 28  # Originally 28 -7 based on feedback from cellphone users.
        self.NON_CONTENT_WIDTH = 7
        if max_width < self.TOTAL_WIDTH_MINIMUM:
            self.widthAllowance = max_width - self.NON_CONTENT_WIDTH
        else:
            self.widthAllowance = self.TOTAL_WIDTH_MINIMUM
        self.PerformWrapping = text_wrapping
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0
        self.MERGE_MARKER = "MERGE"
        self.SECTION_MARKER = "ENDSECTION"
        self.COMBINE_ROW_MARKER = "SAMELINE"
        self.BoxChars = {"Left":
                             {"Corner":
                                  {"Top":
                                       {"single": '┌',
                                        "double": '╔'},
                                   "Bottom":
                                       {"single": '└',
                                        "double": '╚'}},
                              "Vertical":
                                  {"single":
                                       {"intersect":
                                            {"single": '├',
                                             "double": '╞'},
                                        "straight": '│'},
                                   "double":
                                       {"intersect":
                                            {"single": '╟',
                                             "double": '╠'},
                                        "straight": '║'}},
                              },
                         "Horizontal":
                             {"single":
                                  {"intersect":
                                       {"down":
                                            {"single": '┬',
                                             "double": '╥'},
                                        "through":
                                            {"single": '┼',
                                             "double": '╫'},
                                        "up":
                                            {"single": '┴',
                                             "double": '╨'}},
                                   "straight": '─'},
                              "double":
                                  {"intersect":
                                       {"down":
                                            {"single": '╤',
                                             "double": '╦'},
                                        "through":
                                            {"single": '╪',
                                             "double": '╬'},
                                        "up":
                                            {"single": '╧',
                                             "double": '╩'}},
                                   "straight": '═'}
                              },
                         "Right":
                             {"Corner":
                                  {"Top":
                                       {"single": '┐',
                                        "double": '╗'},
                                   "Bottom":
                                       {"single": '┘',
                                        "double": '╝'}},
                              "Vertical":
                                  {"single":
                                       {"intersect":
                                            {"single": '┤',
                                             "double": '╡'},
                                        "straight": '│'},
                                   "double":
                                       {"intersect":
                                            {"single": '╢',
                                             "double": '╣'},
                                        "straight": '║'}},
                              }
                         }
        self.TESTING = [["content", "wraps", "length", "satisfier"]]
        if len(valuesList) > 0:
            self.build(valuesList)

    def clearMeasurements(self):
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0

    def clearRowInfo(self):
        self.RowInfo = []

    def getWrapItemNumber(self, wrap):
        itemNumber = -1
        for namedItem in range(len(self.WrapSheet)):
            for rowAddress in range(len(self.WrapSheet[namedItem])):
                if self.WrapSheet[namedItem][rowAddress] == wrap:
                    itemNumber = namedItem
                    break
        return itemNumber

    def refreshWrapSheet(self):
        stepCount = 0
        for namedItem in range(len(self.WrapSheet)):
            for rowAddress in range(len(self.WrapSheet[namedItem])):
                self.WrapSheet[namedItem][rowAddress] = stepCount
                stepCount += 1

    def addWraps(self, item, wraps):
        for address in range(wraps):
            self.WrapSheet[item].append([address])
        self.refreshWrapSheet()

    def wrapCell(self, row, column, row_max_length):
        text = self.Cell[row][column]
        if column == 0:
            oppositeCell = 1
        else:
            oppositeCell = 0

        newCells = self.Cell[row]
        if row_max_length > (len(text) + len(newCells[oppositeCell])):
            return newCells

        solutionFound = False
        attempts = 0
        while not solutionFound:
            if self.Cell[row][oppositeCell] != self.MERGE_MARKER:
                if len(self.Cell[row][oppositeCell]) > 0:
                    oppositeText = self.Cell[row][oppositeCell]
                else:
                    rowsForItem = self.WrapSheet[self.getWrapItemNumber(row)]
                    if len(rowsForItem) > 1:
                        oppositeText = self.Cell[rowsForItem[0]][oppositeCell]
                    else:
                        oppositeText = self.Cell[row][oppositeCell]
            else:
                oppositeText = ""

            if len(oppositeText) < (row_max_length / 2):
                maxTextLength = row_max_length - len(oppositeText)
            else:
                maxTextLength = row_max_length / 2

            numRowsNeeded = ceil(len(text) / maxTextLength)
            wrapPoints = []

            if (text.count('(') == 1) and (text.count(')') == 1):
                parentheticalText = text[text.find('('):text.rfind(')')]
                if maxTextLength >= (len(text) - len(parentheticalText)):
                    solutionFound = True
                    wrapPoints.append(text.find('(') - 1)

            numSpaces = text.count(' ')
            if not solutionFound and (numSpaces > 0) and not text.isspace():
                if numSpaces >= (1 - numRowsNeeded):
                    indicesOfSpaces = []
                    indicesOfSpaces.append(text.rfind(' '))
                    unsearchedText = text
                    for i in range(numSpaces - 1):
                        unsearchedText = unsearchedText[: indicesOfSpaces[0]]
                        indicesOfSpaces.insert(0, unsearchedText.rfind(' '))
                    breakPoint = ceil(len(text) / numRowsNeeded)
                    remainingIndices = indicesOfSpaces
                    for j in range(numRowsNeeded):
                        if len(remainingIndices) > 0:
                            if j > 0:
                                breakPoint = wrapPoints[-1] + maxTextLength
                                charsRemaining = len(text[wrapPoints[-1]:])
                                if charsRemaining < (2 * maxTextLength):
                                    if charsRemaining < maxTextLength:
                                        break
                                    else:
                                        breakPoint = wrapPoints[-1] + ceil(charsRemaining / 2)
                            minimumDistance = len(text)
                            previousMinimum = minimumDistance
                            closestIndex = 0
                            for index in remainingIndices:
                                distance = abs(breakPoint - index)
                                if distance < minimumDistance:
                                    previousMinimum = minimumDistance
                                    minimumDistance = distance
                                    closestIndex = index
                                elif distance > previousMinimum:
                                    break

                            wrapPoints.append(closestIndex)
                            indexOfIndex = 1 + indicesOfSpaces.index(closestIndex)
                            remainingIndices = indicesOfSpaces[indexOfIndex:]

                    solutionFound = True

            if not solutionFound:
                break

        if solutionFound:
            newCells = []
            newCells.append(text[:wrapPoints[0]])
            numBreaks = len(wrapPoints)
            for k in range(numBreaks):
                if (k > 0) and (k < len(wrapPoints)):
                    if k == 1:
                        startIndex = wrapPoints[0]
                        endIndex = wrapPoints[k]
                    elif k >= (len(wrapPoints) - 1):
                        startIndex = wrapPoints[k - 1]
                        endIndex = wrapPoints[-1]
                    else:
                        startIndex = wrapPoints[k - 1]
                        endIndex = wrapPoints[k]
                    startIndex = startIndex + 1
                    newCells.append(text[startIndex:endIndex])
            newCells.append(text[(wrapPoints[-1] + 1):])

        return newCells

    def testingGetWrapContent(self):
        content = []
        for i in self.WrapsForRow:
            content.append(self.Cell[i])

        return content

    def wrapTable(self, max_length= -1):
        if self.DoesWrap:
            if max_length < 1:
                max_length = self.widthAllowance


            count = 0
            contentToBeWrapped = self.testingGetWrapContent()
            while (len(self.WrapsForRow) > 0) and (count <= len(self.WrapSheet)):
                count = count + 1
                row = self.WrapsForRow[-1]
                for line in self.WrapsForRow:
                    wrapCount = len(self.WrapSheet[self.getWrapItemNumber(line)])
                    if wrapCount == 1:
                        row = line
                        break

                if len(self.Cell[row][0]) > len(self.Cell[row][1]):
                    smallerCell = 1
                    largerCell = 0
                else:
                    smallerCell = 0
                    largerCell = 1

                itemNumber = self.getWrapItemNumber(row)
                rowWidth = len(self.Cell[row][0]) + len(self.Cell[row][1])
                wraps = self.WrapSheet[itemNumber]
                if (1 < len(wraps)) and (rowWidth < ceil(1.2 * max_length)):
                    content = self.Cell[row][largerCell]
                    wraps = len(self.WrapSheet[itemNumber])
                    length = len(self.Cell[row][largerCell])
                    satisfier = ceil(1.25 * max_length)
                    self.TESTING.append([content, wraps, length, satisfier])
                    break

                newCells = self.wrapCell(row, largerCell, max_length)
                if newCells[0] != 0:
                    self.addWraps(itemNumber, len(newCells))

                    if self.RowInfo[row][self.MERGE_MARKER]:
                        matchingCells = [self.MERGE_MARKER] * len(newCells)
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.MERGE_MARKER]
                    else:
                        matchingCells = [" "] * (len(newCells) - 1)
                        matchingCells.insert(0, self.Cell[row][smallerCell])
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.COMBINE_ROW_MARKER]
                    self.Cell.pop(row)
                    for i in range(len(newCells)):
                        if smallerCell == 1:
                            newRow = [newCells[i], matchingCells[i]]
                        else:
                            newRow = [matchingCells[i], newCells[i]]

                        if i == 0:
                            self.Cell.insert(row, newRow)
                        else:
                            self.Cell.insert(sameLineIndex + 1, newRow)
                        if i < (len(newCells) - 1):
                            newRowIndex = self.Cell.index(newRow)
                            self.Cell.insert(newRowIndex + 1, sameLineMarkers)
                            sameLineIndex = self.Cell.index(sameLineMarkers, newRowIndex)

                self.getRowTraits()
                self.measureDimensions()
                contentToBeWrapped = self.testingGetWrapContent()
            self.TESTING.append("Loops: " + str(count))

    def build(self, valuesList):
        self.fillCells(valuesList)
        self.measureDimensions()
        self.getRowTraits()
        for i in range(len(self.Cell)):
            self.WrapSheet.append([i])
        self.refreshWrapSheet()

        if self.PerformWrapping and self.DoesWrap:
            self.wrapTable()

    def fillCells(self, valuesList):
        self.Cell = []

        # Iterate over every line
        for i in range(len(valuesList) // 2):
            i = i * 2
            j = i + 1
            leftColumn = valuesList[i].rstrip()
            leftColumn = leftColumn.strip('"')
            rightColumn = valuesList[j].rstrip()
            rightColumn = rightColumn.strip('"')
            self.Cell.append([leftColumn, rightColumn])

    def checkToWrap(self, row):
        left = 0
        right = 1
        leftValueLength = len(self.Cell[row][left])
        rightValueLength = len(self.Cell[row][right])
        if self.Cell[row][right] == self.MERGE_MARKER:
            rightValueLength = 0

        if (self.Cell[row][left] != self.SECTION_MARKER) and (self.Cell[row][left] != self.COMBINE_ROW_MARKER):
            if leftValueLength > self.widestLeftColumn:
                self.widestLeftColumn = leftValueLength
            if rightValueLength > self.widestRightColumn:
                self.widestRightColumn = rightValueLength

    def measureDimensions(self):
        self.clearMeasurements()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            leftValueLength = len(self.Cell[row][left])
            rightValueLength = len(self.Cell[row][right])
            if self.Cell[row][right] == self.MERGE_MARKER:
                rightValueLength = 0

            if (self.Cell[row][left] != self.SECTION_MARKER) and (self.Cell[row][left] != self.COMBINE_ROW_MARKER):
                if leftValueLength > self.widestLeftColumn:
                    self.widestLeftColumn = leftValueLength
                if rightValueLength > self.widestRightColumn:
                    self.widestRightColumn = rightValueLength

                if self.widthAllowance < (leftValueLength + rightValueLength):
                    self.widestRow = leftValueLength + rightValueLength
                    self.WrapsForRow.append(row)
                    self.numRowsWrapped = self.numRowsWrapped + 1

        if self.numRowsWrapped > 0:
            self.DoesWrap = True

    def getRowTraits(self):
        self.clearRowInfo()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            if self.Cell[row][right] == self.MERGE_MARKER:
                merge = True
            else:
                merge = False

            if self.Cell[row][left] == self.SECTION_MARKER:
                sectionEnd = True
            else:
                sectionEnd = False

            if self.Cell[row][left] == self.COMBINE_ROW_MARKER:
                combine = True
            else:
                combine = False

            self.RowInfo.append({self.MERGE_MARKER: merge, self.SECTION_MARKER: sectionEnd, self.COMBINE_ROW_MARKER: combine})

    def getBoxCharsForRow(self, row):
        merged = self.MERGE_MARKER
        nextMerged = "Next Merged"
        sectionHead = "Section Head"
        tableHead = "Table Head"
        sectionFoot = "Section Foot"
        tableFoot = "Table Foot"
        prevMerged = "Previous Merged"
        sectionMarker = self.SECTION_MARKER
        setOfTraits = [merged, nextMerged, sectionHead, tableHead, sectionMarker, sectionFoot, sectionMarker,
                       prevMerged]

        traits = dict()
        for key in setOfTraits:
            traits[key] = False

        if self.RowInfo[row][merged]:
            traits[merged] = True
        if self.RowInfo[row][sectionMarker]:
            traits[sectionMarker] = True

        if row == 0:
            traits[tableHead] = True
        elif row == len(self.RowInfo):
            traits[tableFoot] = True
        elif self.RowInfo[row - 1][sectionMarker]:
            traits[sectionHead] = True

        # Process information on next printable row
        else:
            if self.RowInfo[row + 1][sectionMarker]:
                traits[sectionFoot] = True
                # If row is a sectionFoot then need to check row after the section marker row
                if row < len(self.RowInfo):
                    if self.RowInfo[row + 2][merged]:
                        traits[nextMerged] = True
            else:
                if self.RowInfo[row + 1][merged]:
                    traits[nextMerged] = True

        nextLine = []

        # Left edge and fill line
        if traits[sectionFoot] or traits[sectionHead] or traits[tableHead]:  # Next line is double
            isDoubleLine = True
            nextLine.append(self.BoxChars["Left"]["Vertical"]["double"]["intersect"]["double"])
            nextLine.append(self.BoxChars["Horizontal"]["double"]["straight"])
            nextLine.append(self.BoxChars["Right"]["Vertical"]["double"]["intersect"]["double"])
        else:  # Next line is single
            isDoubleLine = False
            nextLine.append(self.BoxChars["Left"]["Vertical"]["double"]["intersect"]["single"])
            nextLine.append(self.BoxChars["Horizontal"]["single"]["straight"])
            nextLine.append(self.BoxChars["Right"]["Vertical"]["double"]["intersect"]["single"])

        # Separator
        if traits[merged]:  # Top is flat
            if traits[nextMerged]:  # bottom flat, all flat
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["straight"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["straight"])
            else:  # points down
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["down"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["down"]["single"])
        else:  # Points up
            if traits[nextMerged]:  # bottom is flat
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["up"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["up"]["single"])
            else:  # Points down as well
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["through"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["through"]["single"])

        return nextLine

    def printUnicodeTable(self):
        self.getRowTraits()
        self.measureDimensions()
        print("```")

        left = 0
        right = 1
        widthLeft = self.widestLeftColumn
        widthRight = self.widestRightColumn

        for i in range(len(self.RowInfo)):

            if i == 0:  # Print Table Header
                lineFill = self.BoxChars["Horizontal"]["double"]["straight"]
                if self.RowInfo[i][self.MERGE_MARKER]:
                    separator = lineFill
                else:
                    separator = self.BoxChars["Horizontal"]["double"]["intersect"]["down"]["single"]

                print(self.BoxChars["Left"]["Corner"]["Top"]["double"].ljust(widthLeft + 3, lineFill), end=separator)
                print("".rjust(widthRight + 2, lineFill),
                      end=(self.BoxChars["Right"]["Corner"]["Top"]["double"] + '\n'))

            edgeLeft = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            edgeLeft = edgeLeft + ' '
            separator = self.BoxChars["Left"]["Vertical"]["single"]["straight"]
            edgeRight = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            edgeRight = ' ' + edgeRight + '\n'

            if (not self.RowInfo[i][self.COMBINE_ROW_MARKER]) and (self.Cell[i][left] != self.SECTION_MARKER):

                if self.RowInfo[i][self.MERGE_MARKER]:
                    print(edgeLeft + "%s" % self.Cell[i][left].center(widthLeft + widthRight + 3), end=edgeRight)
                else:
                    print(edgeLeft + "%s %s %s" % (self.Cell[i][left].center(widthLeft), separator,
                                                   self.Cell[i][right].center(widthRight)), end=edgeRight)

                # Print Table Footer
                if i == (len(self.RowInfo) - 1):
                    lineFill = self.BoxChars["Horizontal"]["double"]["straight"]
                    if self.RowInfo[i][self.MERGE_MARKER]:
                        separator = lineFill
                    else:
                        separator = self.BoxChars["Horizontal"]["double"]["intersect"]["up"]["single"]
                    print(self.BoxChars["Left"]["Corner"]["Bottom"]["double"].ljust(widthLeft + 3, lineFill),
                          end=separator)
                    print("".rjust(widthRight + 2, lineFill),
                          end=(self.BoxChars["Right"]["Corner"]["Bottom"]["double"] + '\n'))

                elif not self.RowInfo[i + 1][self.COMBINE_ROW_MARKER]:  # Print bottom line of row
                    characters = self.getBoxCharsForRow(i)
                    edgeLeft = characters[0]
                    lineFill = characters[1]
                    edgeRight = characters[2] + '\n'
                    separator = characters[3]

                    print(edgeLeft.ljust(widthLeft + 3, lineFill), end=separator)
                    print("".rjust(widthRight + 2, lineFill), end=edgeRight)

        print("```")
        for i in self.TESTING:
            print(i)

        self.widestRow = self.widestLeftColumn + self.widestRightColumn + self.NON_CONTENT_WIDTH
        print(self.widestRow)
        print('\n')

