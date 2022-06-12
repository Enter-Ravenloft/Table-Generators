#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti
from Table import *
from time import *

class RowInfo:
    def __init__(self):
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = False

    def reset(self, exist=False):
        self.IsSectionEnd = False
        self.IsMerge = False
        self.DoesExist = exist


def PrintTable(table):
    mergeCell = "MERGE"
    sectionEnd = "ENDSECTION"

    ## columnWidths = measureWidths(table)

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
        PrintRow(currentCellValues, '''columnWidths''', previousRow, currentRow, nextRow, postSectionEndRow)


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


def addDaysToPOSIX(add_days=1, to_hour=-1, day_cycle=-1,  cycle_start=0):
    NANOSECONDS_PER_SECOND = 1000000000
    SECONDS_PER_HOUR = 60 * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24

    currentTimeInPOSIX = time_ns() // NANOSECONDS_PER_SECOND
    secondsElapsedToday = currentTimeInPOSIX % SECONDS_PER_DAY

    currentTimeInPOSIX = currentTimeInPOSIX - secondsElapsedToday

    if day_cycle >= 0:
        cycleOffset = (currentTimeInPOSIX - cycle_start) % (day_cycle * SECONDS_PER_DAY)
        futureTimeInPOSIX = currentTimeInPOSIX - cycleOffset

    futureTimeInPOSIX = futureTimeInPOSIX + (add_days * SECONDS_PER_DAY)

    if to_hour >= 0:
        futureTimeInPOSIX = futureTimeInPOSIX + (to_hour * SECONDS_PER_HOUR)

    return futureTimeInPOSIX


def main():
    TABLE_TITLES_DEFAULTS = ["Magic Items", "Spell Scrolls", "Special Materials"]
    NUM_TABLES_DEFAULT = 3
    DELIMITER_STRING = 'ENDTABLE\n'
    IsCustomTables = True
    MARKET_CYCLE_START_POSIX = 1654988400
    UNIX_TIME_TO_ADD = 259200
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text

    print("Please read the instructions to the left before typing.\n")

    userInput = input("Make default Vistani Market tables? y/n: ")
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
        unprocessedTableInput = inputFile.readlines()
        inputFile.close()

        closingPlayersTag = "@Players the market closes <t:"
        endOfCLosingPlayersTag = ":R>."
        unixTimeStamp = int(input("Enter the previous unix time stamp or 0 to skip: "))
        if unixTimeStamp != 0:
            unixTimeStamp = unixTimeStamp + UNIX_TIME_TO_ADD
            closingPlayersTag = closingPlayersTag + str(unixTimeStamp) + endOfCLosingPlayersTag
        else:
            threeDaysFromNow = str(addDaysToPOSIX(3, 23, 3, MARKET_CYCLE_START_POSIX))
            closingPlayersTag = closingPlayersTag + threeDaysFromNow + endOfCLosingPlayersTag

        numTables = NUM_TABLES_DEFAULT
        if IsCustomTables:
            userInput = input("(Enter 'x' for default '%d') Enter number of tables to be made: " % NUM_TABLES_DEFAULT)
            if userInput != 'x':
                numTables = int(userInput)

        else:
            print("__**Vistani Market**__\n")

        if numTables > 1:
            for i in range(numTables):

                tableTitle = TABLE_TITLES_DEFAULTS[i]
                if IsCustomTables:
                    userInput = input("(Enter 'x' for default '%s') Enter table title: " % TABLE_TITLES_DEFAULTS[i])
                    if userInput != 'x':
                        tableTitle = userInput

                if unprocessedTableInput.count(DELIMITER_STRING) > 0:
                    IndexOfDelimiter = unprocessedTableInput.index(DELIMITER_STRING)
                    tableItems = unprocessedTableInput[0:IndexOfDelimiter]
                    unprocessedTableInput = unprocessedTableInput[(IndexOfDelimiter + 1):]
                else:
                    tableItems = unprocessedTableInput

                print("**%s**" % tableTitle)
                marketTable = Table()
                marketTable.build(tableItems)
                marketTable.printUnicodeTable()

        else:
            userInput = input("(Enter 'x' for default '%s') Enter table title: " % TABLE_TITLES_DEFAULTS[0])
            if userInput != 'x':
                tableTitle = TABLE_TITLES_DEFAULTS[0]
            else:
                tableTitle = userInput

            print("**%s**" % tableTitle)
            marketTable = Table()
            marketTable.build(unprocessedTableInput)
            marketTable.printUnicodeTable()

        print(closingPlayersTag)

    else:
        print("Please upload a file and run again")

    print("\n\nTables Complete.")


main()
