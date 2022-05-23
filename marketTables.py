#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti


class RowInfo:
    def __init__(self):
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = False

    def reset(self, exist=False):
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = exist


class Table:
    def __init__(self):
        self.Cell = []
        self.RowInfo = [{}]
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.widthAllowance = 28 - 7
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0
        self.MERGE_MARKER = "MERGE"
        self.SECTION_MARKER = "ENDSECTION"

    def clearMeasurements(self):
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.widthAllowance = 28 - 7
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0

    def clearRowInfo(self):
        self.RowInfo = [{}]

    def build(self, valuesList):
        self.fillCells(valuesList)
        self.measureDimensions()

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

    def measureDimensions(self):
        self.clearMeasurements()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            leftValueLength = len(self.Cell[row][0])
            rightValueLength = len(self.Cell[row][1])

            if self.Cell[row][left] == self.SECTION_MARKER:
                if leftValueLength > self.widestLeftColumn:
                    self.widestLeftColumn = leftValueLength
                if rightValueLength > self.widestRightColumn:
                    if self.Cell[row][right] != self.MERGE_MARKER:
                        self.widestRightColumn = rightValueLength
                if self.widthAllowance < (leftValueLength + rightValueLength):
                    self.widestRow = leftValueLength + rightValueLength
                    self.WrapsForRow.append(row)
                    self.numRowsWrapped = self.numRowsWrapped + 1
                else:
                    self.WrapsForRow.append(0)

        if self.numRowsWrapped > 0:
            self.DoesWrap = True

    def updateRowInfo(self):
        self.clearRowInfo()
        left = 0
        right = 1

        for row in self.Cell:
            merge = (self.Cell[row][right] == self.MERGE_MARKER)
            sectionEnd = (self.Cell[row][left] == self.SECTION_MARKER)

            self.RowInfo.append({self.MERGE_MARKER: merge, self.SECTION_MARKER: sectionEnd})


def PrintTable(table):
    mergeCell = "MERGE"
    sectionEnd = "ENDSECTION"

    columnWidths = measureWidths(table)

    previousRow = RowInfo()
    currentRow = RowInfo()
    nextRow = RowInfo()
    postSectionEndRow = RowInfo()

    for i in range(len(table)):
        previousRow.reset()
        currentRow.reset(True)
        nextRow.reset()
        postSectionEndRow.reset()

        if i > 0:
            previousRow.DoesExist = True
            if table[i - 1][1] == mergeCell:
                previousRow.IsMerge = True
            elif table[i - 1][1] == sectionEnd:
                previousRow.IsSectionEnd = True

        if table[i][1] == mergeCell:
            currentRow.IsMerge = True
        elif table[i][1] == sectionEnd:
            currentRow.IsSectionEnd = True

        if i < (len(table) - 1):
            nextRow.DoesExist = True
            if table[i + 1][1] == mergeCell:
                nextRow.IsMerge = True
            elif table[i + 1][1] == sectionEnd:
                nextRow.IsSectionEnd = True
                if i < (len(table) - 2):
                    postSectionEndRow.DoesExist = True
                    if table[i + 2][1] == mergeCell:
                        postSectionEndRow.IsMerge = True

        currentCellValues = table[i]
        PrintRow(currentCellValues, columnWidths, previousRow, currentRow, nextRow, postSectionEndRow)


def PrintRow(cells, widths, previous, current, nextRow, nextSectionHead):
    if not current.IsSectionEnd:
        left = 0
        right = 1
        IsWrapText = 3
        rowWraps = 4

        #  Default is same as for NOT IsMerge
        middleLeftEdge = "║ "
        middleRightEdge = " ║\n"
        middleSeparator = '│'

        #  Default is same set as DoesExist && NOT IsMerge && NOT IsSectionEnd
        nextSeparator = '┼'
        nextLine = '─'
        nextLeftEdge = '╟'
        nextRightEdge = "╢\n"

        # Print Top Border
        if not previous.DoesExist:
            prevLeftCorner = '╔'
            prevRightCorner = "╗\n"
            prevLine = '═'
            prevSeparator = '╤'

            if current.IsMerge:
                prevSeparator = prevLine

            print(prevLeftCorner.ljust(widths[left] + 3, prevLine), end=prevSeparator)
            print("".ljust(widths[right] + 2, prevLine), end=prevRightCorner)

        #  Print cell values
        if current.DoesExist and (not current.IsSectionEnd):
            if current.IsMerge:
                print(middleLeftEdge + "%s" % (cells[left]).center(widths[left] + widths[right] + 3),
                      end=middleRightEdge)
            else:
                print(middleLeftEdge + "%s %s %s" % (
                    cells[left].center(widths[left]), middleSeparator, cells[right].center(widths[right])),
                    end=middleRightEdge)

        # Print next Line
        if not nextRow.DoesExist:
            nextLeftEdge = '╚'
            nextRightEdge = "╝\n"
            nextLine = '═'
            if current.IsMerge:
                nextSeparator = nextLine
            else:
                nextSeparator = '╧'

        elif nextRow.IsSectionEnd or previous.IsSectionEnd or (not previous.DoesExist):
            nextLine = '═'
            nextLeftEdge = '╠'
            nextRightEdge = "╣\n"

            if previous.IsSectionEnd or (not previous.DoesExist):
                if current.IsMerge:
                    if nextRow.IsMerge:
                        nextSeparator = nextLine
                    else:
                        nextSeparator = '╤'
                else:
                    if nextRow.IsMerge:
                        nextSeparator = '╧'
                    else:
                        nextSeparator = '╪'

            elif nextSectionHead.DoesExist:
                if current.IsMerge:
                    if nextSectionHead.IsMerge:
                        nextSeparator = nextLine
                    else:
                        nextSeparator = '╤'
                else:
                    if nextSectionHead.IsMerge:
                        nextSeparator = '╧'
                    else:
                        nextSeparator = '╪'

        else:  # Happy path
            if current.IsMerge:
                if nextRow.IsMerge:
                    nextSeparator = nextLine
                else:
                    nextSeparator = '┬'
            else:
                if nextRow.IsMerge:
                    nextSeparator = '┴'

        print(nextLeftEdge.ljust(widths[left] + 3, nextLine), end=nextSeparator)
        print("".ljust(widths[right] + 2, nextLine), end=nextRightEdge)


def PrintCells(leftEdge, rightEdge, leftCell, rightCell, separator, merge, widths):
    left = 0
    right = 1
    IsWrapText = 3
    rowWraps = 4

    if rowWraps < 1:
        if merge:
            print(leftEdge + "%s" % leftCell.center(widths[left] + widths[right] + 3), end=rightEdge)
        else:
            print(leftEdge + "%s %s %s" % (
                leftCell.center(widths[left]), separator, rightCell.center(widths[right])), end=rightEdge)


def MakeTable(table):
    print("```")
    table = GetCellValues(table)
    PrintTable(table)
    print("```")


def main():
    TABLE_TITLES_DEFAULTS = ["Magic Items", "Spell Scrolls", "Special Materials"]
    NUM_TABLES_DEFAULT = 3
    DELIMITER_STRING = 'ENDTABLE\n'
    IsCustomTables = True
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text

    print("Please read the instructions to the left before typing.\n")

    userInput = input("Use only defaults? y/n: ")
    if userInput != 'n':
        IsCustomTables = False

    userFile = FILENAME_DEFAULT
    if IsCustomTables:
        print("\nWhen entering a file name, include the file extension (\".txt\").")
        print("Only enter the file name, do not add anything else.")
        userInput = input("(Enter 'x' for default '%s') Enter file name: " % FILENAME_DEFAULT)
        if userInput != 'x':
            userFile = userInput

    # Open file and save contents in a list
    try:
        inputFile = open(userFile)
        isFileOpen = True
    except OSError:
        print("\nError: No input file uploaded.")
        isFileOpen = False

    if isFileOpen:
        inputColumn = inputFile.readlines()
        inputFile.close()

        numTables = NUM_TABLES_DEFAULT
        if IsCustomTables:
            userInput = input("(Enter 'x' for default '%d') Enter number of tables to be made: " % NUM_TABLES_DEFAULT)
            if userInput != 'x':
                numTables = int(userInput)

        if numTables > 1:
            for i in range(numTables):

                tableTitle = TABLE_TITLES_DEFAULTS[i]
                if IsCustomTables:
                    userInput = input("(Enter 'x' for default '%s') Enter table title: " % TABLE_TITLES_DEFAULTS[i])
                    if userInput != 'x':
                        tableTitle = userInput

                if inputColumn.count(DELIMITER_STRING) > 0:
                    IndexOfDelimiter = inputColumn.index(DELIMITER_STRING)
                    tableItems = inputColumn[0:IndexOfDelimiter]
                    inputColumn = inputColumn[(IndexOfDelimiter + 1):]
                else:
                    tableItems = inputColumn

                print("**%s**" % tableTitle)
                MakeTable(tableItems)

        else:
            userInput = input("(Enter 'x' for default '%s') Enter table title: " % TABLE_TITLES_DEFAULTS[0])
            if userInput != 'x':
                tableTitle = TABLE_TITLES_DEFAULTS[0]
            else:
                tableTitle = userInput

            print("**%s**" % tableTitle)
            MakeTable(inputColumn)
    else:
        print("Please upload a file and run again")

    print("\n\nTables Complete.")
main()
