#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti
from Table import *
from time import *
from math import *

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

def testWrapping(text, maxTextLength):
    numRowsNeeded = ceil(len(text) / maxTextLength)
    solutionFound = False
    wrapPoints = []

    if (text.count('(') == 1) and (text.count(')') == 1):
        parentheticalText = text[text.find('('):text.rfind(')')]
        if len(parentheticalText) > (len(text) * (1 / 3)):
            if maxTextLength > (len(text) - len(parentheticalText)):
                solutionFound = True
                wrapPoints.append(text.find('(') - 1)

    if not solutionFound:

        numSpaces = text.count(' ')
        if numSpaces > numRowsNeeded:
            indicesOfSpaces = []
            indicesOfSpaces.append(text.rfind(' '))
            unsearchedText = text
            for i in range(numSpaces - 1):
                unsearchedText = unsearchedText[: indicesOfSpaces[0]]
                indicesOfSpaces.insert(0, unsearchedText.rfind(' '))

            breakPoint = ceil(len(text) / numRowsNeeded)
            remainingIndices = indicesOfSpaces
            for j in range(numRowsNeeded):
                if j > 0:
                    breakPoint = wrapPoints[-1] + maxTextLength
                    charsRemaining = len(text[wrapPoints[-1]:])
                    if charsRemaining < (2 * maxTextLength):
                        if charsRemaining < maxTextLength:
                            break
                        else:
                            breakPoint = wrapPoints[-1] + ceil(charsRemaining / 2)
                    """
                    numRowsNeeded = ceil(charsRemaining / maxTextLength)
                    breakPoint = wrapPoints[-1] + ceil(charsRemaining / numRowsNeeded)"""
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
                indexOfIndex = indicesOfSpaces.index(closestIndex)
                indexOfIndex += 1
                remainingIndices = indicesOfSpaces[indexOfIndex:]

    newCells = [text[:wrapPoints[0]]]
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

    print(wrapPoints, end=" Wrap points\n\n")
    return newCells


def main():
    TABLE_TITLES_DEFAULTS = ["Magic Items", "Spell Scrolls", "Special Materials"]
    NUM_TABLES_DEFAULT = 3
    DELIMITER_STRING = 'ENDTABLE\n'
    IsCustomTables = True
    MARKET_CYCLE_START_POSIX = 1654387200  # June 5th at 12am UTC
    POSTING_HOUR_DEFAULT = 23  # Vistani Market posting time
    DAYS_IN_CYCLE_DEFAULT = 3  # Vistani Market market cycle length
    DAYS_TO_ADD_DEFAULT = 3  # Number of days in the future for discord time code
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text

    print("Please read the instructions to the left before typing.\n")

    userInput = input("Make default Vistani Market tables? y/n: ")
    if userInput != 'n':
        IsCustomTables = False

    userFile = FILENAME_DEFAULT
    if IsCustomTables:
        prompt = "\nWhen entering a file name, include the file extension (\".txt\").\n"
        prompt = prompt + "Only enter the file name, do not add anything else.\n"
        prompt = prompt + "(Enter 'x' for default '%s') Enter file name: " % FILENAME_DEFAULT
        userFile = getInputOrDefault(prompt, FILENAME_DEFAULT)

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

        if IsCustomTables:

            unixTimeToAdjust = int(getInputOrDefault("Enter unix time stamp. Enter 0 for automatic calculation: ",
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
                prompt = "(Enter 'x' for default '%s') Enter table title: " % TABLE_TITLES_DEFAULTS[i]
                titleDefault = getInputOrDefault(prompt, titleDefault)

            tableTitles.append(titleDefault)

        if numTables > 1:
            for i in range(numTables):

                if unprocessedTableInput.count(DELIMITER_STRING) > 0:
                    IndexOfDelimiter = unprocessedTableInput.index(DELIMITER_STRING)
                    tableItems = unprocessedTableInput[0:IndexOfDelimiter]
                    unprocessedTableInput = unprocessedTableInput[(IndexOfDelimiter + 1):]
                else:
                    tableItems = unprocessedTableInput

                print("**%s**" % tableTitles[i])
                marketTable = Table()
                marketTable.build(tableItems)
                marketTable.printUnicodeTable()

        else:
            print("**%s**" % tableTitles[i])
            marketTable = Table()
            marketTable.build(unprocessedTableInput)
            marketTable.printUnicodeTable()

        print(closingPlayersTag)

    else:
        print("\n\nPlease upload the file and run again. See instructions to the left for further detail.")

    print("\n\nTables Complete.")

