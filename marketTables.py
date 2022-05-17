
class RowInfo:
    def __init__(self):
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = False

    def reset(self, exist=False):
        """

        :type exist: bool
        """
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = exist


def GetCellValues(cellList):
    cellValues = []

    # Iterate over every line
    for i in range(len(cellList) // 2):
        i = i * 2
        j = i + 1
        leftColumn = cellList[i].rstrip()
        leftColumn = leftColumn.strip('"')
        rightColumn = cellList[j].rstrip()
        rightColumn = rightColumn.strip('"')
        cellValues.append([leftColumn, rightColumn])

    return cellValues


def GetColumnWidths(table):
    maxLeft = 0
    maxRight = 0

    row = 0
    for row in range(len(table)):
        if (len(table[row][0]) > maxLeft):
            maxLeft = len(table[row][0])
        if (len(table[row][1]) > maxRight):
            maxRight = len(table[row][1])

    return [maxLeft, maxRight]


def PrintTable(table):
    mergeCell = "MERGE"
    sectionEnd = "ENDSECTION"

    columnWidths = GetColumnWidths(table)

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
                print(middleLeftEdge + "%s" % (cells[left]).center(widths[left] + widths[right] + 3), end= middleRightEdge)
            else:
                print(middleLeftEdge + "%s" % (cells[left]).center(widths[left] + 1), end=middleSeparator)
                print(" %s" % (cells[right]).center(widths[right]), end=middleRightEdge)

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
    FILENAME_DEFAULT = 'market.csv'  # Must be UTF-8 text

    userInput = input("Use only defaults? y/n: ")
    if userInput != 'n':
        IsCustomTables = False

    userFile = FILENAME_DEFAULT
    if IsCustomTables:
        userInput = input("Hit x or Enter file name with full path: ")
        if userInput != 'x':
            userFile = userInput

    # Open file and save contents in a list
    inputFile = open(userFile)
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


main()


