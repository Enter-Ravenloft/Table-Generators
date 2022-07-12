from math import *
from textwrap import wrap
from time import *
from RandItems_OLDFORMAT import *

words = "Common Items\nMERGE\nImbued Wood Focus\n75 gp\nHorn of Silent Alarm\n85 gp\nVeteran's Cane\n50 " \
        "gp\nENDSECTION\nENDSECTION\nUncommon Items\nMERGE\nRing of Truth Telling\n350 gp\nArcane Whip Tip (Fire)\n50 " \
        "gp\nENDSECTION\nENDSECTION\nRare  Items\nMERGE\nLyre of Building\n4,750 gp\nENDTABLE\nCantrip: gp\n1st: " \
        "25gp\nMold earth\nCause Fear\nThorn Whip\nIllusory Script\nSword Burst\nShield of " \
        "Faith\nENDSECTION\nENDSECTION\n2nd: 150gp\n3rd: 400gp\nMisty Step\nCreate Food and Water\nPass Without " \
        "Trace\nEnemies Abound\nMirror Image\nConjure Barrage\nENDTABLE\nCloth\nOrganic\nShadowfell Linen\nPlague " \
        "Wood\nSAMELINE\nSAMELINE\n750gp\n250gp\nENDSECTION\nENDSECTION\nMetal\nMineral\nCold " \
        "Iron\nObsidian\nSAMELINE\nSAMELINE\n100gp\n100gp "

MANUAL_INPUT = words.split('\n')
MANUAL_INPUT = getVistaniItems()


def longestWord(text):
    if len(text) == 0:
        return "0"
    wordList = text.split()
    longest = max(wordList, key=len)
    return longest


def simpleWrap(text, width, whole_words=False):
    return wrap(text, width, break_long_words=whole_words)


def loosestWrap(text, width):
    minimum = len(longestWord(text))
    for i in range(len(text)):
        wrapCap = ceil(len(text) / (i + 2))
        if wrapCap < minimum:
            return 0
        results = simpleWrap(text, wrapCap)
        longestLine = 0
        for line in results:
            if longestLine < len(line):
                longestLine = len(line)
        if longestLine <= width:
            return wrapCap


def evenWrap(text, width):
    wrapCap = loosestWrap(text, width)
    if wrapCap > 0:
        return simpleWrap(text, wrapCap)
    else:
        return [text]


def shortestWrap(text, width):
    even = evenWrap(text, width)
    simple = simpleWrap(text, width)
    if (len(simple) < len(even)) or (even[0] == text):
        return simple
    else:
        return even


class Table:
    def __init__(self, valuesList=[], text_wrapping=False, max_width=-1):
        self.Cell = []
        self.RowInfo = []
        self.WrapSheet = []
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.TOTAL_WIDTH_MINIMUM = 28  # Originally 28 -7 based on feedback from cellphone users.
        self.NON_CONTENT_WIDTH = 7
        self.userWidth = max_width
        if self.userWidth > self.TOTAL_WIDTH_MINIMUM:
            self.widthAllowance = self.userWidth
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
        if len(valuesList) > 0:
            self.build(valuesList)

    def clearMeasurements(self):
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        if self.userWidth > self.TOTAL_WIDTH_MINIMUM:
            self.widthAllowance = self.userWidth
        else:
            self.widthAllowance = self.TOTAL_WIDTH_MINIMUM
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

    def columZipper(self, left_column, right_column):
        if len(left_column) > len(right_column):
            greaterColumn = left_column
            lesserColumn = right_column
            GreaterIsLeftmost = True
        else:
            greaterColumn = right_column
            lesserColumn = left_column
            GreaterIsLeftmost = False

        if len(lesserColumn) == 0:
            filler = self.MERGE_MARKER
        else:
            filler = " "
        for i in range(len(greaterColumn) - len(lesserColumn)):
            lesserColumn.append(filler)

        joinedColumns = []
        if len(greaterColumn) == len(lesserColumn):
            for j in range(len(greaterColumn)):
                if GreaterIsLeftmost:
                    joinedColumns.append([greaterColumn[j], lesserColumn[j]])
                else:
                    joinedColumns.append([lesserColumn[j], greaterColumn[j]])

        return joinedColumns

    def wrapTable(self, max_length=-1):
        if self.DoesWrap:
            if max_length < 1:
                max_length = self.widthAllowance - self.NON_CONTENT_WIDTH

            itemsToWrap = []
            for i in range(len(self.WrapSheet)):
                content = self.Cell[i][0]
                if not ((content == self.COMBINE_ROW_MARKER) or (content == self.SECTION_MARKER)):
                    itemsToWrap.append(self.WrapSheet[i])
            itemsToWrap.reverse()
            for item in itemsToWrap:
                row = item[0]

                if len(self.Cell[row][0]) > len(self.Cell[row][1]):
                    smallerCell = 1
                    largerCell = 0
                    isLargerLeftmost = True
                else:
                    smallerCell = 0
                    largerCell = 1
                    isLargerLeftmost = False

                if self.Cell[row][largerCell] != self.MERGE_MARKER:
                    primaryLengthConstraint = max_length - len(self.Cell[row][smallerCell])
                    primaryCells = shortestWrap(self.Cell[row][largerCell], primaryLengthConstraint)

                    secondaryLengthConstraint = 0
                    for cell in primaryCells:
                        if len(cell) > secondaryLengthConstraint:
                            secondaryLengthConstraint = len(cell)

                    smallCellContent = self.Cell[row][smallerCell]
                    if self.Cell[row][smallerCell] != self.MERGE_MARKER:
                        secondaryCells = shortestWrap(self.Cell[row][smallerCell],
                                                      (max_length - secondaryLengthConstraint))
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.MERGE_MARKER]
                    else:
                        secondaryCells = [self.MERGE_MARKER]
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.MERGE_MARKER]

                    if largerCell == 0:
                        newRows = self.columZipper(primaryCells, secondaryCells)
                    else:
                        newRows = self.columZipper(secondaryCells, primaryCells)

                    self.addWraps(self.getWrapItemNumber(row), len(newRows))

                    self.Cell.pop(row)
                    for i in range(len(newRows)):
                        line = newRows[i]
                        if i == 0:
                            self.Cell.insert(row, line)
                        else:
                            self.Cell.insert(previousLineIndex + 1, line)
                        if i < (len(newRows) - 1):
                            newRowIndex = self.Cell.index(line)
                            self.Cell.insert(newRowIndex + 1, sameLineMarkers)
                            previousLineIndex = self.Cell.index(sameLineMarkers, newRowIndex)

                self.getRowTraits()
                self.measureDimensions()

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

                if self.widestRow < (leftValueLength + rightValueLength):
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

            self.RowInfo.append(
                {self.MERGE_MARKER: merge, self.SECTION_MARKER: sectionEnd, self.COMBINE_ROW_MARKER: combine})

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


#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti

def addDaysToPOSIX(add_days=1, to_hour=-1, day_cycle=-1, cycle_start=0, start_day=-1):
    NANOSECONDS_PER_SECOND = 1000000000
    SECONDS_PER_HOUR = 60 * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24

    if start_day < 0:
        currentTimeInPOSIX = time_ns() // NANOSECONDS_PER_SECOND
    else:
        currentTimeInPOSIX = start_day

    secondsAfterMidnight = currentTimeInPOSIX % SECONDS_PER_DAY
    currentTimeInPOSIX = currentTimeInPOSIX - secondsAfterMidnight

    if day_cycle > 0:
        cycleOffset = (currentTimeInPOSIX - cycle_start) % (day_cycle * SECONDS_PER_DAY)
        futureTimeInPOSIX = currentTimeInPOSIX - cycleOffset

    futureTimeInPOSIX = futureTimeInPOSIX + (add_days * SECONDS_PER_DAY)

    if to_hour > 0:
        futureTimeInPOSIX = futureTimeInPOSIX + (to_hour * SECONDS_PER_HOUR)

    return futureTimeInPOSIX


def getInputOrDefault(prompt="Enter input: ", stored_value="DEFAULT", code_for_default='x'):
    userInput = str(input(prompt))
    if userInput != code_for_default:
        stored_value = userInput

    return stored_value


def main():
    TABLE_TITLES_DEFAULTS = ["Magic Items", "Spell Scrolls", "Special Materials"]
    NUM_TABLES_DEFAULT = 3
    DELIMITER_STRING = 'ENDTABLE'
    IsCustomTables = True
    TextWrapping = True
    WRAP_WIDTH_DEFAULT = 29
    MARKET_CYCLE_START_POSIX = 1654387200  # June 5th at 12am UTC
    POSTING_HOUR_DEFAULT = 23  # Vistani Market posting time
    DAYS_IN_CYCLE_DEFAULT = 3  # Vistani Market market cycle length
    DAYS_TO_ADD_DEFAULT = 3  # Number of days in the future for discord time code
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text

    print("Please read the instructions to the left before typing.\n")

    unprocessedUserInput = MANUAL_INPUT
    userInput = 'y'
    if userInput != 'n':
        IsCustomTables = False

    userFile = FILENAME_DEFAULT
    if IsCustomTables:
        prompt = "\nWhen entering a file name, include the file extension (\".txt\").\n"
        prompt = prompt + "Only enter the file name, do not add anything else.\n"
        prompt = prompt + "(Enter 'x' for default '%s') Enter file name: " % FILENAME_DEFAULT
        userFile = getInputOrDefault(prompt, FILENAME_DEFAULT)

    desiredWidth = WRAP_WIDTH_DEFAULT
    if IsCustomTables:
        desiredWidth = int(getInputOrDefault("Enter how wide you want the tables to be in number of characters."
                                             "Enter x for the default: ", WRAP_WIDTH_DEFAULT))

    # Open file and save contents in a list
    """try:
        inputFile = open(userFile)
        isFileOpen = True
    except OSError:
        print("\nError: No input file uploaded.")
        isFileOpen = False"""

    if True:

        closingPlayersTag = "@Players the market closes <t:"
        endOfCLosingPlayersTag = ":R>."

        if IsCustomTables:

            unixTimeToAdjust = int(getInputOrDefault("Enter unix time stamp. Enter x for automatic calculation: ",
                                                     str(-1)))
            daysOpen = int(getInputOrDefault("Enter the number of days until the market will close. "
                                             "Enter x for the default: ", DAYS_TO_ADD_DEFAULT))
            cycleLength = int(getInputOrDefault("Enter the number of days the market is supposed ot be open. "
                                                "Enter x for the default: ", DAYS_IN_CYCLE_DEFAULT))
            hourToPost = int(getInputOrDefault("Enter the hour to post. 1 to 24 and in UTC time. "
                                               "Enter x for the default: ", POSTING_HOUR_DEFAULT))

            unixTimeStamp = addDaysToPOSIX(daysOpen, hourToPost, cycleLength, MARKET_CYCLE_START_POSIX,
                                           unixTimeToAdjust)
            closingPlayersTag = closingPlayersTag + str(unixTimeStamp)

        else:
            unixTimeStamp = addDaysToPOSIX(DAYS_TO_ADD_DEFAULT, POSTING_HOUR_DEFAULT, DAYS_IN_CYCLE_DEFAULT,
                                           MARKET_CYCLE_START_POSIX)
            closingPlayersTag = closingPlayersTag + str(unixTimeStamp)

        closingPlayersTag = closingPlayersTag + endOfCLosingPlayersTag

        numTables = NUM_TABLES_DEFAULT
        if IsCustomTables:
            prompt = "(Enter 'x' for default '%d') Enter number of tables to be made: " % NUM_TABLES_DEFAULT
            numTables = int(getInputOrDefault(prompt, str(NUM_TABLES_DEFAULT)))
        else:
            print("\n\n")
            print("__**Vistani Market**__\n")

        tableTitles = []
        for i in range(numTables):
            if i < len(TABLE_TITLES_DEFAULTS):
                titleDefault = TABLE_TITLES_DEFAULTS[i]
            else:
                titleDefault = "Table %d" % (i + 1)

            if IsCustomTables:
                if i < len(TABLE_TITLES_DEFAULTS):
                    titleDefault = TABLE_TITLES_DEFAULTS[i]
                else:
                    titleDefault = "Table %d" % (i + 1)
                prompt = "(Enter 'x' for default '%s') Enter table title: " % titleDefault
                titleDefault = getInputOrDefault(prompt, titleDefault)

            tableTitles.append(titleDefault)

        unprocessedTableInput = MANUAL_INPUT
        if numTables > 1:
            for i in range(numTables):

                if unprocessedTableInput.count(DELIMITER_STRING) > 0:
                    IndexOfDelimiter = unprocessedTableInput.index(DELIMITER_STRING)
                    tableItems = unprocessedTableInput[0:IndexOfDelimiter]
                    unprocessedTableInput = unprocessedTableInput[(IndexOfDelimiter + 1):]
                else:
                    tableItems = unprocessedTableInput

                print("**%s**" % tableTitles[i])
                marketTable = Table(tableItems, TextWrapping, desiredWidth)
                marketTable.printUnicodeTable()

        else:
            print("**%s**" % tableTitles[i])
            marketTable = Table(unprocessedTableInput, TextWrapping, desiredWidth)
            marketTable.printUnicodeTable()

        print(closingPlayersTag)

    else:
        print("\n\nPlease upload the file and run again. See instructions to the left for further detail.")

    print("\n\nTables Complete.")


main()
